import zerorpc
import time
import aios
from threading import Thread  # 导入线程函数
import threading
from multiprocessing import Process
import psutil
import json
# zerorpc

sub_ips = ['10.10.10.11','10.10.10.12','10.10.10.13','10.10.10.14','10.10.10.15','10.10.10.16','10.10.10.17']
def pos_init(control_dict):
    
    dict = {
        'accel_limit':32000,
        'decel_limit':32000,
        'vel_limit':40000
        }
    for ip in control_dict:
        aios.setTrapTraj(dict, ip ,1)
    print('control_dict',control_dict)
    aios.trapezoidalMoveClose(control_dict,False,sub_ips,1,accuracy_threshold=50)
    time.sleep(0.5)
def connect_init():
    Server_IP_list = aios.broadcast_func()
        # 由于第一个ip是路由器的ip，无法使用将其剔除
    if Server_IP_list:
        for i in range(len(Server_IP_list)):
            aios.getRoot(Server_IP_list[i])
def joint_enable():
    for i in range(len(sub_ips)):
        aios.getRoot(sub_ips[i])
    success = True
    for i in range(len(sub_ips)):
        if not aios.enable(sub_ips[i],1):
            success = False
    return success
    
def zerorpc_client():
    print('controller1 client')
    c = zerorpc.Client()
    c.connect('tcp://192.168.1.168:4243')
    data = 'lqz nb'
    resp = {'mechine':'Controller1','mode':0,'succeedCode':False}
    start = time.perf_counter()
    
    #init
    connect_init()
    en = joint_enable()
    init_dict = {}
    for ip in sub_ips:
        init_dict[ip] = 0.0
    if en:
        pos_init(init_dict)
    
    #主循环
    while True:
        #先进行请求
        req_res=c.controller1()
        #req_res = []
        #print(req_res)
        if req_res:
            if req_res['mode'] == 2:
                print(req_res['track_stream'])
                en = joint_enable()
                if en:
                    control_dict = {}
                    for ip in sub_ips:
                        control_dict[ip] = 0.0
                    pos_init(control_dict)
                for i in range(len(req_res['track_stream'][sub_ips[0]])):
                    for key,val in  req_res['track_stream'].items():
                        aios.trapezoidalMove(val[i], False, key, 1)
                        time.sleep(0.01)
                        #print(key,':',val[i])
                resp = {'mechine':'Controller1','mode':2,'succeedCode':True, 'gather_data':{}}
                c.sendObj(resp)
            elif req_res['mode'] == 0:
                en = joint_enable()
                if en:
                    control_dict = {}
                    for ip in sub_ips:
                        control_dict[ip] = 0.0
                    pos_init(control_dict)
                resp = {'mechine':'Controller1','mode':0,'succeedCode':True, 'gather_data':{}}
                c.sendObj(resp)
            elif req_res['mode'] == 3:
                for ip in sub_ips:
                    aios.setCurrent(0.0,True,ip,1)
                resp = {'mechine':'Controller1','mode':3,'succeedCode':True, 'gather_data':{}}
                c.sendObj(resp)
            elif req_res['mode'] == 1:
                if not req_res['track_stream']:
                    gather_data = {}
                    for ip in sub_ips:
                        cvp = aios.getCVP(ip,1)
                        gather_data[ip] = cvp[0]
                    c.sendObj({'mechine':'Controller1','mode':1,'succeedCode':True, 'gather_data':gather_data})
                else:
                    print(req_res['track_stream'])
                    en = joint_enable()
                    if en:
                        control_dict = {}
                        for ip in sub_ips:
                            control_dict[ip] = 0.0
                        pos_init(control_dict)
                    
                    for i in range(len(req_res['track_stream'][sub_ips[0]])):
                        for key,val in  req_res['track_stream'].items():
                            #pass
                            aios.trapezoidalMove(val[i], False, key, 1)
                            time.sleep(0.01)
                        #print(key,':',val[i])
                    resp = {'mechine':'Controller1','mode':1,'succeedCode':True, 'gather_data':{}}
                    c.sendObj(resp)
                    
                                                                                        

        
        

    print('total time %s' % (time.perf_counter() - start))
    
    
class RPCServer(object):

    def __init__(self,):
        super(RPCServer, self).__init__()
        print(self)
        self.resp = {'mechine':'Controller1','mode':-1,'succeedCode':False, 'gather_data':{}}
        
        #init
        # connect_init()
        # en = joint_enable()
        # init_dict = {}
        # for ip in sub_ips:
        #     init_dict[ip] = 0.0
        # if en:
        #     pos_init(init_dict)

        self.step_data = {}
        self.t = 0
        self.start = False
        self.stop = False

        self.__flag = threading.Event()  # 用于暂停线程的标识
        self.__flag.set()  # 设置为True
        self.__running = threading.Event()  # 用于停止线程的标识
        self.__running.set()  # 将running设置为True
        self.a = threading.Thread(target=self.do_step)
        self.a.start()


    def do_step(self):
        while self.__running.isSet():
            self.__flag.wait()
            print('main loop')
            if self.start:
                if self.step_data:
                    print('trak')
                    for i in range(len(self.step_data[sub_ips[0]])):
                        for key, val in self.step_data.items():
                            aios.trapezoidalMove(val[i], False, key, 1)
                        if self.stop:
                            break
                        time.sleep(self.t)
                        time.sleep(2)
                self.start = False
            time.sleep(0.1)

    def test(self):
        while self.__running.isSet():
            self.__flag.wait()  # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
            print(time.time())
            time.sleep(1)
    def pause(self):
        self.__flag.clear()     # 设置为False, 让线程阻塞

    def resume(self):
        self.__flag.set()    # 设置为True, 让线程停止阻塞

    def stop(self):
        self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
        self.__running.clear()        # 设置为False

    def getObj(self):
        print('get data')
        return '1234'
    def sendObj(self, sentdata):
        print(sentdata)
    def control(self, control_data,t):
        self.resp = {'mechine':'Controller1','mode':-1,'succeedCode':False, 'gather_data':{}}
        if control_data['mode'] == 2:
            print(control_data['track_stream'])
            en = joint_enable()
            if en:
                control_dict = {}
                for ip in sub_ips:
                    control_dict[ip] = 0.0
                pos_init(control_dict)
            for i in range(len(control_data['track_stream'][sub_ips[0]])):
                for key,val in  control_data['track_stream'].items():
                    aios.trapezoidalMove(val[i], False, key, 1)
                    time.sleep(0.01)
                    #print(key,':',val[i])
            self.resp = {'mechine':'Controller1','mode':2,'succeedCode':True, 'gather_data':{}}
            return self.resp   
                
        elif control_data['mode'] == 0:
            en = joint_enable()
            if en:
                control_dict = {}
                for ip in sub_ips:
                    control_dict[ip] = 0.0
                pos_init(control_dict)
            self.resp = {'mechine':'Controller1','mode':0,'succeedCode':True, 'gather_data':{}}
            return self.resp
            
        elif control_data['mode'] == 3:
            for ip in sub_ips:
                aios.setCurrent(0.0,True,ip,1)
            self.resp = {'mechine':'Controller1','mode':3,'succeedCode':True, 'gather_data':{}}
            return self.resp
            
        elif control_data['mode'] == 1:
            if not control_data['track_stream']:
                gather_data = {}
                for ip in sub_ips:
                    cvp = aios.getCVP(ip,1)
                    gather_data[ip] = cvp[0]
                self.resp = {'mechine':'Controller1','mode':1,'succeedCode':True, 'gather_data':gather_data}
                return self.resp
            else:
                print(control_data['track_stream'])
                en = joint_enable()
                if en:
                    control_dict = {}
                    for ip in sub_ips:
                        control_dict[ip] = 0.0
                    pos_init(control_dict)
                
                for i in range(len(control_data['track_stream'][sub_ips[0]])):
                    for key,val in  control_data['track_stream'].items():
                        #pass
                        aios.trapezoidalMove(val[i], False, key, 1)
                        time.sleep(0.01)
                    #print(key,':',val[i])
                self.resp = {'mechine':'Controller1','mode':1,'succeedCode':True, 'gather_data':{}}
                return self.resp

        elif control_data['mode']  ==  4:
            gather_data = {}
            for ip in sub_ips:
                cvp = aios.getCVP(ip,1)
                gather_data[ip] = cvp[0]
            self.resp = {'mechine':'Controller1','mode':4,'succeedCode':True, 'gather_data':gather_data}
            return self.resp
        elif control_data['mode']  ==  5:
            print(control_data['track_stream'])
            en = joint_enable()
            if en:
                for i in range(len(control_data['track_stream'][sub_ips[0]])):
                    for key,val in  control_data['track_stream'].items():
                        aios.trapezoidalMove(val[i], False, key, 1)
                    time.sleep(t)
            self.resp = {'mechine':'Controller1','mode':5,'succeedCode':True, 'gather_data':{}}
            return self.resp
    def get_data(self,control_data,t):
        print(control_data)
        self.step_data = control_data
        self.t = t
        self.pause()

    def set_start(self):
        self.start = True
        print('start')
        self.resume()
        print(123)
        return

    def reply(self):
        return self.resp
        


if __name__ == '__main__':
    s = zerorpc.Server(RPCServer())
    s.bind('tcp://0.0.0.0:4243')
    s.run()

