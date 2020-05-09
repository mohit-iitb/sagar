#india and south africa match
#Match no-8
#Indian_PLayers_Name=[]
over2=[] #2st inning Over ,india Batting
over1=[] #1nd inning Over ,south africa Batting
run2=[] #run list  scored by indian
run1=[] #run list scored by SA
bb2=[] #batsman Bowler list for 2nd inning
bb1=[] #Batsman Bowler list for 1st inning
count=0
from linecache import getline
import re
fw=open("1941661013_ODIno_scorecard_computed.txt","w+")
with open('194161013_ODIno.4150_commentary.txt','r') as f:
    for ind, i in enumerate(f,1):

        if i !=  '##########\n':
            regex=re.findall("\d{1,2}\.\d?$", i)

            if regex!=[]:

                #y=run1.split(',')
                #print(run1)
                if(count==0):
                    over2.append(regex)
                    nextline = getline(f.name, ind + 1)
                    run2.append(nextline.split('\n')[0])
                    nextline1 = getline(f.name, ind + 2)
                    bb2.append(nextline1)
                if (count == 1):
                    over1.append(regex)
                    nextline = getline(f.name, ind + 1)
                    run1.append(nextline.split('\n')[0])
                    nextline1 = getline(f.name, ind + 2)
                    bb1.append(nextline1)
        if i=='##########\n':
            count=1


Bowler1=[]
Batsman1=[]


for i in range(0,len(bb1)):
    #print(bb1[i])
    x=bb1[i].split(' to ')[0]
    y=bb1[i].split('to')[1]
    yy=y.split(',')[0]
    Bowler1.append(x)
    Batsman1.append(yy)

#1st inning(South Africa) over_list,run_list,Bowler_Batsman_list
print(over1)
print(run1)
print(Bowler1)
print(Batsman1)

'''
#length of the list

print(len(over1))
print(len(run1))
print(len(Bowler1))
print(len(Batsman1))'''


Bowler2=[]
Batsman2=[]



for i in range(0,len(bb2)):
    #print(bb1[i])
    x=bb2[i].split(' to ')[0]
    y=bb2[i].split('to')[1]
    yy=y.split(',')[0]
    Bowler2.append(x)
    Batsman2.append(yy)






# 2nd inning(india) over_list,run_list,Bowler_Batsman_list
#print(over2)
#print(run2)
#print(Bowler2)
#print(Batsman2)
#print(sum(run2))

#length of the list

'''print(len(over2))
print(len(run2))
print(len(Bowler2))
print(len(Batsman2))'''
Indian_Players_Name=[' Pandya',' Sharma',' Dhoni',' Rahul',' Sharma',' Kohli',' Dhawan']
index=[]
indexes= {}
ind=0
for k in range(0,len(Indian_Players_Name)):
    for j in range(0, len(Batsman2)):
       # print(Indian_Players_Name[k])
        if Indian_Players_Name[k] == Batsman2[j]:
            index.append(j)
        indexes.update({Indian_Players_Name[k]:index})
    index=[]

for key,val in indexes.items():
    '''print(key+"->"+str(val))'''

# RUN CALCULATION
#pandya
#print(indexes[' Pandya'])
b1=indexes[' Pandya']
#print(b1)
add1=0
for i in range(0,len(b1)):
    if run2[i]!='1w':
        add1=add1+int(run2[i])
#print('pandya  =',add1,len(b1)-1,round((add1/(len(b1)-1)*100),2))

four='4'
count1=0
for j in range(len(b1)):
    x=b1[j]
    #print(x)
    if four==run2[x]:
        count1=count1+1
#print(count1)
six='6'
c1=0
for j in range(len(b1)):
    x=b1[j]
    #print(x)
    if six==run2[x]:
        c1=c1+1
#print('six',c1)



#dhawan
b2=indexes[' Dhawan']
#print(b2)
add2=0
for j in range(len(b2)):
    x=b2[j]
    #print(x,run2[x])
    if run2[x]!='W':
        add2=add2+int(run2[x])
#print('Dhawan =',add2,len(b2),round((add2/(len(b2))*100),2))




four='4'
count2=0
for j in range(len(b2)):
    x=b2[j]
    #print(x)
    if four==run2[x]:
        count2=count2+1
#print(count2)

six='6'
c2=0
for j in range(len(b2)):
    x=b2[j]
    #print(x)
    if six==run2[x]:
        c2=c2+1
#print('six',c2)


#kohli
b3=indexes[' Kohli']
#print(b3)
add3=0
for j in range(len(b3)):
    x=b3[j]
    #print(x,run2[x])
    if run2[x]!='W':
        add3=add3+int(run2[x])
#print('Kohli=',  add3,len(b3),round((add3/(len(b3))*100),2))

four='4'
count3=0
for j in range(len(b3)):
    x=b3[j]
    #print(x)
    if four==run2[x]:
        count3=count3+1
#print(count3)

six='6'
c3=0
for j in range(len(b3)):
    x=b3[j]
    #print(x)
    if six==run2[x]:
        c3=c3+1
#print('six',c3)

#dhoni
b4=indexes[' Dhoni']
#print(b4)
#print(run2[9])
add4=0
for j in range(len(b4)):
    #print('s')
    x=b4[j]
    #print(x,run2[x])
    if run2[x]=='W':
        continue
    elif run2[x]=='1lb':
        continue
    elif run2[x]=='1w':
        continue
    else:
        add4=add4+int(run2[x])

#print('Dhoni=',  add4,len(b4)-1,round((add4/(len(b4)-1)*100),2))

four='4'
count4=0
for j in range(len(b4)):
    x=b4[j]
    #print(x)
    if four==run2[x]:
        count4=count4+1
#print(count4)


six='6'
c4=0
for j in range(len(b4)):
    x=b4[j]
    #print(x)
    if six==run2[x]:
        c4=c4+1
#print('six',c4)

#sharma
b5=indexes[ ' Sharma']
#print(b4)
#print(run2[9])
add5=0
for j in range(len(b5)):
    #print('s')
    x=b5[j]
    #print(x,run2[x])
    if run2[x]=='W':
        continue
    elif run2[x]=='1lb':
        continue
    elif run2[x]=='1w':
        continue
    else:
        add5=add5+int(run2[x])

#print('sharma=',  add5,len(b5)-2,round((add5/(len(b5)-2)*100),2))
#no of four of sharma
four='4'
count5=0
for j in range(len(b5)):
    x=b5[j]
    #print(x)
    if four==run2[x]:
        count5=count5+1
#print(count5)



# no. of sixes of sharma
six='6'
c5=0
for j in range(len(b5)):
    x=b5[j]
    #print(x)
    if six==run2[x]:
        c5=c5+1
#print('six',c5)

#Rahul
b6=indexes[ ' Rahul']
#print(b6)
#print(run2[9])
add6=0
for j in range(len(b6)):
    #print('s')
    x=b6[j]
    #print(x,run2[x])
    if run2[x]=='W':
        continue
    elif run2[x]=='1lb':
        continue
    elif run2[x]=='1w':
        continue
    else:
        add6=add6+int(run2[x])

#print('Rahul=',  add6,len(b6),round((add6/len(b6)*100),2))

four='4'
count6=0
for j in range(len(b6)):
    x=b6[j]
    #print(x)
    if four==run2[x]:
        count6=count6+1
#print(count6)


six='6'
c6=0
for j in range(len(b6)):
    x=b6[j]
    #print(x)
    if six==run2[x]:
        c6=c6+1
#print('si  x',c6)

#extras run
lb=0
w=0
for i in range(len(run2)):
    if run2[i]=='W':
        continue
    elif run2[i]=='1lb':
        lb=lb+1
        continue
    elif run2[i]=='1w':
        w=w+1
        continue
    else:
        continue
#print(lb)
#print(w)
extras=lb+w
#print('Extras=',lb+w)


#Total_run
Total_run=add1+add2+add3+add4+add5+add6+extras
#Total_over
Total_over=over2[0][0]
#Run Rate
rr=Total_over.split('.')
#print(rr)
#print(rr[0])
Total_ball_played=int(rr[0])*6+int(rr[1])
#print(Total_ball_played)
run_rate=int(Total_run)/float(Total_over)
#print(round(run_rate,2))


'''with open('194161013_ODIno.4150_commentary.txt','r') as f:
    for i in f:
        minute_finding=re.search(r'[W]')'''

fw.write("India Innings"+"\n")

fw.write("BATSMEN".ljust(20)+"R".ljust(5)+"B".ljust(5)+"4s".ljust(5)+"6s".ljust(5)+"SR".ljust(5)+"\n")
#print('Dhawan ',add2,len(b2),count2,c2,round((add2/(len(b2))*100),2))
fw.write('Dhawan  '.ljust(20)+str(add2).ljust(5)+str(len(b2)).ljust(5)+str(count2).ljust(5)+str(c2).ljust(5)+str(round((add2/(len(b2))*100),2))+"\n")
#print('sharma ',  add5,len(b5)-2,count5,c5,round((add5/(len(b5)-2)*100),2))
fw.write('sharma  '.ljust(20) +str(add5).ljust(5)+str(len(b5)-2).ljust(5)+str(count5).ljust(5)+str(c5).ljust(5)+str(round((add5/(len(b5)-2)*100),2))+"\n")
#print('Kohli ',  add3,len(b3),count3,c3,round((add3/(len(b3))*100),2))
fw.write('Kohli  '.ljust(20)+ str(add3).ljust(5)+str(len(b3)).ljust(5)+str(count3).ljust(5)+str(c3).ljust(5)+str(round((add3/(len(b3))*100),2))+"\n")
#print('Rahul  ',  add6,len(b6),count6,c6,round((add6/len(b6)*100),2))
fw.write('Rahul  '.ljust(20)+str( add6).ljust(5)+str(len(b6)).ljust(5)+str(count6).ljust(5)+str(c6).ljust(5)+str(round((add6/len(b6)*100),2))+"\n")
#print('Dhoni  ',  add4,len(b4)-1,count4,c4,round((add4/(len(b4)-1)*100),2))
fw.write('Dhoni  '.ljust(20)+str(add4).ljust(5)+str(len(b4)-1).ljust(5)+str(count4).ljust(5)+str(c4).ljust(5)+str(round((add4/(len(b4)-1)*100),2))+"\n")
#print('pandya ',add1,len(b1)-1,count1,c1,round((add1/(len(b1)-1)*100),2))
fw.write('pandya '.ljust(20)+str(add1).ljust(5)+str(len(b1)-1).ljust(5)+str(count1).ljust(5)+str(c1).ljust(5)+str(round((add1/(len(b1)-1)*100),2))+"\n")
#print('Extras ',extras,'(lb ',lb,',w ',w,')')
fw.write('Extras '.ljust(40)+str(extras)+'(lb '+str(lb)+',w '+str(w)+')'+"\n")
#print('Total_run',str(Total_run)+'/'+str(4))
fw.write('TOTAL'.ljust(32)+str(Total_run)+'/'+str(4)+'('+str(Total_over)+',RR:'+str(round(run_rate,2))+')')
#print(Total_over)


##Bowling



SA_Players_Name=['Phehlukwayo','Morris', 'Rabada', 'Imran Tahir', 'Shamsi']
index_Bowler=[]
indexes_Bowler= {}
ind=0
for k in range(0,len(SA_Players_Name)):
    for j in range(0, len(Bowler2)):
       # print(Indian_Players_Name[k])
        if SA_Players_Name[k] == Bowler2[j]:
            index_Bowler.append(j)
        indexes_Bowler.update({SA_Players_Name[k]:index_Bowler})
    index_Bowler=[]

for key,val in indexes_Bowler.items():
    '''print(key+"->"+str(val))'''



#Imran Tahir
b2_ball=indexes_Bowler['Imran Tahir']
#print(b2_ball)
sum2=0
lb2=0
w2=0
for j in range(len(b2_ball)):
    #print('s')
    x=b2_ball[j]
    #print(x,run2[x])
    if run2[x]=='W':
        continue
    elif run2[x]=='1lb':
        lb2=lb2+1
        continue

    elif run2[x]=='1w':
        w2=w2+1
        continue

    else:
        sum2=sum2+int(run2[x])
#print('Dhawan =',add2,len(b2),round((add2/(len(b2))*100),2))
#print(sum2)



four='4'
countt2=0
for j in range(len(b2_ball)):
    x=b2_ball[j]
    #print(x)
    if four==run2[x]:
        countt2=countt2+1
#print(countt2)

six='6'
c_2=0
for j in range(len(b2_ball)):
    x=b2_ball[j]
    #print(x)
    if six==run2[x]:
        c_2=c_2+1
#print('six',c2)
#Total_over by imran Tahir
over_imran_tahir=int(len(b2_ball)/6)
#print(len(b2_ball))
#print(over_imran_tahir)




#did not bat
fw.write("\n \n")

fw.write("Fall of wickets: 1-13 (Shikhar Dhawan, 5.1 ov), 2-54 (Virat Kohli, 15.3 ov), 3-139 (KL Rahul, 31.3 ov), 4-213 (MS Dhoni, 46.1 ov)")



##




#Phehlukwayo
b1_ball=indexes_Bowler['Phehlukwayo']
#print(b1_ball)
sum1=0
w1=-0
for j in range(len(b1_ball)):
    #print('s')
    x=b1_ball[j]
    #print(x,run2[x])
    if run2[x]=='W':
        continue
    elif run2[x]=='1lb':
        continue
    elif run2[x]=='1w':
        w1=w1+1
        continue
    else:
        sum1=sum1+int(run2[x])
#print('Dhawan =',add2,len(b2),round((add2/(len(b2))*100),2))
#print(sum1+1)



four='4'
countt1=0
for j in range(len(b1_ball)):
    x=b1_ball[j]
    #print(x)
    if four==run2[x]:
        countt1=countt1+1
#print("four",countt1)

six='6'
c_1=0
for j in range(len(b1_ball)):
    x=b1_ball[j]
    #print(x)
    if six==run2[x]:
        c_1=c_1+1
#print('six',c_1)
#Total_over by imran Tahir
over_Phehlukwayo=round(float(len(b1_ball)/6),2)
#print(len(b1_ball))
#print(over_Phehlukwayo)


#Rabada
b3_ball=indexes_Bowler['Rabada']
#print(b1_ball)
sum3=0
w3=0
for j in range(len(b3_ball)):
    #print('s')
    x=b3_ball[j]
    #print(x,run2[x])
    if run2[x]=='W':
        continue
    elif run2[x]=='1lb':
        continue
    elif run2[x]=='1w':
        w3=w3+1
        continue
    else:
        sum3=sum3+int(run2[x])
#print('Dhawan =',add2,len(b2),round((add2/(len(b2))*100),2))
#print(sum3+1)



four='4'
countt3=0
for j in range(len(b3_ball)):
    x=b3_ball[j]
    #print(x)
    if four==run2[x]:
        countt3=countt3+1
#print("four",countt3)

six='6'
c_3=0
for j in range(len(b3_ball)):
    x=b3_ball[j]
    #print(x)
    if six==run2[x]:
        c_3=c_3+1
#print('six',c_3)
#Total_over by rabada
over_Rabada=round(int((len(b3_ball)-1)/6),2)
#print(len(b3_ball))
#print(over_Rabada)




#Shamsi
b4_ball=indexes_Bowler['Shamsi']
#print(b1_ball)
sum4=0
w4=0
for j in range(len(b4_ball)):
    #print('s')
    x=b4_ball[j]
    #print(x,run2[x])
    if run2[x]=='W':
        continue
    elif run2[x]=='1lb':
        continue
    elif run2[x]=='1w':
        w4=w4+1
        continue
    else:
        sum4=sum4+int(run2[x])
#print('Dhawan =',add2,len(b2),round((add2/(len(b2))*100),2))
#print(sum4+1)



four='4'
countt4=0
for j in range(len(b4_ball)):
    x=b4_ball[j]
    #print(x)
    if four==run2[x]:
        countt4=countt4+1
#print("four",countt4)

six='6'
c_4=0
for j in range(len(b4_ball)):
    x=b4_ball[j]
    #print(x)
    if six==run2[x]:
        c_4=c_4+1
#print('six',c_4)
#Total_over by rabada
over_Shamsi=round(int((len(b4_ball)-1)/6),2)
#print(len(b3_ball))
#print(over_Shamsi)







#Morris
b5_ball=indexes_Bowler['Morris']
#print(b1_ball)
sum5=0
w5=0
one5=0
for j in range(len(b5_ball)):
    #print('s')
    x=b5_ball[j]
    #print(x,run2[x])
    if run2[x]=='W':
        continue
    elif run2[x]=='1lb':
        continue
    elif run2[x]=='1w':
        w5=w5+1
        continue
    elif run2[x]=='0':
        one5=one5+1
        continue
    else:
        sum5=sum5+int(run2[x])
#print('Dhawan =',add2,len(b2),round((add2/(len(b2))*100),2))
#print(sum5+1)
#print("1",one5)



four='4'
countt5=0
for j in range(len(b5_ball)):
    x=b5_ball[j]
    #print(x)
    if four==run2[x]:
        countt5=countt5+1
#print("four",countt5)

six='6'
c_5=0
for j in range(len(b5_ball)):
    x=b5_ball[j]
    #print(x)
    if six==run2[x]:
        c_5=c_5+1
#print('six',c_5)
#Total_over by rabada
over_Morris=round(int((len(b5_ball)-1)/6),2)
#print(len(b5_ball))
#print(over_Morris)


####






###
fw.write("\n\n\n")
fw.write('BOWLING'.ljust(20)+'O'.ljust(5)+"R".ljust(5)+"4s".ljust(5)+"6s".ljust(5)+"WD".ljust(5)+"NB"+"\n")
fw.write("Imran Tahir".ljust(20)+str(over_imran_tahir).ljust(5)+str(sum2).ljust(5)+str(countt2).ljust(5)+str(c_2).ljust(5)+str(w2).ljust(5)+'0'+"\n")
fw.write("Rabada".ljust(20)+str(over_Rabada).ljust(5)+str(sum3+1).ljust(5)+str(countt3).ljust(5)+str(c_3).ljust(5)+str(w3).ljust(5)+'0'+"\n")
fw.write("Morris".ljust(20)+str(over_Morris).ljust(5)+str(sum5+1).ljust(5)+str(countt5).ljust(5)+str(c_5).ljust(5)+str(w5).ljust(5)+'0'+"\n")

fw.write("Phehlukwayo".ljust(20)+str(over_Phehlukwayo).ljust(5)+str(sum1+1).ljust(5)+str(countt1).ljust(5)+str(c_1).ljust(5)+str(w1).ljust(5)+'0'+"\n")
fw.write("Shamsi".ljust(20)+str(over_Shamsi).ljust(5)+str(sum4+1).ljust(5)+str(countt4).ljust(5)+str(c_4).ljust(5)+str(w4).ljust(5)+'0'+"\n")



###south africa innings
##batting inning




SA_Players=[' Imran Tahir',' Rabada','du Plessis']
index=[]
indexes= {}
ind=0
for k in range(0,len(SA_Players)):
    for j in range(0, len(Batsman1)):
       # print(Indian_Players_Name[k])
        if SA_Players[k] == Batsman1[j]:
            index.append(j)
        indexes.update({SA_Players[k]:index})
    index=[]

for key,val in indexes.items():
    print(key+"->"+str(val))

#Run calculation
#Rabada
B1=indexes[ ' Rabada']
#print(b4)
#print(run2[9])
addition1=0
for j in range(len(B1)):
    #print('s')
    x=B1[j]
    #print(x,run2[x])
    if run1[x]=='W':
        continue
    elif run1[x]=='1lb':
        continue
    elif run1[x]=='1w':
        continue
    else:
        addition1=addition1+int(run1[x])

print('Rabada=',  addition1,len(B1)-1,round((addition1/(len(B1)-1)*100),2))
#no of four of sharma
four='4'
cc1=0
for j in range(len(B1)):
    x=B1[j]
    #print(x)
    if four==run1[x]:
        cc1=cc1+1
print(cc1)



# no. of sixes of sharma
six='6'
co1=0
for j in range(len(B1)):
    x=B1[j]
    #print(x)
    if six==run1[x]:
        co1=co1+1
print('six',co1)
'''
#du Plessis
B2=indexes[ ' du Plessis']
#print(b4)
#print(run2[9])
addition2=0
for j in range(len(B2)):
    #print('s')
    x=B2[j]
    #print(x,run2[x])
    if run1[x]=='W':
        continue
    elif run1[x]=='1lb':
        continue
    elif run1[x]=='1w':
        continue
    else:
        addition2=addition2+int(run1[x])

#print('Rabada=',  addition1,len(B1)-1,round((addition1/(len(B1)-1)*100),2))
#no of four of sharma
four='4'
cc2=0
for j in range(len(B1)):
    x=B1[j]
    #print(x)
    if four==run1[x]:
        cc2=cc2+1
#print(cc2)



# no. of sixes of sharma
six='6'
co2=0
for j in range(len(B1)):
    x=B1[j]
    #print(x)
    if six==run1[x]:
        co2=co2+1
#print('six',co2)'''


fw.write("\n\n\n")
fw.write("South Africa Inning\n")
fw.write("BATSMEN".ljust(20)+"R".ljust(5)+"B".ljust(5)+"4s".ljust(5)+"6s".ljust(5)+"SR".ljust(5)+"\n")
#fw.write('du Plessis '.ljust(20) +str(addition2).ljust(5)+str(len(B2)-1).ljust(5)+str(cc2).ljust(5)+str(co2).ljust(5)+str(round((addition2/(len(B2)-1)*100),2))+"\n")

fw.write('Rabada  '.ljust(20) +str(addition1).ljust(5)+str(len(B1)-1).ljust(5)+str(cc1).ljust(5)+str(co1).ljust(5)+str(round((addition1/(len(B1)-1)*100),2))+"\n")
