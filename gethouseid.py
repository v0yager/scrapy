# -*- coding: utf-8 -*-
import requests
import sys
import re

from sqlalchemy import create_engine,Column,Integer,String,Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

ID=0  #数据库id赋值

Base = declarative_base()
class HouseId(Base):
    __tablename__='houseid'
    id = Column(String(50),index=True)
    house_id = Column(String(50),primary_key=True,unique=True,index=True)	#house_id是主键，唯一,索引
    price = Column(String(50))
    unit_price = Column(String(50))
    room = Column(String(50))
    room_shi = Column(String(50))
    room_ting = Column(String(50))
    area = Column(String(50))
    district = Column(String(50))
    community = Column(String(50))
    address = Column(String(50))
    xiaoqu = Column(String(50))
    floor = Column(String(50))
    buildyear = Column(String(50))
    towards = Column(String(50))
    decoration = Column(String(50))
    buyyear = Column(String(50))

DB_URI = 'mysql+mysqldb://lianjia:lianjia@localhost/lianjia?charset=utf8'
engine = create_engine(DB_URI)
#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine) #创建house表
DB_Session = sessionmaker(bind=engine) #创建DB_session类型
session = DB_Session() #创建session对象
for i in range(1,100):
    url='http://sh.lianjia.com/ershoufang/d'+str(i)
    print url
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
    proxies={
        "http":"http://120.92.3.127",
        #"http":"http://222.61.20.147:808", 
    }
    r=requests.get(url,headers=headers)
    htmlhouseid=r.content

    reg_house_id=re.compile(r"(?<=\/ershoufang\/)sh\d+(?=\.html)")
    match_house_id=re.findall(reg_house_id,htmlhouseid)
    print match_house_id
    print type(match_house_id)

    house_id_list=list(set(match_house_id))
    #print house_id_list
    print house_id_list
    print len(house_id_list)

    query=session.query(House.house_id)
    for index in range(0,len(house_id_list)):
        
        new_house=House(id=ID+1,house_id=house_id_list[index])
        ID=ID+1
        session.merge(new_house)
        print house_id_list[index]
        session.commit()

#print session.query(House.house_id)
#session.commit()
#print  "查询第一列\n"
#query=session.query(House.house_id)
#for j in range(1,len(house_id_list)+1):
#     print query.filter_by(id=j).all()
print "mysql一共有%s行" % query.count()
session.close()
print "恭喜，%d个house_id已经存入mysql！" % (ID)
