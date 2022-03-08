import zerorpc
import time
from Difference import Difference
from threading import Thread  # 导入线程函数
from multiprocessing import Process





Controller1IP = ['10.10.10.11', '10.10.10.12', '10.10.10.13', '10.10.10.14', '10.10.10.15', '10.10.10.16','10.10.10.17']
Controller1DefaultQ = []
Controller2IP = ['10.10.10.11', '10.10.10.12', '10.10.10.13', '10.10.10.14', '10.10.10.15', '10.10.10.16','10.10.10.17']
Controller2DefaultQ = []
Controller3IP = ['10.10.10.11', '10.10.10.12', '10.10.10.13', '10.10.10.14', '10.10.10.15', '10.10.10.16','10.10.10.17']
Controller3DefaultQ = []
Controller4IP = ['10.10.10.11', '10.10.10.12', '10.10.10.13', '10.10.10.14', '10.10.10.15', '10.10.10.16','10.10.10.17']
Controller4DefaultQ = []
Controller5IP = ['10.10.10.11', '10.10.10.12', '10.10.10.13', '10.10.10.14', '10.10.10.15', '10.10.10.16','10.10.10.17']
Controller5DefaultQ = []
Controller6IP = ['10.10.10.11', '10.10.10.12', '10.10.10.13', '10.10.10.14', '10.10.10.15', '10.10.10.16','10.10.10.17']
Controller6DefaultQ = []


T = 0.6



#  动作1
Controller1StepDefaultQ =  {'10.10.10.11': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0.44, 0.44, 0.44, 0.44], '10.10.10.12': [0.44, -67705.56, -67701.5, -67701.5, -67701.5, -67349.56, -67350.56, -67359.56, -68266.5, -68266.56, -68267.56, -68269.56, -68269.56, -68267.5, -68269.56, -76129.5, -67181.5, -67182.56, -57083.56, -57083.56, -68495.5, -68500.56, -19360.56, 547.5], '10.10.10.13': [0.5, 42.5, 87.44, 86.44, 86.44, 46.5, 46.5, 53.5, 48.44, 50.5, 52.5, 52.5, 51.44, 49.44, 50.5, 55.5, 50.5, 51.5, 2712.5, 2712.5, 2708.44, 2708.44, 2708.44, 463.5], '10.10.10.14': [0.44, 17016.5, 46798.44, 68174.5, 68174.5, 68001.44, 68009.44, 64836.5, 68904.44, 68834.5, 68839.5, 68841.5, 68840.44, 68841.5, 69038.44, 95713.44, 67019.5, 65328.44, 39263.44, 71413.44, 71367.44, 71411.5, 20216.44, 20.44], '10.10.10.15': [0.5, 37.5, 16.44, 16.44, 16.44, 14.44, 14.44, 14.44, 8.44, 8.44, 8.44, 8.44, 8.44, 8.44, 8.44, 16.5, 16.5, 16.5, -0.56, -0.56, -0.56, -0.56, 15.5, 1215.44], '10.10.10.16': [-0.56, 17785.5, 17894.5, 17482.5, 17482.5, -10705.5, -15168.56, -13549.5, 19691.5, 45340.5, 55600.5, 57301.44, 21740.88, 19844.44, 47595.75, 59497.44, 17659.44, -11242.06, -22987.5, 6284.5, 21707.57, 21872.44, 21777.44, -942.56], '10.10.10.17': [-0.56, 817.44, 791, 791, 791, -15214, -43039.69, -878.57, -891.57, -20236, 2178, 30009, 30002.43, 4754, -1207.57, -1218.57, -1215, -1213, -1208.57, -1210.57, -1210.57, -1210.57, -1203, -217.57]}
Controller2StepDefaultQ =  {'10.10.10.11': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0.44, 0.44, 0.44, 0.44], '10.10.10.12': [0.44, -67705.56, -67701.5, -67701.5, -67701.5, -67349.56, -67350.56, -67359.56, -68266.5, -68266.56, -68267.56, -68269.56, -68269.56, -68267.5, -68269.56, -76129.5, -67181.5, -67182.56, -57083.56, -57083.56, -68495.5, -68500.56, -19360.56, 547.5], '10.10.10.13': [0.5, 42.5, 87.44, 86.44, 86.44, 46.5, 46.5, 53.5, 48.44, 50.5, 52.5, 52.5, 51.44, 49.44, 50.5, 55.5, 50.5, 51.5, 2712.5, 2712.5, 2708.44, 2708.44, 2708.44, 463.5], '10.10.10.14': [0.44, 17016.5, 46798.44, 68174.5, 68174.5, 68001.44, 68009.44, 64836.5, 68904.44, 68834.5, 68839.5, 68841.5, 68840.44, 68841.5, 69038.44, 95713.44, 67019.5, 65328.44, 39263.44, 71413.44, 71367.44, 71411.5, 20216.44, 20.44], '10.10.10.15': [0.5, 37.5, 16.44, 16.44, 16.44, 14.44, 14.44, 14.44, 8.44, 8.44, 8.44, 8.44, 8.44, 8.44, 8.44, 16.5, 16.5, 16.5, -0.56, -0.56, -0.56, -0.56, 15.5, 1215.44], '10.10.10.16': [-0.56, 17785.5, 17894.5, 17482.5, 17482.5, -10705.5, -15168.56, -13549.5, 19691.5, 45340.5, 55600.5, 57301.44, 21740.88, 19844.44, 47595.75, 59497.44, 17659.44, -11242.06, -22987.5, 6284.5, 21707.57, 21872.44, 21777.44, -942.56], '10.10.10.17': [-0.56, 817.44, 791, 791, 791, -15214, -43039.69, -878.57, -891.57, -20236, 2178, 30009, 30002.43, 4754, -1207.57, -1218.57, -1215, -1213, -1208.57, -1210.57, -1210.57, -1210.57, -1203, -217.57]}
Controller3StepDefaultQ =  {'10.10.10.11': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0.44, 0.44, 0.44, 0.44], '10.10.10.12': [0.44, -67705.56, -67701.5, -67701.5, -67701.5, -67349.56, -67350.56, -67359.56, -68266.5, -68266.56, -68267.56, -68269.56, -68269.56, -68267.5, -68269.56, -76129.5, -67181.5, -67182.56, -57083.56, -57083.56, -68495.5, -68500.56, -19360.56, 547.5], '10.10.10.13': [0.5, 42.5, 87.44, 86.44, 86.44, 46.5, 46.5, 53.5, 48.44, 50.5, 52.5, 52.5, 51.44, 49.44, 50.5, 55.5, 50.5, 51.5, 2712.5, 2712.5, 2708.44, 2708.44, 2708.44, 463.5], '10.10.10.14': [0.44, 17016.5, 46798.44, 68174.5, 68174.5, 68001.44, 68009.44, 64836.5, 68904.44, 68834.5, 68839.5, 68841.5, 68840.44, 68841.5, 69038.44, 95713.44, 67019.5, 65328.44, 39263.44, 71413.44, 71367.44, 71411.5, 20216.44, 20.44], '10.10.10.15': [0.5, 37.5, 16.44, 16.44, 16.44, 14.44, 14.44, 14.44, 8.44, 8.44, 8.44, 8.44, 8.44, 8.44, 8.44, 16.5, 16.5, 16.5, -0.56, -0.56, -0.56, -0.56, 15.5, 1215.44], '10.10.10.16': [-0.56, 17785.5, 17894.5, 17482.5, 17482.5, -10705.5, -15168.56, -13549.5, 19691.5, 45340.5, 55600.5, 57301.44, 21740.88, 19844.44, 47595.75, 59497.44, 17659.44, -11242.06, -22987.5, 6284.5, 21707.57, 21872.44, 21777.44, -942.56], '10.10.10.17': [-0.56, 817.44, 791, 791, 791, -15214, -43039.69, -878.57, -891.57, -20236, 2178, 30009, 30002.43, 4754, -1207.57, -1218.57, -1215, -1213, -1208.57, -1210.57, -1210.57, -1210.57, -1203, -217.57]}
Controller4StepDefaultQ =  {'10.10.10.11': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0.44, 0.44, 0.44, 0.44], '10.10.10.12': [0.44, -67705.56, -67701.5, -67701.5, -67701.5, -67349.56, -67350.56, -67359.56, -68266.5, -68266.56, -68267.56, -68269.56, -68269.56, -68267.5, -68269.56, -76129.5, -67181.5, -67182.56, -57083.56, -57083.56, -68495.5, -68500.56, -19360.56, 547.5], '10.10.10.13': [0.5, 42.5, 87.44, 86.44, 86.44, 46.5, 46.5, 53.5, 48.44, 50.5, 52.5, 52.5, 51.44, 49.44, 50.5, 55.5, 50.5, 51.5, 2712.5, 2712.5, 2708.44, 2708.44, 2708.44, 463.5], '10.10.10.14': [0.44, 17016.5, 46798.44, 68174.5, 68174.5, 68001.44, 68009.44, 64836.5, 68904.44, 68834.5, 68839.5, 68841.5, 68840.44, 68841.5, 69038.44, 95713.44, 67019.5, 65328.44, 39263.44, 71413.44, 71367.44, 71411.5, 20216.44, 20.44], '10.10.10.15': [0.5, 37.5, 16.44, 16.44, 16.44, 14.44, 14.44, 14.44, 8.44, 8.44, 8.44, 8.44, 8.44, 8.44, 8.44, 16.5, 16.5, 16.5, -0.56, -0.56, -0.56, -0.56, 15.5, 1215.44], '10.10.10.16': [-0.56, 17785.5, 17894.5, 17482.5, 17482.5, -10705.5, -15168.56, -13549.5, 19691.5, 45340.5, 55600.5, 57301.44, 21740.88, 19844.44, 47595.75, 59497.44, 17659.44, -11242.06, -22987.5, 6284.5, 21707.57, 21872.44, 21777.44, -942.56], '10.10.10.17': [-0.56, 817.44, 791, 791, 791, -15214, -43039.69, -878.57, -891.57, -20236, 2178, 30009, 30002.43, 4754, -1207.57, -1218.57, -1215, -1213, -1208.57, -1210.57, -1210.57, -1210.57, -1203, -217.57]}
Controller5StepDefaultQ =  {'10.10.10.11': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 0.44, 0.44, 0.44, 0.44], '10.10.10.12': [0.44, -67705.56, -67701.5, -67701.5, -67701.5, -67349.56, -67350.56, -67359.56, -68266.5, -68266.56, -68267.56, -68269.56, -68269.56, -68267.5, -68269.56, -76129.5, -67181.5, -67182.56, -57083.56, -57083.56, -68495.5, -68500.56, -19360.56, 547.5], '10.10.10.13': [0.5, 42.5, 87.44, 86.44, 86.44, 46.5, 46.5, 53.5, 48.44, 50.5, 52.5, 52.5, 51.44, 49.44, 50.5, 55.5, 50.5, 51.5, 2712.5, 2712.5, 2708.44, 2708.44, 2708.44, 463.5], '10.10.10.14': [0.44, 17016.5, 46798.44, 68174.5, 68174.5, 68001.44, 68009.44, 64836.5, 68904.44, 68834.5, 68839.5, 68841.5, 68840.44, 68841.5, 69038.44, 95713.44, 67019.5, 65328.44, 39263.44, 71413.44, 71367.44, 71411.5, 20216.44, 20.44], '10.10.10.15': [0.5, 37.5, 16.44, 16.44, 16.44, 14.44, 14.44, 14.44, 8.44, 8.44, 8.44, 8.44, 8.44, 8.44, 8.44, 16.5, 16.5, 16.5, -0.56, -0.56, -0.56, -0.56, 15.5, 1215.44], '10.10.10.16': [-0.56, 17785.5, 17894.5, 17482.5, 17482.5, -10705.5, -15168.56, -13549.5, 19691.5, 45340.5, 55600.5, 57301.44, 21740.88, 19844.44, 47595.75, 59497.44, 17659.44, -11242.06, -22987.5, 6284.5, 21707.57, 21872.44, 21777.44, -942.56], '10.10.10.17': [-0.56, 817.44, 791, 791, 791, -15214, -43039.69, -878.57, -891.57, -20236, 2178, 30009, 30002.43, 4754, -1207.57, -1218.57, -1215, -1213, -1208.57, -1210.57, -1210.57, -1210.57, -1203, -217.57]}
Controller6StepDefaultQ =  {'10.10.10.11': [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.56, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], '10.10.10.12': [0.44, -18166, -67453.57, -67453.57, -67456.57, -67456.57, -67456.57, -67456.57, -46634.01, -34669.01, -46452.01, -67179.57, -91504.01, -96038.01, -96128.01, -66313.01, -40787.57, -40787.57, -40787.57, -40787.57, -40787.57, -42671.57, -42672.57, -70309.01, -16209.57, -697.01, -1336.57, -1336.57, -1336.57, -1336.57, -1336.57], '10.10.10.13': [0.5, -577.56, -569.56, -566, -566, -565, -565, -561, -515, -517.56, -521.56, -518.56, -559, -521, -513, -516.56, -519.56, -517, -517, -516, -516, -514, -516.56, -519.56, -523, -522.56, 1755.44, 1755.44, 1755.44, 1755.44, 1755.44], '10.10.10.14': [0.5, 16825.44, 16797.5, 69010.51, 69019.51, 69018.45, 69003.45, 67509.51, 67182.45, 67206.51, 87230.45, 69793.45, 69800.45, 90577.45, 68400.45, 68399.51, 66213.51, 65981.51, 65956.45, 65582.51, 65586.45, 63952.45, 64403.45, 69094.45, 20177.45, 12.45, -20.49, -20.49, -20.49, -20.49, -20.49], '10.10.10.15': [0.44, -124.56, -95.56, -115.56, -115.56, -115.56, -114, -114, -112, -111, 2320.44, 2310, 2310, 2329.44, 2331, 2331, 2326.44, 2325.44, 2325.44, 2325.44, 2325.44, 2327.44, 2327.44, 2320.44, 144.44, 311.44, 311.44, 311.44, 311.44, 311.44, 311.44], '10.10.10.16': [0.5, 15314.5, 15709.44, 43120.5, 15830.44, -1979.94, -16475, -27037.56, -27261, -26498.56, -14482, -26272, -25272.56, -17287.56, -27104, -26457.56, -30319, -29491, -29079.56, -30309.56, -30305.56, -33725.38, -32113.57, 17527.43, 15048.43, -706.57, -706.57, -706.57, -706.57, -706.57, -706.57], '10.10.10.17': [0.5, -1004.56, -791.5, -572.56, -572.56, -572.56, -570.5, -560.56, 226.5, 777.44, 214.5, 1200.44, 619.5, 183.5, 601.5, 595.44, 532.44, 31822.5, 42049.44, 19222.44, 224.5, -17181.5, 2151.44, -453.5, -1241.56, 203.44, -191.5, -191.5, -191.5, -190.5, -190.5]}



# 连接Controller1服务器
CtrlC = zerorpc.Client(heartbeat=None, timeout=300)
CtrlC.connect('tcp://192.168.11.179:4243')
Ctr2C = zerorpc.Client(heartbeat=None, timeout=300)
Ctr2C.connect('tcp://192.168.11.176:4243')
Ctr3C = zerorpc.Client(heartbeat=None, timeout=300)
Ctr3C.connect('tcp://192.168.11.121:4243')
Ctr4C = zerorpc.Client(heartbeat=None, timeout=300)
Ctr4C.connect('tcp://192.168.11.114:4243')
Ctr5C = zerorpc.Client(heartbeat=None, timeout=300)
Ctr5C.connect('tcp://192.168.11.113:4243')
Ctr6C = zerorpc.Client(heartbeat=None, timeout=300)
Ctr6C.connect('tcp://192.168.11.121:4243')

# zerorpc
class RPCClient:

    def __init__(self):

        self.controller_ob = Difference(Controller1IP, Controller1DefaultQ)
        self.controller_init_pos = {}
        # for ip in Controller1IP:
        #     self.controller_init_pos[ip] = 0.0
        # en = self.controller_ob.joint_enable()
        # if en:
        #     self.controller_ob.pos_init(self.controller_init_pos)
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
        self.ctrl3_gather_count = 0
        self.ctrl3_gather_q = {
            Controller3IP[0]: [],
            Controller3IP[1]: [],
            Controller3IP[2]: [],
            Controller3IP[3]: [],
            Controller3IP[4]: [],
            Controller3IP[5]: [],
            Controller3IP[6]: []
        }
        self.ctrl4_gather_count = 0
        self.ctrl4_gather_q = {
            Controller4IP[0]: [],
            Controller4IP[1]: [],
            Controller4IP[2]: [],
            Controller4IP[3]: [],
            Controller4IP[4]: [],
            Controller4IP[5]: [],
            Controller4IP[6]: []
        }
        self.ctrl5_gather_count = 0
        self.ctrl5_gather_q = {
                '10.10.10.11': [0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44, 0.44,
                             0.44],
             '10.10.10.12': [1286.44, -6706.56, -22292.56, -37239.94, -51515.5, -64311.56, -67796.5, -67795.5,
                             -67799.56, -67800.5, -67795.5, -67792.5, -67792.5, -67796.56, -67797.56, -67797.56],
             '10.10.10.13': [95.44, 203, -2536.56, -2511, -2511, -2511, -2511, -2511, -2511, -2511, -2511, -2511, -2510,
                             -2509, -2509, -2509],
             '10.10.10.14': [31.44, 24.44, -1171.56, -1062.56, 739.44, 714.44, 2752.44, 13515.94, 26957.19, 44602.5,
                             62600, 68962.44, 68950.44, 68947.5, 68951.5, 68951.5],
             '10.10.10.15': [-0.56, -16.56, -51.56, -40, -38, -40.56, -21, 3, -9.56, -51.56, -106, -106, -105, -105,
                             -105, -105],
             '10.10.10.16': [-89.56, -191.5, -851.56, -852.56, -839.5, -840.5, 6544.44, 11817.5, 21659.5, 36346.5,
                             49881.56, 50599.44, 42340.44, 34702.94, 28511.81, 21609.06],
             '10.10.10.17': [-0.56, 8, -13.56, 3, 4, 4, 1.44, 1.44, 3, -6.56, -220.56, -565, -544, -545.56, -546.56,
                             -546.56]
        }
        self.ctrl6_gather_count = 0
        self.ctrl6_gather_q = {
            Controller6IP[0]: [],
            Controller6IP[1]: [],
            Controller6IP[2]: [],
            Controller6IP[3]: [],
            Controller6IP[4]: [],
            Controller6IP[5]: [],
            Controller6IP[6]: []
        }


        self.ctrl1_gather_step_count = 0
        self.ctrl1_gather_step_q = {Controller1IP[0]: [],
                                    Controller1IP[1]: [],
                                    Controller1IP[2]: [],
                                    Controller1IP[3]: [],
                                    Controller1IP[4]: [],
                                    Controller1IP[5]: [],
                                    Controller1IP[6]: []}

        self.ctrl2_gather_step_count = 0
        self.ctrl2_gather_step_q = {
            Controller2IP[0]: [],
            Controller2IP[1]: [],
            Controller2IP[2]: [],
            Controller2IP[3]: [],
            Controller2IP[4]: [],
            Controller2IP[5]: [],
            Controller2IP[6]: []
        }
        self.ctrl3_gather_step_count = 0
        self.ctrl3_gather_step_q = {
            Controller3IP[0]: [],
            Controller3IP[1]: [],
            Controller3IP[2]: [],
            Controller3IP[3]: [],
            Controller3IP[4]: [],
            Controller3IP[5]: [],
            Controller3IP[6]: []
        }
        self.ctrl4_gather_step_count = 0
        self.ctrl4_gather_step_q = {
            Controller4IP[0]: [],
            Controller4IP[1]: [],
            Controller4IP[2]: [],
            Controller4IP[3]: [],
            Controller4IP[4]: [],
            Controller4IP[5]: [],
            Controller4IP[6]: []
        }
        self.ctrl5_gather_step_count = 0
        self.ctrl5_gather_step_q = {
            Controller5IP[0]: [],
            Controller5IP[1]: [],
            Controller5IP[2]: [],
            Controller5IP[3]: [],
            Controller5IP[4]: [],
            Controller5IP[5]: [],
            Controller5IP[6]: []
        }
        self.ctrl6_gather_step_count = 0
        self.ctrl6_gather_step_q = {
            Controller6IP[0]: [],
            Controller6IP[1]: [],
            Controller6IP[2]: [],
            Controller6IP[3]: [],
            Controller6IP[4]: [],
            Controller6IP[5]: [],
            Controller6IP[6]: []
        }



        self.send_data = 'hello,world!!!'


        self.recv_data = None
        self.controller1_data = {}

        self.recv_data2 = None
        self.controller2_data = {}

        self.recv_data3 = None
        self.controller3_data = {}

        self.recv_data4 = None
        self.controller4_data = {}

        self.recv_data5 = None
        self.controller5_data = {}

        self.recv_data6 = None
        self.controller6_data = {}

        # self.op_input = '1,2,3,4,5 5,5,5,5,5'
        self.op_input = '4,5 5,5'
        self.controller = list(map(int,self.op_input.split(' ')[0].split(',')))
        self.mode = list(map(int,self.op_input.split(' ')[1].split(',')))

        self.control_mode = {}
        for i in range(len(self.controller)):
            self.control_mode[self.controller[i]] = self.mode[i]

        # t3 = Thread(target=self.op_input_fun)
        # t3.start()

    def op_input_fun(self):
        while True:
            # self.op_input = input('input:')
            if self.op_input:
                self.controller = list(map(int,self.op_input.split(' ')[0].split(',')))
                self.mode = list(map(int,self.op_input.split(' ')[1].split(',')))
                self.control_mode = {}
                for i in range(len(self.controller)):
                    self.control_mode[self.controller[i]] = self.mode[i]
            if len(self.controller) > 1:
                proc_record = []
                for j in range(len(self.controller)):
                    if self.controller[j] == 1:
                        if self.mode[j] == 1 or self.mode[j] ==4 or self.mode[j] ==3:
                            self.controller1()
                        else:
                            p = Process(target=self.controller1)
                            p.start()
                            proc_record.append(p)
                    elif self.controller[j] == 2:
                        if self.mode[j] == 1 or self.mode[j] ==4 or self.mode[j] ==3:
                            self.controller2()
                        else:
                            p = Process(target=self.controller2)
                            p.start()
                            proc_record.append(p)
                    elif self.controller[j] == 3:
                        if self.mode[j] == 1 or self.mode[j] ==4 or self.mode[j] ==3:
                            self.controller3()
                        else:
                            p = Process(target=self.controller3)
                            p.start()
                            proc_record.append(p)
                    elif self.controller[j] == 4:
                        if self.mode[j] == 1 or self.mode[j] ==4 or self.mode[j] ==3:
                            self.controller4()
                        else:
                            p = Process(target=self.controller4)
                            p.start()
                            proc_record.append(p)
                    elif self.controller[j] == 5:
                        if self.mode[j] == 1 or self.mode[j] ==4 or self.mode[j] ==3:
                            self.controller5()
                        else:
                            p = Process(target=self.controller5)
                            p.start()
                            proc_record.append(p)
                    elif self.controller[j] == 6:
                        if self.mode[j] == 1 or self.mode[j] ==4 or self.mode[j] ==3:
                            self.controller6()
                        else:
                            p = Process(target=self.controller6)
                            p.start()
                            proc_record.append(p)
                    elif self.controller[j] == 7:
                        if self.mode[j] == 1 or self.mode[j] ==4 or self.mode[j] ==3:
                            self.controller7()
                        else:
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
                self.recv_data = CtrlC.control(self.controller1_data,T)
            elif self.control_mode[1] == 1:


                if self.ctrl1_gather_count < 5:
                    self.ctrl1_gather_count += 1
                    print('%d times has finished!!' % self.ctrl1_gather_count)
                    self.controller1_data = {'mechine': 'controller1', 'mode': 1, 'track_stream': {}}
                    self.recv_data = CtrlC.control(self.controller1_data,T)
                    if self.recv_data['gather_data']:
                        for ip in self.recv_data['gather_data']:
                            self.ctrl1_gather_q[ip].append(self.recv_data['gather_data'][ip])
                else:
                    if len(self.ctrl1_gather_q[Controller1IP[0]]) == 5:
                        control_dict = self.controller_ob.runin(self.ctrl1_gather_q)
                        self.controller1_data = {'mechine': 'controller1', 'mode': 1, 'track_stream': control_dict}
                        print('len',len(control_dict[Controller1IP[1]]))
                        self.recv_data = CtrlC.control(self.controller1_data,T)
                print('ctrl1_gather_q:', self.ctrl1_gather_q)
            elif self.control_mode[1] == 2:
                for i in range(len(Controller1DefaultQ)):
                    control_dict = self.controller_ob.runin(Controller1DefaultQ[i])
                    self.controller1_data = {'mechine': 'controller1', 'mode': 2, 'track_stream': control_dict}
                    self.recv_data = CtrlC.control(self.controller1_data,T)
            elif self.control_mode[1] == 3:
                self.controller1_data = {'mechine': 'controller1', 'mode': 3, 'track_stream': {}}
                self.recv_data = CtrlC.control(self.controller1_data,T)

            elif self.control_mode[1] == 4:
                self.ctrl1_gather_step_count +=1
                self.controller1_data = {'mechine': 'controller1', 'mode': 4, 'track_stream': {}}
                self.recv_data = CtrlC.control(self.controller1_data,T)
                if self.recv_data['gather_data']:
                    for ip in self.recv_data['gather_data']:
                        self.ctrl1_gather_step_q[ip].append(self.recv_data['gather_data'][ip])
                print('Controller1StepDefaultQ = ', self.ctrl1_gather_step_q)
            elif self.control_mode[1] == 5:
                control_dict   = Controller1StepDefaultQ
                self.controller1_data = {'mechine': 'controller1', 'mode': 5, 'track_stream': control_dict}
                self.recv_data = CtrlC.control(self.controller1_data,T)
                print('code5 recv data:',self.recv_data)
            elif self.control_mode[1] == 55:
                self.recv_data = CtrlC.control(self.controller1_data, T)



        self.controller1_data = {}

    def controller2(self):
        if 2 in self.controller:
            if self.control_mode[2] == 0:
                self.controller2_data = {'mechine':'Controller2', 'mode': 0, 'track_stream': {}}
                self.recv_data2 = Ctr2C.control(self.controller2_data,T)
            elif self.control_mode[2] == 1:


                if self.ctrl2_gather_count < 5:
                    self.ctrl2_gather_count += 1
                    print('%d times has finished!!' % self.ctrl2_gather_count)
                    self.controller2_data = {'mechine': 'controller2', 'mode': 1, 'track_stream': {}}
                    self.recv_data2 = Ctr2C.control(self.controller2_data,T)
                    if self.recv_data2['gather_data']:
                        for ip in self.recv_data2['gather_data']:
                            self.ctrl2_gather_q[ip].append(self.recv_data2['gather_data'][ip])
                else:
                    if len(self.ctrl2_gather_q[Controller2IP[0]]) == 5:
                        control_dict = self.controller_ob.runin(self.ctrl2_gather_q)
                        self.controller2_data = {'mechine': 'controller2', 'mode': 1, 'track_stream': control_dict}
                        self.recv_data2 = Ctr2C.control(self.controller2_data,T)
                print('ctrl2_gather_q:', self.ctrl2_gather_q)
            elif self.control_mode[2] == 2:
                for i in range(len(Controller2DefaultQ)):
                    control_dict = self.controller_ob.runin(Controller2DefaultQ[i])
                    self.controller2_data = {'mechine': 'controller2', 'mode': 2, 'track_stream': control_dict}
                    self.recv_data2 = Ctr2C.control(self.controller2_data,T)
            elif self.control_mode[2] == 3:
                self.controller2_data = {'mechine': 'controller2', 'mode': 3, 'track_stream': {}}
                self.recv_data2 = Ctr2C.control(self.controller2_data,T)

            elif self.control_mode[2] == 4:
                self.ctrl2_gather_step_count +=1
                # print('%d times has finished!!' % self.ctrl2_gather_step_count)
                self.controller2_data = {'mechine': 'controller2', 'mode': 4, 'track_stream': {}}
                self.recv_data2 = Ctr2C.control(self.controller2_data,T)
                if self.recv_data2['gather_data']:
                    for ip in self.recv_data2['gather_data']:
                        self.ctrl2_gather_step_q[ip].append(self.recv_data2['gather_data'][ip])
                print('Controller2StepDefaultQ = ', self.ctrl2_gather_step_q,T)
            elif self.control_mode[2] == 5:
                control_dict   = Controller2StepDefaultQ
                self.controller2_data = {'mechine': 'controller2', 'mode': 5, 'track_stream': control_dict}
                self.recv_data2 = Ctr2C.control(self.controller2_data,T)

        self.controller2_data = {}

    def controller3(self):
        if 3 in self.controller:
            if self.control_mode[3] == 0:
                self.controller3_data = {'mechine':'Controller3', 'mode': 0, 'track_stream': {}}
                self.recv_data3 = Ctr3C.control(self.controller3_data,T)
            elif self.control_mode[3] == 1:


                if self.ctrl3_gather_count < 5:
                    self.ctrl3_gather_count += 1
                    print('%d times has finished!!' % self.ctrl3_gather_count)
                    self.controller3_data = {'mechine': 'controller3', 'mode': 1, 'track_stream': {}}
                    self.recv_data3 = Ctr3C.control(self.controller3_data,T)
                    if self.recv_data3['gather_data']:
                        for ip in self.recv_data3['gather_data']:
                            self.ctrl3_gather_q[ip].append(self.recv_data3['gather_data'][ip])
                else:
                    if len(self.ctrl3_gather_q[Controller3IP[0]]) == 5:
                        control_dict = self.controller_ob.runin(self.ctrl3_gather_q)
                        self.controller3_data = {'mechine': 'controller3', 'mode': 1, 'track_stream': control_dict}
                        self.recv_data3 = Ctr3C.control(self.controller3_data,T)
                print('ctrl3_gather_q:', self.ctrl3_gather_q)
            elif self.control_mode[3] == 2:
                for i in range(len(Controller3DefaultQ)):
                    control_dict = self.controller_ob.runin(Controller3DefaultQ[i])
                    self.controller3_data = {'mechine': 'controller3', 'mode': 2, 'track_stream': control_dict}
                    self.recv_data3 = Ctr3C.control(self.controller3_data,T)
            elif self.control_mode[3] == 3:
                self.controller3_data = {'mechine': 'controller3', 'mode': 3, 'track_stream': {}}
                self.recv_data3 = Ctr3C.control(self.controller3_data,T)
            elif self.control_mode[3] == 4:
                self.ctrl3_gather_step_count +=1
                # print('%d times has finished!!' % self.ctrl3_gather_step_count)
                self.controller3_data = {'mechine': 'controller3', 'mode': 4, 'track_stream': {}}
                self.recv_data3 = Ctr3C.control(self.controller3_data,T)
                if self.recv_data3['gather_data']:
                    for ip in self.recv_data3['gather_data']:
                        self.ctrl3_gather_step_q[ip].append(self.recv_data3['gather_data'][ip])
                print('Controller3StepDefaultQ = ', self.ctrl3_gather_step_q)
            elif self.control_mode[3] == 5:
                control_dict   = Controller3StepDefaultQ
                self.controller3_data = {'mechine': 'controller3', 'mode': 5, 'track_stream': control_dict}
                self.recv_data3 = Ctr3C.control(self.controller3_data,T)

        self.controller3_data = {}

    def controller4(self):
        if 4 in self.controller:
            if self.control_mode[4] == 0:
                self.controller4_data = {'mechine':'Controller4', 'mode': 0, 'track_stream': {}}
                self.recv_data4 = Ctr4C.control(self.controller4_data,T)
            elif self.control_mode[4] == 1:


                if self.ctrl4_gather_count < 5:
                    self.ctrl4_gather_count += 1
                    print('%d times has finished!!' % self.ctrl4_gather_count)
                    self.controller4_data = {'mechine': 'controller4', 'mode': 1, 'track_stream': {}}
                    self.recv_data4 = Ctr4C.control(self.controller4_data,T)
                    if self.recv_data4['gather_data']:
                        for ip in self.recv_data4['gather_data']:
                            self.ctrl4_gather_q[ip].append(self.recv_data4['gather_data'][ip])
                else:
                    if len(self.ctrl4_gather_q[Controller4IP[0]]) == 5:
                        control_dict = self.controller_ob.runin(self.ctrl4_gather_q)
                        self.controller4_data = {'mechine': 'controller4', 'mode': 1, 'track_stream': control_dict}
                        self.recv_data4 = Ctr4C.control(self.controller4_data,T)
                print('ctrl4_gather_q:', self.ctrl4_gather_q)
            elif self.control_mode[4] == 2:
                for i in range(len(Controller4DefaultQ)):
                    control_dict = self.controller_ob.runin(Controller4DefaultQ[i])
                    self.controller4_data = {'mechine': 'controller4', 'mode': 2, 'track_stream': control_dict}
                    self.recv_data4 = Ctr4C.control(self.controller4_data,T)
            elif self.control_mode[4] == 3:
                self.controller4_data = {'mechine': 'controller4', 'mode': 3, 'track_stream': {}}
                self.recv_data4 = Ctr4C.control(self.controller4_data,T)

            elif self.control_mode[4] == 4:
                self.ctrl4_gather_step_count +=1
                # print('%d times has finished!!' % self.ctrl4_gather_step_count)
                self.controller4_data = {'mechine': 'controller4', 'mode': 4, 'track_stream': {}}
                self.recv_data4 = Ctr4C.control(self.controller4_data,T)
                if self.recv_data4['gather_data']:
                    for ip in self.recv_data4['gather_data']:
                        self.ctrl4_gather_step_q[ip].append(self.recv_data4['gather_data'][ip])
                print('Controller4StepDefaultQ = ', self.ctrl4_gather_step_q)
            elif self.control_mode[4] == 5:
                control_dict   = Controller4StepDefaultQ
                self.controller4_data = {'mechine': 'controller4', 'mode': 5, 'track_stream': control_dict}
                self.recv_data4 = Ctr4C.control(self.controller4_data,T)

        self.controller4_data = {}

    def controller5(self):
        if 5 in self.controller:
            if self.control_mode[5] == 0:
                self.controller5_data = {'mechine':'Controller5', 'mode': 0, 'track_stream': {}}
                self.recv_data5 = Ctr5C.control(self.controller5_data,T)
            elif self.control_mode[5] == 1:


                if self.ctrl5_gather_count < 5:
                    self.ctrl5_gather_count += 1
                    print('%d times has finished!!' % self.ctrl5_gather_count)
                    self.controller5_data = {'mechine': 'controller5', 'mode': 1, 'track_stream': {}}
                    self.recv_data5 = Ctr5C.control(self.controller5_data,T)
                    if self.recv_data5['gather_data']:
                        for ip in self.recv_data5['gather_data']:
                            self.ctrl5_gather_q[ip].append(self.recv_data5['gather_data'][ip])
                else:
                    if len(self.ctrl5_gather_q[Controller5IP[0]]) == 5:
                        control_dict = self.controller_ob.runin(self.ctrl5_gather_q)
                        self.controller5_data = {'mechine': 'controller5', 'mode': 1, 'track_stream': control_dict}
                        self.recv_data5 = Ctr5C.control(self.controller5_data,T)
                print('ctrl5_gather_q:', self.ctrl5_gather_q)
            elif self.control_mode[5] == 2:
                for i in range(len(Controller5DefaultQ)):
                    control_dict = self.controller_ob.runin(Controller5DefaultQ[i])
                    self.controller5_data = {'mechine': 'controller5', 'mode': 2, 'track_stream': control_dict}
                    self.recv_data5 = Ctr5C.control(self.controller5_data,T)
            elif self.control_mode[5] == 3:
                self.controller5_data = {'mechine': 'controller5', 'mode': 3, 'track_stream': {}}
                self.recv_data5 = Ctr5C.control(self.controller5_data,T)
            elif self.control_mode[5] == 4:
                self.ctrl5_gather_step_count +=1
                # print('%d times has finished!!' % self.ctrl5_gather_step_count)
                self.controller5_data = {'mechine': 'controller5', 'mode': 4, 'track_stream': {}}
                self.recv_data5 = Ctr5C.control(self.controller5_data,T)
                if self.recv_data5['gather_data']:
                    for ip in self.recv_data5['gather_data']:
                        self.ctrl5_gather_step_q[ip].append(self.recv_data5['gather_data'][ip])
                print('Controller5StepDefaultQ = ', self.ctrl5_gather_step_q)
            elif self.control_mode[5] == 5:
                control_dict   = Controller5StepDefaultQ
                self.controller5_data = {'mechine': 'controller5', 'mode': 5, 'track_stream': control_dict}
                self.recv_data5 = Ctr5C.control(self.controller5_data,T)

        self.controller5_data = {}

    def controller6(self):
        if 6 in self.controller:
            if self.control_mode[6] == 0:
                self.controller6_data = {'mechine':'Controller6', 'mode': 0, 'track_stream': {}}
                self.recv_data6 = Ctr6C.control(self.controller6_data,T)
            elif self.control_mode[6] == 1:


                if self.ctrl6_gather_count < 5:
                    self.ctrl6_gather_count += 1
                    print('%d times has finished!!' % self.ctrl6_gather_count)
                    self.controller6_data = {'mechine': 'controller6', 'mode': 1, 'track_stream': {}}
                    self.recv_data6 = Ctr6C.control(self.controller6_data,T)
                    if self.recv_data6['gather_data']:
                        for ip in self.recv_data6['gather_data']:
                            self.ctrl6_gather_q[ip].append(self.recv_data6['gather_data'][ip])
                else:
                    if len(self.ctrl6_gather_q[Controller6IP[0]]) == 5:
                        control_dict = self.controller_ob.runin(self.ctrl6_gather_q)
                        self.controller6_data = {'mechine': 'controller6', 'mode': 1, 'track_stream': control_dict}
                        self.recv_data6 = Ctr6C.control(self.controller6_data,T)
                print('ctrl6_gather_q:', self.ctrl6_gather_q)
            elif self.control_mode[6] == 2:
                for i in range(len(Controller6DefaultQ)):
                    control_dict = self.controller_ob.runin(Controller6DefaultQ[i])
                    self.controller6_data = {'mechine': 'controller6', 'mode': 2, 'track_stream': control_dict}
                    self.recv_data6 = Ctr6C.control(self.controller6_data,T)
            elif self.control_mode[6] == 3:
                self.controller6_data = {'mechine': 'controller6', 'mode': 3, 'track_stream': {}}
                self.recv_data6 = Ctr6C.control(self.controller6_data,T)
            elif self.control_mode[6] == 4:
                self.ctrl6_gather_step_count +=1
                # print('%d times has finished!!' % self.ctrl6_gather_step_count)
                self.controller6_data = {'mechine': 'controller6', 'mode': 4, 'track_stream': {}}
                self.recv_data6 = Ctr6C.control(self.controller6_data,T)
                if self.recv_data6['gather_data']:
                    for ip in self.recv_data6['gather_data']:
                        self.ctrl6_gather_step_q[ip].append(self.recv_data6['gather_data'][ip])
                print('Controller6StepDefaultQ = ', self.ctrl6_gather_step_q)
            elif self.control_mode[6] == 5:
                control_dict = Controller6StepDefaultQ
                self.controller6_data = {'mechine': 'controller6', 'mode': 5, 'track_stream': control_dict}
                self.recv_data6 = Ctr6C.control(self.controller6_data,T)

        self.controller6_data = {}

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