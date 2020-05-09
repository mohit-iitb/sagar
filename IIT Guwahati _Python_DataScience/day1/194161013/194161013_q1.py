day=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY']
dept=['PHYSICS','CSE','MATH','RURAL_TECHNOLOGY','BIOSCIENCE','ENERGY']
programme=['BTECH3','BTECH5','BTECH7','MSC1','MSC3','DATA_SCIENCE','MTECH1','RURAL_TECHNOLOGY','ENERGY']
time=['8:00-8:55','9:00-9:55','10:00-10:55','11:00-11:55','12:00-12:55','1:00-1:55','2:00-2:55','3:00-3:55','4:00-4:55','5:00-5:55']

for x in day:
    for y in dept:
        for z in programme:
            with open("194161013_q1.txt") as f:
                for line in f:
                    if x!=line.strip():
                        continue
                    else:
                        break


                nextLine=next(f)
                #print(nextLine)
                l=nextLine.split('#')
                #print(l)

                sub=[]

                for index in range(len(l)):
                    slot_sub=''

                    m=l[index].split(',')
                    #print(m)
                    for i in range(len(m)):
                        with open('194161013_q1.txt') as f:
                            for line in f:
                                if line.strip()!=y:
                                    continue
                                else:
                                    break
                            #print(next(f))
                            for line in f:
                                if line.strip()=='%':
                                    break
                                if line.strip()!=z:
                                    continue
                                else:
                                    break
                            if line.strip()=='%':
                                break

                            for line in f:
                                if line.strip()=='$':
                                    break
                                if line.strip()!=m[i]:
                                    continue
                                else:
                                    break
                            if line.strip()=='$':
                                break
                            nL=next(f).strip()

                            #print(nL)

                            if(nL!=''):
                                if slot_sub== '':
                                    slot_sub=nL
                                else:
                                    slot_sub=slot_sub+'/'+nL


                    sub.append(slot_sub)

                #print(sub)

            for j in range(len(sub)):
                if(len(sub[j].split('/'))>1):
                    #clash_sub=sub[j].split('/')
                    print("For "+y+" , "+z+" Time slot "+time[j]+" has clash in "+sub[j]+" on "+x)
