from random import randint
DICO_NBJOUEURS = {8:(2,6),9:(2,7),10:(2,8),11:(2,9),12:(3,9),13:(3,10),14:(3,11),15:(3,12),16:(3,13),17:(3,14),18:(4,14)}

class Loup:

    def __init__(self,pseudos):
        '''Initialisation du loup garou'''
        self.__role=["mj","loup","loup","voyante","sorciere","voleur","chasseur","cupidon"]
        self.__pseudos=pseudos
        self.__nb_player=len(pseudos)
        self.__nom={}
        self.__tue = []
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

    #--------------------------JOUR--------------------------------------------------------------
    def tuer(self):
        phrase = ''
        for i in self.__tue:
            del(self.__nom[i])
            if i == 0:
                phrase += str(i)
            elif i == len(self.__tue)-1:
                phrase += ' et '+str(i)
            else :
                phrase += ', ' + str(i)

        if len(self.__tue)>1:
            return 'Les joueurs ' + phrase + ' sont morts cette nuit'
        return 'Le joueur ' + str(self.__tue[0]) + ' est mort cette nuit'

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
    #-------------------------NUIT---------------------------------------------------------
    def voleur(self):
        '''Fonction voleur'''
        pass

    def cupidon(self):
        '''Fonction cupidon'''
        nom1= input("Donner le nom du premier amoureux : ")
        nom2= input("Donner le nom du deuxième amoureux : ")
        self.__amoureux=(nom1,nom2)

    def amoureux(self):
        '''Fonction amoureux'''
        print("les deux amoureux se réveille (",self.__amoureux[0],",",self.__amoureux[1],")")

    def voyante(self):
        '''Fonction voyante'''
        nom=input("la voyante se réveille et donne le nom de la personne qu elle veux connaître : ")
        print("Cette personne est : ",self.__nom[nom])

    def loup(self,nom):
        '''Fonction loup'''
        self.__tue.append(nom)

    def sorciere(self):
        '''Fonction sorciere'''
        choix=input("la sorciere veut elle faire quelque chose ? : ")
        choix.uppercase()
        if choix == "OUI":
            popo=input("potion/poison ? : ")
            popo.uppercase()
            if self.__potion == True and popo=="POTION":
                choix2=input("Est ce que la sorciere veut sauver ",self.__tue[-1])
            elif self.__poison == True and popo=="POISON":
                choix3=input("Qui la sorciere veut elle empoisonné : ")
                self.__tue.append(choix3)
            else:
                print("la sorciere ne fait rien")

    def chasseur(self):
        '''Fonction chasseur'''
        choix=input("Qui le chasseur veut-il tuer ? : ")
        self.__tue.append(choix)



    def ordre_premiere_nuit(self):
        ordre = ['voleur','cupidon','amoureux','voyante','loup','sorciere']
        self.__vrai_ordre = []
        for i in ordre :
            if i in self.__nom.values():
                self.__vrai_ordre.append(i)

        return vrai_ordre

    def ordre_nuits(self):
        ordre = ['voyante','loup','sorciere']
        self.__vrai_ordre = []
        for i in ordre :
            if i in self.__nom.values():
                self.__vrai_ordre.append(i)

        return vrai_ordre

if 'name' == 'name':
    prout=Loup(["jean miche","kevin","gertrude","neuf","françois"])
    prout.role()
    print(prout.nom_role())
