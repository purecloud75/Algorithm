List = list(map(int, input().split()))

a = 0
for i in range(6):
    if List.count(i + 1) == 3:
        print(10000 + (i + 1) * 1000)
        a = 1
        break
    elif List.count(i + 1) == 2:
        print(1000 + (i + 1) * 100)
        a = 1
        break
if a != 1:
    List.sort()
    print(List[2] * 100)
