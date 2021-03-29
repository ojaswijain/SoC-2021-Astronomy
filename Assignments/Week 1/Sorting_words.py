# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 00:12:18 2021

@author: ojasw
"""

print("Enter number of words.\n")
n=int(input())
count=0
a=[(1, "test")]
print("Enter the words:\n")
while(count<n):
    count=count+1
    s=input()
    x=len(s)
    a.append((x,s))
del a[0]
a.sort()
print("\n")
k=len(a)
coun=0
while(coun<k):
    print(a[coun][1],"\n")
    coun=coun+1
    