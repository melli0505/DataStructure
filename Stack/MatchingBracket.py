class Stack:
	def __init__(self):
		self.item = []
		
	def push(self, val):
		self.item.append(val)
	
	def pop(self):
		try:
			self.item.pop()
		except IndexError:
			return 0
			#print("Stack is empty")
	
	def top(self):
		try:
			return self.item[-1]
		except:
			print("Stack is empty")
		
	def __len__(self):
		return len(self.item)
	
	# def isEmpty(self):
	# 	return self.__len__() = 0
	
	
# pseudo code
def parChecker(parSeq):
	S = Stack()
	for p in parSeq:
		if p == '(':
			S.push(p)
		elif p == ')':
			S.pop()
		else: print("Not allowed symbol")
	if len(S) > 0: return False
	else: return True
	
	
print(parChecker(input()))