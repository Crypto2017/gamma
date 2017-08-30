
class QueueError(Exception):
	def __init__(self,msg):
		self.message=msg
		
class Queue():
	def __init__(self,*itmes,maxsize=None):
		self.maxsize=maxsize
		self.items=list(items)
	def put(self,*items):
		dif=[]
		self.items.append(list(items))
		if self.maxsize!=None:
			if self.length()>self.maxsize:
				dif=self.items[self.maxsize:]
				self.itmes=self.items[:self.maxsize]
		return dif
	
	def attach(self,q):
		dif=[]
		self.items.extend(q.items)
		if self.maxsize!=None:
			if self.length()>self.maxsize:
				dif=self.items[self.maxsize:]
				self.itmes=self.items[:self.maxsize]
		return dif
		
	def get(self):
		if len(self.items)>0:
			item=self.items[0]
			self.items=self.items[1:]
			return item
		else:
			raise QueueError(" queue is empty.")
			
	def empty(self):
		if len(self.items)>0: return False
		return True
	def full(self):
		if self.maxsize!=None:
			if len(self.items)>=self.maxsize: return True
		return False
	def length(self):
		return len(self.items)
		
	def __len__(self):
		return self.length()
		
