import zerorpc
import time

class RPCServer(object):
    """docstring for RPCServer"""

    def __init__(self):
        super(RPCServer, self).__init__()
        self.data = {str(i): i for i in range(10)}
        self.data2 = None
        self.flag = False

    def getObj(self):
        print('get data')
        return self.data
    def flag(self,flag):
        self.flag = flag

    def sendObj(self, data):
        print('send data')
        if data:
            while True:
                print(time.clock())
                time.sleep(1)

                if self.flag:
                    break
# zerorpc
s = zerorpc.Server(RPCServer())
s.bind('tcp://0.0.0.0:4243')
s.run()
