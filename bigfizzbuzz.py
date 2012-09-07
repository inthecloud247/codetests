#!/usr/bin/python
# Purpose: bigfizzbuzz. this will work on massive numbers. 
# Note: Since python range uses lists, it can exceed the list size limit at some point.
# This code uses loops instead, and is more efficient, particularly at large number
# sizes. Definitely not as elegant however. But functionality is the goal here.  

def fizzbuzzme(numtotest):
  "i do the fizzbuzz. using while loop instead of range. i can handle big numbers."
  numtotest += 1
  i = 1
  
  while i < numtotest:
    result = ''
    if i % 3 == 0:
      result = 'fizz'
    if i % 5 == 0:
      result += 'buzz'
    if result:
      print result, i
    else:
      print i
    i += 1

if __name__ == "__main__":
  # the test amount...
  defaultamount = 100
  fizzbuzzme(defaultamount)