import random
import math
from Packet import Packet

"""retourne une strategie aleatoire (pour les tests avec toutes les strategies dans des ordres differents"""
def ack():
    return random.choice([0.1,0.4,0.9])

def ub1(xj,n,nj):
    return xj+math.sqrt(2*math.log(n))/nj

"""
fonction qui retourne le max entre 3 valeurs (pour les strategies)
"""
def max(a, y, z):
    Max = a
    if y > Max:
        Max = y
    if z > Max:
        Max = z
        if y > z:
            Max = y

    return Max

"""
definit la strategie d'envoi des paquets
"""
def strategiePaquets(listPaquets):
    a2=0.2
    a3=0.3
    a4=0.4
    reward2=a2
    reward3=a3
    reward4=a4
    n=3
    n2=1
    n3=1
    n4=1
    listStrategie=[]
    for i in range (len(listPaquets)):
        if(i==0):
            #Envoyer le paquet avec la strategie 4 = 4fois
            n4+=1
            ack = random.choice([0.1,0.4,0.9])
            reward4=(a4+ack*(n4-1))/n4
            strategie4=ub1(reward4,n,n4)
            strategie2=ub1(reward2,n,n2)
            strategie3=ub1(reward3,n,n3)
            n+=1
        else:
            if(max(strategie2,strategie3,strategie4)==strategie2):
                n2+=1
                ack=random.choice([0.1,0.4,0.9])
                reward2=(a2+ack*(n2-1))/n2
                strategie2=ub1(reward2,n,n2)
                strategie3=ub1(reward3,n,n3)
                strategie4=ub1(reward4,n,n4)
                n+=1

            elif(max(strategie2,strategie3,strategie4)==strategie3):
                n3+=1
                ack=random.choice([0.1,0.4,0.9])
                reward3=(a3+ack*(n3-1))/n3
                strategie2=ub1(reward2,n,n2)
                strategie3=ub1(reward3,n,n3)
                strategie4=ub1(reward4,n,n4)
                n+=1
            elif(max(strategie2,strategie3,strategie4)==strategie4):
                n4+=1
                ack=random.choice([0.1,0.4,0.9])
                reward4=(a4+ack*(n4-1))/n4
                strategie2=ub1(reward2,n,n2)
                strategie3=ub1(reward3,n,n3)
                strategie4=ub1(reward4,n,n4)
                n+=1
        if(strategie2> strategie3 and strategie2> strategie4):
            str=2
        if(strategie3> strategie2 and strategie3> strategie4):
            str=3
        if(strategie4> strategie3 and strategie4> strategie2):
            str=4
        listStrategie.append(str)
    return listStrategie

