# -*- coding: utf-8 -*-
import KBEngine
import random
import copy
import math
from KBEDebug import *
from interfaces.GameObject import GameObject
import d_spaces
import d_city
import Functor
import xml.etree.ElementTree as etree 

class Space(KBEngine.Entity, GameObject):
	"""
	一个可操控cellapp上真正space的实体
	注意：它是一个实体，并不是真正的space，真正的space存在于cellapp的内存中，通过这个实体与之关联并操控space。
	"""
	def __init__(self):
		KBEngine.Entity.__init__(self)
		GameObject.__init__(self)
		#self.createCellEntityInNewSpace(None)
		
		#self.spaceUTypeB = self.cellData["spaceUType"]
		
		#self.spaceResName = d_spaces.datas.get(self.spaceUTypeB)['resPath']

		#self._city = list(d_city.datas.keys())
		for CityID in d_city.datas.keys():
			if d_city.datas[CityID]["SpaceID"] == self.spaceUType:
				KBEngine.createEntityAnywhere("City",{"CityID":CityID,"CityName":d_city.datas[CityID]["CityName"]},Functor.Functor(self.onCityCreatedCB, CityID))

	def onCityCreatedCB(self, CityID, space):
		"""
		一个space创建好后的回调
		"""
		DEBUG_MSG("Spaces::onCityCreatedCB: city %i. spaceID=%i" % (CityID, self.id))	
		
	def loginToSpace(self, avatarEntityCall, context):
		"""
		defined method.
		某个玩家请求登陆到这个space中
		"""
		avatarEntityCall.createCell(self.cell)
		self.onEnter(avatarEntityCall)
		
	def logoutSpace(self, entityID):
		"""
		defined method.
		某个玩家请求登出这个space
		"""
		self.onLeave(entityID)
		
	def teleportSpace(self, entityCall, position, direction, context):
		"""
		defined method.
		请求进入某个space中
		"""
		entityCall.cell.onTeleportSpaceCB(self.cell, self.spaceUTypeB, position, direction)

	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		#DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.getScriptName(), self.id, tid, userArg))
		if SCDefine.TIMER_TYPE_SPACE_SPAWN_TICK == userArg:
			self.spawnOnTimer(tid)
		
		GameObject.onTimer(self, tid, userArg)
		
	def onEnter(self, entityCall):
		"""
		defined method.
		进入场景
		"""
		self.avatars[entityCall.id] = entityCall
		
		if self.cell is not None:
			self.cell.onEnter(entityCall)
		
	def onLeave(self, entityID):
		"""
		defined method.
		离开场景
		"""
		if entityID in self.avatars:
			del self.avatars[entityID]
		
		if self.cell is not None:
			self.cell.onLeave(entityID)

	def onLoseCell(self):
		"""
		KBEngine method.
		entity的cell部分实体丢失
		"""
		KBEngine.globalData["Spaces"].onSpaceLoseCell(self.spaceUTypeB, self.spaceKey)
		GameObject.onLoseCell(self)
		
	def onGetCell(self):
		"""
		KBEngine method.
		entity的cell部分实体被创建成功
		"""
		DEBUG_MSG("Space::onGetCell: %i" % self.id)
		self.addTimer(0.1, 0.1, SCDefine.TIMER_TYPE_SPACE_SPAWN_TICK)
		KBEngine.globalData["Spaces"].onSpaceGetCell(self.spaceUTypeB, self, self.spaceKey)
		GameObject.onGetCell(self)
		

