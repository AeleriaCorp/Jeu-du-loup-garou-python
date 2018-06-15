# -*- coding: utf-8  -*-

# A lire si vous faîtes une mise à jour et si vous avez ajouté ou modifié les commandes du bot :
# 1) Copiez vos commandes (pas les commandes par défaut) que vous avez créer dans votre ancienne version dans la nouvelle version.
# 2) Si vous avez modifié une commande de NextBot par défaut, supprimez la commande de la nouvelle version puis copiez le code de la commande de l'ancienne version dans la nouvelle version.

import asyncio, discord

token = "NDU3MTM4ODA4MTc4MzQzOTM3.DgUvSg.RMVhx9zi6POk3Cxsfljx26jp0yg" #Mettez dans cette variable le token du bot
trust = [".BROVIN[apprenti modo]#8991", "TheMegaPhoenix#0999"] #Mettez dans cette variable les utilisateurs pouvant utiliser les commandes restreintes
trust_roles = [""]
ranks = False

client = discord.Client()
ver = "1.3.0"
lang = "fr"

print("NextBot " + ver + " " + lang)

@client.event
@asyncio.coroutine


def on_message(message):
    rep = text = msg = message.content
    rep2 = text2 = msg2 = rep.split()
    user = str(message.author)
    user_bot_client = client.user.name
    user_bot = user_bot_client.split("#")[0]
    role_trusted = False
    if type(message.server) is discord.server.Server:
        server_msg = str(message.channel.server)
        chan_msg = str(message.channel.name)
        for role_name in trust_roles:
            if ":" in role_name and role_name.split(":")[0] == server_msg:
                rank_role = discord.utils.get(message.server.roles, name = ":".join(role_name.split(":")[1:]))
            else:
                rank_role = discord.utils.get(message.server.roles, name = role_name)
            if type(rank_role) is discord.role.Role and rank_role.id in [r.id for r in message.author.roles]:
                role_trusted = True
        pm = False
    else:
        server_msg = user
        chan_msg = user
        pm = True
    trusted = user in trust or role_trusted
    print(trusted)
    try:
        command = rep2[0].lower()
        params = rep2[0:]
    except IndexError:
        command = ""
        params = ""

    print(user + " (" + server_msg + ") [" + chan_msg + "] : " + rep)

    if ranks and not pm:
        open("msgs_user_" + server_msg + ".txt", "a").close()
        msgs = open("msgs_user_" + server_msg + ".txt", "r")
        msgs_r = msgs.read()
        if user not in msgs_r or user != user_bot_client:
            msgs_w = open("msgs_user_" + server_msg + ".txt", "a")
            msgs_w.write(user + ":0\n")
            msgs_w.close()
            msgs.close()
            msgs = open("msgs_user_" + server_msg + ".txt", "r")
            msgs_r = msgs.read()
        msgs_user = msgs_r.split(user + ":")[1]
        msgs.close()
        user_msgs_n = int(msgs_user.split("\n")[0])
        user_msgs_n += 1
        msgs_r = msgs_r.replace(user + ":" + str(user_msgs_n - 1), user + ":" + str(user_msgs_n))
        msgs = open("msgs_user_" + server_msg + ".txt", "w")
        msgs.write(msgs_r)
        msgs.close()
    #PARTIE SPECIFIQUE AU LOUP GAROU    
    pseudos = []
    def commence_par_vote(message):
        '''montre si le message commence par !vote'''
        v = '!vote'
        for i in range(5) :
            if message[i] != v[i] :
                return False

        return True
    def veux_jouer(message):
        '''montre si le message commence par !vote'''
        v = '!jejoue'
        for i in range(7) :
            if message[i] != v[i] :
                return False

        return True
        
        
    
#Début des commandes

    if veux_jouer(message.content):
        pseudos.append(user)
        print(pseudos)
    if commence_par_vote(message.content):
        print(message.content)

    #FIN DE LA PARTIE SPECIFIQUE AU LOUP GAROU
    
    if (command == "!purge" or command == "!clear") and trusted and not pm: #Cette commande sert à effacer les messages, en tapant !purge 10, le bot supprimera les 10 derniers messages.
        yield from client.purge_from(message.channel, limit = int(10)) #Cette ligne sert à supprimer les messages avec params[1] qui est le premier paramètre (le nombre de messages), il y a int(params[1]) car le paramètre doit être converti en un nombre.

    if (command == "!quit" or command == "!exit") and trusted: #Cette commande sert à fermer le bot
        yield from client.close()

    if command == "!say" and trusted: #Cette commande sert à envoyer un message sur un channel du serveur, le paramètre 1 doit être l'identifiant du channel et après, on doit mettre le message (exemple : !say 1234567890 Bonjour !)
        yield from client.send_message(client.get_channel('454387337955246091'), "".join('BONJOUR'))

    if command == "!say_user" and trusted:
        if params[2].lower() == params[2].upper():
            yield from client.send_message(client.get_server(params[1]).get_member(params[2]), " ".join(params[3:]))
        else:
            yield from client.send_message(client.get_server(params[1]).get_member_named(params[2]), " ".join(params[3:]))
#Fin des commandes

client.run(token)



