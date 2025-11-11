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