import time
import random


def prefixSum1(X, n):
    S = []
    # code for prefixSum1
    for i in range(0, n):
        S.append(0)
        for j in range(0, i+1):
            S[i] = S[i] + X[j]

    return S


def prefixSum2(X, n):
    S = []
    # code for prefixSum2
    S.append(X[0])
    for i in range(1, n):
        S.append(S[i - 1] + X[i])

    return S


random.seed()  # random 함수 초기화

n = int(input()) # n 입력받음

X = []
i = 0
while i < n: # 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
    flexible = random.randint(-999, 999)
    X.append(flexible)
    i += 1


before1 = time.perf_counter()
prefixSum1(X, n)
after1 = time.perf_counter()

before2 = time.perf_counter()
prefixSum2(X, n)
after2 = time.perf_counter()

print("prefix1 time: ", after1-before1)
print("prefix2 time: ", after2-before2)

