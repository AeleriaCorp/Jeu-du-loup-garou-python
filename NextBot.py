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
def autres_loup(dico,loup):
    phrase = 'les autres loup sont : \n'
    for i in dico.keys():
        if dico[i] == 'loup' and i != loup:
            phrase += '| i'
    return phrase
        

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
        await client.send_message(message.author, "".join('participation validée'))
        
    if message.content == '!start':
        loup = Loup(pseudos)
        loup.ordre_premiere_nuit()
        await client.send_message(message.channel, "".join('LA PARTIE COMMENCE'))
        for i in pseudos :
            if loup.nom_role()[i] == 'mj':
                await client.send_message(message.channel, "".join('le maître du jeu est : ' + str(i)))
            await client.send_message(i, "".join('Votre rôle : ' + str(loup.nom_role()[i])))
        for i in loup.nom_role().keys():
            if i == 'loup':
                await client.send_message(i, "".join(autres_loup(loup.nom_role(),i)))
                
        if len(loup.ordre_premiere_nuit()) != 0 :
            await client.send_message(message.channel, "".join("voici l'ordre des joueurs de la première nuit : " + str(loup.ordre_premiere_nuit())))
        await client.send_message(message.channel, "".join("voici l'ordre des joueurs des autres nuits : " + str(loup.ordre_nuits())))
        phrase = ''
        for i in loup.nom_role().keys():
            phrase +=  '\n' + loup.nom_role()[i]
        await client.send_message(message.channel, "".join("voici les rôles présents dans le jeu : " + phrase))
        if len(pseudos) < 10 :
            await client.send_message(message.channel, "".join("Il faut élire un capitaine"))
        await client.send_message(message.channel, "".join("\n si le mj se sent en difficulté, faire !aide"))
        await client.send_message(message.channel, "".join("Pour les autres, les règles sont épinglées dans ce salon"))
    if message.content == '!voleur': 
        await client.send_message(message.channel, "".join("Le voleur se réveille et donne le nom de la personne à voler"))
            
    if message.content == '!cupidon':
        await client.send_message(message.channel, "".join("Cupidon se réveille et donne le nom des deux amoureux"))

    if message.content == '!voyante':
        await client.send_message(message.channel, "".join("La voyante se réveille et donne le nom du joueur dont elle veut connaître le rôle"))

    if message.content == '!loup':
        await client.send_message(message.channel, "".join("Les loups se réveillent et choisissent ensemble une proie"))

    if message.content == '!sorciere':
        await client.send_message(message.channel, "".join("La voyante se réveille, prend connaissance de la proie, et indique si elle veut la sauver, empoisonner quelqu'un d'autre ou ne rien faire"))
    
    if message.content == '!chasseur':
        await client.send_message(message.channel, "".join("Le chasseur va tuer quelqu'un avant de mourir"))

    if message.content == '!bouc emissaire':
        await client.send_message(message.channel, "".join("Egalité de voies, le bouc émissaire meurt"))

    if message.content == '!aide':
        phrase = '''Voici une aide récapitulant le travail du maître du jeu :
        -envoyer la commande !jejoue attendre que tous les joueurs ont fait de même et entrer la commande !start
        -regarder les tous premiers messages du bot lors du démarrage de la partie, il donnera l'ordre de passage des rôles (de gauche à droite) et des instructions a faire
        avant celles qui suivent (comme le vote du capitaine dont l'issue sera annoncé à tous les joueurs)
        
        -le jeu commence sur la première nuit (donc s'interresser à l'ordre de passage de la premiere nuit donnée par le bot (il se peut que aucun rôle n'y apparaisse,
        le jeu commencera alors sur une nuit ordinaire (voir ordre des autres nuits donné par le bot)
        
        -le mj doit envoyer des commandes aux bots qui donnera les instructions au(x) joueur(s) ayant le rôle concerné en suivant l'ordre
        (les commandes sont facile !voyante pour la voyante, !sorciere pour la sorcière (sans accents))
        
        -il doit memoriser certaines actions (ouvrir un txt pour les noter) comme par exemple les morts de la nuit, les joueurs qui ont fini de jouer, le nombre restant de
        villageois, de loup, le nom du capitaine etc....
        
        -une fois la nuit finie, le mj annonce les morts de la nuit et demande au joueur de débattre et de voter pour tuer quelqu'un (faire un !vote), les joueurs envoyent en
        message privée au mj leur vote (attention le capitaine aura 2 voies) si l'issue du vote est une égalité, le bouc emissaire meurt (faire la commande !bouc emissaire), et
        si il est déjà mort ou inexistant, le capitaine choisit alors le joueur qui meurt entre ceux qui ont le plus grand nombre de voies
        
        Lorsque des joueurs meurts, indiquer le rôle qu'ils avaient
        
        -puis la nuit suivante commence,.....puis le jour et ainsi de suite jusqu'à ce qu'il ne reste plus qu'un villageois ou qu'il ne reste plus de loups le mj annonce les
        gagnants''' 
        await client.send_message(message.author, "".join(phrase))

    
client.run(token)


    
