

# fonction permettant de convertir le fichier.txt en string
def txt_transform(fichiertxt):
    """Return the file.txt in string without space"""
    with open(fichiertxt, "r") as infile:

        char = infile.read()
    infile_in_string = char.replace("\n", "")
    return infile_in_string


# fonction permettant de print la liste en labyrinthe
def display_map(var):
    """Return """
    for x, tile in enumerate(var):
        print(tile, end= "")
        if (x+1) % 15 == 0:
            print("")