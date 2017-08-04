# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class HouseItem(Item):
    title = Field()  #标题
    link = Field()  #链接
    price = Field()  #价格
    time_unit = Field()  #价格对应的时间单位（每天，每月）
    area = Field()  #面积(㎡)
    rooms = Field()  #几居室
    halls = Field()  #几厅
    rentType = Field()  #租借类型(合，整，直)
    floorLoc = Field()  #房间所在楼层
    floorTotal = Field()  #大楼总层数
    lng = Field()  #房间所在经度
    lat = Field()  #房间所在维度
    direction = Field()  #房屋朝向
    confGen = Field()  #第几代配置
    confType = Field()  #配置风格(布丁，木棉等)
    privateBathroom = Field()  #是否有独立卫生间(0:否,1:是)
    privateBalcony = Field()  #是否有独立阳台(0:否,1:是)
    heatingType = Field()  #供暖方式(0:集体供暖,1:独立供暖,2:中央空调)
    nearestSubWayDist = Field()  #最近地铁距离(m)
    confStatus = Field()  #房屋配置状态(0:配置中,1:配置完成)
    district = Field()  #区(东城、西城、朝阳、海淀、丰台、石景山、门头沟、房山、大兴、通州、顺义、昌平、平谷、怀柔、密云、延庆、亦庄开发区)
