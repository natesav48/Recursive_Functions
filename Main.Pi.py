#First recursive function
def rec(x, y):
    if x <= 2 or y <= 1:
        return 1
    else:
        return rec(x - 1, y) + rec(x, y - 2)

result = rec(4, 5)
print(result)

#second recursive function
def rec2 (a,b):
    if a == 2 or a+b >=5:
        return 2
    else:
        return rec2(a+b-2, b) + rec2(a, b+b-a)
result = rec2(4,5)
print(result)