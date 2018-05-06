# -*- coding: utf-8 -*-
import KBEngine
import random
from KBEDebug import *
from interfaces.cardBase import cardBase
import d_card_dis


class CardInfo(cardBase):
    def __init__(self):
        DEBUG_MSG('Card.cell::__init__: [%i]  playerID:[%i]' % (self.id, self.playerID))
        cardBase.__init__(self)