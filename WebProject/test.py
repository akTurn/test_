def transform(a = 2):

    if a == 1:
        print("a",a)
        return a +- 2
    return a

total = 1

for x in [3,5,1]:
    print(x)
    total = total + transform(x)

print(total)