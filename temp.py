# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#Import what I need
import random
import matplotlib.pyplot as plt
from math import log, e, ceil, floor,sqrt,pi,exp
import numpy as np
from numpy import arange,array, empty
import pdb
from random import randint
import copy
from operator import add 
import scipy
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy


def walk(n):
    '''
    n = number of substates that we want the system to have
        I should run this several time, changing some parameters
        to see: a) what is the minimal number of states/substates
        that I need in order to get a precise simulation (i.e.
        we can compare the resulting histogram.) b) if there are
        differences between using few states or a lot. Maybe with few
        the simulation does not agree with the lognormal distribution.
    '''
    time = 0   # we set time equal to zero, later we'll add the times.
    i = 0    # i indicates the position among the states
    while i < n:
        if i == 0:      #at position 0 we just go right
            r = random.random()   # random number between 0 and 1
            t = -log(1-r,e)    # Gillespie: t is the time for the change of state
            time = time+t     # add the time of the first step to the time counter
            i=i+1
        
        elif i !=0 and i!=n-1 :  # the particle is not at the extremes
            r_2 = random.random()
            t_2 = -log(1-r_2,e)
            time = time+t_2
            
            R = random.random()   # Notice that in this case I am basically saying
            if 0 <= R < 0.5:     # that I have 50% going right, 50% going left. I should change this in the future
                i = i -1    # goes left
            elif 0.5 <= R <=1:
                i=i+1     # goes right
        else:   # the particle is at position n
            i = n
    return time



def many_walks(n,m):
    '''
    repeats n-walks m times
    and stores all the times in a vector, it will
    be used to plot, later.
    '''
    v_t = []    # vector of times
    for i in range(m):
        w = walk(n)
        v_t.append(w)
    
    return v_t    
        
n = 20
m = 2000     
bins =  [10*i for i in range(2000)]    
numpy_hist = plt.figure()        
plt.hist(many_walks(n,m), bins)

def func(x,s):
    x = np.array(x)
    return (4/(x*np.sqrt(np.pi*n*s)))*np.exp(-(np.log(x)**2)/(2*n*s))

xx = np.linspace(0.1,2000,10000)



    
popt, pcov = curve_fit(func, bins, many_walks(n,m))        
'''
x = np.linspace(0,2000,10000)       
y = func(x,*popt)
'''