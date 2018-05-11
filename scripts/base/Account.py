# -*- coding: utf-8 -*-
import KBEngine
from AVATAR_INFOS import TAvatarInfos
from KBEDebug import *

class Account(KBEngine.Proxy):
	def __init__(self):
		KBEngine.Proxy.__init__(self)
		
	def onTimer(self, id, userArg):
		"""
		KBEngine method.
		使用addTimer后， 当时间到达则该接口被调用
		@param id		: addTimer 的返回值ID
		@param userArg	: addTimer 最后一个参数所给入的数据
		"""
		DEBUG_MSG(id, userArg)
		
	def onClientEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		INFO_MSG("account[%i] entities enable. entityCall:%s" % (self.id, self.client))
			
	def onLogOnAttempt(self, ip, port, password):
		"""
		KBEngine method.
		客户端登陆失败时会回调到这里
		"""
		INFO_MSG(ip, port, password)
		return KBEngine.LOG_ON_ACCEPT
		
	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
		self.destroy()

	def reqCreateAvatar(self, country, sex, name):
		INFO_MSG("account[%i] reqCreateAvatar:%s" % (self.id, name))
		avatarinfo = TAvatarInfos()
		avatarinfo.extend([0, "", 0, 0, )])

		if self.Character != None:
			self.client.onCreateAvatarResult(3, avatarinfo)
			return
		props = {
			"name"				: name,
			"roleType"			: roleType,
			"level"				: 1,
			"spaceUType"		: spaceUType,
			"direction"			: (0, 0, d_avatar_inittab.datas[roleType]["spawnYaw"]),
			"position"			: spaceData.get("spawnPos", (0,0,0)),

			"component1"		: { "bb" : 1231, "state" : 456},
			"component3"		: { "state" : 888 },
			}
			
		avatar = KBEngine.createEntityLocally('Avatar', props)
		if avatar:
			avatar.writeToDB(self._onAvatarSaved)
		self.Country = country
		self.Sex = sex
		self.Name = name

	def reqAvatar(self):
		DEBUG_MSG("Account[%i].reqAvatar:" % self.id)
		if self.Character != None:
			self.client.onReqAvatar(1,self.Character)
		else:
			self.client.onReqAvatar(0,self.Character)

