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
