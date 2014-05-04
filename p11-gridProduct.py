#!/usr/bin/python

# TODO
#
# figure out how to remember which tuple max came from. 
#
# figure out how to get numbers from example into 2d array

import pprint
import math
from itertools import izip_longest
from operator import mul


input_str="""08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

input_list=input_str.split()
print input_str
print len(input_list)


w = 20
h = 20
arr = [[int(input_list[((j+1)*(i+1))-1]) for j in range(w)] for i in range(h)]
#arr = [[j for j in range(w)] for i in range(h)]
#arr = [[i] * w for i in range(h+1)]

pp = pprint.PrettyPrinter(width=160)
pp.pprint(arr)

sect = 4
maxR = [0,0]
maxC = [0,0]
maxDf = [0,0]
maxDr = [0,0]

def row1():
    global maxR
    #for row in arr:
    for r in range(h):
        for c in range(w-sect+1):
            #print r,c,c+sect,arr[r][c:c+sect]
            tmp = reduce(mul, arr[r][c:c+sect])
            if (tmp > maxR[0]):
                maxR[0]=tmp
                maxR[1]=(r,c,c+sect,arr[r][c:c+sect])
                
    print "maxR",maxR

# didn't work. got different/wrong result from multiplying. And
# couldn't figure out a pythonic way to save coords and list of nums.
def row():
    maxR = 0
    for row in arr:
        maxR = max(reduce(mul, row[i:i+sect]) for i in range(len(row)-sect+1))
    print "maxR",maxR

def col1():
    global maxC
    for r in range(h-sect+1):
        #print r, arr[r]
        for c in range(w):
            tmp_arr=[]
            for i in range(r,r+sect):
                tmp_arr.append(arr[i][c])
            #print r,c,r+sect,tmp_arr
            tmp = reduce(mul, tmp_arr)
            if (tmp > maxC[0]):
                maxC[0]=tmp
                maxC[1]=(r,c,r+sect,tmp_arr)

            #maxC = max(reduce(mul, [arr[i][c] for i in range(r,r+sect)]), maxC)
    print "maxC",maxC

# didn't work. got different/wrong result from multiplying. And
# couldn't figure out a pythonic way to save coords and list of nums.
def col():
    global maxC
    for r in range(h-sect+1):
        maxC = max(reduce(mul, [arr[i][c] for i in range(r,r+sect)]) for c in range(w))
    print "maxC",maxC

def diag1():
    global maxDf, maxDr
    for r in range(h-sect+1):
        for c in range(w-sect+1):
            #print [arr[r+i][c+i] for i in range(0,sect)]
            tmp_arr=[]
            for i in range(sect):
                tmp_arr.append(arr[r+i][c+i])
            #print (r,c),(r+sect-1,c+sect-1),tmp_arr
            tmp = reduce(mul, tmp_arr)
            if (tmp > maxDf[0]):
                maxDf[0]=tmp
                maxDf[1]=((r,c),(r+sect-1,c+sect-1),tmp_arr)

            #maxDf = max(reduce(mul, [arr[r+i][c+i] for i in range(0,sect)]), maxDf)
    print "maxDf",maxDf

    for r in range(h-sect+1):
        for c in range(sect-1,w):
            tmp_arr=[]
            for i in range(sect):
                tmp_arr.append(arr[r+i][c-i])
#            print (r,c),(r+sect-1,c-sect+1),tmp_arr
            tmp = reduce(mul, tmp_arr)
            if (tmp > maxDr[0]):
                maxDr[0]=tmp
                maxDr[1]=((r,c),(r+sect-1,c-sect+1),tmp_arr)


#            maxDr = max(reduce(mul, [arr[r-i][c-i] for i in range(0,sect)]), maxDr)
    print "maxDr",maxDr

# didn't work. got different/wrong result from multiplying. And
# couldn't figure out a pythonic way to save coords and list of nums.
def diag():
    for r in range(h-sect+1):
        maxDf = max(reduce(mul, [arr[r+i][c+i] for i in range(0,sect)]) for c in range(w-sect+1))
            #print [arr[r+i][c+i] for i in range(0,sect)]
    print "maxDf",maxDf

    for r in range(sect-1,h):
        maxDr = max(reduce(mul, [arr[r-i][c-i] for i in range(0,sect)]) for c in range(sect-1,w))
            #print [arr[r+i][c+i] for i in range(0,sect)]
    print "maxDr",maxDr      



def bruteSolve():
    pass

def solveIt():
    pass

if __name__ == '__main__':

    import timeit
    bruteSolve()

    reps=1
    print(timeit.timeit("row1()", setup="from __main__ import row1", number=reps))
    #print(timeit.timeit("row()", setup="from __main__ import row", number=reps))

    print(timeit.timeit("col1()", setup="from __main__ import col1", number=reps))
    #print(timeit.timeit("col()", setup="from __main__ import col", number=reps))

    print(timeit.timeit("diag1()", setup="from __main__ import diag1", number=reps))
    #print(timeit.timeit("diag()", setup="from __main__ import diag", number=reps))

    print max(maxR[0], maxC[0], maxDf[0], maxDr[0])
