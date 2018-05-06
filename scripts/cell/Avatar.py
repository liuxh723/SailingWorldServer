# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *
from interfaces.cardBase import cardBase
import d_card_dis


class Avatar(cardBase):
    def __init__(self):
        DEBUG_MSG('Avatar.cell::__init__: [%i]  playerID:[%i]' % (self.id, self.playerID))
        self.cardID = (20003000 + self.RoleType)
        cardBase.__init__(self)
        cardBase.initProperty(self)

        self.CardEnityList = []
        self.CardEnityList.append(self)
        self.CreateCardEntity(20001000 + self.RoleType,"SKILL")
        self.creatCardListEntity()

        self.Battlefield.AvatarRegiste(self, self.playerID)

    def CreateCardEntity(self,cardID,pos = "KZ"):
        DEBUG_MSG('Avatar[%i].cell::creat cardennity cardID:[%i]' % (self.id, cardID))
        params = {
            'cardID': cardID,
            'battlefield': self.Battlefield,
            'avatar': self,
            'playerID':self.playerID
                    }
        entity = KBEngine.createEntity("CardInfo",self.spaceID,tuple(self.position),tuple(self.direction),params)
        self.CardEnityList.append(entity)

    def creatCardListEntity(self):
        for cardInfo in self.CardList["values"]:
            self.CreateCardEntity(cardInfo[0])
