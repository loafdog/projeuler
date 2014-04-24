#!/usr/bin/python

# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1 and 2, the first 10 terms
# will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do
# not exceed four million, find the sum of the even-valued terms.


sum=0

def fib(x, y):
    return x+y

a=0
b=1
i=fib(a,b)
while i < 4000000:
    a=b
    b=i
    if i % 2 == 0:
        sum+=i
    i=fib(a,b)

print sum
