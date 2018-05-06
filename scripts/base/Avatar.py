# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from CARD_INFO import TCardInfo
from CARD_INFO import TCardList

class Avatar(KBEngine.Proxy):
    def __init__(self):
        KBEngine.Proxy.__init__(self)
        self.NameB = self.cellData["NameA"]
        self.bf = self.cellData["Battlefield"]
        self.cellData["playerID"] = self.PlayerIDB
        self.createCellEntity(self.bf )
        DEBUG_MSG('Avatar.Base::__init__: [%i]  playerID:[%i]' % (self.id, self.PlayerIDB))

    def onGetClient(self):
        DEBUG_MSG("Avatar.Base:playerID:[%i] onGetClient!" % self.PlayerIDB)

