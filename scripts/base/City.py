# -*- coding: utf-8 -*-
import KBEngine
import d_city
from KBEDebug import *

class City(KBEngine.Proxy):
    def __init__(self):
        KBEngine.Proxy.__init__(self)
        DEBUG_MSG("City::__init__: city %i name: %s entityID=%i" % (self.CityID, self.CityName, self.id))
        self.initProperty()

    def initProperty(self):
        CityID = self.CityID
        self.CityName = d_city.datas[CityID]["CityName"]
        self.CityType = d_city.datas[CityID]["CityType"]
        self.CityCountry = d_city.datas[CityID]["CityCountry"]
        self.BusinessDvelopment = d_city.datas[CityID]["BusinessDvelopment"]
        self.MilitaryDvelopment = d_city.datas[CityID]["MilitaryDvelopment"]

    def onTimer(self, id, userArg):
        """
        KBEngine method.
        使用addTimer后， 当时间到达则该接口被调用
        @param id		: addTimer 的返回值ID
        @param userArg	: addTimer 最后一个参数所给入的数据
        """
        DEBUG_MSG(id, userArg)

    def reqSellGoodsList(self):
        INFO_MSG("account[%i] reqSellGoodsList" % self.id)

