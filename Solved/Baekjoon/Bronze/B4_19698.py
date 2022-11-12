a, b, c, d = map(int, input().split())

e = b // d
f = c // d

g = e * f

if a >= g:
    print(g)
else:
    print(a)