nums = list(map(int, input().split()))
x = []
for i in nums:
    hund = i // 100
    ten = (i % 100) // 10
    one = ((i % 100) % 10) // 1

    x.append(one * 100 + ten * 10 + hund * 1)

if x[0] > x[1]:
    print(x[0])
elif x[0] < x[1]:
    print(x[1])










num1, num2 = input().split()
num1 = int(num1[::-1])  # [::-1] : 역순
num2 = int(num2[::-1])

if num1 > num2:
    print(num1)
else:
    print(num2)
