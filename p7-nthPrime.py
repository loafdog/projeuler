#!/usr/bin/python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we
# can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

primes={}

def isPrime(num):
    if num is 1 or num is 2:
        primes[num]=num
        return True
    if num % 2 == 0:
        return False
    if num in primes:
        return True
    end=int(math.ceil(math.sqrt(num)))
    #print "  check from 3 to %d"%(end)
    for i in xrange(3, end+1):
        if num % i == 0:
            #print "  NOT PRIME %d / %d = %d" % (num, i, num/i)
            return False
    #print "  PRIME %d" % (num)
    primes[num]=num
    return True

def bruteSolve(n):
    num=1
    p=False
    for i in xrange(2,(1000*1000),1):
        if isPrime(i):
            num+=1
            p=True
        if num == n + 1:
            break
        if num % 500 == 0 and p:
            print "Found %dth prime %d" %(num, i)
            p=False

    print sorted(primes.values())[0:10]
    print sorted(primes.values())[-10:-1]
    print "Found %dth prime: %d" %(n,i)



def solveIt():
    bruteSolve(10001)
    #bruteSolve(10)




if __name__ == '__main__':
    import timeit

    print(timeit.timeit("solveIt()", setup="from __main__ import solveIt", number=1))
