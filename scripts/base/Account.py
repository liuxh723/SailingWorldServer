# -*- coding: utf-8 -*-
import KBEngine
import time
import d_spaces
import d_avatar_inittab
from AVATAR_INFOS import TAvatarInfos
from KBEDebug import *

class Account(KBEngine.Proxy):
	def __init__(self):
		KBEngine.Proxy.__init__(self)
		self.activeAvatar = None
		self.relogin = time.time()
		
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
		if self.activeAvatar:
			self.activeAvatar.accountEntity = None
			self.activeAvatar = None

		DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
		self.destroy()

	def onDestroy(self):
		"""
		KBEngine method.
		entity销毁
		"""
		DEBUG_MSG("Account::onDestroy: %i." % self.id)
		
		if self.activeAvatar:
			self.activeAvatar.accountEntity = None

			try:
				self.activeAvatar.destroySelf()
			except:
				pass
				
			self.activeAvatar = None
	def reqCreateAvatar(self, country, sex, name):
		INFO_MSG("account[%i] reqCreateAvatar:%s" % (self.id, name))
		if self.Character != 0:
			self.client.onCreateAvatarResult(3, None)
			return

		if country == 1 or country == 2:
			spaceUType = 1
		if country == 3 or country == 4:
			spaceUType = 2
		if country == 5 or country == 6:
			spaceUType = 3
		props = {
			"PlayerName"		: name,
			"Sex"				: sex,
			"Level"				: 1,
			"Country"			: country,
			"Gold"				:1000,

			"spaceUType"		: spaceUType,
			#"direction"			: (0, 0, d_avatar_inittab.datas[roleType]["spawnYaw"]),
			"position"			: d_avatar_inittab.datas[country]["spawnPos"],

			#"component1"		: { "bb" : 1231, "state" : 456},
			#"component3"		: { "state" : 888 },
			}
			
		avatar = KBEngine.createEntityLocally('Avatar', props)
		if avatar:
			avatar.writeToDB(self._onAvatarSaved)

	def reqAvatar(self):
		DEBUG_MSG("Account[%i].reqAvatar:%i" % (self.id,self.Character))
		if self.Character != 0:
			avatar = KBEngine.createEntityFromDBID("Avatar", self.Character, self.__onAvatarCreated)
		else:
			self.client.onReqAvatar(0)


	"""
	Call Back
	"""
	def __onAvatarCreated(self, baseRef, dbid, wasActive):
		"""
		选择角色进入游戏时被调用
		"""
		if wasActive:
			ERROR_MSG("Account::__onAvatarCreated:(%i): this character is in world now!" % (self.id))
			return
		if baseRef is None:
			ERROR_MSG("Account::__onAvatarCreated:(%i): the character you wanted to created is not exist!" % (self.id))
			return
			
		avatar = KBEngine.entities.get(baseRef.id)
		if avatar is None:
			ERROR_MSG("Account::__onAvatarCreated:(%i): when character was created, it died as well!" % (self.id))
			return
		
		if self.isDestroyed:
			ERROR_MSG("Account::__onAvatarCreated:(%i): i dead, will the destroy of Avatar!" % (self.id))
			avatar.destroy()
			return
			
		#info = self.characters[dbid]
		#avatar.cellData["modelID"] = d_avatar_inittab.datas[info[2]]["modelID"]
		#avatar.cellData["modelScale"] = d_avatar_inittab.datas[info[2]]["modelScale"]
		#avatar.cellData["moveSpeed"] = d_avatar_inittab.datas[info[2]]["moveSpeed"]
		avatar.accountEntity = self
		self.activeAvatar = avatar
		self.giveClientTo(avatar)

	def _onAvatarSaved(self, success, avatar):
		"""
		新建角色写入数据库回调
		"""
		#INFO_MSG('Account::_onAvatarSaved:(%i) create avatar state: %i, %s, %i' % (self.id, success, avatar.cellData["name"], avatar.databaseID))
		
		# 如果此时账号已经销毁， 角色已经无法被记录则我们清除这个角色
		if self.isDestroyed:
			if avatar:
				avatar.destroy(True)		
			return

		if success:
			self.Character =  avatar.databaseID
			self.activeAvatar = avatar
			avatar.accountEntity = self
			self.writeToDB()
			if self.client:
				self.client.onCreateAvatarResult(1, avatar)
				self.giveClientTo(avatar)
		else:
			avatar.destroy()
			if self.client:
				self.client.onCreateAvatarResult(0, None)


		
		

