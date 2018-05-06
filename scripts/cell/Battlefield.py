# -*- coding: utf-8 -*-
import KBEngine
import d_card_dis
import random
import re
from KBEDebug import *
from array import *


class Battlefield(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        DEBUG_MSG('BattleField.cell::__init__')
        self.player0 = None
        self.player1 = None

    def AvatarRegiste(self,avatarEntity,playerID):
        DEBUG_MSG('BattleField.cell::AvatarRegiste[%i]' % playerID)
        if playerID == 1:
            self.player1 = avatarEntity
        elif playerID == 0:
            self.player0 = avatarEntity
        if self.player0 != None and self.player1 != None:
            self.players = [
                self.player0,
                self.player1,
            ]
            self.startBattle();

    def startBattle(self):
        DEBUG_MSG('BattleField.cell::startBattle!')

    def getAllEntity(self):
        return self.player0.CardEnityList + self.player1.CardEnityList