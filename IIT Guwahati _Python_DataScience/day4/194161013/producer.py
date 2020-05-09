from kafka import KafkaProducer
import threading

#p=f.read()
#print(p)
#print(len(p))

def fun1():
    producer1 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match1_commentry.txt','r')
    for j in f:
        print('Match1',j)
        producer1.send("Match1", value=bytes(j,encoding='utf-8'))
        producer1.flush()

def fun2():
    producer2 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match2_commentry.txt','r')
    for j in f:
        print('Match2',j)
        producer2.send("Match2", value=bytes(j,encoding='utf-8'))
        producer2.flush()



def fun3():
    producer3 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match3_commentry.txt','r')
    for j in f:
        print('Match3',j)
        producer3.send("Match3", value=bytes(j,encoding='utf-8'))
        producer3.flush()

def fun4():
    producer4 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match4_commentry.txt','r')
    for j in f:
        print('Match4',j)
        producer4.send("Match4", value=bytes(j,encoding='utf-8'))
        producer4.flush()

def fun5():
    producer5 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match5_commentry.txt','r')
    for j in f:
        print('Match5',j)
        producer5.send("Match5", value=bytes(j,encoding='utf-8'))
        producer5.flush()

def fun6():
    producer6 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match6_commentry.txt','r')
    for j in f:
        print('Match6',j)
        producer6.send("Match6", value=bytes(j,encoding='utf-8'))
        producer6.flush()



def fun7():
    producer7 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match7_commentary.txt','r')
    for j in f:
        print('Match7',j)
        producer7.send("Match7", value=bytes(j,encoding='utf-8'))
        producer7.flush()



def fun8():
    producer8 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match8_commentary.txt','r')
    for j in f:
        print('Match8',j)
        producer8.send("Match8", value=bytes(j,encoding='utf-8'))
        producer8.flush()


def fun12():
    producer12 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match12_commentary.txt','r')
    for j in f:
        print('Match12',j)
        producer12.send("Match12", value=bytes(j,encoding='utf-8'))
        producer12.flush()


def fun13():
    producer13 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match13_commentary.txt','r')
    for j in f:
        print('Match13',j)
        producer13.send("Match13", value=bytes(j,encoding='utf-8'))
        producer13.flush()


def fun14():
    producer14 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match14_commentary.txt','r')
    for j in f:
        print('Match14',j)
        producer14.send("Match14", value=bytes(j,encoding='utf-8'))
        producer14.flush()


def fun19():
    producer19 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match19_commentary.txt','r')
    for j in f:
        print('Match19',j)
        producer19.send("Match19", value=bytes(j,encoding='utf-8'))
        producer19.flush()


def fun20():
    producer20 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match20_commentary.txt','r')
    for j in f:
        print('Match20',j)
        producer20.send("Match20", value=bytes(j,encoding='utf-8'))
        producer20.flush()


def fun21():
    producer21 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match21_Commentary.txt','r')
    for j in f:
        print('Match21',j)
        producer21.send("Match21", value=bytes(j,encoding='utf-8'))
        producer21.flush()


def fun22():
    producer22 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match22_Commentary.txt','r')
    for j in f:
        print('Match22',j)
        producer22.send("Match22", value=bytes(j,encoding='utf-8'))
        producer22.flush()


def fun25():
    producer25 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match25_commentary.txt','r')
    for j in f:
        print('Match25',j)
        producer25.send("Match25", value=bytes(j,encoding='utf-8'))
        producer25.flush()



def fun26():
    producer26 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match26_commentary.txt','r')
    for j in f:
        print('Match26',j)
        producer26.send("Match26", value=bytes(j,encoding='utf-8'))
        producer26.flush()


def fun27():
    producer27 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match27_commentary.txt','r')
    for j in f:
        print('Match27',j)
        producer27.send("Match27", value=bytes(j,encoding='utf-8'))
        producer27.flush()



def fun28():
    producer28 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match28_commentary.txt','r')
    for j in f:
        print('Match28',j)
        producer28.send("Match28", value=bytes(j,encoding='utf-8'))
        producer28.flush()



def fun29():
    producer29 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match29_commentary.txt','r')
    for j in f:
        print('Match29',j)
        producer29.send("Match29", value=bytes(j,encoding='utf-8'))
        producer29.flush()


def fun30():
    producer30 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match30_commentary.txt','r')
    for j in f:
        print('Match30',j)
        producer30.send("Match30", value=bytes(j,encoding='utf-8'))
        producer30.flush()


def fun31():
    producer31 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match31_commentary.txt','r')
    for j in f:
        print('Match31',j)
        producer31.send("Match31", value=bytes(j,encoding='utf-8'))
        producer31.flush()


def fun32():
    producer32 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match32_commentary.txt','r')
    for j in f:
        print('Match32',j)
        producer32.send("Match32", value=bytes(j,encoding='utf-8'))
        producer32.flush()




def fun33():
    producer33 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match33_commentary.txt','r')
    for j in f:
        print('Match33',j)
        producer33.send("Match33", value=bytes(j,encoding='utf-8'))
        producer33.flush()


def fun35():
    producer35 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match35_commentary.txt','r')
    for j in f:
        print('Match35',j)
        producer35.send("Match35", value=bytes(j,encoding='utf-8'))
        producer35.flush()



def fun36():
    producer36 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match36_commenary.txt','r')
    for j in f:
        print('Match36',j)
        producer36.send("Match36", value=bytes(j,encoding='utf-8'))
        producer36.flush()


def fun41():
    producer41 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match41_commentary.txt','r')
    for j in f:
        print('Match41',j)
        producer41.send("Match41", value=bytes(j,encoding='utf-8'))
        producer41.flush()


def fun42():
    producer42 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match42_commentary.txt','r')
    for j in f:
        print('Match42',j)
        producer42.send("Match42", value=bytes(j,encoding='utf-8'))
        producer42.flush()


def fun43():
    producer43 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match43_commentry.txt','r')
    for j in f:
        print('Match43',j)
        producer43.send("Match43", value=bytes(j,encoding='utf-8'))
        producer43.flush()


def fun44():
    producer44 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match44_commentry.txt','r')
    for j in f:
        print('Match44',j)
        producer44.send("Match44", value=bytes(j,encoding='utf-8'))
        producer44.flush()

def fun45():
    producer45 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match45_Commentary.txt','r')
    for j in f:
        print('Match45',j)
        producer45.send("Match45", value=bytes(j,encoding='utf-8'))
        producer45.flush()




def fun46():
    producer46 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match46_Commentary.txt','r')
    for j in f:
        print('Match46',j)
        producer46.send("Match46", value=bytes(j,encoding='utf-8'))
        producer46.flush()




def fun47():
    producer47 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match47_commentary.txt','r')
    for j in f:
        print('Match47',j)
        producer47.send("Match47", value=bytes(j,encoding='utf-8'))
        producer47.flush()




def fun48():
    producer48 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match48_commentary.txt','r')
    for j in f:
        print('Match48',j)
        producer48.send("Match48", value=bytes(j,encoding='utf-8'))
        producer48.flush()



t1=threading.Thread(target=fun1)
t2=threading.Thread(target=fun2)
t3=threading.Thread(target=fun3)
t4=threading.Thread(target=fun4)
t5=threading.Thread(target=fun5)
t6=threading.Thread(target=fun6)
t7=threading.Thread(target=fun7)
t8=threading.Thread(target=fun8)
t12=threading.Thread(target=fun12)
t13=threading.Thread(target=fun13)
t14=threading.Thread(target=fun14)
t19=threading.Thread(target=fun19)
t20=threading.Thread(target=fun20)
t21=threading.Thread(target=fun21)
t22=threading.Thread(target=fun22)
t25=threading.Thread(target=fun25)
t26=threading.Thread(target=fun26)
t27=threading.Thread(target=fun27)
t28=threading.Thread(target=fun28)
t29=threading.Thread(target=fun29)
t30=threading.Thread(target=fun30)
t31=threading.Thread(target=fun31)
t32=threading.Thread(target=fun32)
t33=threading.Thread(target=fun33)
t35=threading.Thread(target=fun35)
t36=threading.Thread(target=fun36)
t41=threading.Thread(target=fun41)
t42=threading.Thread(target=fun42)
t43=threading.Thread(target=fun43)
t44=threading.Thread(target=fun44)
t45=threading.Thread(target=fun45)
t46=threading.Thread(target=fun46)
t47=threading.Thread(target=fun47)
t48=threading.Thread(target=fun48)






t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t12.start()
t13.start()
t14.start()
t19.start()
t20.start()
t21.start()
t22.start()
t25.start()
t26.start()
t27.start()
t28.start()
t29.start()
t30.start()
t31.start()
t32.start()
t33.start()
t35.start()
t36.start()
t41.start()
t42.start()
t43.start()
t44.start()
t45.start()
t46.start()
t47.start()
t48.start()
