#!/usr/bin/python

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# I didn't know how to determine if a number is prime. I found some
# useful info here: http://www.wikihow.com/Check-if-a-Number-Is-Prime
#
# I used trial by division. My first try at it was not efficient. I
# was testing all numbers between 2 and n.  I thought I could make it
# better by trying 2 to n/2.  I wanted to cut the range down. Right
# idea, wrong method of limiting range.  Turns out the factors will
# start to reverse and repeat after you reach sqrt (rounded up for
# cases where it isn't exact).  I.E. 16: 1x16 2x8 4x4 8x2 16x1
#
# Another optimization is to test if number is even. If it is can't be
# prime.

# I first find all the factors and save them in a hash. Then I look at
# each factor and test if it is prime. I use the python timeit module
# to measure how long it takes to solve.

import sys
import math

factors={}

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
    print "  check from 3 to %d"%(end)
    for i in xrange(3, end+1):
        if num % i == 0:
            print "  NOT PRIME %d / %d = %d" % (num, i, num/i)
            return False
    print "  PRIME %d" % (num)
    primes[num]=num
    return True

def findFactors(num):
    for i in xrange(2, num):
        if i in factors:
            #print "found %d in factors"%(factors[i])
            return

        if num % i == 0:
            print "%d * %d = %d" % (i, num/i, num)
            factors[i]=i
            other=num/i
            factors[other]=other
            #print sorted(factors.values())
    return 0

def findLargestPrime(num):
    findFactors(num)
    print "%d has %d factors"%(num, len(factors))
    print sorted(factors.values())
    for f in sorted(factors.values()):
        p = isPrime(f)
        print "%d prime=%s " % (f, str(p))

    return 0

def testIdeas():
    num=600851475143
    findLargestPrime(num)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("testIdeas()", setup="from __main__ import testIdeas", number=1))

    print sorted(primes.values())

