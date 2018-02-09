# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Qnq3Item(scrapy.Item):
    #商品型号
    p_Name = scrapy.Field()
    #店铺名称
    shop_name = scrapy.Field()
    #商品ID
    ProductID = scrapy.Field()
    #正价
    price = scrapy.Field()
    #折扣价
    PreferentialPrice = scrapy.Field()
    #评论总数
    CommentCount = scrapy.Field()
    #好评度
    GoodRateShow = scrapy.Field()
    #好评
    GoodCount = scrapy.Field()
    #中评
    GeneralCount = scrapy.Field()
    #差评
    PoorCount = scrapy.Field()
    #评论关键字
    keyword = scrapy.Field()
    #商品详情
    type = scrapy.Field()
    #品牌
    brand = scrapy.Field()
    #商品型号
    X_name = scrapy.Field()
    #类型(电热油汀等)
    X_type = scrapy.Field()
    # 放置方式，款式
    placement= scrapy.Field()
    # 功率
    power = scrapy.Field()
    # 负离子功能
    Negative = scrapy.Field()
    # 加热片数量
    brand_num = scrapy.Field()
    # 产品尺寸
    size = scrapy.Field()
    # 防水功能
    waterproof = scrapy.Field()
    # 商品链接
    product_url = scrapy.Field()
    # 来源
    source = scrapy.Field()
    # 爬取时间
    ProgramStarttime = scrapy.Field()

    # 加湿功能无，空气净化==负离子功能，功能性功能没有

