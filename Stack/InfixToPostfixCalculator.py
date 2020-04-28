'''
Infix to postfix
'''


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


def infix_to_postfix(infix):
    opstack = Stack()
    outstack = []
    #token_list = infix.split(' ')

    # 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in infix:
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while opstack.top() != '(':
                outstack.append(opstack.pop())
            opstack.pop()
        elif token == '+' or token == '-' or token == '*' or token == '/' or token == '^':
            if opstack.isEmpty() == True:
                opstack.push(token)
            elif prec[token] > prec[opstack.top()]:
                opstack.push(token)
            else:  # operand일 때
                while prec[opstack.top()] >= prec[token]:
                    outstack.append(opstack.pop())
                    if opstack.isEmpty() == True: break
                opstack.push(token)
        else:
            outstack.append(token)

    while opstack.isEmpty() == False:
        outstack.append(opstack.pop())
    return outstack


def compute_postfix(postfix):
    result = Stack()
    while True:
        if postfix[0] == '+':
            b = result.pop()
            a = result.pop()
            result.push(a+b)
            postfix.pop(0)
        elif postfix[0] == '-':
            b = result.pop()
            a = result.pop()
            result.push(a-b)
            postfix.pop(0)
        elif postfix[0] == '*':
            b = result.pop()
            a = result.pop()
            result.push(a*b)
            postfix.pop(0)
        elif postfix[0] == '/':
            b = result.pop()
            a = result.pop()
            result.push(a/b)
            postfix.pop(0)
        elif postfix[0] == '^':
            b = result.pop()
            a = result.pop()
            result.push(a**b)
            postfix.pop(0)
        else:
            result.push(postfix.pop(0))

        if len(postfix) == 0:
            break

    # a = result.pop*.4
    # return a
    return result.pop()


def get_token_list(expr):
    postfix = list()
    index1 = 0
    i = expr[index1]
    while index1 < len(expr):
        i = expr[index1]
        if i == ' ':
            index1 += 1
            continue
        elif i in '()+-/*^':
            postfix.append(i)
            index1 += 1
        else:
            index2 = index1
            for j in expr[index2:]:
                index2 += 1
                if index2 >= len(expr):
                    postfix.append(float(expr[index1:]))
                    index1 = index2
                    break

                elif expr[index2] in '+-/*^() ':
                    postfix.append(float(expr[index1:index2]))
                    index1 = index2
                    break

    return postfix




expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)
