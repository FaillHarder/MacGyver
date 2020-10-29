

def move(liste, y):
    """Fonction en charge du déplacement de MacGyver ("m") dans la liste (char_of_the_map)
    avec comme parametre y (-15 = up, +15 = down, -1 = left et +1 = right)"""
    
    # récupère l'index de macgyver dans la liste et attribue sa valeur à x
    x = char_of_the_map.index(HERO_CHARACTER)
    
    if char_of_the_map[x + (y)] == PATH_CHARACTER:
        char_of_the_map[x] = PATH_CHARACTER
        char_of_the_map[x + (y)] = HERO_CHARACTER   
    elif char_of_the_map[x + (y)] == OBJECT_CHARACTER:
        char_of_the_map[x] = PATH_CHARACTER
        char_of_the_map[x + (y)] = HERO_CHARACTER
    elif char_of_the_map[x + (y)] == GUARDIAN_CHARACTER:
        char_of_the_map[x] = PATH_CHARACTER
        char_of_the_map[x + (y)] = HERO_CHARACTER
    else:
        print("C'est un mur !")