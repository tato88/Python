l = [1, 2, 3, 4, 2, 5, 1]
x = []
for i in l:
    if i not in x:
        x.append(i)
    elif i in x:
        x.remove(i)
print(x)
