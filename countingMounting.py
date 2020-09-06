
import math
import os
import random
import re
import sys

def countingValleys(n, s):
    valleycount = 0
    level = 0
    d = {'U':1,'D':-1}

    for step in s:
        level +=d[step]
        if level == 0 and step =='D':
            valleycount +=1
    return valleycount 

n=int(input())
s=input()
countingValleys(n,s)