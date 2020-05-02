class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size

    def __str__(self):
        s = ""
        for k in self:
            if k == None:
                t = "{0:5s}|".format("")
            else:
                t = "{0:-5d}|".format(k)
            s = s + t
        return s

    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def find_slot(self, key):
        i = self.hash_function(key)
        start = i
        while self.keys[i] is not None and self.keys[i] != key:
            i = (i+1) % self.size
            if i == start:
                return None #full
        return i

    def set(self, key, value=None):
        i = self.find_slot(key)
        if i is None:
            return None #꽉 차서 넣을 수 없어요
        elif self.keys[i] is None:
            self.values[i] = value
            self.keys[i] = key
            return key
        else:
            self.keys[i], self.values[i] = key, value
            return key

    def hash_function(self, key):
        return key % self.size

    def remove(self, key):
        i = self.find_slot(key)
        if self.keys[i] is None:
            return None
        j = i
        while True:
            self.keys[i] = None
            while True:
                j = (j+1) % self.size
                if self.keys[j] is None:
                    return key
                k = self.hash_function(self.keys[j])
                if not( i < k <= j or j < i < k or k <= j < i):
                    break
            self.keys[i], self.values[i] = self.keys[j], self.values[j]
            i = j

    def search(self, key):
        i = self.find_slot(key)
        if self.keys[i] is None:
            return None
        elif self.keys[i] == key:
            return key
        else:
            while True:
                start = i
                i = (i+1) % self.size
                if self.keys[i] == key:
                    return key
                elif i == start:
                    return None

    def __getitem__(self, key):
        return self.search(key)
    def __setitem__(self, key, value):
        self.set(key, value)


k = int(input()) #합쳐서 달성해야하는 수
n = list(map(int, input().split())) #입력받는 정수 리스트

l = len(n) * 1.5 #n에 들어있는 요소 개수 * 1.5로 H.size 맞춰줌

H = HashOpenAddr(int(l))

for i in range (0, len(n)): #set 성공
    H.set(n[i])

count = 0

for j in range(0, H.size):
    if H.keys[j] is not None:
        jjak = k - H.keys[j]
        answer = H.search(jjak)
        if answer is None:
            continue
        else:
            count += 1
    else:
        continue

print(count/2)
# print(H)



