
class QueueError(Exception):
	def __init__(self,msg):
		self.message=msg
		
class Queue():
	def __init__(self,*itmes):
		self.items=list(items)
	def add(self,*items):
		self.items.append(list(items))
		return self
	
	def attach(self,q):
		self.items.extend(q.items)
		return self
		
	def get(self):
		if len(self.items)>0:
			item=self.items[0]
			self.items=self.items[1:]
			return item
		else:
			raise QueueError(" queue is empty.")
			
	def is_empty(self):
		if len(self.items)>0: return False
		return True
		
	def length(self):
		return len(self.items)
		
	def __len__(self):
		return self.length()
		
