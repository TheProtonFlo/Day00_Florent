import random

taille = 15
tableau_aléa = [random.randint(1, 100) for _ in range(taille)]

def triTableauCroissant(tableau):
    for i in range(1, len(tableau)):
        valeur = tableau[i]
        position = i

        while position > 0 and tableau[position - 1] > valeur:
            tableau[position] = tableau[position - 1]
            position -= 1

        tableau[position] = valeur

    return tableau
    
print(tableau_aléa)    
tableauTrié = triTableauCroissant(tableau_aléa)
print(f"Votre trableau a été trié par ordre croissant, le voici : {tableauTrié}")
