#!/usr/bin/python


# Find the largest palindrome made from the product of two 3-digit
# numbers.
#
# A palindromic number reads the same both ways. The largest
# palindrome made from the product of two 2-digit numbers is 9009 =
# 91x99.

def isPalindrome(num):
    if num == int(str(num)[::-1]):
        return True
    return False


def testIsPalindrome():
    nums=[1,10,11,101,110,1001,1010]
    for n in nums:
        print "%d palindrome %s"%(n, str(isPalindrome(n)))



palindromes=set()

def largestPalindrome():
    lpal=0
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            if isPalindrome(i*j):
                #print "%d = %d * %d PALINDROME"%(i*j, i, j)
                if i*j >= lpal:
                    print "%d = %d * %d LARGEST PALINDROME"%(i*j, i, j)
                    lpal=i*j
                #palindromes.update((str(i+j)))
                palindromes.add(str(i*j))
                #print sorted(list(palindromes))
                #print list(palindromes)

def solveIt():
    largestPalindrome()




if __name__ == '__main__':
    import timeit
    print(timeit.timeit("solveIt()", setup="from __main__ import solveIt", number=1))
