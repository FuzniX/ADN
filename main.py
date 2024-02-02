from flask import Flask, render_template, request, redirect, url_for
import fonctions as f
from werkzeug.utils import secure_filename
from unidecode import unidecode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# Accueil du site
@app.route('/index.html')
def affiche_index():
  return render_template("index.html")

# Recevoir un fichier et retourner la liste des mots présents dans le génome donné
@app.route('/upload', methods=['GET', 'POST'])
def upload():

    # Récupérer le fichier
    file = request.files['file']
    file.save('static/'+ secure_filename(file.filename))
    
    global nom_fichier
    nom_fichier = 'static/'+ secure_filename(file.filename)
    gen = f.transposition(f.fic_to_txt(nom_fichier))

    global mots # Variable globale de la liste des mots dans le génome triée dans l'ordre alphabétique
    mots = sorted({(mot, gen.find(mot)) for mot in f.get_set() if mot in gen}, key=lambda x: x[1])
    
    return render_template("chercheur.html", nf=nom_fichier, les_mots = mots, status="", phrase="-1")

# Rechercher une phrase parmi les mots d'un génome donné
@app.route('/recherche', methods = ['GET'])
def rechercher():
    phrase = request.args.get("phrase")
    # Vérifier qu'une phrase est passée, si oui, enlever les accents et la rend en majuscule
    if phrase: phrase = unidecode(phrase.upper())
    else: return render_template("chercheur.html", 
                                 nf=nom_fichier, 
                                 les_mots = mots, 
                                 status="Aucune phrase n'a été donnée", 
                                 phrase="-1")

    try:
        liste_mots = [mot[0] for mot in mots]
        
        liste_phrase = phrase.split(" ")
        i = 0
        
        for el in liste_phrase:
            # Pas la phrase dans le génome
            if el not in liste_mots:
                return render_template("chercheur.html", 
                                       nf=nom_fichier, 
                                       les_mots = mots, 
                                       status=f"{el} n'est pas dans le génome.", 
                                       phrase="-1")

            # Vérifier que c'est dans l'ordre
            elif el in liste_mots and liste_mots.index(el) < i:
                return render_template("chercheur.html",
                                       nf=nom_fichier, 
                                       les_mots = mots, 
                                       status=f"Les mots qui constituent la phrase ne sont pas dans l'ordre dans le génome.", 
                                       phrase="-1")

            # Affecter un nouveau i
            else:
                i = liste_mots.index(el)
        
        return render_template("chercheur.html", 
                               nf = nom_fichier, 
                               les_mots = mots,
                               status = f"La phrase '{phrase}' est dans le génome",
                               phrase=phrase.capitalize())

    # Dans le cas où il y a une exception, l'afficher à l'utilisateur
    except Exception as e:
        return f"{type(e)}: {e}"
        

app.run(host="0.0.0.0", port=81)
