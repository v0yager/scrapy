# -*- coding: utf-8 -*-
from sqlalchemy import create_engine,Column,Integer,String,Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import requests,re,sys
'''
url='http://sh.lianjia.com/ershoufang/'+HOUSE_ID+'.html'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}

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

house={'price':'','unit_pric':'','room':'','room_shi':'','room_ting':'','area':'','district':'','address':'','xiaoqu':'','floor':'','buildyear':'','decoration':'','towards':'','buyyear':''}	#定义房子为字典
reg_price=re.compile(r"(?<=mainInfo bold\">)\d+(?=<span class=\"unit\">万)")
match_price=re.search(reg_price,html)
house['price']=match_price.group(0)
price=house['price']

reg_room_shi=re.compile(r"(?<=mainInfo\">)\d+(?=<span class=\"unit\">室)")
match_room_shi=re.search(reg_room_shi,html)
#shi=match_room_shi.group(0)
house['room_shi']=match_room_shi.group(0)
#print shi
#print type(shi)
reg_room_ting=re.compile(r"(?<=室</span>\s)\d+(?=<span class=\"unit\">厅)")
match_room_ting=re.search(reg_room_ting,html)
#ting=match_room_ting.group(0)
#print ting
house['room_ting']=match_room_ting.group(0)


reg_room=re.compile(r"(?<=房屋户型\：</span>).+?(?=</li>)")
match_room=re.search(reg_room,html)
house['room']=match_room.group(0)

#print type(house['room'])
#reg_area=re.compile(r"(?<=mainInfo\">)\d+\.?\d+(?=<span class=\"unit\">平)")
reg_area=re.compile(r"(?<=建筑面积\：</span>).+?(?=</li>)")
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

#reg_floor=re.compile(r"(?<=</span>).+?\/\d层")
reg_floor=re.compile(r"(?<=所在楼层\：</span>).+?(?=</li>)")
match_floor=re.search(reg_floor,html)
house['floor']=match_floor.group(0)

reg_buildyear=re.compile(r"\d+年建")
match_buildyear=re.search(reg_buildyear,html)
house['buildyear']=match_buildyear.group(0)

reg_towards=re.compile(r"(?<=房屋朝向\：</span>).+?(?=</li>)")
match_towards=re.search(reg_towards,html)
house['towards']=match_towards.group(0)

reg_decoration=re.compile(r"(?<=装修情况\：</span>).+?(?=</li>)")
match_decoration=re.search(reg_decoration,html)
house['decoration']=match_decoration.group(0)

reg_buyyear=re.compile(r"(?<=房本年限\：</span>).+?(?=</li>)")
match_buyyear=re.search(reg_buyyear,html)
house['buyyear']=match_buyyear.group(0)

reg_unit_price=re.compile(r"\d+?元\/平")
match_unit_price=re.search(reg_unit_price,html)
house['unit_price']=match_unit_price.group(0)
print house
'''
Base = declarative_base()
class House(Base):
    __tablename__='xuhui'
    id = Column(String(50))
    house_id = Column(String(50),primary_key=True,unique=True)
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
#Base.metadata.drop_all(bind=engine)
#Base.metadata.create_all(bind=engine) #创建house表
DB_Session = sessionmaker(bind=engine) #创建DB_session类型
session = DB_Session() #创建session对象
query=session.query(House)
#count=query.count()
#HOUSE_ID=[0]*100
print query.filter_by(id=1).first()


for j in range(1,count):
    HOUSE_ID[j] = query.filter_by(id=j).all()
    print query.all()
    housesellid= HOUSE_ID[j].encode("utf-8")
    #print query.all()
    #print type(query.all())
    #housesellid=''.join(HOUSE_ID)
    #print housesellid

    url="http://sh.lianjia.com/ershoufang/"+housesellid+".html"
    print '第%d次查询的url是%s'% (j,url)
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}
    r=requests.get(url,headers=headers,timeout=7)
    html=r.content

    house={'price':'','unit_pric':'','room':'','room_shi':'','room_ting':'','area':'','district':'','address':'','xiaoqu':'','floor':'','buildyear':'','decoration':'','towards':'','buyyear':''}   #定义房子为字典
    
    reg_price=re.compile(r"(?<=mainInfo bold\">)\d+(?=<span class=\"unit\">万)")
    match_price=re.search(reg_price,html)
    house['price']=match_price.group(0)
    #price=house['price']

    reg_room_shi=re.compile(r"(?<=mainInfo\">)\d+(?=<span class=\"unit\">室)")
    match_room_shi=re.search(reg_room_shi,html)
    house['room_shi']=match_room_shi.group(0)
    
    reg_room_ting=re.compile(r"(?<=室</span>\s)\d+(?=<span class=\"unit\">厅)")
    match_room_ting=re.search(reg_room_ting,html)
    house['room_ting']=match_room_ting.group(0)

    reg_room=re.compile(r"(?<=房屋户型\：</span>).+?(?=</li>)")
    match_room=re.search(reg_room,html)
    house['room']=match_room.group(0)

    #reg_area=re.compile(r"(?<=mainInfo\">)\d+\.?\d+(?=<span class=\"unit\">平)")
    reg_area=re.compile(r"(?<=建筑面积\：</span>).+?(?=</li>)")
    match_area=re.search(reg_area,html)
    house['area']=match_area.group(0)

    reg_district=re.compile(r"(?<=areaEllipsis\">).+?(?=</span>)")
    match_district=re.search(reg_district,html)
    house['district']=match_district.group(0)

    reg_address=re.compile(r"(?<=addrEllipsis fl ml_5\" title=\").+?(?=\">)")
    match_address=re.search(reg_address,html)
    house['address']=match_address.group(0)

    reg_xiaoqu=re.compile(r"(?<=propertyEllipsis ml_5\">).+?(?=</a>)")
    match_xiaoqu=re.search(reg_xiaoqu,html)
    house['xiaoqu']=match_xiaoqu.group(0)

    #reg_floor=re.compile(r"(?<=</span>).+?\/\d层")
    reg_floor=re.compile(r"(?<=所在楼层\：</span>).+?(?=</li>)")
    match_floor=re.search(reg_floor,html)
    house['floor']=match_floor.group(0)

    reg_buildyear=re.compile(r"\d+年建")
    match_buildyear=re.search(reg_buildyear,html)    
    house['buildyear']=match_buildyear.group(0)

    reg_towards=re.compile(r"(?<=房屋朝向\：</span>).+?(?=</li>)")
    match_towards=re.search(reg_towards,html)
    house['towards']=match_towards.group(0)

    reg_decoration=re.compile(r"(?<=装修情况\：</span>).+?(?=</li>)")
    match_decoration=re.search(reg_decoration,html)
    house['decoration']=match_decoration.group(0)

    reg_buyyear=re.compile(r"(?<=房本年限\：</span>).+?(?=</li>)")
    match_buyyear=re.search(reg_buyyear,html)
    house['buyyear']=match_buyyear.group(0)

    reg_unit_price=re.compile(r"\d+?元\/平")
    match_unit_price=re.search(reg_unit_price,html)
    house['unit_price']=match_unit_price.group(0)

    new_house=House(price=house['price'],unit_price=house['unit_price'],room=house['room'],room_shi=house['room_shi'],room_ting=house['room_ting'],area=house['area'],district=house['district'],address=house['address'],xiaoqu=house['xiaoqu'],floor=house['floor'],buildyear=house['buildyear'],towards=house['towards'],decoration=house['decoration'],buyyear=house['buyyear']) #创建House对象

    session.merger(new_house) #添加到session

session.commit() #提交即保存到数据库
session.close() #关闭session
