List = []
for i in range(5):
    List.append(int(input()))
if List[0] < 0:
    print(abs(List[0]) * List[2] + List[3] + List[1] * List[4])
else:
    print(abs(List[1] - List[0]) * List[4])
