

def trouver_visiteur_par_nom(visiteur_nom, data):
    visiteurs = {}
    for visiteur in data:
        if visiteur['nom'] == visiteur_nom:
            visiteurs.update({visiteur['id']: visiteur})
    return visiteurs

