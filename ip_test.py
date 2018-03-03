# -*- coding:utf8 -*-
import urllib.request
import time
import random
import socket
from pyquery import PyQuery as pq
from collections import deque

class get_ip(object):
    def __init__(self,arg,agent):
        super(get_ip, self).__init__()
        self.ipNo=1
        self.index=0
        self.checkUrl="http://www.baidu.com/"
        self.arg = arg
        self.iplist=[]
        self.agent=agent
        self.queue=deque([])


    def request(self):
        try:
            req=urllib.request.Request(self.arg,headers=self.agent)
            html=urllib.request.urlopen(req).read()
            qt=pq(html)
            table=qt('table').children()
            for self.index in range(len(table('tr'))):
                #print ("ip:",table('tr').find('td').eq(1))
                #print ("ip-port:",table('tr').find('td').eq(2))
                self.queue.append([table('tr').eq(self.ipNo).find('td').eq(1).text(),table('tr').eq(self.ipNo).find('td').eq(2).text()])
                self.ipNo+=1
            return self.queue
        except urllib.error.HTTPError as e:
            if 500<e.code<600:
                self.request()
            elif e.code==404:
                print("404")

    def checkip(self):
        #iplist=[]
        #for self.index in range(len(self.queue)):
        while len(self.queue):
            #print("队列总长度:",len(self.queue))
            proxy=self.queue.popleft()
            proxie={'http':'http://%s:%s'%(proxy[0],proxy[1])}
            handler=urllib.request.ProxyHandler(proxies=proxie)
            openr=urllib.request.build_opener(handler)
            openr.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
            try:
                repcode=openr.open(self.checkUrl,timeout=10).code
                time.sleep(random.uniform(10,15))
                if repcode==200:
                    self.iplist.append(proxy)
                    print("有效ip:%s-状态码:%d" % (proxy, repcode))
                else:
                    print("无效ip:%s-状态码:%d" % (proxy, repcode))
            except urllib.error.HTTPError as e:
                print("无效ip:%s-状态码:%d" % (proxy, e.code))
                self.checkip()
            except urllib.error.URLError as e:
                print("无效ip:%s-状态码:%s" % (proxy, e))
                self.checkip()
            except socket.timeout as e:
                print("无效ip:%s-状态码:%s"%(proxy,e))
                self.checkip()
            except socket.error as e:
                print("无效ip:%s-状态码:%s"%(proxy,e))
                self.checkip()
        return self.iplist


