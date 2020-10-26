def move_up(liste):

    num = liste.index(HERO_CHARACTER)

    if liste[num - 15] == PATH_CHARACTER:
        liste[num] = PATH_CHARACTER
        liste[num - 15] = HERO_CHARACTER
        return display_map(liste)
    elif liste[num - 15] == GUARDIAN_CHARACTER:
        liste[num] = PATH_CHARACTER
        liste[num - 15] = HERO_CHARACTER
        return display_map(liste)
    else:
        print("C'est un mur !")
        

def move_down(liste):
    num = liste.index(HERO_CHARACTER)
    if liste[num + 15] == PATH_CHARACTER:
        liste[num] = PATH_CHARACTER
        liste[num + 15] = HERO_CHARACTER
        return display_map(liste)
    elif liste[num + 15] == GUARDIAN_CHARACTER:
        liste[num] = PATH_CHARACTER
        liste[num + 15] = HERO_CHARACTER
        return display_map(liste)
    else:
        print("C'est un mur !")

def move_left(liste):
    num = liste.index(HERO_CHARACTER)
    if liste[num - 1] == PATH_CHARACTER:
        liste[num] = PATH_CHARACTER
        liste[num - 1] = HERO_CHARACTER
        return display_map(liste)
    elif liste[num - 1] == GUARDIAN_CHARACTER:
        liste[num] = PATH_CHARACTER
        liste[num - 1] = HERO_CHARACTER
        return display_map(liste)
    else:
        print("C'est un mur !")

def move_right(liste):
    num = liste.index(HERO_CHARACTER)
    if liste[num + 1] == PATH_CHARACTER:
        liste[num] = PATH_CHARACTER
        liste[num + 1] = HERO_CHARACTER
        return display_map(liste)
    elif liste[num + 1] == GUARDIAN_CHARACTER:
        liste[num] = PATH_CHARACTER
        liste[num + 1] = HERO_CHARACTER
        return display_map(liste)
    else:
        print("C'est un mur !")