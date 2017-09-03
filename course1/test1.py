import numpy as np

A = np.array([[12,3,4,5],
             [34,5,2,1],
             [34,56,4,8]])

print A
print ' '

cal = A.sum(axis=0)
print cal
print cal.sum(axis=0)

print 100*A/cal
a = np.random.randn(2, 3) # a.shape = (2, 3)
b = np.random.randn(2, 1) # b.shape = (2, 1)
c = a + b
print c.shape

