a = 100
b = [1,2,3]

def f1():
    global a
    a = 75
    #b = 20
    b[2] = 4
    print (a)

def f2():
    a = 80
    print (a)

f1()
f2()

print (a)
print (b)