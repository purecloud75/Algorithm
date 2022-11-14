List = []

while True:
    x = int(input())
    if x == -1:
        break
    List.append(x)

count = 0
for i in List:
    count += i

print(count)
