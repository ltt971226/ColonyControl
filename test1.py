import os
import subprocess
import socket

"""
python获取主机内网中所有MAC地址
"""


def get_local_net():  # 主机所在网段
    # 获取主机名
    hostname = socket.gethostname()
    # 获取主机的局域网ip
    localip = socket.gethostbyname(hostname)
    localipnums = localip.split('.')
    localipnums.pop()
    localipnet = '.'.join(localipnums)
    return localipnet


def getmacaddr():
    devnull = open(os.devnull, 'wb')
    res = subprocess.Popen("arp -a", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=devnull)
    sout, serr = res.communicate()
    honstip = get_local_net()
    mac_ip = dict()
    if type(sout) == bytes:
        # x = str(sout, encoding="gbk")
        y = str(sout, encoding="gbk").split()
        for i in range(len(y)):
            if y[i].find(honstip) >= 0:
                mac_ip[y[i]] = y[i + 1]
                i += 1
                print(y[i])
                print(y[i + 1])

        print(mac_ip)
    return mac_ip


if __name__ == '__main__':
    getmacaddr()