import pickle
class DataBase():
	def __init__(self,path="."):
		self.path=path

class Unit():
	def __init__(self,path):
		self.path=path

class Table(Unit):
	def __init__(self,path):
		pass
		
class Pool(Unit):
	def __init__(self,path):
		pass
