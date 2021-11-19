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


testeNumpy()
