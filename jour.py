from random import *

def assign_capitaine(votes):
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
    return capitaine

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
