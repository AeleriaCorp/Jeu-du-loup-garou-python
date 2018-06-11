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
        
