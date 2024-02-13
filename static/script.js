function demarrerTraitement() {
    document.getElementById("chargement").style.display = "block";
    document.getElementById("background").style.display = "none";
    setInterval(conseils, 2500)
}



function conseils() {
    const conseils = [
        "VERIFICATION ANTIGOUVERNEMENTALE...",
        "LA TERRE EST PLATE...",
        "ANALYSE G8N0ME...",
        "MAIS OU SONT LES REPTILIENS...",
        "ARRÊTEZ...",
        "ANALYSE DES ONDES CÉRÉBRALES...",
        "LOCALISATION DES AGENTS SECRETS...",
        "CALCUL DES COORDONNÉES DU TRIANGLE DES BERMUDES...",
        "DÉCHIFFREMENT DES HIÉROGLYPHES ALIENS...",
        "RECHERCHE DE PREUVES DE L'EXISTENCE DES LICORNES...",
        "CALCUL DE LA FRÉQUENCE DES MESSAGES SUBLIMINAUX...",
        "DÉTECTION DES SIGNAUX EXTRATERRESTRES...",
        "ILS SE CACHENT PEUT-ÊTRE DANS LE NOIR...",
        "LIVRAISON DE PIZZAS MYSTÉRIEUSES...",
        "ILS VIENNENT DIRE BONJOUR...",
        "IDENTIFICATION DES AGENTS DU COMPLOT...",
        "RECHERCHE DE PREUVES D'UNE CIVILISATION SOUTERRAINE...",
        "ANALYSE DES PHÉNOMÈNES PARANORMAUX...",
        "MESSAGES CODÉS...",
        "ILS NOUS OBSERVENT...",
        "TEMPS PERDU DANS LES FILES D'ATTENTE...",
        "JE VOUS AVAIS PRÉVENU...",
        "JE VOUS LE JURE..."
    ]
    
     spanConseils = document.getElementById("conseils");
    const indiceAleatoire = Math.floor(Math.random() * conseils.length);
    spanConseils.textContent = conseils[indiceAleatoire];
}

document.addEventListener("DOMContentLoaded", function () {
    var backButton = document.getElementById("back-to-top");

    window.addEventListener("scroll", function () {
        // Afficher ou masquer le bouton en fonction du défilement
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            backButton.style.display = "block";
        } else {
            backButton.style.display = "none";
        }
    });

    backButton.addEventListener("click", function () {
        // Appel de la fonction pour faire défiler la page avec une animation
        scrollToTop(1000); // 1000 milliseconds (1 seconde) pour l'animation
    });

    // Fonction pour faire défiler la page vers le haut avec une animation
    function scrollToTop(duration) {
        var start = document.body.scrollTop || document.documentElement.scrollTop;
        var startTime = new Date().getTime();

        var animateScroll = function () {
            var now = new Date().getTime();
            var timeElapsed = now - startTime;

            document.body.scrollTop = document.documentElement.scrollTop = easeInOut(timeElapsed, start, -start, duration);

            if (timeElapsed < duration) {
                requestAnimationFrame(animateScroll);
            } else {
                document.body.scrollTop = document.documentElement.scrollTop = 0;
            }
        };

        requestAnimationFrame(animateScroll);
    }

    // Fonction d'accélération/décélération (EaseInOut)
    function easeInOut(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--;
        return -c / 2 * (t * (t - 2) - 1) + b;
    }
});