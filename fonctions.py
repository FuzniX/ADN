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
