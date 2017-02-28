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



def walk(n):

    time = 0  
    i = 0    
    while i < n:
        if i == 0:      
            r = random.random()  
            t = -log(1-r,e)  
            time = time+t  
            i=i+1
        
        elif i !=0 and i!=n-1 :  
            r_2 = random.random()
            t_2 = -log(1-r_2,e)
            time = time+t_2
            
            R = random.random()   
            if 0 <= R < 0.5:    
                i = i -1    
            elif 0.5 <= R <=1:
                i=i+1    
        else:   
            i = n
    return time



def many_walks(n,m):
    v_t = []    
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
# I would like to use curve_fit to find s such that func fitts the curve
'''
x = np.linspace(0,2000,10000)       
y = func(x,*popt)
'''
