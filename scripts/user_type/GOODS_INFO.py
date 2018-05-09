# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class TCitySellGoodsInfo(list):
    """
    """
    def __init__(self):
        """
        """
        list.__init__(self)

    def asDict(self):
        data = {
            "CoodsID": self[0],
            "CoodsNum": self[1],
        }
        return data

    def createFromDict(self, dictData):
        self.extend([dictData["CoodsID"], dictData["CoodsNum"]])
        return self

class CITY_SELL_GOODS_INFO_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dict):
        return TCitySellGoodsInfo().createFromDict(dict)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TCitySellGoodsInfo)

city_sell_goods_info_inst = CITY_SELL_GOODS_INFO_PICKLER()

class TCitySellGoodsList(dict):
    """
    """

    def __init__(self):
        """
        """
        dict.__init__(self)

    def asDict(self):
        datas = []
        dct = {"values": datas}

        for key, val in self.items():
            datas.append(val)

        return dct

    def createFromDict(self, dictData):
        for data in dictData["values"]:
            self[data[0]] = data
        return self


class CITY_SELL_GOODS_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dct):
        return TCitySellGoodsList().createFromDict(dct)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TCitySellGoodsList)


city_sell_goods_list_inst = CITY_SELL_GOODS_LIST_PICKLER()

