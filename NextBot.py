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
    if veux_jouer(message.content):
        pseudos.append(message.author)
        print(pseudos)
        
    if message.content == '!start':
        loup = Loup(pseudos)
        await client.send_message(message.channel, "".join('LA PARTIE COMMENCE'))
        for i in pseudos :
            await client.send_message(i, "".join('Votre rôle : ' + str(loup.nom_role()[i])))
    if message.content == '!private':
        await client.send_message(pseudos[-1],"".join('votre rôle :'))
    

client.run(token)


    
