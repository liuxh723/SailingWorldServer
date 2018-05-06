# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Hall(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        DEBUG_MSG("Hall init")
        #save hall
        KBEngine.globalData["Halls"] = self

        #存放正在匹配玩家mailbox
        self.OnMatchingPlayer = []

        self.addTimer(6,3,1)

    def reqAddMatcher(self,player):
        DEBUG_MSG("Hall:Account[%i].reqAddMatcher"% player.id)
        if player in self.OnMatchingPlayer:
            return
        self.OnMatchingPlayer.append(player)

    def reqRemoveMatcher(self,player):
        DEBUG_MSG("Hall: Account[%i].reqRemoveMatcher"% player.id)
        if player in self.OnMatchingPlayer:
            self.OnMatchingPlayer.remove(player)
            return


    def Match(self):
        #DEBUG_MSG("Hall:Matchplayer num[%s]"% len(self.OnMatchingPlayer))
        if(len( self.OnMatchingPlayer) > 1):
            players = [self.OnMatchingPlayer[0],self.OnMatchingPlayer[1]]
            self.MatchSuccess(players)
            del self.OnMatchingPlayer[1]
            del self.OnMatchingPlayer[0]

    def MatchSuccess(self,players):
        DEBUG_MSG("Hall: MatchSuccess player")
        prarms = {
            "Player0":players[0],
            "Player1":players[1]
        }
        Battlefield  = KBEngine.createEntityAnywhere("Battlefield",prarms)


    def onTimer(self, id, userArg):
        """
        KBEngine method.
        使用addTimer后， 当时间到达则该接口被调用
        @param id		: addTimer 的返回值ID
        @param userArg	: addTimer 最后一个参数所给入的数据
        """
        if userArg == 1:
            self.Match()


