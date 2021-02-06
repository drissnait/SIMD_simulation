# encoding: utf-8
from Packet import Packet
from Trame import Trame
from random import uniform
from numpy import random
import math
from time import sleep
import sys
from Unbuffered import Unbuffered
sys.stdout = Unbuffered(sys.stdout)
from functions_calcul import strategiePaquets
import os

VLAMBDA=4
NB_EQUIPEMENTS=3

def exp(vlambda):
    exp=0
    while(exp<=0):
        exp=math.floor(random.exponential(scale=vlambda))
    return exp

def arrivee_trames():
    slot_sum=0
    num_trame=0
    listePaquets=[]
    nb_paquets=0
    i=0
    while (i<10):
        slot=exp(VLAMBDA)%10
        slot_sum+=slot
        if (slot_sum<10):
            print( "on recoit sur le slot ", slot_sum)
            listePaquets.append(slot_sum)
            nb_paquets+=1
        i+=1

    return nb_paquets


def processus_poisson(nbEquipements, vlambda):
  #decide avec la loi de poisson combien de packet un equipement envoie
  nb_paquet_equipement = dict()
  for e in range(nbEquipements):
    nb_paquet_equipement[e] = numpy.random.poisson(vlambda)
    print(nb_paquet_equipement[e])

  return nb_paquet_equipement

def execute_simulation(listeEquipementsPaquets, nbTrames, _lambda):
    nbEquipements=len(listeEquipementsPaquets)
    nbPacketsEquipement = processus_poisson(nbEquipements, _lambda)
    i=0
    while (i<nbTrames):
        trame=Trame()
        for k in listeEquipementsPaquets:
            j=0
            while(j<len(listeEquipementsPaquets[k])):
                print("equipement = ", listeEquipementsPaquets.keys()[k], "paquet : ", listeEquipementsPaquets[k][j].contenu)
                trame.sendPacket(listeEquipementsPaquets[k][j], nbPacketsEquipement[k])
                j+=1
        i+=1

def send_indexes(n):
    indices_tires=[]
    indice_slot=0
    i=0
    while (i<n):
        indice_slot=int(uniform(0, 10))
        if (indice_slot not in indices_tires):
            indices_tires.append(indice_slot)
            i+=1
        else:
            continue
    return indices_tires

def initPaquets(n):
    listePaquets=[]
    listeAlphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
     'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    i=0
    for i in range (n):
        indice=random.randint(0,25)
        packet=Packet(i,listeAlphabet[indice])
        listePaquets.append(packet)
    return listePaquets

nb_total_paquets=10
nb_paquets_restants=0
iter=1
indice_packet=0
l=0
os.remove("strat.dat")
filedata = open("strat.dat", "a")
while(nb_paquets_restants<nb_total_paquets):
    equipement=1
    indexes=[]
    nb_paquets=arrivee_trames()
    listPaquets=initPaquets(nb_paquets)
    listStrategie=strategiePaquets(listPaquets)
    longueur=len(listStrategie)+l
    indice_str=0
    while l <longueur:
    	num_packet=l+1
	data=str(num_packet)+";"+str(listStrategie[indice_str])+"\n"
	l+=1
	indice_str+=1
	filedata.write(data)

    i=1
    for i in range(nb_paquets):
        #choix équipement
        num_equipement=int(uniform(1, NB_EQUIPEMENTS))
        nb_copies=listStrategie[i]
        indexes=send_indexes(nb_copies)
        for j in range (listStrategie[i]):
            print("l'equipement ", equipement, " va envoyer le paquet ", listPaquets[i-1].contenu," dans le slot ",
            indexes[j], "dans la trame", iter+1)
        sleep(0.8)
        equipement+=1
        indice_packet+=1
    nb_total_paquets-=nb_paquets
    iter+=1
filedata.close()

