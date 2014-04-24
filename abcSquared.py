#!/usr/bin/python


import math

results={}

def bruteSolve(n):
    end=n
    for i in xrange(2,end+1):
        a=i
        for b in xrange(i+1, end+1):
            csq = (a*a) + (b*b)
            c=math.sqrt(csq)
            if c.is_integer():
                c = int(c)
                aPlusb=a+b
                #print "%7d %7d %7d | a+b=%7d csq=%7d"%(a,b,c,aPlusb, csq)
                if a+b+c == 1000:
                    print "** %7d %7d %7d %d**"%(a,b,c,a*b*c)
                    return
                if csq not in results:
                    results[csq] = [[a,b,c]]
                else:
                    results[csq].append([a,b,c])

    # for k in sorted(results):
    #     l = results[k]
    #     if len(l) > 1:
    #         print k, l


def solveIt():
    bruteSolve(10000)



if __name__ == '__main__':
    import timeit

    print(timeit.timeit("solveIt()", setup="from __main__ import solveIt", number=1))
