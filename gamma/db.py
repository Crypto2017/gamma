import pickle
class DataBase():
	def __init__(self,path="."):
		self.path=path
		
	def createTable(self,name):
		pass
	def createPool(self,name):
		pass
	def get(self,name):
		pass
	def __getitem__(self,name):
		return self.get(name)

class Unit():
	def __init__(self,path):
		self.path=path
	def get(self,key):
		pass
	def set(self,key,inf):
		pass
	def update(self,key,inf):
		pass		

class Table(Unit):
	def __init__(self,path):
		pass
		
class Pool(Unit):
	def __init__(self,path):
		pass
	
class MultiThreadDB(Unit):
	def __init__(self,path):
		self.index={}
		pass
