score = int(input())

for x in range(score, 101, 1):
    if x >= 90:
        print("A", end = " ")
    elif x >= 80:
        print("B", end = " ")
    elif x >= 70:
        print("C", end = " ")
    elif x >= 60:
        print("D", end = " ")
    else:
        print("F", end = " ")
