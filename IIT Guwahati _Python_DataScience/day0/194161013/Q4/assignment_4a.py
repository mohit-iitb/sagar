s=input()
while(s!='0'):
    s1=0
    s2=0.0
    flag=1
    s=s.lower()
    n=len(s)
    if(s.count('.')>1):
        flag=0;
    if(flag==1):
        for i in range(n):
            if((ord(s[i])>=48 and ord(s[i])<=57) or (ord(s[i])>=97 and ord(s[i])<=102) or s[i]=='.'):
                continue
            else:
                flag=0
                break
    if(flag==0):
        print('Wrong input')
        t=t-1
        
    else:
        
        a=s.find('.')
       
        if(a==-1):
            a=n
        for j in range(a):
            i=a-1-j
            if(s[j]=='a'):
                s1=s1+10*16**i
            elif(s[j]=='b'):
                s1=s1+11*16**i
            elif(s[j]=='c'):
                s1=s1+12*16**i
            elif(s[j]=='d'):
                s1=s1+13*16**i
            elif(s[j]=='e'):
                s1=s1+14*16**i
            elif(s[j]=='f'):
                s1=s1+15*16**i
            else:
                s1=s1+int(s[j],10)*16**i

        #print(s1)
        for j in range(a+1,n,1):
            i=a-j
            if(s[j]=='a'):
                s2=s2+10*16**i
            elif(s[j]=='b'):
                s2=s2+11*16**i
            elif(s[j]=='c'):
                s2=s2+12*16**i
            elif(s[j]=='d'):
                s2=s2+13*16**i
            elif(s[j]=='e'):
                s2=s2+14*16**i
            elif(s[j]=='f'):
                s2=s2+15*16**i
            else:
                s2=s2+int(s[j],10)*16**i
        
        deci=s1+s2
        print(deci)
        s=input()
        

        
            
