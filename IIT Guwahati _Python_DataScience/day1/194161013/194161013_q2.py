file=open('194161013_q2.txt','r')
y=file.readlines()
x=[]
f=[]
g=[]
for a in y[2:31]:
    if '##' in a:
        continue
    p=a.split(',')
    course=p[0];
    midsem=p[3];
    endsem=p[4];
    x.append(course)
    f.append(midsem)
    g.append(endsem)

#print(x)
print("\t\t\tBIOTECHNOLOGY\n")
#for mid sem clash
print("\t\t\tmid sem")
for i in range(len(f)):
    for j in range(i,len(f)):
        if(i!=j ):
            if(f[i]==f[j] and x[i][2]==x[j][2] ):

                print("Clash in mid sem "+x[i]+" and "+x[j])


for i in range (len(f)):
    if(f[i]==''):
        print("no exam of ",x[i])



#for end sem clash
print("\t\t\tend sem")
for i in range(len(g)):
    for j in range(i,len(g)):
        if(i!=j):
            if(g[i]==g[j] and  x[i][2]==x[j][2] ):
                print("Clash in end sem "+x[i]+" and "+x[j])


for i in range (len(f)):
    if(g[i]==''):
        print("no exam of ",x[i])


#CIVIL
x=[]
f=[]
g=[]
for a in y[32:95]:
    if '##' in a:
        continue
    p=a.split(',')
    course=p[0];
    midsem=p[3];
    endsem=p[4];
    x.append(course)
    f.append(midsem)
    g.append(endsem)
print("\t\t\tCIVIL\n")
#for mid sem clash
print("\t\t\tmid sem")
for i in range(len(f)):
    for j in range(i,len(f)):
        if(i!=j ):
            if(f[i]==f[j] and  x[i][2]==x[j][2] ):
                print("Clash in mid sem "+x[i]+" and "+x[j])


for i in range (len(f)):
    if(f[i]==''):
        print("no exam of ",x[i])

#for end sem clash
print("\t\t\tend sem")
for i in range(len(g)):
    for j in range(i,len(g)):
        if(i!=j):
            if(g[i]==g[j] and  x[i][2]==x[j][2] ):
                print("Clash in end sem "+x[i]+" and "+x[j])

for i in range (len(f)):
    if(g[i]==''):
        print("no exam of ",x[i])

#CHEMICAL
x=[]
f=[]
g=[]
for a in y[96:131]:
    if '##' in a:
        continue
    p=a.split(',')
    course=p[0];
    midsem=p[3];
    endsem=p[4];
    x.append(course)
    f.append(midsem)
    g.append(endsem)
print("\t\t\tCHEMICAL\n")
#for mid sem clash
print("\t\t\tmid sem")
for i in range(len(f)):
    for j in range(i,len(f)):
        if(i!=j ):
            if(f[i]==f[j] and  x[i][2]==x[j][2] ):
                print("Clash in mid sem "+x[i]+" and "+x[j])



for i in range (len(f)):
    if(f[i]==''):
        print("no exam of ",x[i])
#for end sem clash
print("\t\t\tend sem")
for i in range(len(g)):
    for j in range(i,len(g)):
        if(i!=j):
            if(g[i]==g[j] and  x[i][2]==x[j][2] ):
                print("Clash in end sem "+x[i]+" and "+x[j])



for i in range (len(f)):
    if(g[i]==''):
        print("no exam of ",x[i])
#CL

x=[]
f=[]
g=[]

for a in y[132:166]:
    if '##' in a:
        continue
    p=a.split(',')
    course=p[0];
    midsem=p[3];
    endsem=p[4];
    x.append(course)
    f.append(midsem)
    g.append(endsem)
#print (x)
#print(f)
#print(g)
print("\t\t\tCL\n")
#for mid sem clash
print("\t\t\tmid sem")
for i in range(len(f)):
    for j in range(len(f)):
        if(i!=j):
            if(f[i]==f[j] and  x[i][2]==x[j][2] ):
                print("Clash in mid sem "+x[i]+" and "+x[j])

for i in range (len(f)):
    if(f[i]==''):
        print("no exam of ",x[i])
#for end sem clash
print("\t\t\tend sem")
for i in range(len(g)):
    for j in range(len(g)):
        if(i!=j):
            if(g[i]==g[j] and  x[i][2]==x[j][2] ):
                print("Clash in end sem "+x[i]+" and "+x[j])




for i in range (len(f)):
    if(g[i]==''):
        print("no exam of ",x[i])

#CSE

x=[]
f=[]
g=[]

for a in y[167:201]:
    if '##' in a:
        continue
    p=a.split(',')
    course=p[0];
    midsem=p[3];
    endsem=p[4];
    x.append(course)
    f.append(midsem)
    g.append(endsem)
#print (x)
#print(f)
#print(g)
print("\t\t\tCSE\n")
#for mid sem clash
print("\t\t\tmid sem")
for i in range(len(f)):
    for j in range(len(f)):
        if(i!=j):
            if(f[i]==f[j] and  x[i][2]==x[j][2] ):
                print("Clash in mid sem "+x[i]+" and "+x[j])


for i in range (len(f)):
    if(f[i]==''):
        print("no exam of ",x[i])


#for end sem clash
print("\t\t\tend sem")
for i in range(len(g)):
    for j in range(len(g)):
        if(i!=j):
            if(g[i]==g[j] and  x[i][2]==x[j][2] ):
                print("Clash in end sem "+x[i]+" and "+x[j])



for i in range (len(f)):
    if(g[i]==''):
        print("no exam of ",x[i])



#EEE

x=[]
f=[]
g=[]

for a in y[205:260]:
    if '##' in a:
        continue
    p=a.split(',')
    course=p[0];
    midsem=p[3];
    endsem=p[4];
    x.append(course)
    f.append(midsem)
    g.append(endsem)
#print (x)
#print(f)
#print(g)
print("\t\t\tEEE\n")
#for mid sem clash
print("\t\t\tmid sem")
for i in range(len(f)):
    for j in range(len(f)):
        if(i!=j):
            if(f[i]==f[j] and  x[i][2]==x[j][2] ):
                print("Clash in mid sem "+x[i]+" and "+x[j])

for i in range (len(f)):
    if(f[i]==''):
        print("no exam of ",x[i])
#for end sem clash
print("\t\t\tend sem")
for i in range(len(g)):
    for j in range(len(g)):
        if(i!=j):
            if(g[i]==g[j] and  x[i][2]==x[j][2] ):
                print("Clash in end sem "+x[i]+" and "+x[j])


for i in range (len(f)):
    if(g[i]==''):
        print("no exam of ",x[i])
#RURAL TECHNOLOGY


x=[]
f=[]
g=[]

for a in y[268:274]:
    if '##' in a:
        continue
    p=a.split(',')
    course=p[0];
    midsem=p[3];
    endsem=p[4];
    x.append(course)
    f.append(midsem)
    g.append(endsem)
#print (x)
#print(f)
#print(g)
print("\t\t\tRURAL TECHNOLOGY\n")
#for mid sem clash
print("\t\t\tmid sem")
for i in range(len(f)):
    for j in range(len(f)):
        if(i!=j):
            if(f[i]==f[j] and  x[i][2]==x[j][2] ):
                print("Clash in mid sem "+x[i]+" and "+x[j])


for i in range (len(f)):
    if(f[i]==''):
        print("no exam of ",x[i])
#for end sem clash
print("\t\t\tend sem")
for i in range(len(g)):
    for j in range(len(g)):
        if(i!=j):
            if(g[i]==g[j] and  x[i][2]==x[j][2] ):
                print("Clash in end sem "+x[i]+" and "+x[j])


for i in range (len(f)):
    if(g[i]==''):
        print("no exam of ",x[i])

#humanities


x=[]
f=[]
g=[]

for a in y[275:303]:
    if '##' in a:
        continue
    p=a.split(',')
    course=p[0];
    midsem=p[3];
    endsem=p[4];
    x.append(course)
    f.append(midsem)
    g.append(endsem)
#print (x)
#print(f)
#print(g)
print("\t\t\tHUMANITIES\n")
#for mid sem clash
print("\t\t\tmid sem")
for i in range(len(f)):
    for j in range(len(f)):
        if(i!=j):
            if(f[i]==f[j] and  x[i][2]==x[j][2] ):
                print("Clash in mid sem "+x[i]+" and "+x[j])


for i in range (len(f)):
    if(f[i]==''):
        print("no exam of ",x[i])
#for end sem clash
print("\t\t\tend sem")
for i in range(len(g)):
    for j in range(len(g)):
        if(i!=j):
            if(g[i]==g[j] and  x[i][2]==x[j][2] ):
                print("Clash in end sem "+x[i]+" and "+x[j])



for i in range (len(f)):
    if(g[i]==''):
        print("no exam of ",x[i])
#MATH


x=[]
f=[]
g=[]

for a in y[305:317]:
    if '##' in a:
        continue
    p=a.split(',')
    course=p[0];
    midsem=p[3];
    endsem=p[4];
    x.append(course)
    f.append(midsem)
    g.append(endsem)
#print (x)
#print(f)
#print(g)
print("\t\t\tMATH\n")
#for mid sem clash
print("\t\t\tmid sem")
for i in range(len(f)):
    for j in range(len(f)):
        if(i!=j):
            if(f[i]==f[j] and  x[i][2]==x[j][2] ):
                print("Clash in mid sem "+x[i]+" and "+x[j])


for i in range (len(f)):
    if(f[i]==''):
        print("no exam of ",x[i])
#for end sem clash
print("\t\t\tend sem")
for i in range(len(g)):
    for j in range(len(g)):
        if(i!=j):
            if(g[i]==g[j] and  x[i][2]==x[j][2] ):
                print("Clash in end sem "+x[i]+" and "+x[j])

for i in range (len(f)):
    if(g[i]==''):
        print("no exam of ",x[i])
#Mechanical


x=[]
f=[]
g=[]

for a in y[318:327]:
    if '##' in a:
        continue
    p=a.split(',')
    course=p[0];
    midsem=p[3];
    endsem=p[4];
    x.append(course)
    f.append(midsem)
    g.append(endsem)
#print (x)
#print(f)
#print(g)
print("\t\t\tMECHANICAL\n")
#for mid sem clash
print("\t\t\tmid sem")
for i in range(len(f)):
    for j in range(len(f)):
        if(i!=j):
            if(f[i]==f[j] and  x[i][2]==x[j][2] ):
                print("Clash in mid sem "+x[i]+" and "+x[j])


for i in range (len(f)):
    if(f[i]==''):
        print("no exam of ",x[i])



#for end sem clash
print("\t\t\tend sem")
for i in range(len(g)):
    for j in range(len(g)):
        if(i!=j):
            if(g[i]==g[j] and  x[i][2]==x[j][2] ):
                print("Clash in end sem "+x[i]+" and "+x[j])

for i in range (len(f)):
    if(g[i]==''):
        print("no exam of ",x[i])


#ifts


x=[]
f=[]
g=[]

for a in y[329:333]:
    if '##' in a:
        continue
    p=a.split(',')
    course=p[0];
    midsem=p[3];
    endsem=p[4];
    x.append(course)
    f.append(midsem)
    g.append(endsem)
#print (x)
#print(f)
#print(g)
print("\t\t\tMECHANICAL\n")
#for mid sem clash
print("\t\t\tmid sem")
for i in range(len(f)):
    for j in range(len(f)):
        if(i!=j):
            if(f[i]==f[j] and  x[i][2]==x[j][2] ):
                print("Clash in mid sem "+x[i]+" and "+x[j])


for i in range (len(f)):
    if(f[i]==''):
        print("no exam of ",x[i])



#for end sem clash
print("\t\t\tend sem")
for i in range(len(g)):
    for j in range(len(g)):
        if(i!=j):
            if(g[i]==g[j] and  x[i][2]==x[j][2] ):
                print("Clash in end sem "+x[i]+" and "+x[j])

for i in range (len(f)):
    if(g[i]==''):
        print("no exam of ",x[i])
