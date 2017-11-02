# -*- coding: utf-8 -*-
import numpy as np

w1=np.random.randn(2, 2)
w2=np.array([[0.0543,0.0579],[-0.0291,0.0999]])
#b = np.ones((2,1))
b = np.array([[-0.0703],[-0.0939]])
#c = w + b
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]).T
d = np.dot(w1.T, X)
e =d+b
w3 = np.array([[1],[1]])
w4 = np.array([[2],[2]])
c = w3 * w4
#print w
print np.shape(c)
#print c
print e



