from math import ceil, floor
import datetime
import numpy



def testeNumpy() :
     
    print(ceil(3.1))   # => 4.0
    print(floor(3.7))  # => 3.0

    xlist = [x for x in range(10) if x > 3]
    print(xlist)

    X = datetime.datetime.now()
    print(X)
    print("Dia da semana " + X.strftime("%u"))


def func (x, y) :
    
    if y :
        print("tem y")
        return
    if (y == 0) :
        return 0
    elif (y == 1) :
        return x
    else :
        return x + func (x, y-1)
    
print(func(14, 1))
