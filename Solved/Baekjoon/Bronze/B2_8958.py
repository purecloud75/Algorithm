num = int(input())

for i in range(num):

    ox = input()

    score = 0
    count = 0

    for j in range(len(ox)):
        if ox[j] == 'O':
            count = count + 1
            score = score + count
        else:
            count = 0

    print(score)
