import random
a=['b','B','KB','MB','GB','TB','PB','EB']
r=random.randint(1,10)
for r in range(1,r):
    p=0
    for p in range(0,8):
        q=0
        for q in range(0,8):
            s=random.randint(0,1000)
            print(s,a[p],a[q])
            q=q+1
        p=p+1
    r=r-1
print('0 00 00')

            
    

    

