num_ = int(input())

cond_1 = (num_ % 2 != 0) & (num_ % 3 == 0)
cond_2 = (num_ % 2 == 0) & (num_ % 5 == 0)

if cond_1 | cond_2:
    print("true")
else:
    print("false")