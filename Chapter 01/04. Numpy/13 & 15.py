import numpy as np

##13
g=np.random.random((10,10))
print(g)
print("the maximum number is "+ g.max())
print("the minimum number is "+g.min())


##15
x = np.ones((3,3))
x[1,1]=0
print(x)