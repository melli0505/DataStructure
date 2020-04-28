class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.size = 0

    def deleteNode(self, x):  # delete x
        if x is None or x == self.head:
            return
        # 노드 x를 리스트에서 분리해내기
        x.prev.next, x.next.prev = x.next, x.prev
        self.size -= 1

    def search(self, key):
        v = self.head.next
        while v is not self.head:
            if v.key == key:
                return v
            v = v.next
        return None

    def remove(self, x):
        if x is None or x == self.head:
            return None
        x.prev.next = x.next
        x.next.prev = x.prev
        del x
        self.size -= 1

    def popFront(self):
        if self.head.next == self.head:
            return None
        key = self.head.next.key
        self.deleteNode(self.head.next)
        self.size -= 1
        return key

    def popBack(self):
        if self.head.prev == self.head:
            return None
        key = self.head.prev.key
        self.deleteNode(self.head.prev)
        self.size -= 1
        return key

    def pushFront(self, key):
        self.insertAfter(self.head, key)

    def pushBack(self, key):
        self.insertBefore(self.head, key)


    def splice(self, a, b, x):
        xn = x.next

        x.next = a
        a.prev = x
        b.next = xn
        xn.prev = b
        self.size += 1

    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)

    def moveAfter(self, a, x):
        self.splice(a, a, x)

    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x)

    def insertAfter(self, x, key):
        self.moveAfter(Node(key), x)

    def printList(self):
        v = self.head.next
        print("h ->", end=' ')
        while v.next is not self.head.next:
            print(v.key, '->', end=' ')
            v = v.next
        print('h')

    def first(self):
        return self.head.next.key

    def last(self):
        return self.head.prev.key

    def isEmpty(self):
        if self.head.next == self.head:
            return True
        return False




# 각자 작성해볼 것!


def josephus(n, k):
    L = DoublyLinkedList()

    for i in range(1, n+1):
        L.pushBack(i)

    v = L.head.next
    # print(L.head.key)

    while L.size != 1:
        # if v.key is None:
        #     v = v.next
        for i in range (1, k):
            if v.key is None:
                v = v.next
            v = v.next
        if v.key is None:
            v = v.next
        # print("delete Node is", v.key)
        L.deleteNode(v)
        # L.printList()
        v = v.next
        # print("next Node is", v.key)

    return L.head.next.key


n = input().split()
print(josephus(int(n[0]), int(n[1])))