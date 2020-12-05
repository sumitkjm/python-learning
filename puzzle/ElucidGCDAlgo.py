def GCDByElucid(a, b):
    if a == b:
        return a
    if (a > b):
        return GCDByElucid(a-b,b)
    else:
        return GCDByElucid(a, b-a)

a = int(input("Enter the first number").strip())
b = int(input("Enter the second number").strip())
print("GCD {} & {} is {}".format(a,b,GCDByElucid(a,b)))
