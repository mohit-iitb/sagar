import numpy as np
a=np.random.randint(1,11,size=(10,10))
b=np.zeros((10,10))
c=a-1
for i in range(0,10):
    d=[]
    d=np.bincount(c[i],minlength=10)
    d=d.tolist()
    b[i]=d
