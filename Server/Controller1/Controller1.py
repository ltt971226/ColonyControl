import zerorpc
import time
import aios
import json
# zerorpc

sub_ips = ['10.10.10.62','10.10.10.63','10.10.10.61','10.10.10.64','10.10.10.65','10.10.10.66','10.10.10.67']
def pos_init(control_dict):
    
    dict = {
        'accel_limit':8000,
        'decel_limit':8000,
        'vel_limit':20000
        }
    for ip in control_dict:
        aios.setTrapTraj(dict, ip ,1)
    print('control_dict',control_dict)
    aios.trapezoidalMoveClose(control_dict,False,sub_ips,1,accuracy_threshold=50)
    time.sleep(0.5)
def connect_init():
    Server_IP_list = aios.broadcast_func()
        # 由于第一个ip是路由器的ip，无法使用将其剔除
    if '10.10.10.200' in Server_IP_list:
        Server_IP_list.remove('10.10.10.200')
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


if __name__ == '__main__':
    zerorpc_client()