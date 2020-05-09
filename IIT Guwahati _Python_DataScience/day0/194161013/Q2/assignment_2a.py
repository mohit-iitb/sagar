p=0
q=0
r=0
s=0
t=0
u=0
v=0
w=0
x=0
y=0
e=input()
while(e!='0'):
    a=int(e[2])
    b=int(e[3])
    if(a==0 and b==1):
        p=p+1
    elif(a==0 and b==2):
        q=q+1
    elif(a==2 and b==1):
        r=r+1
    elif(a==2 and b==2):
        s=s+1
    elif(a==4 and b==1):
        t=t+1
    elif(a==4 and b==2):
        u=u+1
    elif(a==4 and b==3):
        v=v+1
    elif(a==6 and b==1):
        w=w+1
    elif(a==6 and b==2):
        x=x+1
    elif(a==6 and b==3):
        y=y+1
    e=input()
print(" Total No. Of students in BTECH: ",p)
print(" Total No. Of students in BDES: ",q)
print(" Total No. Of students in MSC: ",r)
print(" Total No. Of students in MA: ",s)
print(" Total No. Of students in MTECH:",t)
print("Total No. Of students in MDES: ",u)
print("Total No. Of students in MS: ",v)
print("Total No. Of students in PHD:",w)
print("Total No. Of students in DUAL CSE:",x)
print("Total No. Of students in DUAL EEE:",y)



    


    
    





    
