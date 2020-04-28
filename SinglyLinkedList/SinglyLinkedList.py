class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None
	def __str__(self):
		return str(self.key)
	
class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def __iter__(self):
		v = self.head
		while v is not None:
			yield v
			v = v.next
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")
		

	def pushFront(self, key):
		v = Node(key)
		v.next =self.head
		self.head = v
		self.size += 1

	def pushBack(self, key):
		v = Node(key)
		if len(self) == 0:
			self.head = v
		else:
			tail = self.head
			while tail.next is not None:
				tail = tail.next
			tail.next = v
		self.size += 1

	def popFront(self):
		# head 노드의 값 리턴. empty list이면 None 리턴
		if len(self) == 0:
			return None
		else:
			x = self.head
			key = x.key
			self.head = x.next
			self.size -= 1
			del x
			return key

	def popBack(self):
		# tail 노드의 값 리턴. empty list이면 None 리턴
		if len(self) == 0:
			return None
		else: 
			prev = None
			tail = self.head
			while tail.next != None:
				prev = tail
				tail = tail.next
			if len(self) == 1:
				self.head = None
			else:
				prev.next = tail.next
			key = tail.key
			del tail
			self.size -= 1
			return key

	def search(self, key):
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		v = self.head
		while v:
			if v.key == key:
				return v
			v = v.next
		return None

	def remove(self, x):
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
		# x는 key 값이 아니라 노드임에 유의!
		v = self.head
		prev = None
		if x == None:
			return False
		elif x == self.head:
			self.head = v.next
			self.size -= 1
			return True
		while v:
			if v.next == x:
				v.next = x.next
				self.size -= 1
				return True
			v = v.next

	def sizeOfList(self):
		return self.size