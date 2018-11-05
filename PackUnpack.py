print (1,2,3,4)

numbers = [1,2,3,4]

def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

#print (*'abc')

print (add(1,2,3,4))

#print (*numbers)

def foo(**kwargs):
    for key, value in kwargs.items():
        print ("{}:{}".format(key,value))

foo(sumit="Male", Archana="Female")

foo(Manasvi ="Female",Manshu="Female",Darsh = "Male",Dishu="Male")