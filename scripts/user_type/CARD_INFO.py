# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class TCardInfo(list):
    """
    """
    def __init__(self):
        """
        """
        list.__init__(self)

    def asDict(self):
        data = {
            "CardID": self[0],
            "CardNum": self[1],
        }
        return data

    def createFromDict(self, dictData):
        self.extend([dictData["CardID"], dictData["CardNum"]])
        return self

class CARD_INFO_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dict):
        return TCardInfo().createFromDict(dict)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TCardInfo)


card_info_inst = CARD_INFO_PICKLER()


class TCardList(dict):
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


class CARD_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dct):
        return TCardList().createFromDict(dct)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TCardList)


card_list_inst = CARD_LIST_PICKLER()

class TGroupCardList(dict):
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


class GROUP_CARD_LIST_PICKLER:
    def __init__(self):
        pass

    def createObjFromDict(self, dct):
        return TGroupCardList().createFromDict(dct)

    def getDictFromObj(self, obj):
        return obj.asDict()

    def isSameType(self, obj):
        return isinstance(obj, TGroupCardList)


group_card_list_inst = GROUP_CARD_LIST_PICKLER()