#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#


def happyLadybugs(b):
    lettercount = dict()
    for letter in b:
        if letter in lettercount.keys():
            lettercount[letter]  += 1 
        else:
            lettercount[letter] = 1
            
    underscorecount = 0
    
    for count in lettercount.keys():
        if lettercount[count] < 2 and count != "_":
            return "NO" 
        if count == "_":
            underscorecount = lettercount['_']
    
            
            
            
            

    happyinitially = 0
    for li in range(1,len(b)-1):
        if b[li] == b[li+1] or b[li] == b[li-1]:
            happyinitially = 0
        else:
            happyinitially = 1
            
    
    
    
    if underscorecount>0:
        return "YES"
    else:
        if happyinitially == 1:
            return "NO"
        

    
    return "YES"
        

    
        
    # do the swapping
    
    
    
        
        

if __name__ == '__main__':

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input().strip()

        result = happyLadybugs(b)


        print(result)
