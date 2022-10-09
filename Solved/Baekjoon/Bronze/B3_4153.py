while True:
    List = list(map(int, input().split()))
    if sum(List) == 0:
        break
    List.sort()
    if List[len(List) - 1] ** 2 == List[0] ** 2 + List[1] ** 2:
        print("right")
    else:
        print("wrong")


