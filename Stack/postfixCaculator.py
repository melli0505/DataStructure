class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0




def compute_postfix(postfix):
    result = Stack()
    l = list()
    while len(postfix) != 0:
        if postfix[0] not in '+-*/^':
            l.append(int(postfix.pop(0)))
        else:
            l.append(postfix.pop(0))

    while True:
        if l[0] == '+':
            b = result.pop()
            a = result.pop()
            result.push(a+b)
            l.pop(0)
        elif l[0] == '-':
            b = result.pop()
            a = result.pop()
            result.push(a-b)
            l.pop(0)
        elif l[0] == '*':
            b = result.pop()
            a = result.pop()
            result.push(a*b)
            l.pop(0)
        elif l[0] == '/':
            b = result.pop()
            a = result.pop()
            result.push(a/b)
            l.pop(0)
        elif l[0] == '^':
            b = result.pop()
            a = result.pop()
            result.push(a**b)
            l.pop(0)
        else:
            result.push(l.pop(0))

        if len(l) == 0:
            break
    
    #a = round(result.pop(), 6)
    return result.pop()
    #return a


ap = input()
expr = ap.split(' ')
#print(expr)

result_expr = compute_postfix(expr)
print('%.4f' %result_expr)
#print(result_expr)

