from random import randint
from my_map import txt_transform, display_map
from constants import constants

# transformation du fichier txt en une string
data = txt_transform("labyrinthe.txt")


def string_to_list(string):
    """Fonction permettant de transformer la string "data" en liste"""
    liste = []
    for char in string:
        liste.append(char)
    return liste


# création de la liste char_of_the_map depuis la string data
char_of_the_map = string_to_list(data)


# fonction permettant d'insérer aléatoirement les 3 objets
def random_object(liste):
    """Fonction en charge de remplacer aléatoirement 3 path par 3 object
    et de retourner la liste (char_of_th_map) avec les modifications."""
    i = 0
    while i < 3:
        x = randint(0, len(liste))
        if char_of_the_map[x] == PATH_CHARACTER:
            char_of_the_map[x] = OBJECT_CHARACTER
            i += 1
    return liste


# insertion des 3 objets dans la liste
random_object(char_of_the_map)


def win_condition(liste):
    x = char_of_the_map.index(HERO_CHARACTER)
    if char_of_the_map[x + 1] == GUARDIAN_CHARACTER:
        if char_of_the_map.count(OBJECT_CHARACTER) == 0:
            print("Victoire, vous avez endormi le Gargien du labyrinthe.")
            return 0

        print("Game Over!!! Le Gardien du labyrinthe vous a tué!!!")
        return 0


def move(liste, y):
    """Fonction en charge du déplacement de MacGyver ("m") par rapport à
    son index "x" dans la liste (char_of_the_map) avec comme parametre y
    (-15 = up, +15 = down, -1 = left et +1 = right)"""
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
    display_map(char_of_the_map)


display_map(char_of_the_map)


while win_condition(char_of_the_map) != 0:

    joueur = input("Que voulez vous faire : ? ('z' pour up, 'q' pour left, 's' pour down, 'd' pour right : ")
    destination = {"z": -15, "q": -1, "d": +1, "s": +15}    

    move(char_of_the_map, destination[joueur])



#faire une liste de mes PATH pour random object

#pour vendredi refaire le code en POO