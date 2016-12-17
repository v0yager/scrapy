# -*- coding: utf-8 -*-
from sqlalchemy import create_engine,Column,Integer,String,Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import requests
import sys
import re
'''for i in range(1,100):
    url='http://sh.lianjia.com/ershoufang/xuhui/d'+str(i)
    print url
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
    r=requests.get(url,headers=headers,timeout=7)
    htmlhouseid=r.content

#print html
#syscode=sys.getfilesystemencoding()                     #获取文件编码格式
#print syscode
#html=houseid.decode('utf-8').encode(syscode)      #html.decode(网页编码格式).encode(系统文件格式)

    #f=open("htmlhouseid.txt",'wb')                                         #保存文件到同一路径
    #f.write(htmlhouseid)
    #f.close()

    reg_house_id=re.compile(r"(?<=\/ershoufang\/)sh\d+(?=\.html)")
    match_house_id=re.findall(reg_house_id,htmlhouseid)
    print match_house_id
    print type(match_house_id)
    
    house_id_list=list(set(match_house_id))
#house_id.sort(match_house_id.index)
    #print house_id_list
'''
Base = declarative_base()
class House(Base):
    __tablename__='xuhui'
    id = Column(String(50))
    house_id = Column(String(50),primary_key=True,unique=True,index=True)	#house_id是主键，唯一,索引
    price = Column(String(50))
    unit_price = Column(String(50))
    room = Column(String(50))
    room_shi = Column(String(50))
    room_ting = Column(String(50))
    area = Column(String(50))
    district = Column(String(50))
    address = Column(String(50))
    xiaoqu = Column(String(50))
    floor = Column(String(50))
    buildyear = Column(String(50))
    towards = Column(String(50))
    decoration = Column(String(50))
    buyyear = Column(String(50))

DB_URI = 'mysql+mysqldb://lianjia:lianjia@localhost/lianjia?charset=utf8'
engine = create_engine(DB_URI,echo=True)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine) #创建house表
DB_Session = sessionmaker(bind=engine) #创建DB_session类型
session = DB_Session() #创建session对象
for i in range(1,100):
    url='http://sh.lianjia.com/ershoufang/xuhui/d'+str(i)
    print url
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
    r=requests.get(url,headers=headers,timeout=7)
    htmlhouseid=r.content

    reg_house_id=re.compile(r"(?<=\/ershoufang\/)sh\d+(?=\.html)")
    match_house_id=re.findall(reg_house_id,htmlhouseid)
    print match_house_id
    print type(match_house_id)

    house_id_list=list(set(match_house_id))
    #print house_id_list

    query=session.query(House.house_id)
    ID=query.count()

    for index in range(len(house_id_list)):
        new_house=House(id=ID+index,house_id=house_id_list[index])
        
        session.merge(new_house)
        print house_id_list[index]


#print session.query(House.house_id)
session.commit()
print  "查询第一列\n"
query=session.query(House.house_id)
for j in range(1,len(house_id_list)):
     print query.filter_by(id=j).all()
print "mysql一共有%s行" % query.count()
session.close()
print "恭喜，1000个house_id已经存入mysql！"
