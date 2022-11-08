x, y = map(int, input().split())

if y == 1 or y == 2:
    print("NEWBIE!")
elif y <= x and (y != 1 and y != 2):
    print("OLDBIE!")
else:
    print("TLE!")
