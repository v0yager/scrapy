这是一个基于request库爬取链家二手房信息，并且用sqlalchemy存入mysql数据库,未完待续

####
现在已经把houseid存入数据库中

但是从数据库中拿出houseid时候，数据类型list[(u'sh4243494',)]，无法转换为string类型拼接成url，使用过类型转换还是无效。
####

下一步，程序更加pythonic，模块化规范化。

用flask框架完成web查询和可视化展现
