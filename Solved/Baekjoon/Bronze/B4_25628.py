a, b = map(int, input().split())

count = 0
while a > 1 and b > 0:
    if a < 1:
        break
    a -= 2
    b -= 1
    count += 1

print(count)
