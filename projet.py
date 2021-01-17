import random
import math

def ack():
    return random.choice([0.1,0.4,0.9])

def ub1(xj,n,nj):
    return xj+math.sqrt(2*math.log(n))/nj

def max(a, y, z):
    Max = a
    if y > Max:
        Max = y
    if z > Max:
        Max = z
        if y > z:
            Max = y
    return Max

def sendPaquets():
    listPaquets=['a','b','c','d','e']
    a2=0.2
    a3=0.3
    a4=0.4
    n=4
    n2=1
    n3=1
    n4=1
    for i in range (len(listPaquets)):
        if(i==0):
            s2=ub1(a4,n,n4)
            n4+=1
            a4=a4+ack()/n4
            n+=1
        else:
            s2=ub1(a2,n,n2)
            s3=ub1(a3,n,n3)
            s4=ub1(a4,n,n4)
            if(max(s2,s3,s4)==s2):
                n2+=1
            elif(max(s2,s3,s4)==s3):
                n3+=1
            elif(max(s2,s3,s4)==s4):
                n4+=1


def main():
    print(xjAleatoire())
    sendPaquets()

if __name__ == "__main__":
    main()
