# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 16:05:48 2021

@author: ojaswi
"""

import matplotlib.pyplot as plt
import numpy as np
  
# Creating dataset
np.random.seed(34647)
  
# Creating distribution
x = []
count=0
while(count<10000):#tossing the dice 10000 times
    x.append(np.random.randint(1,7)+np.random.randint(1,7)+0.1)
    count=count+1
  
# Creating histogram
fig, axs = plt.subplots(figsize =(20, 10),tight_layout = True)
axs.set_xlabel('Sum of Die')
axs.set_ylabel('Probability')  
axs.hist(x,[1,2,3,4,5,6,7,8,9,10,11,12], density=True)
# Show plot
plt.show()