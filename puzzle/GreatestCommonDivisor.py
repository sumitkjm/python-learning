def compGreatestCommDiv(a, b):
    smallerNum = min(a,b)
    gGrtComDiv = 1;
    print("Smaller number {}".format(smallerNum))
    for i in range(smallerNum, 2, -1):
        print("range iterator: {}".format(i))
        if a % i == 0 and b % i == 0:
            gGrtComDiv = i;
            break;

    return gGrtComDiv;


print(compGreatestCommDiv(45,30))
