#!/usr/bin/python

# Enter total items to check here. 
numtotest = 100

# Cannot do this in the range itself.
numtotest += 1

for i in range(1,numtotest):
  result = ''
  if i % 3 == 0:
    result = 'fizz'
  if i % 5 == 0:
    result += 'buzz'
  if result:
    print result, i
  else:
    print i