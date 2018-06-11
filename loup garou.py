from random import randint

class Loup:

    def __init__(self,nb_player,pseudos):
        '''Initialisation du loup garou'''
        self.__role=[mj,loup,loup,voyante,sorciere,voleur,chasseur,cupidon]

    def role(self,roles,nb_player,pseudos):
        '''Defini les rôles des personnes'''
        liste=pseudos.copy()
        tmp=0
        i=0
        while liste != []:
            x=randint(0;len(liste))
            if tmp==0:
                self.__nom[pseudos[x]] = self.__role[i]
            else :
                self.__nom[pseudos[x]] = "villageois"
            del(pseudos[x])
            i+=1
            tmp= (tmp+1)%2
