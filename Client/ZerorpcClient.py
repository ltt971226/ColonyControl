import zerorpc
import time
from Difference import Difference
from threading import Thread  # 导入线程函数
from multiprocessing import Process

Controller1IP = ['10.10.10.85', '10.10.10.86', '10.10.10.87', '10.10.10.88', '10.10.10.89', '10.10.10.90','10.10.10.91']
Controller1DefaultQ = {'10.10.10.85': [-10, 5654.5, 15085.5, 35009.5, 49881.5],
                       '10.10.10.86': [0, 0, 0, 0, 0],
                       '10.10.10.87': [-13.56, -29907.5, -30817.56, -34768.5, -36762.5],
                       '10.10.10.88': [5.5, 13.5, -1149.56, 1241.44, -775.56],
                       '10.10.10.89': [10.5, -412.5, 4583.5, -4327, 17181.44],
                       '10.10.10.90': [57.5, 33688.5, 38259.44, 24579.44, 30254.5],
                       '10.10.10.91': [1.5, 1.5, 1.5, 1.5, 1.5]}

Controller2IP = ['10.10.10.78', '10.10.10.79', '10.10.10.80', '10.10.10.81', '10.10.10.82', '10.10.10.83','10.10.10.84']
Controller2DefaultQ = {'10.10.10.78': [0.5, -0.56, -0.56, -14619.5, -30056.5],
                       '10.10.10.79': [-20.56, -19153.56, -46880.56, -10222.56, 13999.5],
                       '10.10.10.80': [4, -2512.56, -21676.56, 7870.44, 32658.5],
                       '10.10.10.81': [0.5, 56.5, 7091.44, 31852.44, 17032.44],
                       '10.10.10.82': [0, 582.44, 577, 41508.44, 41468.44],
                       '10.10.10.83': [11.5, -1183.56, -9616.5, -28800.56, -17507.56],
                       '10.10.10.84': [1, -0.56, -0.56, -0.56, -0.56]}



# 连接Controller1服务器
CtrlC = zerorpc.Client()
CtrlC.connect('tcp://192.168.11.177:4243')
Ctr2C = zerorpc.Client()
Ctr2C.connect('tcp://192.168.11.31:4243')

# zerorpc
class RPCClient:

    def __init__(self):

        self.controller1_ob = Difference(Controller1IP, Controller1DefaultQ)
        self.controller1_init_pos = {}
        # for ip in Controller1IP:
        #     self.controller1_init_pos[ip] = 0.0
        # en = self.controller1_ob.joint_enable()
        # if en:
        #     self.controller1_ob.pos_init(self.controller1_init_pos)
        self.ctrl1_gather_count = 0
        self.ctrl1_gather_q = {
            '10.10.10.85': [],
            '10.10.10.86': [],
            '10.10.10.87': [],
            '10.10.10.88': [],
            '10.10.10.89': [],
            '10.10.10.90': [],
            '10.10.10.91': []
        }
        self.ctrl2_gather_count = 0
        self.ctrl2_gather_q = {
            Controller2IP[0]: [],
            Controller2IP[1]: [],
            Controller2IP[2]: [],
            Controller2IP[3]: [],
            Controller2IP[4]: [],
            Controller2IP[5]: [],
            Controller2IP[6]: []
        }



        self.send_data = 'hello,world!!!'


        self.recv_data = None
        self.controller1_data = {}

        self.recv_data2 = None
        self.controller2_data = {}

        self.op_input = '2 0'
        self.controller = list(map(int,self.op_input.split(' ')[0].split(',')))
        self.mode = list(map(int,self.op_input.split(' ')[1].split(',')))

        self.control_mode = {}
        for i in range(len(self.controller)):
            self.control_mode[self.controller[i]] = self.mode[i]

        # t3 = Thread(target=self.op_input_fun)
        # t3.start()

    def op_input_fun(self):
        while True:
            self.op_input = input('input:')
            if self.op_input:
                self.controller = list(map(int,self.op_input.split(' ')[0].split(',')))
                self.mode = list(map(int,self.op_input.split(' ')[1].split(',')))
                self.control_mode = {}
                for i in range(len(self.controller)):
                    self.control_mode[self.controller[i]] = self.mode[i]
            if len(self.controller) > 1:
                proc_record = []
                for co in self.controller:
                    if co == 1:
                        p = Process(target=self.controller1)
                        p.start()
                        proc_record.append(p)
                    elif co == 2:
                        p = Process(target=self.controller2)
                        p.start()
                        proc_record.append(p)
                    elif co == 3:
                        p = Process(target=self.controller3)
                        p.start()
                        proc_record.append(p)
                    elif co == 4:
                        p = Process(target=self.controller4)
                        p.start()
                        proc_record.append(p)
                    elif co == 5:
                        p = Process(target=self.controller5)
                        p.start()
                        proc_record.append(p)
                    elif co == 6:
                        p = Process(target=self.controller6)
                        p.start()
                        proc_record.append(p)
                    elif co == 7:
                        p = Process(target=self.controller7)
                        p.start()
                        proc_record.append(p)
                for p in proc_record:
                    p.join()
            else:
                for co in self.controller:
                    if co == 1:
                        self.controller1()
                    elif co == 2:
                        self.controller2()
                    elif co == 3:
                        self.controller3()
                    elif co == 4:
                        self.controller4()
                    elif co == 5:
                        self.controller5()
                    elif co == 6:
                        self.controller6()
                    elif co == 7:
                        self.controller7()
            print(self.op_input, self.mode)

    def controller1(self):
        if 1 in self.controller:
            if self.control_mode[1] == 0:
                self.controller1_data = {'mechine': 'controller2', 'mode': 0, 'track_stream': {}}
                self.recv_data = CtrlC.control(self.controller1_data)
            elif self.control_mode[1] == 1:

                print('ctrl1_gather_q:', self.ctrl1_gather_q)
                if self.ctrl1_gather_count < 5:
                    self.ctrl1_gather_count += 1
                    print('%d times has finished!!' % self.ctrl1_gather_count)
                    self.controller1_data = {'mechine': 'controller1', 'mode': 1, 'track_stream': {}}
                    self.recv_data = CtrlC.control(self.controller1_data)
                    if self.recv_data['gather_data']:
                        for ip in self.recv_data['gather_data']:
                            self.ctrl1_gather_q[ip].append(self.recv_data['gather_data'][ip])
                else:
                    if len(self.ctrl1_gather_q[Controller1IP[0]]) == 5:
                        control_dict = self.controller1_ob.runin(self.ctrl1_gather_q)
                        self.controller1_data = {'mechine': 'controller1', 'mode': 1, 'track_stream': control_dict}
                        self.recv_data = CtrlC.control(self.controller1_data)
            elif self.control_mode[1] == 2:
                control_dict = self.controller1_ob.runin(Controller1DefaultQ)
                self.controller1_data = {'mechine': 'controller1', 'mode': 2, 'track_stream': control_dict}
                self.recv_data = CtrlC.control(self.controller1_data)
            elif self.control_mode[1] == 3:
                self.controller1_data = {'mechine': 'controller1', 'mode': 3, 'track_stream': {}}
                self.recv_data = CtrlC.control(self.controller1_data)

        self.controller1_data = {}

    def controller2(self):
        if 2 in self.controller:
            if self.control_mode[2] == 0:
                self.controller2_data = {'mechine':'Controller2', 'mode': 0, 'track_stream': {}}
                self.recv_data2 = Ctr2C.control(self.controller2_data)
            elif self.control_mode[2] == 1:

                print('ctrl2_gather_q:', self.ctrl2_gather_q)
                if self.ctrl2_gather_count < 5:
                    self.ctrl2_gather_count += 1
                    print('%d times has finished!!' % self.ctrl2_gather_count)
                    self.controller2_data = {'mechine': 'controller2', 'mode': 1, 'track_stream': {}}
                    self.recv_data2 = Ctr2C.control(self.controller2_data)
                    if self.recv_data2['gather_data']:
                        for ip in self.recv_data2['gather_data']:
                            self.ctrl2_gather_q[ip].append(self.recv_data2['gather_data'][ip])
                else:
                    if len(self.ctrl2_gather_q[Controller2IP[0]]) == 5:
                        control_dict = self.controller1_ob.runin(self.ctrl2_gather_q)
                        self.controller2_data = {'mechine': 'controller2', 'mode': 1, 'track_stream': control_dict}
                        self.recv_data2 = Ctr2C.control(self.controller2_data)
            elif self.control_mode[2] == 2:
                control_dict = self.controller1_ob.runin(Controller2DefaultQ)
                self.controller2_data = {'mechine': 'controller2', 'mode': 2, 'track_stream': control_dict}
                self.recv_data2 = Ctr2C.control(self.controller2_data)
            elif self.control_mode[2] == 3:
                self.controller2_data = {'mechine': 'controller2', 'mode': 3, 'track_stream': {}}
                self.recv_data2 = Ctr2C.control(self.controller2_data)

        self.controller2_data = {}

    def zerorpc_client(self):
        print('zerorpc client')
        c = zerorpc.Client()
        c.connect('tcp://192.168.11.31:4243')
        data = 'lqz nb'
        start = time.clock()
        for i in range(10):
            a=c.getObj()
            print(a)
        for i in range(10):
            c.sendObj(data)

        print('total time %s' % (time.clock() - start))


if __name__ == '__main__':
    c = RPCClient()
    c.op_input_fun()
    # c.zerorpc_client()