from random import randint
from my_map import txt_transform, display_map


PATH_CHARACTER = " "
WALL_CHARACTER = "#"
HERO_CHARACTER = "m"
GUARDIAN_CHARACTER = "g"
OBJECT_CHARACTER = "@"


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

# fonction permettant d'insérer aléatoirement les 3 objets dans le labyrinthe à la place de 3 caractère path
def random_object(liste):
    """Fonction en charge de remplacer aléatoirement 3 PATH_CHARACTER par 3 OBJECT_CHARACTER
    et de retourner la liste (char_of_th_map) avec les modifications"""
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
            
        else: 
            print("Game Over!!! Le Gardien du labyrinthe vous a tué!!!")
            return 0
            

def move(liste, y):
    """Fonction en charge du déplacement de MacGyver ("m") par rapport à son index "x" 
    dans la liste (char_of_the_map) avec comme parametre y (-15 = up, +15 = down, -1 = left et +1 = right)"""
    
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

    

while win_condition(char_of_the_map) !=0:

    
    display_map(char_of_the_map)
    joueur = input("Que voulez vous faire : ? ('z' pour up, 'q' pour left, 's' pour down, 'd' pour right : ")
    

    if joueur == "z":
        move(char_of_the_map, -15)
        
    elif joueur == "q":
        move(char_of_the_map, -1)   
        
    elif joueur == "d":
        move(char_of_the_map, +1)
        
    elif joueur == "s":
        move(char_of_the_map, +15)
        