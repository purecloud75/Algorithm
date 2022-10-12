a = list(map(int, input().split()))

sum = 0
for i in a:
    sum += pow(i, 2)
print(sum % 10)
