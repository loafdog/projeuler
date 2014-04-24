#!/usr/bin/python



# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?


def isDivisible(num, minDiv, maxDiv):
    for i in range(minDiv, maxDiv):
        if num % i != 0:
            return False
    return True
            
def findIt(minDiv, maxDiv):
    smallestNum=maxDiv*maxDiv
    num=maxDiv
    maxR=1
    for i in range(num-1, minDiv, -1):
        num=num*i
        d=isDivisible(num, minDiv, maxDiv)
        print "%d is div  %s"%(num, str(d))
        if d:
            smallestNum=num
            maxR=i
            break

    print "Now see if it can be smaller %d-%d"%(minDiv,maxR)
    #for j in range(minDiv, maxR):
    for j in range(maxR,minDiv-1,-1):
        num=num/j
        d=isDivisible(num, minDiv, maxDiv)
        print "j=%d %d is div %s"%(j, num, str(d))
        if d:
            if num < smallestNum:
                smallestNum=num
        else:
            num=num*j

    print "Smallest num %d"%(smallestNum)


def solveIt():
    findIt(2,10)
    print "-"*10
    findIt(2,11)
    print "-"*10
    findIt(2,20)
    #num=2520
    #print "%d is div %s"%(num,str(isDivisible(num)))

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("solveIt()", setup="from __main__ import solveIt", number=1))
