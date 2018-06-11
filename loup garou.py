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
    
    def assign_capitaine(self,votes):
    '''assigne le role de capitaine en fonction des resultat du votes
    vote = {pseudo:vote}'''
    maxi = []
    for i in votes.keys():
        if votes[i] >= max(votes.values()) :
            maxi.append(i)

    if len(maxi)>1:
        a = randint(0,len(maxi)-1)
        joueur = maxi[a]

    return joueur

    def design_capitaine(self,capitaine):
        '''designe le nouveau capitaine'''
        self.__capitaine = capitaine

    def vote(self,votes):
        '''fait un vote si personne ex oequos : le joueur est stocké dans self.__tue
         sinon on annonce les joueurs a égalité de votes'''

        maxi = []
        for i in votes.keys():
            if votes[i] >= max(votes.values()) :
                maxi.append(i)

        if len(maxi) > 1 :
            phrase = "le vote se fera entre : "
            for i in range(len(maxi)):
                if i == 0:
                    phrase += str(maxi[i])
                elif i == len(maxi)-1:
                    phrase += ' et '+str(maxi[i])
                else :
                    phrase += ', ' + str(maxi[i])
            return phrase
        
        self.__tue = maxi[0]
        return maxi[0]


if 'name' == 'name':
    prout=Loup(["jean miche","kevin","gertrude","neuf","françois"])
    prout.role()
    print(prout.nom_role())
