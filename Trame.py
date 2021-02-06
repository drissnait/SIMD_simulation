# encoding: utf-8
from Packet import Packet
from random import uniform

class Trame:
    def __init__(self):
        self.slots = [[] for i in range(10)]

    """choix des slots sur lesquels envoyer"""
    def sendPacket(self, packet, nbCopies):
        indices_tires=[]
        indice_slot=0
        if(nbCopies>10):
            print("Erreur : nombre de copies supérieur à la taille de la Trame")
        else:
            i=0
            while (i<nbCopies):
                indice_slot=int(uniform(0, 10))
                if (indice_slot not in indices_tires):
                    indices_tires.append(indice_slot)
                    self.slots[indice_slot].append(packet)
                    i+=1
                else:
                    continue


    def str_paquets(self):
        for i in range (0,10):
            if (self.slots[i]):
                print("i == ", self.slots[i])
