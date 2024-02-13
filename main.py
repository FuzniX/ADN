import time

from flask import Flask, render_template, request
import fonctions as f
from werkzeug.utils import secure_filename
from unidecode import unidecode

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", disp="none")


# Accueil du site
@app.route('/index.html')
def affiche_index():
    return render_template("index.html", disp="none")


# Recevoir un fichier et retourner la liste des mots présents dans le génome donné
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    global gen
    global mots  # Variable globale de la liste des mots dans le génome triée dans l'ordre alphabétique

    # Récupérer le fichier
    file = request.files['file']

    if not file:
        return render_template("index.html", disp=True)

    nom_fichier = 'static/' + secure_filename(file.filename)
    file.save(nom_fichier)

    if not f.is_valid(nom_fichier):
        return render_template("index.html", disp=True)

    gen = f.transposition(f.fic_to_txt(nom_fichier))
    t1 = time.time()
    mots = sorted({(mot, gen.find(mot)) for mot in f.get_set() if mot in gen}, key=lambda x: x[1])  # POSE PROBLEME
    print(time.time()-t1)

    return render_template("chercheur.html", les_mots=mots, status="", phrase="-1")


# Rechercher une phrase parmi les mots d'un génome donné
@app.route('/recherche', methods=['GET'])
def rechercher():
    phrase = request.args.get("phrase")
    # Vérifier qu'une phrase est passée, si oui, enlever les accents et la rend en majuscule
    if phrase:
        phrase = unidecode(phrase.upper())
    else:
        return render_template("chercheur.html",
                               les_mots=mots,
                               status="Aucune phrase n'a été donnée.",
                               phrase="-1",)

    try:

        mots_sans_indice = (mot[0] for mot in mots)
        liste_phrase = phrase.split(" ")
        gen_tempo = gen

        for el in liste_phrase:
            if el in gen_tempo:
                gen_tempo = gen_tempo[gen_tempo.find(el) + len(el):]
                print(gen_tempo)
            elif el in mots_sans_indice:
                return render_template("chercheur.html",
                                       les_mots=mots,
                                       status=f"Les mots qui constituent la phrase ne sont pas dans l'ordre dans le génome.",
                                       phrase="-1",)
            else:
                return render_template("chercheur.html",
                                       les_mots=mots,
                                       status=f"{el} n'est pas dans le génome.",
                                       phrase="-1")

        chaine = [f.in_string(mot, gen) for mot in liste_phrase]
        
        return render_template("chercheur.html",
                               les_mots=mots,
                               status=f"La phrase '{phrase.capitalize()}' est dans le génome.",
                               phrase=liste_phrase,
                               chaine=chaine)

    # Dans le cas où il y a une exception, l'afficher à l'utilisateur
    except Exception:
        return index()


app.run(host="0.0.0.0", port=26008)
