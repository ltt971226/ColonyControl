import zerorpc
from threading import Thread  # 导入线程函数
from Difference import Difference

Controller1IP = ['10.10.10.63', '10.10.10.61', '10.10.10.62', '10.10.10.65', '10.10.10.64', '10.10.10.66','10.10.10.67']
Controller1DefaultQ = {'10.10.10.62': [1.5, 5573.44, 19325.44, 17439.5, 25658.44],
                  '10.10.10.63': [1.5, -578.5, 230.5, 382.5, 208.5],
                  '10.10.10.61': [1.5, 3784.5, 16769.5, 25756.44, 37355.44],
                  '10.10.10.64': [1.5, 4908.44, 18144.5, 22710.5, 28430.44],
                  '10.10.10.65': [1.5, -14845.5, -20080.5, -31466.5, -40094.5],
                  '10.10.10.66': [0, 3.5, 7584.44, 11631.5, 11631.5],
                  '10.10.10.67': [0, 0, 0, 0, 0]}
class RPCServer(object):

    def __init__(self,):
        super(RPCServer, self).__init__()
        print(self)



        self.controller1_ob = Difference(Controller1IP,Controller1DefaultQ)
        self.controller1_init_pos = {}
        # for ip in Controller1IP:
        #     self.controller1_init_pos[ip] = 0.0
        # en = self.controller1_ob.joint_enable()
        # if en:
        #     self.controller1_ob.pos_init(self.controller1_init_pos)
        self.gather_count = 0
        self.gather_q = {
            '10.10.10.62': [],
            '10.10.10.63': [],
            '10.10.10.61': [],
            '10.10.10.64': [],
            '10.10.10.65': [],
            '10.10.10.66': [],
            '10.10.10.67': []
        }
        self.do_switvh = True
        self.send_data = 'hello,world!!!'
        self.recv_data = None
        self.controller1_data = {}
        self.op_input = '1,0'
        self.controller = int(self.op_input.split(',')[0])
        self.mode = int(self.op_input.split(',')[1])

        t3 = Thread(target=self.op_input_fun)
        t3.start()

    def op_input_fun(self):
        while True:
            self.op_input = input()
            if self.op_input:
                self.controller = int(self.op_input.split(',')[0])
                self.mode = int(self.op_input.split(',')[1])
            self.do_switvh = True
            print(self.op_input,self.mode)

    def getObj(self):
        print('get data')
        return self.send_data
    def controller1(self):
        if self.controller == 1 and self.do_switvh:
            if self.mode ==0:
                self.controller1_data = {'mechine':'controller1','mode':0,'track_stream':{}}
                return self.controller1_data
            elif self.mode == 1:
                print('%d times has finished!!'%self.gather_count)
                print('gather_q:', self.gather_q)
                if self.gather_count < 5:
                    self.gather_count +=1
                    self.controller1_data = {'mechine': 'controller1', 'mode': 1, 'track_stream': {}}
                    return self.controller1_data
                else:
                    if len(self.gather_q['10.10.10.62']) == 5:
                        control_dict = self.controller1_ob.runin(self.gather_q)
                        self.controller1_data = {'mechine': 'controller1', 'mode': 1, 'track_stream': control_dict}
                        return self.controller1_data
            elif self.mode == 2:
                control_dict = self.controller1_ob.runin(Controller1DefaultQ)
                self.controller1_data = {'mechine': 'controller1', 'mode': 2, 'track_stream': control_dict}
                return self.controller1_data
            elif self.mode ==3:
                self.controller1_data = {'mechine': 'controller1', 'mode': 3, 'track_stream': {}}
                return self.controller1_data

            return {}


    def sendObj(self, data):
        print('send data')
        self.recv_data = data
        print(self.recv_data)
        self.do_switvh = False
        if self.recv_data['succeedCode']:
            self.do_switvh = False
        if self.recv_data['gather_data']:
            for ip in self.recv_data['gather_data']:
                self.gather_q[ip].append(self.recv_data['gather_data'][ip])


class ControllerMode():

    def __init__(self, controller, mode):
        self.controller = controller
        self.mode = mode

# zerorpc
if __name__ == '__main__':
    '''
   |----------|--------|------|-----|-----|
   |-modecode-|---0----|--1---|--2--|--3--|
   |---mode---|回到初始|-采集-|-插补-|电流-|
    '''
    op_input = '1,2'
    controller_mode = ControllerMode(int(op_input.split(',')[0]), int(op_input.split(',')[1]))

    s = zerorpc.Server(RPCServer())
    s.bind('tcp://0.0.0.0:4243')
    s.run()