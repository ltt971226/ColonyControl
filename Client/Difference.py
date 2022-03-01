#coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import math
import aios
import time

# q_array=[[180,100,150,50,100],[0,90,150,180,0],[0,20,80,100,150],[0,50,150,100,40]]#指定起止位置
# q_array=[[0,90,150,180,0],[0,20,80,100,150]]#指定起止位置

class Difference:

    def __init__(self,server_ips,default_q):
        #一条默认轨迹点
        self.q_array = default_q
        self.t_array = [0, 3, 6, 12, 14]  # 指定起止时间
        self.v_array = [0, 0, 0, 0, 0]  # 指定起止速度
        self.a_array = [0, 0, 0, 0, 0]  # 指定起止加速度
        self.paint_switch = False
        self.Server_IP_list = server_ips

    def connect_init(self):
        self.Server_IP_list = aios.broadcast_func()
        # 由于第一个ip是路由器的ip，无法使用将其剔除
        if '10.10.10.200' in self.Server_IP_list:
            self.Server_IP_list.remove('10.10.10.200')
        if self.Server_IP_list:
            for i in range(len(self.Server_IP_list)):
                aios.getRoot(self.Server_IP_list[i])

    def gather(self):
        five_q = {}
        for i in range(len(self.Server_IP_list)):
            five_q[self.Server_IP_list[i]] = []
        if self.Server_IP_list:
            count = 0
            for i in range(50):
                count += 1
                for i in range(len(self.Server_IP_list)):
                    cvp = aios.getCVP(self.Server_IP_list[i], 1)
                    print("Position = %.2f, Velocity = %.0f, Current = %.4f" % (cvp[0], cvp[1], cvp[2]))
                    if count % 10 == 0:
                        five_q[self.Server_IP_list[i]].append(cvp[0])
                if count % 10 == 0:
                    input()
        self.q_array = five_q
        print("q_dict:", self.q_array)

    def paint_on(self):
        self.paint_switch = True

    def runin(self, q_array):
        #初始状态
        t=[]
        q=[]
        v=[]
        a=[]
        joints_q_list = {}
        fig_count = 0
        for key,val in q_array.items():
            for j in range(len(val)-1):
                T = self.t_array[j + 1] - self.t_array[j]  # 时间差
                a0 = val[j]
                a1 = self.v_array[j]
                a2 = self.a_array[j] / 2
                a3 = (20 * val[j + 1] - 20 * val[j] - (8 * self.v_array[j + 1] + 12 * self.v_array[j]) * T - (3 * self.a_array[j] - self.a_array[j + 1]) * math.pow(T, 2)) / (2 * math.pow(T, 3))
                a4 = (30 * val[j] - 30 * val[j + 1] + (14 * self.v_array[j + 1] + 16 * self.v_array[j]) * T + (3 * self.a_array[j] - 2 * self.a_array[j + 1]) * math.pow(T, 2)) / (2 * math.pow(T, 4))
                a5 = (12 * val[j + 1] - 12 * val[j] - (6 * self.v_array[j + 1] + 6 * self.v_array[j]) * T - ( self.a_array[j] - self.a_array[j + 1]) * math.pow(T, 2)) / (2 * math.pow(T, 5))
                ti = np.arange(self.t_array[j], self.t_array[j + 1], .1)

                '''
                求解出角度，角速度，角加速度随某个时间区间随时间变换的曲线
                '''

                qi = a0 + a1 * (ti - self.t_array[j]) + a2 * np.power((ti - self.t_array[j]), 2) + a3 * np.power((ti - self.t_array[j]), 3) + a4 * np.power( (ti - self.t_array[j]), 4) + a5 * np.power((ti - self.t_array[j]), 5)
                vi = a1 + 2 * a2 * (ti - self.t_array[j]) + 3 * a3 * np.power((ti - self.t_array[j]), 2) + 4 * a4 * np.power( (ti - self.t_array[j]), 3) + 5 * a5 * np.power((ti - self.t_array[j]), 4)
                ai = 2 * a2 + 6 * a3 * (ti - self.t_array[j]) + 12 * a4 * np.power((ti - self.t_array[j]), 2) + 20 * a5 * np.power((ti - self.t_array[j]), 3)
                ti = ti.tolist()  # 将矩阵转换为list，否则进行数据整合会报错
                qi = qi.tolist()  # 将矩阵转换为list，否则进行数据整合会报错
                vi = vi.tolist()  # 将矩阵转换为list，否则进行数据整合会报错
                ai = ai.tolist()  # 将矩阵转换为List，否则进行数据整合会报错
                t = t + ti[1:] #进行数据整合，用来绘制函数图像
                q = q + qi[1:] #进行数据整合，用来绘制函数图像
                v = v + vi[1:] #进行数据整合，用来绘制函数图像
                a = a + ai[1:] #进行数据整合，用来绘制函数图像

            if self.paint_switch:
                plt.figure(fig_count)
                fig_count +=1
                plt.title(key)
                plt.plot(t, q, linestyle=":", color=(1, 0, 0, 1.0), label="angle curve")
                plt.scatter(self.t_array, val, marker='*', s=70, label="angle spot", zorder=3)

                plt.plot(t, v, linestyle="-", color=(1, 0.5, 1, 1.0), label="speed curve")
                plt.scatter(self.t_array, self.v_array, marker='^', s=70, label="speed spot", zorder=3)

                plt.plot(t, a, linestyle="-.", color=(0, 0, 0, 1.0), label="acceleration curve")
                plt.scatter(self.t_array, self.a_array, marker='o', s=70, label="acceleration spot", zorder=3)

                plt.grid()#显示网格
                plt.legend()#显示图例
                #保存图片
                # figpath = 'E:/Python代码/机械臂运动轨迹规划/servo'+i.__str__()
                # plt.savefig(figpath)
            joints_q_list[key] = q
            t=[]
            q=[]
            v=[]
            a=[]
        if self.paint_switch:
            plt.show()
        return joints_q_list

    def joint_enable(self):
        for i in range(len(self.Server_IP_list)):
            aios.getRoot(self.Server_IP_list[i])
        Success = True
        for i in range(len(self.Server_IP_list)):
            if not aios.enable(self.Server_IP_list[i], 1):
                Success = False

        return Success

    def pos_init(self,control_dict):
        dict = {
            'accel_limit': 8000,
            'decel_limit': 8000,
            'vel_limit': 20000
        }
        for i in range(len(self.Server_IP_list)):
            aios.setTrapTraj(dict, self.Server_IP_list[i], 1)
        print('\n')
        aios.trapezoidalMoveClose(control_dict, False, self.Server_IP_list, 1, accuracy_threshold = 50)
        time.sleep(0.5)

    def defference(self, control_dict):
        for i in range(len(control_dict[self.Server_IP_list[0]])):
            for key, val in control_dict.items():
                aios.setPosition(val[i], 0, 0, True, key, 1)

if __name__ == "__main__":
    #对象初始化
    diff_object = Difference()
    #连接控制器初始化
    diff_object.connect_init()
    #是否要获取五个点（可选）
    # diff_object.gather()
    #选择是否打开画图开关（可选）
    # diff_object.paint_on()
    #计算插补轨迹
    control_dict = diff_object.runin(diff_object.q_array)
    pos_init_dict = {}
    for key,val in control_dict.items():
        pos_init_dict[key] = val[0]
    #使能关节控制器
    enable_flag = diff_object.joint_enable()
    if enable_flag:
        #控制机械臂回到初始位置
        diff_object.pos_init(pos_init_dict)
        #结束后执行插补控制
        diff_object.defference(control_dict)
        print(123)

