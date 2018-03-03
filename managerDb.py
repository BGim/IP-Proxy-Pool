# -*- coding:utf8 -*-
import datetime
import time
import pymysql

class manager(object):
    def __init__(self,host,usr,passwd,dbase,Vaildip):
        super(manager,self).__init__()
        self.host=host
        self.usr=usr
        self.passwd=passwd
        self.dbase=dbase
        self.Vaildip=Vaildip
        self.index=0
        self.tnow=datetime.datetime.now()
        self.tdelay=self.tnow+datetime.timedelta(minutes=10)

    def connect(self):
        try:
            Db=pymysql.connect(self.host,self.usr,self.passwd,self.dbase,charset='utf8')
        except pymysql.Error as e:
            print("连接错误:",e)
            Db.rollback()
        pass
        return Db

    def insert(self,Database):
        cursor = Database.cursor()
        for self.index in range(len(self.Vaildip)-1):
            sql = "insert into proxy_ip VALUES ('%s','%s','%s')" % (self.Vaildip[self.index][0], self.Vaildip[self.index][1], time.ctime())
            cursor.execute(sql)
            Database.commit()
        Database.close()
        while self.tnow < self.tdelay:
            self.tnow = datetime.datetime.now()
            time.sleep(5)
            if self.tnow > self.tdelay:
                print("数据插入操作完成")

    def delete(self,Database):
        cursor = Database.cursor()
        while self.tnow<self.tdelay:
            self.tnow = datetime.datetime.now()
            time.sleep(5)
            if self.tnow>self.tdelay:
                sql="DELETE FROM `proxy_ip` order by Time limit 2 AND DELETE FROM `proxy_ip` WHERE IP=''"
                cursor.execute(sql)
                Database.commit()
            Database.close()
            print("数据删除操作完成")



