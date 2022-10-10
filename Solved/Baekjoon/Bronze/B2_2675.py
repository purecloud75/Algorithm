num = int(input())

for i in range(num):
    R, code = map(str, input().split())
    R = int(R)

    P = ''

    for j in range(len(code)):
        for k in range(R):
            P = P + code[j]

    print(P)
