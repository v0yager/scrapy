# -*- coding: utf-8 -*-
from sqlalchemy import create_engine,Column,Integer,String,Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import requests,re,sys
HOUSE_ID='sh4251963'
url='http://sh.lianjia.com/ershoufang/'+HOUSE_ID+'.html'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
# HTTP代理 #
'''proxies={
        "http":"http://192.168.1.4:8080"
}
'''
# HTTP代理 #
#s=requests.session()
r=requests.get(url,headers=headers,timeout=7)

html=r.content
#print html
syscode=sys.getfilesystemencoding()			#获取文件编码格式
print syscode
#html=html.decode('utf-8').encode(syscode)	#html.decode(网页编码格式).encode(系统文件格式)

f=open("html.txt",'wb')						#保存文件到同一路径
f.write(html)
f.close()
house={'price':'','room':'','area':'','district':'','address':'','xiaoqu':''}
reg_price=re.compile(r"(?<=mainInfo bold\">)\d+(?=<span class=\"unit\">万)")
match_price=re.search(reg_price,html)
house['price']=match_price.group(0)
price=house['price']

reg_shi=re.compile(r"(?<=mainInfo\">)\d+(?=<span class=\"unit\">室)")
match_shi=re.search(reg_shi,html)
shi=match_shi.group(0)
#print shi
#print type(shi)
reg_ting=re.compile(r"(?<=室</span>\s)\d+(?=<span class=\"unit\">厅)")
match_ting=re.search(reg_ting,html)
ting=match_ting.group(0)
#print ting
house['room']=(shi,ting)
#print type(house['room'])
reg_area=re.compile(r"(?<=mainInfo\">)\d+\.?\d+(?=<span class=\"unit\">平)")
match_area=re.search(reg_area,html)
house['area']=match_area.group(0)

reg_district=re.compile(r"(?<=areaEllipsis\">).+?(?=</span>)")
match_district=re.search(reg_district,html)
house['district']=match_district.group(0)
#district=house['district']
#print type(district)
#print district

reg_address=re.compile(r"(?<=addrEllipsis fl ml_5\" title=\").+?(?=\">)")
match_address=re.search(reg_address,html)
house['address']=match_address.group(0)

reg_xiaoqu=re.compile(r"(?<=propertyEllipsis ml_5\">).+?(?=</a>)")
match_xiaoqu=re.search(reg_xiaoqu,html)
house['xiaoqu']=match_xiaoqu.group(0)
print house

Base = declarative_base()
class House(Base):
    __tablename__='house'

    house_id = Column(String(50),primary_key=True)
    price = Column(String(50))
    room = Column(String(50))
    area = Column(String(50))
    district = Column(String(50))
    address = Column(String(50))
    xiaoqu = Column(String(50))

DB_URI = 'mysql+mysqldb://lianjia:lianjia@localhost/lianjia?charset=utf8'
engine = create_engine(DB_URI,echo=True)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine) #创建house表
Session = sessionmaker(bind=engine)
session = Session()
new_house=House(house_id=HOUSE_ID,price=house['price'],room=str(house['room']),area=house['area'],district=house['district'],address=house['address'],xiaoqu=house['xiaoqu']) #存入数据库
#session.add_all([House(house_id='sh4159824')])
#print house['price']
session.add(new_house)

session.commit()
