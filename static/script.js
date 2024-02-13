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
        "ARRÊTEZ..."
    ]
    
     spanConseils = document.getElementById("conseils");
    const indiceAleatoire = Math.floor(Math.random() * conseils.length);
    spanConseils.textContent = conseils[indiceAleatoire];
}

