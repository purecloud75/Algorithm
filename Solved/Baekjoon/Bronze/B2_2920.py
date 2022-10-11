notes = list(map(int, input().split()))

asc = notes.copy()
des = notes[:]

asc.sort()
des.sort(reverse=True)

if asc == notes:
    print("ascending")
elif des == notes:
    print("descending")
else:
    print("mixed")










a = list(map(int, input().split()))

if a == sorted(a):
    print('ascending')
elif a == sorted(a, reverse=True):
    print('descending')
else:
    print('mixed')