#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
from numpy.linalg import norm
import math, random

#def vlen(v):
#    return math.sqrt(norm(v))

def closestPoint(v, s):
    u = s[1] - s[0]
    rate = max(0, min(u.dot(v - s[0])/u.dot(u), 1))
    return (s[0] + rate*(s[1] - s[0]))

v = np.array([2, 1])
s = np.array([[0, 0], [1, 0]])
closestPoint(v, s)


# In[14]:


def shortestDistance(v, segments):
    r = float("inf")
    for s in segments:
        u = closestPoint(v, s)
        if norm(v - u) < r:
            r = norm(v - u)
    return r


# In[15]:


segments = [np.array([[0, 0], [1, 0]]), np.array([[0, 0], [0, 1]])]
shortestDistance(v, segments)


# In[34]:


def solver(v, segments, g):
    eps = 0.01
    nWalks = 256
    vWalks = 0
    maxSteps = 16
    sumEst = 0
    
    for i in range(0, nWalks):
        x0 = v
        for step in range(0, maxSteps):
            r = shortestDistance(x0, segments)
            if r < eps: 
                sumEst += g(x0)
                vWalks += 1
                print("walk: " + str(vWalks) + " hit " + str(x0) + " boundary " + str(g(x0)))
                break
            theta = random.uniform(0, 2*math.pi)
            x0 = x0 + np.array([r * math.cos(theta), r * math.sin(theta)])
        
    if vWalks == 0:
        return 0
    return sumEst/vWalks


# In[35]:


def boundary(v):
    return norm(v)/2


# In[36]:


segments = [np.array([[0, 0], [2, 0]]), np.array([[0, 0], [0, 2]]), np.array([[2, 0], [2, 2]]), np.array([[0, 2], [2, 2]])]
v = np.array([1, 1])
solver(v, segments, boundary)


# In[ ]:




