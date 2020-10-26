from random import randint
from my_map import txt_transform, display_map

# constants
PATH_CHARACTER = " "
WALL_CHARACTER = "#"
HERO_CHARACTER = "m"
GUARDIAN_CHARACTER = "g"
OBJECT_CHARACTER = "@"

# transformation du fichier txt en une string
data = txt_transform("labyrinthe.txt")

# transformation de la string "data" en liste
liste = []
for char in data:
    liste.append(char)

# fonction permettant d'insérer aléatoirement les 3 objets dans le labyrinthe
def random_object(liste):
    
    i = 0
    while i < 3:

        x = randint(0, len(liste))
        
        if liste[x] == PATH_CHARACTER:
            liste[x] = OBJECT_CHARACTER
            i += 1
        else:
            pass
    return liste

random_object(liste)



def move_up(liste):

    x = liste.index(HERO_CHARACTER)

    if liste[x - 15] == PATH_CHARACTER:
        liste[x] = PATH_CHARACTER
        liste[x - 15] = HERO_CHARACTER
        return display_map(liste)
    elif liste[x - 15] == GUARDIAN_CHARACTER:
        liste[x] = PATH_CHARACTER
        liste[x - 15] = HERO_CHARACTER
        return display_map(liste)
    elif liste[x - 15] == OBJECT_CHARACTER:
        liste[x] = PATH_CHARACTER
        liste[x - 15] = HERO_CHARACTER
        return display_map(liste)
    else:
        print("C'est un mur !")
        

def move_down(liste):

    x = liste.index(HERO_CHARACTER)

    if liste[x + 15] == PATH_CHARACTER:
        liste[x] = PATH_CHARACTER
        liste[x + 15] = HERO_CHARACTER
        return display_map(liste)
    elif liste[x + 15] == GUARDIAN_CHARACTER:
        liste[x] = PATH_CHARACTER
        liste[x + 15] = HERO_CHARACTER
        return display_map(liste)
    elif liste[x + 15] == OBJECT_CHARACTER:
        liste[x] = PATH_CHARACTER
        liste[x + 15] = HERO_CHARACTER
        return display_map(liste)
    else:
        print("C'est un mur !")

def move_left(liste):

    x = liste.index(HERO_CHARACTER)

    if liste[x - 1] == PATH_CHARACTER:
        liste[x] = PATH_CHARACTER
        liste[x - 1] = HERO_CHARACTER
        return display_map(liste)
    elif liste[x - 1] == GUARDIAN_CHARACTER:
        liste[x] = PATH_CHARACTER
        liste[x - 1] = HERO_CHARACTER
        return display_map(liste)
    elif liste[x - 1] == OBJECT_CHARACTER:
        liste[x] = PATH_CHARACTER
        liste[x - 1] = HERO_CHARACTER
        return display_map(liste)
    else:
        print("C'est un mur !")

def move_right(liste):

    x = liste.index(HERO_CHARACTER)

    if liste[x + 1] == PATH_CHARACTER:
        liste[x] = PATH_CHARACTER
        liste[x + 1] = HERO_CHARACTER
        return display_map(liste)
    elif liste[x + 1] == GUARDIAN_CHARACTER:
        liste[x] = PATH_CHARACTER
        liste[x + 1] = HERO_CHARACTER
        return display_map(liste)
    elif liste[x + 1] == OBJECT_CHARACTER:
        liste[x] = PATH_CHARACTER
        liste[x + 1] = HERO_CHARACTER
        return display_map(liste)
    else:
        print("C'est un mur !")

display_map(liste)
game = True
while game:

    joueur = input("Que voulez vous faire : ? ('z' pour up, 'q' pour left, 's' pour down, 'd' pour right : ")

    if joueur == "z":
        move_up(liste)

    elif joueur == "q":
        move_left(liste)   

    elif joueur == "d":
        move_right(liste)    

    elif joueur == "s":
        move_down(liste)
        
        




    
    

    