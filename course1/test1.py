import numpy as np

A = np.array([[12,3,4,5],
             [34,5,2,1],
             [34,56,4,8]])

print A
print ' '

cal = A.sum(axis=0)
print cal

print 100*A/cal
