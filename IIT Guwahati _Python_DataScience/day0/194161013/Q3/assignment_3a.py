i=0
while(i<1000):
    import random
    a=random.randint(2017,2019)
    a=str(a)
    c=a[2]
    d=a[3]
    s1=["BTECH","BDES","MSC","MA","MTECH","MDES","MS","PHD","DUAL_CSE","DUAL_EEE"]
    b=random.choice(s1)
    b=str(b)
    xy=random.randint(100,999)
    xy=str(xy)
    if b=="BTECH":
        s2=["CSE","ECE","ME","CE","BSBE","CL","EEE"]
        ss=random.choice(s2)
        if ss=="CSE":
            ab='01'
        elif ss=="ECE":
            ab='02'
        elif ss=="ME":
            ab='03'
        elif ss=="CE":
            ab='04'
        elif ss=="BSEB":
            ab='06'
        elif ss=="CL":
            ab='07'
        elif ss=="EEE":
            ab='08'
        print(a+"   "+b+"          "+ss+"                              "+xy+ "                     "+" _ "+c+d+'01'+ab+xy)
    elif b=="BDES":
        print(a+"   "+b+"           "+"DESIGN"+"                           "+xy+"                    "+" _ "+c+d+'02'+'05'+xy)
    elif b=="MSC":
        s3=["Physics","Cemistry"]
        x=random.choice(s3)
        if x=="Physics":
            abc='21'
        elif x=="Chemistry":
            abc='22'
        print(a+"   "+b+"            "+x+"                          "+xy+"                 " +"_ "+c+d+'21'+abc+xy)
    elif b=="MA":
        print(a+"   "+b+"             "+"Development Studies"+"              "+xy+"                "+"  _ "+c+d+'22'+'41'+xy)
    elif b=="MTECH":
        s5=["CSE","ME","CE","BSBE","CL","EEE","DATA SCIENCE"]
        y=random.choice(s5)
        if y=="CSE":
            ab='01'
        elif y=="ME":
            ab='03'
        elif y=="CE":
            ab='04'
        elif y=="BSBE":
            ab='06'
        elif y=="CL":
            ab='07'
        elif y=="EEE":
            ab='08'
        elif y=="DATA SCIENCE":
            ab='61'
        print(a+"   "+b+"          "+y+"                            "+xy+"                 "+" _ "+c+d+'41'+ab+xy)
    elif b=="MDES":
         print(a+"   "+b+"           "+"DESIGN"+"                           "+xy+"                 "+" _ "+c+d+'42'+'05'+xy)
    elif b=="MS":
        print(a+"   "+b+"             "+"ENERGY"+"                           "+xy+"               " +" _ "+c+d+'43'+'51'+xy)
    elif b=="PHD":
        s7=["CSE","EEE","ME","CE"]
        p=random.choice(s7)
        if p=="CSE":
            ab='01'
        elif p=="EEE":
            ab='08'
        elif p=="ME":
            ab='03'
        elif p=="CE":
            ab='04'
        print(a+"   "+b+"            "+p+"                              "+xy+"                        "+" _ "+c+d+'61'+ab+xy)
    elif b=="DUAL_CSE":
        print(a+"   "+b+"       "+"CSE"+"                              "+xy+"              "+" _ "+c+d+'62'+'01'+xy)
    elif b=="DUAL_EEE":
        print(a+"   "+b+"       "+"EEE"+"                              "+xy+"               "+" _ "+c+d+'63'+'08'+xy)
    i=i+1

    
    

    
    
