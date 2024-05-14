def personnalLen(chaine):
    count = 0
    for character in chaine:
        count += 1
    return count

texte = "Il y a 42 dans cette phrase espace compris"
longueur_texte = personnalLen(texte)
print(f"Ce texte contient {longueur_texte} caractères, espaces compris.")