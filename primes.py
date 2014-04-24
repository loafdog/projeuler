#!/usr/bin/python

import sys

import sys
import math

primes={}

def isPrime1(num):
    if num is 1 or num is 2:
        return True
    for i in range(3, num-1):
        if num % i == 0:
            return False
    return True

def isPrime2(num):
    if num is 1 or num is 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num-1):
        if num % i == 0:
            return False
    return True


def isPrimeMine(num):
    if num == 1:
        return False
    if num is 2:
        primes[str(num)]=num
        return True
    if num % 2 == 0:
        return False
    end=int(math.ceil(math.sqrt(num)))
    #print "check from 3 to %d"%(end)
    for i in range(3, end+1):
        if num % i == 0:
            #print "  NOT PRIME %d / %d = %d" % (num, i, num/i)
            return False
    #print "  PRIME %d" % (num)
    primes[str(num)]=num
    return True

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

def testPrimes(limit):

    print "Looking from primes from 1 to %d"%(limit)
    for n in range(1, limit+1):
        b = isPrimeMine(n)
        #print "%d prime=%s " % (n, str(b))

    print "Found %d "%(len(primes))
    if len(primes)<100:
        print sorted(primes.values())
    else:
        s = sorted(primes.values())
        print s[0:20]
        print s[-10:-1]

if __name__ == '__main__':
    import timeit

    if len(sys.argv) is 1:
        testPrimes(10)
    else:
        num=int(sys.argv[1])
        # print "%d prime=%s " % (num, str(isPrime(num)))
        # print(timeit.timeit("isPrime1(%d)"%(num), setup="from __main__ import isPrime1", number=100))
        # print(timeit.timeit("isPrime2(%d)"%(num), setup="from __main__ import isPrime2", number=100))

#        print(timeit.timeit("isPrime(%d)"%(num), setup="from __main__ import isPrime", number=100))

        print(timeit.timeit("testPrimes(%d)"%(num), setup="from __main__ import testPrimes", number=1))



