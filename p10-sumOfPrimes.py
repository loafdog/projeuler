#!/usr/bin/python


import math

primes={}

def isPrime(num):
    if num == 1:
        return False
    if num < 4:
        primes[str(num)]=num
        return True
    if num % 2 == 0:
        return False
    elif num < 9:
        primes[str(num)]=num
        return True
    elif num % 3 == 0:
        return False

    end=int(math.ceil(math.sqrt(num)))
    #print "check from 3 to %d"%(end)
    for i in range(5, end+1, 6):
        if num % i == 0:
            #print "  NOT PRIME %d / %d = %d" % (num, i, num/i)
            return False
        if num % (i+2) == 0:
            return False
    #print "  PRIME %d" % (num)
    primes[num]=num
    return True

def bruteSolve(n):
    end=n
    total=2
    for i in xrange(3,end+1, 2):
        if isPrime(i):
            total+=i

    print total

def solveIt():
    bruteSolve(10)

    bruteSolve(2 * 10**6)



if __name__ == '__main__':
    import timeit

    print(timeit.timeit("solveIt()", setup="from __main__ import solveIt", number=1))
