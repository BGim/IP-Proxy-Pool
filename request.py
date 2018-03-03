import urllib.request
import datetime
import time
import random

class scrapy(object):

    def __init__(self):
        super(scrapy,self).__init__()
        self.url='https://mp.weixin.qq.com/s?__biz=MjM5NjUwMTE1Ng==&mid=2652902136&idx=1&sn=bcd64166e2897c6f0843be6724015a51&chksm=bd3cf1338a4b7825be0ab4c6f8233c152f8e452ce5c06886b18692a317f88cefde4250b26b54&scene=0&key=5bd52544ea7dc71ba1dbc3821c63d8961386f4de15d3bfc42aada95c2c2e2acdec3eb3e2f88570d0b69769bff5578e8d0dd6e58ced8c65082504a7f1813c118e95ad385070383552ffebb8dc1616ef00&ascene=1&uin=MjQ5NjQwMTMwMg%3D%3D&devicetype=Windows+8&version=6204014f&pass_ticket=i6L7%2BiIlNUkp0XC%2BSgKEUpaDnp8WEaN3XZB1Zh7bpC6foxi20JLY%2FeZ07kvzsLfs&winzoom=1'
        self.header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.373.400 QQBrowser/9.0.2524.400'}
        
    def get_url(self): 
        try:
            req = urllib.request.Request(self.url,headers=self.header)
            html = urllib.request.urlopen(req).read()
            now=time.ctime()
            i=random.uniform(3,7)
            print("请求时间：%s"%(now))
            if urllib.request.urlopen(req).code==200:
                time.sleep(i)
                s=time.strptime(now)
                Hour,Min,Sec=s.tm_hour,s.tm_min,s.tm_sec
                if datetime.time(8,10)<datetime.time(Hour,Min,Sec)<datetime.time(11,22):
                    return self.get_url()
                else:
                    while True:
                        time.sleep(2)
                        if datetime.time(8,10)<datetime.time(Hour,Min,Sec)<datetime.time(11,22):
                            break
                    return self.get_url()
        except urllib.error.HTTPError as e:
            print("请求错误代码：%d"%(e.code))

S=scrapy()
S.get_url()
