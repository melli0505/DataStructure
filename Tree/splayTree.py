class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0

    def __str__(self):
        return str(self.key)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0


    def __len__(self):
        return self.size

    def preorder(self, v):
        if v != None:
            print(v.key, end=' ')
            if v.left: self.preorder(v.left)
            if v.right: self.preorder(v.right)
        else:
            return None

    def inorder(self, v):
        if v is not None:
            if v.left:
                self.inorder(v.left)
            print(v.key, end=' ')
            # ino.append(v)
            if v.right:
                self.inorder(v.right)
        # return ino
        else:
            return None

    def inorderFor(self):
        current = self.root
        splist = []
        while current is not None:
            if current.left is None:
                splist.append(current)
                current = current.right
            else:
                pre = current.left
                while pre.right is not None and pre.right is not current:
                    pre = pre.right
                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    splist.append(current)
                    current = current.right
        return splist

    def postorder(self, v):
        if v is not None:
            if v.left: self.postorder(v.left)
            if v.right: self.postorder(v.right)
            print(v.key, end=' ')
        else:
            return None


    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v is not None:
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p

    def search(self, key):
        v = self.find_loc(key)
        if v and v.key == key:
            return v
        else: return None

    def insert(self, key):
        p = self.find_loc(key)
        if p is None or p.key is not key:
            v = Node(key)
            if p is None: # 빈 트리였을 때
                self.root = v
                v.height = 0
            else: # 빈 트리가 아닐 때
                height = -1
                v.parent = p # height 조정
                pt = p
                a = p.left
                b = p.right
                if a is None or b is None:
                    v.height = 0
                    if p.key > key:
                        p.left = v
                    else:
                        p.right = v
                    while pt:
                        if pt.left is None: lheigt = -1
                        else: lheigt = pt.left.height
                        if pt.right is None: rheight = -1
                        else: rheight = pt.right.height
                        if lheigt >= pt.height or rheight >= pt.height:
                            pt.height += 1
                        pt = pt.parent

                v.height = 0
            self.size += 1
            return v
        else:
            print("key is already in tree")
            return p

        #------------------------ 위 건들지 마

    def deleteByMerging(self, x):
        if x is None:
            return None

        a, b, pt = x.left, x.right, x.parent
        if a is None:
            c = b
            s = pt
        else:
            c = m = a # C = x 자리를 대체할 노드, m = C의 left tree에서 가장 큰 노드
            while m.right:
                m = m.right
            m.right = b
            if b is not None:
                b.parent = m
            s = m
        if self.root == x:
            if c:
                c.parent = None
            self.root = c
        else:
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
            if c: c.parent = pt
        h = b # 지우고 대체한 노드의 right 노드부터 시작
        self.releveling(h)
        # while h:
        #     if h.left is None: # 없는 부분의 height를 -1로
        #         lheight = -1
        #     else:
        #         lheight = h.left.height # 왼쪽 아래 노드의 높이
        #     if h.right is None: # 없는 부분의 height를 -1로
        #         rheight = -1
        #     else:
        #         rheight = h.right.height # 오른쪽 아래 노드의 높이
        #
        #     # 더 큰 높이에 1 더한 값을 parent 노드의 높이로 할당
        #     if lheight > rheight:
        #         h.height = lheight + 1
        #     else:
        #         h.height = rheight + 1
        #     h = h.parent

        self.size -= 1
        return s

    def releveling(self, h):
        if h is None:
            return None
        while h:
            if h.left is None: # 없는 부분의 height를 -1로
                lheight = -1
            else:
                lheight = h.left.height # 왼쪽 아래 노드의 높이
            if h.right is None: # 없는 부분의 height를 -1로
                rheight = -1
            else:
                rheight = h.right.height # 오른쪽 아래 노드의 높이

            # 더 큰 높이에 1 더한 값을 parent 노드의 높이로 할당
            if lheight > rheight:
                h.height = lheight + 1
            else:
                h.height = rheight + 1
            h = h.parent

    def height(self, x): # 노드 x의 height 값을 리턴
        if x == None: return -1
        else: return x.height

    def deleteByCopying(self, x):

        if x is None:
            return None

        mr = x.left
        ml = x.right

        if x.left is None and x.right is None: # leaf node 일 때
            pt = x.parent
            if x is not self.root:
                if x.parent.left == x:
                    x.parent.left = None
                else:
                    x.parent.right = None
            else:
                self.root = None

            self.releveling(pt)
                # del x
        elif x.left is not None: # 오른쪽이 있던 없던 일단 왼쪽이 있으면
            # mr = x.left
            while mr.right:
                mr = mr.right
            pt = mr.parent.key
            x.key = mr.key
            ll = mr.left
            if mr.left is not None:
                if mr.left.key > mr.parent.key:
                    mr.parent.right = mr.left
                else:
                    mr.parent.left = mr.left
                mr.left.parent = mr.parent
                while ll.left is not None:
                    ll = ll.left
                self.releveling(ll)
            else:
                if pt > mr.key:
                    mr.parent.left = None
                else: mr.parent.right = None
                self.releveling(ll)

            # del mr
        elif x.left is None and x.right is not None: # 오른쪽만 있으면
            while ml.left: # 오른쪽 트리 가장 작은 값 찾기
                ml = ml.left
            x.key = ml.key
            rr = ml.right
            if ml.right is not None:
                if ml.parent.right == ml:
                    ml.parent.right = ml.right
                else:
                    ml.parent.left = ml.right
                ml.right.parent = ml.parent

                self.releveling(rr)
            else:
                if ml.parent.right == ml:
                    ml.parent.right = None
                else:
                    ml.parent.left = None
                self.releveling(ml.parent)
            # del ml

    def succ(self, x): # 재귀 안 쓰고 하는 inorder 방법 찾을 필요 존재함
        if x is None:
            return None

        # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
        # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
        suc = [None]
        suc = self.inorderFor()
        count = len(suc)
        for i in range(0, count):
            if suc[i].key == x.key:
                if i+1 == count:
                    return None
                # result = suc[i+1]
                # suc = None
                return suc[i+1]

    def pred(self, x): # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
        # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
        if x is None:
            return None
        suc = []
        suc = self.inorderFor()
        count = len(suc)
        for i in range(0, count):
            if suc[i].key == x.key:
                if i == 0:
                    return None
                return suc[i - 1]

    def rotateLeft(self, x): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        if x is None: return
        z = x.right
        if z is None: return
        b = z.left
        z.parent = x.parent
        if x.parent is not None:
            if x.parent.right == x:
                x.parent.right = z
            else:
                x.parent.left = z
        z.left = x
        x.parent = z
        x.right = b
        # height 정보 수정
        if b is not None:
            b.parent = x
            if x.left is not None:
                if x.left.height > b.height:
                    x.height = x.left.height + 1
                else:
                    x.height = b.height + 1
        else:
            if x.left == None:
                x.height = 0
            else:
                x.height = x.left.height + 1

        if z.right is not None :
            if x.height > z.right.height:
                z.height = x.height + 1
            else:
                z.height = z.right.height + 1
        else:
            z.height = x.height + 1
        self.releveling(z)
        if self.root == x:
            self.root = z

    def rotateRight(self, x): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        if x is None:
            return None
        z = x.left
        if z is None:
            return None
        b = z.right
        z.parent = x.parent
        if x.parent is not None:
            if x.parent.left == x:
                x.parent.left = z
            else:
                x.parent.right = z
        z.right = x
        x.parent = z
        x.left = b
        # height 정보 수정
        if b is not None:
            b.parent = x
            if x.right is not None:
                if x.right.height > b.height:
                    x.height = x.right.height + 1
                else:
                    x.height = b.height + 1
            else:
                x.height = b.height + 1
        else:
            if x.right is not None:
                x.height = x.right.height + 1
            else:
                x.height = 0
        if z.left is not None:
            if x.height > z.left.height:
                z.height = x.height + 1
            else:
                z.height = z.left.height + 1
        else:
            z.height = z.right.height + 1
        self.releveling(z)
        if x is self.root:
            self.root = z


class SplayTree(BST):
    def __init__(self):
        self.root = None
        self.size = 0

    def splay(self, x):
        while x.parent is not None:
            if x.parent.left is x:
                self.rotateRight(x.parent)
            else:
                self.rotateLeft(x.parent)
                # print(x.parent.key)
        return x

    def search(self, key):
        v = super().search(key)
        if v is not None:
            self.splay(v)
        return v

    def insert(self, key):
        v = super().insert(key)
        self.splay(v)
        return v

    def delete(self, x):
        if x.left is None and x.right is None and self.root:
            self.root = None
            return None
        # self.splay(x)
        l = x.left
        r = x.right
        if l is not None:
            while l.right is not None:
                l = l.right
            self.splay(l)
            l.right = r
            if r is not None:
                r.parent = l
            self.root = l
        else:
            r.parent = None
            self.root = r


T = SplayTree()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'delete':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'splay':
        v = T.search(int(cmd[1]))
        T.splay(v)
        T.preorder(T.root)
        print()
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")

# insert 20
# insert 10
# insert 30
# insert 15
# insert 25
# insert 35
# insert 5
