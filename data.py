import numpy as ap
from numpy.random import *
import random

individuals=100
genetic=[]
for i in range(individuals):
    genetic.append(0)

#genetic=None
#seed(1)#乱数の固定

def generation():
    for i in range(individuals):
        genetic[i]=randint(-50,50,(8,8))
        print(str(i+1) + "個目")
        print(genetic[i])
        print("\n")
    return genetic

generation()
