from random import randint
DICO_NBJOUEURS = {8:(2,6),9:(2,7),10:(2,8),11:(2,9),12:(3,9),13:(3,10),14:(3,11),15:(3,12),16:(3,13),17:(3,14),18:(4,14)}

class Loup:

    def __init__(self,pseudos):
        '''Initialisation du loup garou'''
        self.__role=["mj","loup","loup","voyante","sorciere","voleur","chasseur","cupidon"]
        self.__pseudos=pseudos
        self.__nb_player=len(pseudos)
        self.__nom={}
        self.__tue = ''
        self.__amoureux = ()

    def role(self):
        '''Defini les rôles des personnes'''
        liste=self.__pseudos.copy()
        tmp=0
        i=0
        while liste != []:
            x=randint(0,len(liste)-1)
            if tmp==0:
                self.__nom[liste[x]] = self.__role[i]
            else :
                self.__nom[liste[x]] = "villageois"
            del(liste[x])
            i+=1
            tmp= (tmp+1)%2

    def nom_role(self):
        return self.__nom


if 'name' == 'name':
    prout=Loup(["jean miche","kevin","gertrude","neuf","françois"])
    prout.role()
    print(prout.nom_role())
