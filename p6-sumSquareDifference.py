#!/usr/bin/python

# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

from itertools import izip, tee

def pairwise(iterable):
    "s -> (s0,s1), (s2,s3), (s4, s5), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

#    a = iter(iterable)
#    return izip(a, a)


sumsdiff=[0]

def sumSquares(n):
    sum=0
    for i in xrange(1,n+1):
        sum=sum+(i*i)
    return sum

def squareSums(n):
    sum=0
    for i in xrange(1,n+1):
        sum=sum+i
    return sum*sum

def bruteDiff(n):
    a=sumSquares(n)
    b=squareSums(n)
    c=b-a
    print "n=%d %d %d = %d"%(n, a,b,c)
    #sumsdiff.append(c)

def testDiffs():
    for x in range(1,11):
        bruteDiff(x)
        print "-"*20
    print sumsdiff
    for x,y in pairwise(sumsdiff):
        print "%d %d = %d"%(x,y,y-x)

def equationDiff(n):
    sumsq = n * (n + 1) / 2
    sumsq=sumsq*sumsq
    sqsum = (((2 * n) + 1) * (n + 1) * n)/6
    c=sumsq-sqsum
    print "n=%d %d %d = %d"%(n, sqsum,sumsq,c)

def solveIt():
    bruteDiff(100)




if __name__ == '__main__':
    import timeit

#    print(timeit.timeit("solveIt()", setup="from __main__ import solveIt", number=1))
    print(timeit.timeit("bruteDiff(10)", setup="from __main__ import bruteDiff", number=1))

    print(timeit.timeit("equationDiff(10)", setup="from __main__ import equationDiff", number=1))
    print "-"*20

    print(timeit.timeit("bruteDiff(100)", setup="from __main__ import bruteDiff", number=1))

    print(timeit.timeit("equationDiff(100)", setup="from __main__ import equationDiff", number=1))
    print "-"*20

    print(timeit.timeit("bruteDiff(10000000)", setup="from __main__ import bruteDiff", number=1))

    print(timeit.timeit("equationDiff(10000000)", setup="from __main__ import equationDiff", number=1))


    print(timeit.timeit("equationDiff(10000000000000)", setup="from __main__ import equationDiff", number=1))
