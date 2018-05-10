# -*- coding: utf-8 -*-
import KBEngine
import d_city
import SCDefine
import random

from GOODS_INFO import TCityTypePriceInfo
from GOODS_INFO import TCitySellGoodsInfo

from KBEDebug import *

class City(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)

        CityID = self.CityID
        self.CityName = d_city.datas[CityID]["CityName"]
        self.CityType = d_city.datas[CityID]["CityType"]
        self.addTimer(3, 10, SCDefine.TIMER_TYPE_GOODS_TYPE_PRICR_RACE)
        DEBUG_MSG("City::__init__: city %i name: %s entityID=%i" % (self.CityID, self.CityName, self.id))
        #dic = {"GoodsType": 1, "TypePrice": 1.0}
        #self.TypePriceList.append(dic)

        #self.writeToDB()

    def initProperty(self):
        DEBUG_MSG("City::initProperty city %i name: %s entityID=%i" % (self.CityID, self.CityName, self.id))
        CityID = self.CityID
        self.CityCountry = d_city.datas[CityID]["CityCountry"]
        self.BusinessDvelopment = d_city.datas[CityID]["BusinessDvelopment"]
        self.MilitaryDvelopment = d_city.datas[CityID]["MilitaryDvelopment"]
        for i in range(16):
            dic = {"GoodsType": i, "TypePrice": 1.0}
            self.TypePriceList.append(dic)
        self.writeToDB()
        

        

    def onTimer(self, id, userArg):
        """
        KBEngine method.
        使用addTimer后， 当时间到达则该接口被调用
        @param id		: addTimer 的返回值ID
        @param userArg	: addTimer 最后一个参数所给入的数据
        """
        #self.TypePriceList[1]["TypePrice"] = self.TypePriceList[1]["TypePrice"] +0.1
        #DEBUG_MSG(id, userArg)
        if userArg == SCDefine.TIMER_TYPE_GOODS_TYPE_PRICR_RACE:
             #DEBUG_MSG("City[%i]::TypePriceList :type%i price:%f" % (self.CityID, 1,self.TypePriceList[1]["TypePrice"]))
             self.RandomPrice()
             self.writeToDB()

    def RandomPrice(self):
        for info in self.TypePriceList:
            info["TypePrice"] += random.uniform(-0.1, 0.1)
            if info["TypePrice"] > 1.5:
                info["TypePrice"] = 1.5
            if info["TypePrice"] < 0.5:
                info["TypePrice"] = 0.5

    def reqSellGoodsList(self):
        INFO_MSG("account[%i] reqSellGoodsList" % self.id)

