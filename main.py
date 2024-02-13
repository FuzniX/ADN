import time

from flask import Flask, render_template, request
import fonctions as f
from werkzeug.utils import secure_filename
from unidecode import unidecode

app = Flask(__name__)

# Accueil
@app.route('/')
def index():
    return render_template("index.html", disp="none")

# Recevoir un fichier et retourner la liste des mots présents dans le génome donné
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    global gen, gen_etoile  # Variables globales des gènes à traiter
    global mots  # Variable globale de la liste des mots dans le génome triée dans l'ordre alphabétique

    # Récupérer le fichier
    file = request.files['file']

    if not file:
        return render_template("index.html", disp=True)
    nom_fichier = 'static/' + secure_filename(file.filename)
    file.save(nom_fichier)

    # Vérifier que le fichier est valide
    if not f.is_valid(nom_fichier):
        return render_template("index.html", disp=True)

    gen = f.transposition(f.fic_to_txt(nom_fichier)) # Le gène sous forme transformée avec des lettres prédifinies pour récupérer une liste de mots
    gen_etoile = f.transposition_etoile(f.fic_to_txt(nom_fichier)) # Gène brut où les * seront traités comme n'importe quel caractère

    # t1 = time.time() # COMPLEXITE DE L'AFFICHAGE DE TOUS LES MOTS PRESENTS DANS LE GENOME
    if request.form.get('afficherMots') == "True":
        # Si l'utilisateur décide d'afficher les mots
        mots = sorted({(mot, gen.find(mot)) for mot in f.get_set() if mot in gen}, key=lambda x: x[1])  # POSE PROBLEME
    else:
        # Si l'utilisateur décide de ne pas afficher les mots, gagne un temps proportionnel à la longueur du génome
        mots = set()

    # print(time.time()-t1) # AFFICHAGE DE LA COMPLEXITE

    return render_template("chercheur.html", les_mots=mots, status="", phrase="-1")


# Rechercher une phrase parmi les mots d'un génome donné
@app.route('/recherche', methods=['GET'])
def rechercher():
    phrase = request.args.get("phrase")
    # Vérifier qu'une phrase est passée, si oui, enlever les accents et la rend en majuscule
    if phrase:
        phrase = unidecode(phrase.upper())
    else:
        # Cas où aucune phrase n'est donnée.
        return render_template("chercheur.html",
                               les_mots=mots,
                               status="Aucune phrase n'a été donnée.",
                               phrase="-1",)

    try:
        # Initialisation de variables utilisées dans la boucle for suivante
        mots_sans_indice = (mot[0] for mot in mots)
        liste_phrase = phrase.split(" ")
        gen_tempo = gen_etoile
        chaine = []

        for i, el in enumerate(liste_phrase):
            if f.recherche_mot(gen_tempo, el) != -1:
                # Formatage de l'affichage de la séquence de caractères
                string = f.in_string(el, gen_tempo)

                # Cas où il n'y a pas 19 caractères avant le premier tiret et où il y a répétition
                if string.find("-") != 19 and i != 0:
                    chaine[-1] = chaine[-1][:-21] + "- " + string

                # Cas où il n'y a pas de répétition
                else:
                    chaine.append(string)
                
                gen_tempo = gen_tempo[gen_tempo.find(el) + len(el):]
                              
            elif el in mots_sans_indice:
                # Les mots qui constituent la phrase ne sont pas dans l'ordre dans le génome.
                return render_template("chercheur.html",
                                       les_mots=mots,
                                       status=f"Les mots qui constituent la phrase ne sont pas dans l'ordre dans le génome.",
                                       phrase="-1",)
            else:
                # Un élément n'est pas dans le génome
                return render_template("chercheur.html",
                                       les_mots=mots,
                                       status=f"{el} n'est pas dans le génome.",
                                       phrase="-1")

        # La phrase est dans le génome
        return render_template("chercheur.html",
                               les_mots=mots,
                               status=f"La phrase '{phrase.capitalize()}' est dans le génome.",
                               phrase=liste_phrase,
                               chaine=chaine)

    # Dans le cas où il y a une exception, retourner à l'accueil
    except: return index()


# Démarrer le serveur Web
app.run(host="0.0.0.0", port=26008)
