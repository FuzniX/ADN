from flask.sansio.scaffold import T_route
from assets import Assets as a

def get_lettre(triplet: str) -> str:
    """
    Renvoie la lettre correspondant au triplet d'un code génétique donné
    """
    return a.DICO2.get(triplet, "Z")

def in_string(mot: str, chaine: str) -> str:
    """
    Retourne une chaine de caractères entourant le mot donné dans le génome donné.
    ...404 - NOT FOUND... si non trouvée.

    """
    index = chaine.find(mot)

    if index >= 0:
        return "..." + chaine[index-15:index+18] + "..."
    else:
        return "...404 - NOT FOUND..."
    

def transposition(texte: str) -> str:
    """
    Reçoit un code génétique en str et renvoie le code transposé par le dico
    """
    texte_transposé = ""
    for i in range(0, len(texte)//3*3, 3):
        lettre_tempo = texte[i:i+3]
        texte_transposé += get_lettre(lettre_tempo)
    return texte_transposé

def fic_to_txt(file_name: str) -> str:
    """
    Reçoit un nom de fichier et retourne une chaine de caractères du contenu du fichier.
    """
    with open(file_name, "r") as fic:
        return ''.join(fic.readlines()).replace("\n", "")

def get_set():
    with open("static/MOTS.txt", "r") as f:
        return {mot.strip() for mot in f.readlines()}

def is_valid(file_name: str) -> bool:
    """
    Reçoit un nom de fichier et retourne la validité d'un fichier (s'il est au format txt et ne contient que des A, T, C, G ou N)
    """

    if file_name[-3:] == "fna":
        fna_to_txt(file_name)
        file_name = f"{file_name[:-3]}txt"
        print("a")

    print("b")
    if file_name[-3:] == "txt":
        print("c")
        with open(file_name, "r") as fic:
            for ligne in fic.readlines():
                for char in ligne:
                    if char not in ["A", "T", "C", "G", "N", "\n"]:
                        print(char)
                        print("d")
                        return False
            # if any((char not in ["A", "T", "C", "G", "N", "\n"] for char in ligne) for ligne in fic.readlines()):
            #     print("d")
            #     return False
        print("e")
        return True
    


def fna_to_txt(file_name: str) -> None:
    with open(file_name, "r") as fic:
        lignes = [ligne for ligne in fic.readlines() if all(char in ["A", "T", "C", "G", "N", "\n"] for char in ligne)]
    file_name = f"{file_name[:-3]}txt"
    
    with open(file_name, "w") as f:
        f.write("".join(lignes))
            