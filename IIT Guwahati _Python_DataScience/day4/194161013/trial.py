from kafka import KafkaProducer
import threading

#p=f.read()
#print(p)
#print(len(p))

def fun1():
    producer1 = KafkaProducer(bootstrap_servers=['localhost:9092'])
    f=open('Match1_commentry.txt','r')
    for line in reversed(list(open("Match1_commentry.txt"))):
        #print(line.rstrip())
        print('Match1',line.rstrip())
        producer1.send("Match1", value=bytes(line.rstrip(),encoding='utf-8'))
        producer1.flush()




t1=threading.Thread(target=fun1)
t1.start()
