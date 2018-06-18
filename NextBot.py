from loup_garou import *
import asyncio, discord

token = "NDU3MTM4ODA4MTc4MzQzOTM3.DgUvSg.RMVhx9zi6POk3Cxsfljx26jp0yg" #Mettez dans cette variable le token du bot
client = discord.Client()
pseudos = ['jean-miche','moi','toi','lioi','mali','coco','buit','hr']

def commence_par_vote(message):
    '''montre si le message commence par !vote'''
    v = '!vote'
    for i in range(5) :
        if message[i] != v[i] :
            return False

    return True

def veux_jouer(message):
    '''montre si le message commence par !jejoue'''
    v = '!jejoue'
    for i in range(7) :
        if message[i] != v[i] :
            return False

    return True

def init_dico(pseudos):
    dico = {}
    for i in pseudos:
        dico[i] = 0
    return dico

def select_vote(message):
    for a in range(6):
        message = message[1:]
    return message

def ajoute_vote(dico,vote):
    if vote != '' :
        dico[vote] += 1
    return dico

@client.event

async def on_ready():
    ver = "1.3.0"
    lang = "fr"
    print("NextBot " + ver + " " + lang)
    
@client.event
async def on_message(message):

    class Votes:
        def __init__(self,pseudos):
            self.__pseudos = pseudos
            self.__dico = {}
            for i in self.__pseudos:
                self.__dico[i] = 0
            self.__vote = True
                
        def vote(self,vote):
            self.dico[vote] += 1
            self.stop_vote()
            
        def vote_ouvert(self):
            return self.__vote

        def dico(self):
            return self.__dico
        
        def stop_vote(self):
            cpt = 0
            for i in self.__dico.keys():
                cpt += self.__dico[i]
            if cpt == len(self.__pseudos):
                self.__vote = False
                

    def gestion_vote(message,votes):
        if commence_par_vote(message.content) and votes.vote_ouvert():
            vote = select_vote(message.content)
            votes.vote(vote)
            
    if veux_jouer(message.content):
        pseudos.append(message.author)
        print(pseudos)
        
    if message.content == '!start':
        await client.send_message(message.channel, "".join('LA PARTIE COMMENCE'))
        if len(pseudos) < 10 :
            await client.send_message(message.channel, "".join('Il faut élire le capitaine(!vote)'))
            votes = Votes(pseudos)
            while votes.vote_ouvert():
                gestion_vote(message,votes)
            await client.send_message(message.channel, "".join('vote terminé'))
                
        
    if message.content == '!private':
        await client.send_message(pseudos[-1],"".join('votre rôle :'))
    

client.run(token)


    
