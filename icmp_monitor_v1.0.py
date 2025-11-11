#Icmp_Monitor_Version_1.0_20251111
#Author:Zeng Xianglong/Nowasiki zengxianglong53@outlook.com zengxinaglong@nbut.edu.cn
#Features:This program could automatically detect your platform and change the parameters.And it could output the result.
import time
import platform
import os
def ping(host):
    system=platform.system()
    if system == "Windows" :
        result=os.popen(f"ping -n 4 {host}").read()
    else: result=os.popen(f"ping -n 4 {host}").read()
    print(result)
print("正在监控网络")
ping("baidu.com")