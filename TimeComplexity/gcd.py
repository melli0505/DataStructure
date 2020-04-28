def gcd_sub(q, w):
    while q != 0 and w != 0:
        if q > w:
            q = q - w
        else:
            w = w - q
    return q + w


def gcd_mod(c, d):
    while c != 0 and d != 0:
        if c > d:
            c %= d
        else:
            d %= c
    return c + d

# def gcd_rec(e, f):
#     t = e
#     if f > e:
#         e = f
#         f = t
#     e = e - f
#     if e - f != 0:
#         gcd_rec(e, f) 
#     return f

def gcd_rec(e, f):
    if e > f:
        return gcd_sub(e-f,f)
    else:
        return gcd_sub(e, f-e)
    return e+f


# a, b를 입력받는다
a, b = input().split()

a = int(a)
b = int(b)

x = gcd_sub(a, b)
y = gcd_mod(a, b)
z = gcd_rec(a, b)
# gcd_sub, gcd_mod, gcd_rec을 각각 호출하여, x, y, z에 리턴값을 저장한다
print(x, y, z)