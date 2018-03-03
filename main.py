# -*- coding:utf8 -*-
pass
#
#   西刺ip代理池
#
pass
#create_time=2017/8/21
#author=zyy

from ip_test import get_ip
from managerDb import manager
from configure import *
import time
import threading
import datetime
import random

class start_proxy(threading.Thread):
    def __init__(self,init_proxy,No,threadLock):
        threading.Thread.__init__(self)
        self.init_proxy = init_proxy
        self.iplist=[]
        self.threadLock = threadLock
        self.No = No

    def run(self):
        print("线程启动",self.No)
        # 获取锁，用于线程同步
        #self.threadLock.acquire()
        self.iplist=proxy_ip(self.init_proxy)
        # 释放锁，开启下一个线程
        #self.threadLock.release()
        print("退出线程",self.No)

    def result(self):
        return self.iplist

class main(object):
    def __init__(self,host,usr,passwd,dbase):
        self.page=1
        self.host=host
        self.usr=usr
        self.passwd=passwd
        self.dbase=dbase

    def main(self):
        iplist=[]
        threads = []
        url = 'http://www.xicidaili.com/wt/' + str(self.page)
        tnow=datetime.datetime.now()
        tdelay = tnow + datetime.timedelta(minutes=1)
        threadLock=threading.Lock()
        if tnow <= tdelay:

            # 注册代理ip类
            init_proxy = get_ip(url, header)
            init_proxy.request()  # 请求xici页面即解析html

            for i in range(10):
                t=start_proxy(init_proxy,i,threadLock)
                t.start()
                threads.append(t)
            for t in threads:
                t.join()

            #print(t.result())

            # 注册数据库管理类
            init_manager = manager(host, usr, passwd, dbase,t.result())
            init_Db = init_manager.connect()  # 初始化数据库
            init_manager.insert(init_Db)      # 插入数据集
            init_manager.delete(init_Db)     # 删除冗余ip

            # 每十分钟请求一次
            while True:
                time.sleep(5)
                tnow = datetime.datetime.now()  # 刷新当前时间
                if tnow >= tdelay:
                    self.page += 1
                    return self.main()                # 递归请求

def proxy_ip(arg):
    iplist = arg.checkip()  # 检查ip是否有效
    return iplist

if __name__=='__main__':
    m=main(host,usr,passwd,dbase)
    m.main()

    
    
    
    
