i=0
while i<50:
    import random
    a=random.randint(16,19)
    s1=['01','02','21','22','41','42','43','61','62','63']
    b=random.choice(s1)
    s2=['01','02','03','04','05','06','07','08','21','22','23','41','51','52','53','54','55']
    c=random.choice(s2)
    d=random.randint(101,999)
    a=str(a)
    d=str(d)
    e=a+b+c+d
    print(e)
    i=i+1
print('0')


