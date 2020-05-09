i=0
while i<50:
    import random
    s=random.randint(1,5)
    t=random.randint(1,5)
    import os
    a=os.urandom(t).hex()
    b=os.urandom(s).hex()
    c=a+'.'+b
    print(c)
    i=i+1
print('0')
