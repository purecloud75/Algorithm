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
