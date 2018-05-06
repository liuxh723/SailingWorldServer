# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Battlefield(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        DEBUG_MSG("Battlefield[%s] created！" % self.id)
        self.createCellEntityInNewSpace(None)

    def onGetCell(self):
        DEBUG_MSG("Battlefield[%s] Cell created！"% self.id)
        self.Player0.onMatchSuccess(self.cell,0)
        self.Player1.onMatchSuccess(self.cell,1)






