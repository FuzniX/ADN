from flask.sansio.scaffold import T_route
from assets import Assets as a


def in_string(mot: str, chaine: str) -> str:
    """
    Retourne une chaine de caractères entourant le mot donné dans le génome donné.
    ...404 - NOT FOUND... si non trouvée.

    """
    index = recherche_mot(chaine, mot)

    mot_dans_sequence = chaine[index: index + len(mot)]
    
    if 0 <= index < 16:
        return (chaine[:index + 18] + "...").replace(mot_dans_sequence, f" - {mot_dans_sequence} - ", 1)
    elif len(chaine) - 19 < index:
        return ("..." + chaine[index - 15:]).replace(mot_dans_sequence, f" - {mot_dans_sequence} - ", 1)
    elif index >= 16:
        return ("..." + chaine[index - 15:index + 18] + "...").replace(mot_dans_sequence, f" - {mot_dans_sequence} - ", 1)
    else:
        print(index)
        return "...404 - NOT FOUND..."


def transposition(texte: str) -> str:
    """
    Reçoit un code génétique en str et renvoie le code transposé par le dico
    """
    texte_transpose = ""
    for i in range(0, len(texte) // 3 * 3, 3):
        triplet = texte[i:i + 3]
        texte_transpose += a.DICO2.get(triplet, "Z")
    return texte_transpose

def transposition_etoile(texte: str) -> str:
    """
    Reçoit un code génétique en str et renvoie le code transposé par le dico
    """
    texte_transpose = ""
    for i in range(0, len(texte) // 3 * 3, 3):
        triplet = texte[i:i + 3]
        texte_transpose += a.DICO.get(triplet, "Z")
    return texte_transpose



def fic_to_txt(file_name: str) -> str:
    """
    Reçoit un nom de fichier et retourne une chaine de caractères du contenu du fichier.
    """
    with open(file_name, "r") as fic:
        return ''.join(fic.readlines()).replace("\n", "")


def get_set():
    """
    Retourne un set de tous les mots du fichier MOTS.txt
    """
    with open("static/MOTS.txt", "r") as f:
        return {mot.strip() for mot in f.readlines()}


def is_valid(file_name: str) -> bool:
    """
    Reçoit un nom de fichier et retourne la validité d'un fichier (s'il est au format txt et ne contient que des A, T, C, G ou N)
    """

    if file_name[-3:] == "fna":
        fna_to_txt(file_name)
        file_name = f"{file_name[:-3]}txt"

    if file_name[-3:] == "txt":
        with open(file_name, "r") as fic:
            for char in "\n".join(fic.readlines()):
                if char not in ["A", "T", "C", "G", "N", "\n"]:
                    return False
        return True


def fna_to_txt(file_name: str) -> None:
    """
    Convertit un fichier FNA (format de base pour NBCI) en fichier TXT.
    Les lignes de description du génome sont retirées.
    """
    with open(file_name, "r") as fic:
        lignes = [ligne for ligne in fic.readlines() if all(char in ["A", "T", "C", "G", "N", "\n"] for char in ligne)]
    file_name = f"{file_name[:-3]}txt"

    with open(file_name, "w") as f:
        f.write("".join(lignes))

def recherche_mot(sequence: str, mot: str) -> int:
    """
    Recherche un mot dans une séquence transposée du génome en prenant en compte l'étoile comme joker.
    Retourne l'indice de la première occurence du mot s'il est trouvé, sinon -1.
    """
    longueur_mot = len(mot)
    for i in range(len(sequence) - longueur_mot + 1):
        sous_sequence = sequence[i:i + longueur_mot]
        match = True
        for j in range(longueur_mot):
            if mot[j] != "*" and sous_sequence[j] != mot[j] and sequence[i+j] != "*":
                match = False
                break
        if match:
            return i
    return -1
