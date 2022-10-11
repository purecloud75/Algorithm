s = input()

count = 0
for i in range(26):
    count = 0
    for j in range(len(s)):
        if s[j] == chr(97 + i):
            print(j, end=' ')
            break
        count += 1

    if count == len(s):
        print(-1, end=' ')










word = input()
alphabet = list(range(97, 123))

for x in alphabet:
    print(word.find(chr(x)), end=' ')
