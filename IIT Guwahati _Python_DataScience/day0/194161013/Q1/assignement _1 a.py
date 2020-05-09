x,y,z=input().split()
while x!='0' and y!='00' and z!='00':
    
   
    arr=['b','B','KB','MB','GB','TB','PB','EB']
    n=arr.index(y)-arr.index(z)
    x=int(x)

    if y=='b':
        x=x/8
        n=n+1
    if z=='b':
        x=x*8
        n=n-1
    n1=x*(1024**n)
    print(n1)
    x,y,z=input().split()

