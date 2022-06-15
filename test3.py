#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scapy.all import srp,Ether,ARP,conf
import socket

def getPCName(ip):
    return socket.gethostbyaddr(ip)

ipscan='192.168.88.1/24'
try:
    ans,unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=ipscan),timeout=2,verbose=False)
except Exception as e:
    print(str(e))
else:
    for snd,rcv in ans:
        list_mac=rcv.sprintf("%Ether.src% - %ARP.psrc%")
        ip = list_mac.split('-')[1].strip()
        list_mac = list_mac + ' - ' + str(getPCName(ip))
        print(list_mac)
