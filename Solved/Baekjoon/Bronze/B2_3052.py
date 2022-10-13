a, b = [], []
for i in range(10):
    a.append(int(input()))
    b.append(a[i] % 42)

cnt = 0
Sum = 0
for i in range(42):
    if b.count(i) >= 1:
        Sum = b.count(i) + Sum
        cnt += 1
    if Sum == 10:
        print(cnt)
        break










arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)
print(len(arr))

