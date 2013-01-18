# coding=utf-8
from mpi4py import MPI
from simplifieSat import *
from utility import *
from retireSingleton import *

def comportementEsclave(comm):
	print "Hello! I'm rank %d from %d running in total..." % (comm.rank, comm.size)


	data=comm.recv(source=0,tag=1)
	print "Received " + str(data)
	
    result=[]
    for probleme in data:
        #Recuperation de la liste des variables avec valeurs T pour True, F pour False et U pour Undefined
        valeursVariables=probleme[0]
        #Recuperation du Probleme SAT a traiter
        problemeSAT=probleme[1]

        pb=simplifieSat(valeursVariables,problemeSAT)
        nouveauSat,nouveauData=retireSingleton(pb)
        result=testSatOk(nouveauSat)

        if result==True:
            #On envoie un message de type tag 2 au maître pour lui indiquer que le pb SAT a ete resolu
            #On envoie au maitre la valeur des variables resolvant le probleme SAT
            #comm.send(valeursVariables,dest=0,tag=2)
            pass
        elif result==False:
            #On envoie un message de type tag 3 au maître pour lui indiquer que le pb ne peut pas etre resolu
            #comm.send(dest=0,tag=3)
            pass
        else:
            pass