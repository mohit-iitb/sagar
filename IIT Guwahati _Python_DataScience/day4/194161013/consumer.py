from kafka import KafkaConsumer
import threading

#auto_offset_reset = 'earliest'
#consumer = KafkaConsumer('foobar')

def fun1():
    consumer1 = KafkaConsumer("Match1",bootstrap_servers=['localhost:9092'])
    f=open('out_match1.txt','w')
    for msg in consumer1:
        print("match1",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s\n" % msg.value.decode('utf-8'))


def fun2():

    consumer2 = KafkaConsumer("Match2",bootstrap_servers=['localhost:9092'])
    f=open('out_match2.txt','w')
    for msg in consumer2:
        print("match2",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))


def fun3():

    consumer3 = KafkaConsumer("Match3",bootstrap_servers=['localhost:9092'])
    f=open('out_match3.txt','w')
    for msg in consumer3:
        print("match3",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))


def fun4():

    consumer4 = KafkaConsumer("Match4",bootstrap_servers=['localhost:9092'])
    f=open('out_match4.txt','w')
    for msg in consumer4:
        print("match4",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))

def fun5():

    consumer5 = KafkaConsumer("Match5",bootstrap_servers=['localhost:9092'])
    f=open('out_match5.txt','w')
    for msg in consumer5:
        print("match5",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))


def fun6():

    consumer6 = KafkaConsumer("Match6",bootstrap_servers=['localhost:9092'])
    f=open('out_match6.txt','w')
    for msg in consumer6:
        print("match6",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))


def fun7():

    consumer7 = KafkaConsumer("Match7",bootstrap_servers=['localhost:9092'])
    f=open('out_match7.txt','w')
    for msg in consumer7:
        print("match7",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))





def fun8():

    consumer8 = KafkaConsumer("Match8",bootstrap_servers=['localhost:9092'])
    f=open('out_match8.txt','w')
    for msg in consumer8:
        print("match8",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))



def fun12():

    consumer12 = KafkaConsumer("Match12",bootstrap_servers=['localhost:9092'])
    f=open('out_match12.txt','w')
    for msg in consumer12:
        print("match12",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))

def fun13():

    consumer13 = KafkaConsumer("Match13",bootstrap_servers=['localhost:9092'])
    f=open('out_match13.txt','w')
    for msg in consumer13:
        print("match13",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))


def fun14():

    consumer14 = KafkaConsumer("Match14",bootstrap_servers=['localhost:9092'])
    f=open('out_match14.txt','w')
    for msg in consumer14:
        print("match14",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))

def fun19():

    consumer19 = KafkaConsumer("Match19",bootstrap_servers=['localhost:9092'])
    f=open('out_match19.txt','w')
    for msg in consumer19:
        print("match19",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))


def fun20():

    consumer20 = KafkaConsumer("Match20",bootstrap_servers=['localhost:9092'])
    f=open('out_match20.txt','w')
    for msg in consumer20:
        print("match20",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))



def fun21():

    consumer21 = KafkaConsumer("Match21",bootstrap_servers=['localhost:9092'])
    f=open('out_match21.txt','w')
    for msg in consumer21:
        print("match21",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))



def fun22():

    consumer22 = KafkaConsumer("Match22",bootstrap_servers=['localhost:9092'])
    f=open('out_match22.txt','w')
    for msg in consumer22:
        print("match22",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))



def fun25():

    consumer25 = KafkaConsumer("Match25",bootstrap_servers=['localhost:9092'])
    f=open('out_match25.txt','w')
    for msg in consumer25:
        print("match25",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))



def fun26():

    consumer26 = KafkaConsumer("Match26",bootstrap_servers=['localhost:9092'])
    f=open('out_match26.txt','w')
    for msg in consumer26:
        print("match26",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))



def fun27():

    consumer27 = KafkaConsumer("Match27",bootstrap_servers=['localhost:9092'])
    f=open('out_match27.txt','w')
    for msg in consumer27:
        print("match27",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))


def fun28():

    consumer28 = KafkaConsumer("Match28",bootstrap_servers=['localhost:9092'])
    f=open('out_match28.txt','w')
    for msg in consumer28:
        print("match28",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))

def fun29():

    consumer29 = KafkaConsumer("Match29",bootstrap_servers=['localhost:9092'])
    f=open('out_match29.txt','w')
    for msg in consumer29:
        print("match29",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))




def fun30():

    consumer30 = KafkaConsumer("Match30",bootstrap_servers=['localhost:9092'])
    f=open('out_match30.txt','w')
    for msg in consumer30:
        print("match30",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))



def fun31():

    consumer31 = KafkaConsumer("Match31",bootstrap_servers=['localhost:9092'])
    f=open('out_match31.txt','w')
    for msg in consumer31:
        print("match31",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))




def fun32():

    consumer32 = KafkaConsumer("Match32",bootstrap_servers=['localhost:9092'])
    f=open('out_match32.txt','w')
    for msg in consumer32:
        print("match32",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))


def fun33():

    consumer33 = KafkaConsumer("Match33",bootstrap_servers=['localhost:9092'])
    f=open('out_match33.txt','w')
    for msg in consumer33:
        print("match33",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))



def fun35():

    consumer35 = KafkaConsumer("Match35",bootstrap_servers=['localhost:9092'])
    f=open('out_match35.txt','w')
    for msg in consumer35:
        print("match35",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))



def fun36():

    consumer36 = KafkaConsumer("Match36",bootstrap_servers=['localhost:9092'])
    f=open('out_match36.txt','w')
    for msg in consumer36:
        print("match36",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))



def fun41():

    consumer41 = KafkaConsumer("Match41",bootstrap_servers=['localhost:9092'])
    f=open('out_match41.txt','w')
    for msg in consumer41:
        print("match41",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))



def fun42():

    consumer42 = KafkaConsumer("Match42",bootstrap_servers=['localhost:9092'])
    f=open('out_match42.txt','w')
    for msg in consumer42:
        print("match42",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))




def fun43():

    consumer43 = KafkaConsumer("Match43",bootstrap_servers=['localhost:9092'])
    f=open('out_match43.txt','w')
    for msg in consumer43:
        print("match43",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))


def fun44():

    consumer44 = KafkaConsumer("Match44",bootstrap_servers=['localhost:9092'])
    f=open('out_match44.txt','w')
    for msg in consumer44:
        print("match44",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))




def fun45():

    consumer45 = KafkaConsumer("Match45",bootstrap_servers=['localhost:9092'])
    f=open('out_match45.txt','w')
    for msg in consumer45:
        print("match45",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))






def fun46():

    consumer46 = KafkaConsumer("Match46",bootstrap_servers=['localhost:9092'])
    f=open('out_match46.txt','w')
    for msg in consumer46:
        print("match46",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))




def fun47():

    consumer47 = KafkaConsumer("Match47",bootstrap_servers=['localhost:9092'])
    f=open('out_match47.txt','w')
    for msg in consumer47:
        print("match47",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))




def fun48():

    consumer48 = KafkaConsumer("Match48",bootstrap_servers=['localhost:9092'])
    f=open('out_match48.txt','w')
    for msg in consumer48:
        print("match48",end=" ")
        print("%s" % msg.value.decode('utf-8'))
        f.write("%s" % msg.value.decode('utf-8'))




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
