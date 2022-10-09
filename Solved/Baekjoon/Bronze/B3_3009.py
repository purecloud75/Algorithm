List = [[],
        [],
        []]

for i in range(3):
    List[i] = list(map(int, input().split()))

a = []
b = []
for i in range(len(List)):
    a.append(List[i][0])
    b.append(List[i][1])

if a[0] == a[1]:
    x1 = a[2]
elif a[0] != a[1]:
    if a[0] == a[2]:
        x1 = a[1]
    else:
        x1 = a[0]

if b[0] == b[1]:
    y1 = b[2]
elif b[0] != b[1]:
    if b[0] == b[2]:
        y1 = b[1]
    else:
        y1 = b[0]

print(f"{x1} {y1}")










x_nums = []
y_nums = []
for _ in range(3):
    x, y = map(int, input().split())
    x_nums.append(x)
    y_nums.append(y)

for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x4 = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y4 = y_nums[i]
print(x4, y4)
