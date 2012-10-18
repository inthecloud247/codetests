#!/usr/bin/env python
import os
import sys
import random
from UserDict import UserDict

class Stringfun:
  '''Fun with Strings and Lists'''  
  def __init__(self, funstring):
    self.column = 0
    self.row = 0
    self.funstring = funstring
    self.funstringlen = len(self.funstring) #to avoid needing to continuously recalculate this

  def reset(self):
    self.column = 0
    self.row = 0
      
  def hasnext(self):
    while self.column <= self.funstringlen : #loop until the end of list unless break or find good value
      try:
        valexist = self.funstring[self.column][self.row]
        self.row += 1
        return True        
      except: # if error, move to next column and reset row.
        self.column += 1
        self.row = 0
    self.reset() # cleanup for next use
    return False

  def getnext(self):
    return self.funstring[self.column][self.row - 1]

  def strstr(self, needle):
    ''' String comparison. The needle is the item to search for, and if it finds the needle within the data structure (the haystack) then it returns it. Otherwise returns False.'''

    # init
    self.needle = needle
    self.i = 0
    self.matchstring = ''
    self.output = ''   
    self.reset()
    
    while self.hasnext():
      if self.getnext() == self.needle[self.i] :
        self.matchstring += self.needle[self.i]
        self.i += 1        
      else: # reset
        self.i = 0
        self.matchstring = ''
      if len(self.matchstring) > 0 and len(self.needle) == len(self.matchstring) :
        #matched!
        return self.matchstring
    return False


if __name__ == '__main__':
  
  # Python's multi-dimensional lists are a good simulation of the data structure we are discussing here.
  
  # example data structure diagram:
  
  # w l - t - h
  # a     e
  #       r
   
  # Test simulation lists entered below, enter your own to see the amazing output!

  print '\nData Structure Contents Output'

#  x = Stringfun([ [], [], [], [], ['w', 'a'], [], ['l','t','e'], ['r'] ])
  x = Stringfun([['w','a'],[],['l','t','e'],['r','f']])
  while x.hasnext() :
    sys.stdout.write(x.getnext()) # can't use print because it leaves spaces after each character

  print '\n\nStrStr Testing'  

  print x.strstr('wa')
  print x.strstr('wal')
  print x.strstr('er')
  print x.strstr('aers') # should return false
