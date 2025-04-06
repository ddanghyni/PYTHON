arr = ['apple', 'banana', 'grape', 'blueberry', 'orange']
count = 0
str_ = input()
for i in arr:
   
    if str_ in i[2]:
        count += 1
        print(i)
    if str_ in i[3]:
        count += 1
        print(i)

print(count)