from random import randint
from string import *

DICO_NBJOUEURS = {7:(2,0,0,0,0,0,3),8:(2,0,0,0,0,0,4),9:(2,0,0,0,0,0,5),10:(2,0,1,1,0,0,4),
11:(2,1,1,1,0,0,4),12:(2,0,1,1,1,0,5),13:(3,1,1,1,0,1,4),14:(3,0,1,1,1,1,5),15:(3,1,1,1,0,1,6)
,16:(3,0,1,1,1,1,7),17:(3,1,1,1,1,1,7),18:(4,1,1,1,1,1,7),19:(4,1,1,1,1,1,8)}
'''DICO = {nb_joueurs:(nb_loups,nb_bouc,nb_cupidon,nb_chasseur,nb_sorciere,nb_capitaine,nb__voleur,nb_villageois)}
le capitaine est compté dans les villageois pour 7,8 et 9'''


class Loup:

    def __init__(self,pseudos):
        '''Initialisation du loup garou'''
        self.__role = ["loup","bouc_emissaire","cupidon","chasseur","sorciere","voleur",'villageois']
        self.__pseudos=pseudos
        self.__nb_player=len(pseudos)
        self.__nom={}
        self.__tue = []
        self.__amoureux = ()
        self.role()
        self.__potion=True
        self.__poison=True

    def nb_player(self):
        return self.__nb_player

    def role(self):
        pseudos = self.__pseudos.copy()
        roles_usuels = ['voyante','mj']
        for i in range(2):
            num = randint(0,len(pseudos)-1)
            self.__nom[pseudos[num]] = roles_usuels[i]
            del(pseudos[num])

        i = 0
        while i < len(self.__role):
            for a in range(DICO_NBJOUEURS[self.__nb_player][i]):
                if DICO_NBJOUEURS[self.__nb_player][i] != 0 and not pseudos == []:
                    num = randint(0,len(pseudos)-1)
                    self.__nom[pseudos[num]] = self.__role[i]
                    del(pseudos[num])
            i += 1

    def nom_role(self):
        return self.__nom

    def nom(self):
        liste=[]
        for nom in self.__nom:
            if self.__nom[nom]!="mj":
                liste.append(nom)
        return liste

    #--------------------------JOUR--------------------------------------------------------------
    def tuer(self):
        phrase = ''
        for i in self.__tue:
            del(self.__nom[i])
            phrase += ', ' + i

        if len(self.__tue)>1:
            return 'Les joueurs ' + phrase + ' sont morts cette nuit'
        elif len(self.__tue) == 1:
            return 'Le joueur ' + str(self.__tue[0]) + ' est mort cette nuit'
        else :
            return "Personne n'est mort cette nuit"

        if self.__capitaine in self.__tue :
            self.design_capitaine()
        for pseudo in self.__nom.keys() :
            if pseudo in self.__tue and self.__nom[pseudo] == "chasseur":
                self.chasseur()
        self.__tue = []


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

        self.__capitaine = joueur


    def design_capitaine(self):
        '''designe le nouveau capitaine'''
        nv_capitaine = input("Le défunt capitaine nomme son succésseur : ")
        self.__capitaine = nv_capitaine

    def vote(self,votes):
        '''fait un vote si personne ex oequos : le bouc_emissaire meurt et si c'est déjà le cas le joueur est stocké dans self.__tue
         sinon on annonce les joueurs a égalité de votes'''

        maxi = []
        for i in votes.keys():
            if votes[i] == max(votes.values()) :
                maxi.append(i)
        if len(maxi) == 1 :
            self.__tue.append(maxi[0])

        elif 'bouc_emissaire' in self.__nom.values():
            for pseudo in self.__nom.keys():
                if self.__nom[pseudo] == 'bouc_emissaire':
                    self.__tue.append(pseudo)
                    print(self.__nom[pseudo],"(le bouc émissaire), est sur le point d'être sacrifié")
        else:
            print('Le vote se fera entre : ')
            for j in range(len(maxi)):
                print(' - ',maxi[j])
            x = input('Votre choix : ')
            self.__tue.append(x)





    #-------------------------NUIT---------------------------------------------------------
    def voleur(self):
        '''Fonction voleur'''
        self.nom()
        print("Le voleur se réveille")
        choix=input("Donner le nom de la personne a voler : ")
        tmp=self.__nom[choix]
        self.__nom[choix]="villageois"
        for nom in self.__nom:
            if self.__nom[nom] == "voleur":
                self.__nom[nom]=tmp

    def cupidon(self):
        '''Fonction cupidon'''
        self.nom()
        print("Cupidon se réveille")
        nom1= input("Donner le nom du premier amoureux : ")
        nom2= input("Donner le nom du deuxième amoureux : ")
        self.__amoureux=(nom1,nom2)

    def amoureux(self):
        '''Fonction amoureux'''
        print("les deux amoureux se réveillent (",self.__amoureux[0],",",self.__amoureux[1],")")

    def voyante(self):
        '''Fonction voyante'''
        self.nom()
        nom=input("la voyante se réveille et donne le nom de la personne qu'elle veux connaître : ")
        print("Cette personne est : ",self.__nom[nom])

    def loup(self):
        '''Fonction loup'''
        self.nom()
        print("les loups se réveillent")
        votes = input('Entrez le dictionnaire des votes (loup) : ')
        self.vote(votes)


    def sorciere(self):
        '''Fonction sorciere'''
        if self.__potion==True or self.__poison==True:
            self.nom()
            print("La sorcière se réveille")
            choix=input("veut-elle faire quelque chose ? : ")
            choix=choix.upper()
            if choix == "OUI":
                popo=input("potion/poison ? : ")
                popo=popo.upper()
                if self.__potion == True and popo=="POTION":
                    print("Est ce que la sorciere veut sauver ",self.__tue[-1],"?",end="")
                    choix2=input(" ")
                    choix2=choix2.upper()
                    if choix2 == "OUI" and len(self.__tue)!=0:
                        print(self.__tue[-1],"a été sauvé")
                        del(self.__tue[-1])
                        self.__potion=False

                elif self.__poison == True and popo=="POISON":
                    choix3=input("Qui la sorciere veut-elle empoisonner ? : ")
                    self.__tue.append(choix3)
                    self.__poison=False
                else:
                    print("la sorciere ne fait rien")

    def chasseur(self):
        '''Fonction chasseur'''
        self.nom()
        print("Le chasseur va tuer par vengeance une personne")
        choix=input("Qui le chasseur veut-il tuer ? : ")
        self.__tue.append(choix)

    def ordre_premiere_nuit(self):
        ordre = ['voleur','cupidon']
        self.__vrai_ordre = []
        for i in ordre :
            if i in self.__nom.values():
                self.__vrai_ordre.append(i)



    def ordre_nuits(self):
        ordre = ['voyante','loup','sorciere']
        self.__vrai_ordre = []
        for i in ordre :
            if i in self.__nom.values():
                self.__vrai_ordre.append(i)



    def appel_fonction(self):
        if "voyante" in self.__vrai_ordre:
            self.voyante()
        if "loup" in self.__vrai_ordre:
            self.loup()
        if "sorciere" in self.__vrai_ordre:
            self.sorciere()
        if "voleur" in self.__vrai_ordre:
            self.voleur()
        if "cupidon" in self.__vrai_ordre:
            self.cupidon()
            self.amoureux()


    def loup_vivant(self):
        return "loup" in self.__nom.values()

    def villageois_vivant(self):
        x=0
        for i in self.__nom.keys():
            if self.__nom[i] != "loup" and self.__nom[i] != "mj":
                x+=1
        return x>=2

if 'name' == 'name':
    loup=Loup(["jean miche","kevin","gertrude","neuf","françois","bourdin","courgette","licorne","tesla",'milka','bite','couille','testicule droit','chocolatine','testicule gauche','ponyta','mamie'])
    print(loup.nom_role())
    if loup.nb_player() < 10 :
        votes = input('Entrez les votes (capitaine) : ')
        loup.assign_capitaine(votes)
    loup.ordre_premiere_nuit()
    print('Les loups se réveillent prennent connaissance de leur meute et se rendorment')
    loup.appel_fonction()
    print('fin de la première nuit')
    loupgarou=False
    villageois=False
    while villageois == False and loupgarou == False:
        loup.ordre_nuits()
        loup.appel_fonction()
        loup.tuer()
        print("La nuit est finie, le village se réveille")
        votes = input('Entrez les votes : ')
        dico = {votes:1}
        loup.vote(dico)
        loup.tuer()
        if loup.loup_vivant() == False:
            loupgarou=True
        elif loup.villageois_vivant() == False:
            villageois=True
    if loupgarou == True:
        print("Les loups garou ont gagné")
    else :
        print("Les villageois ont gagné")
