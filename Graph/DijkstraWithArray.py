    class MinHeap:
        def __init__(self, L=[]):
            self.A = L
            self.left = None
            self.right = None

        def __str__(self):
            return str(self.A)

        def heapify_down(self, k, n):
            while 2*k+1 < n:
                L, R = 2*k+1, 2*k+2
                if self.A[L] < self.A[k]:
                    m = L
                else: m = k
                if R < n and self.A[R] < self.A[m]:
                    m = R
                if m != k:
                    self.A[k], self.A[m] = \
                        self.A[m], self.A[k]
                    k = m
                else: break

        def make_heap(self):
            n = len(self.A)
            for k in range(n-1, -1, -1):
                self.heapify_down(k, n)

        def find_min(self):
            min = 10000
            for i in range(len(self.A)):
                if min > self.A[i]:
                    min = self.A[i]
            return min

        def heap_sort(self):
            n = len(self.A)
            for k in range (len(self.A)-1, -1, -1):
                self.A[0], self.A[k] = \
                    self.A[k], self.A[0]
                n = n-1
                self.heapify_down(0, n)

        def heapify_up(self, k):
            while k > 0 and self.A[(k-1)//2] > self.A[k]:
                self.A[k], self.A[(k-1)//2] = \
                    self.A[(k-1)//2], self.A[k]
                k = (k-1)//2

        def insert(self, key, L = []):
            self.A.append(key)
            self.heapify_up(len(self.A)-1)

        def delete_min(self):
            if len(self.A) == 0: return None
            min = self.find_min()
            if min == 9999:
                return 9999
            index = self.A.index(min)
            self.A[index] = 9999
            return index

        def heap_sort(self):
            n = len(self.A)
            for k in range(len(self.A) - 1, -1, -1):
                self.A[0], self.A[k] = \
                    self.A[k], self.A[0]
                n = n - 1
                self.heapify_down(0, n)



    H = MinHeap() # 소스 노드에서 시작하는 distance를 저장하고 지워서 리턴하고 할 때 씀

    node = int(input()) # 노드 개수
    edge = int(input()) # 엣지 개수

    graph = [[] for i in range(node)] # 그래프. [u][v][w]로 첫번째 인덱스의 리스트 안에 [v, w]가 들어가게.
    # dist = [float('inf')] * node # 최종 거리를 저장할.
    dist = [9999] * node # 최종 거리를 저장할.
    parent = [None] * node # 부모노드를 저장함.

    dist[0] = 0
    parent[0] = 0

    for j in range(node): # heap에다가 넣음. dist 유동적으로 움직일 거임. 제일 작은 dist 찾아서 deleteMin
        H.insert(dist[j])

    for i in range(edge): # 그래프 완성
        u, v, w = map(int, input().split())
        graph[u].append([v, w])

    #[행-출발 엣지][열-몇번째 엣지][0 = 도착 노드, 1 = 가중치]
    leng = len(H.A)
    # print(graph[0][0][1])
    for i in range(leng):
        u = int(H.delete_min())
        if u == 9999:
            continue
        for v in range(1, 1 + len(graph[u])): #1부터 엣지 개수까지 dist 할당해야됨
        # for v in range(0, len(graph[u])):
            if graph[u][v-1] == []:
                arrive_node = None
                weight = None
            else:
                arrive_node = graph[u][v-1][0] # u에서 도착하는 노드
                weight = graph[u][v-1][1] # u에서 v까지의 가중치

            # if H.A[arrive_node] == 10000:
            #     pass

            if dist[u] + weight < dist[arrive_node]:
                dist[arrive_node] = dist[u] + weight
                parent[arrive_node] = u
                # H.heapify_up(dist[arrive_node])
                H.A[arrive_node] = dist[arrive_node]
                # H.make_heap()

    for a in dist:
        if a == 9999:
            print('inf', end=' ')
        else:
            print(a, end=' ')




    # 6
    # 10
    # 0 1 4
    # 0 3 7
    # 1 2 1
    # 1 3 2
    # 2 3 3
    # 2 4 1
    # 3 2 2
    # 3 4 5
    # 3 5 4
    # 4 5 2