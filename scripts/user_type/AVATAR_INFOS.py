# -*- coding: utf-8 -*-
import KBEngine
import GlobalConst
from KBEDebug import * 

class TAvatarInfos(list):
	"""
	"""
	def __init__(self):
		"""
		"""
		list.__init__(self)
		
	def asDict(self):
		data = {
			"dbid"			: self[0],
			"Name"			: self[1],
			"RoleType"		: self[2],
			"Country"		: self[3],
			"Sex"			: self[4],
			"Level"			: self[5],
			"Gold"			: self[6],
		}
		
		return data

	def createFromDict(self, dictData):
		self.extend([dictData["dbid"], dictData["Name"], dictData["RoleType"], dictData["Country"], dictData["Sex"], dictData["Level"], dictData["Gold"]])
		return self
		
class AVATAR_INFOS_PICKLER:
	def __init__(self):
		pass

	def createObjFromDict(self, dct):
		return TAvatarInfos().createFromDict(dct)

	def getDictFromObj(self, obj):
		return obj.asDict()

	def isSameType(self, obj):
		return isinstance(obj, TAvatarInfos)

avatar_info_inst = AVATAR_INFOS_PICKLER()