# 🎧 Simulateur d'atténuation sonore d'une installation domestique
Une application web simple pour simuler l’atténuation du bruit d’un appareil extérieur (climatiseur, pompe à chaleur, etc.) en fonction de la distance et des protections acoustiques utilisées.

🔗 Lien de l'appli: https://installationdomestiqueexterieure.streamlit.app/

## 🌟 Fonctionnalités

📏 Choix de la distance jusqu’au point d’écoute (jusqu’à 20 mètres),

🔊 Niveau sonore initial réglable entre 35 et 100 dB ,

🛡️ Sélection multiple de dispositifs d’atténuation acoustique :

    - Caisson insonorisé (-10dB)
    - Écran acoustique (-20dB)
    - Mur béton (10 cm d'épaisseur -25dB)
    - Végétation dense (haies -10dB)
    
📈 Affichage d’un graphique interactif montrant l’évolution du niveau sonore en fonction de la distance,

🚦 Comparaison automatique avec le plafond réglementaire de 30 dB (bruit de voisinage extérieur),

📊 Résultat clair : conforme ou non-conforme au seuil légal (Code de la santé publique).

## 🧮 Méthodologie de calcul
L’application utilise une modélisation simplifiée de l’atténuation sonore en extérieur, basée sur deux principaux facteurs :

### 1. **Atténuation due à la distance**
La propagation du son dans l'air libre suit la **loi du carré inverse**, ce qui donne une atténuation exprimée en décibels (dB) selon la formule suivante :

    Atténuation (dB) = 20 × log10(Distance en mètres)
        
Par exemple : à 10 mètres, l’atténuation est de 20 dB. 

> Cette formule suppose une source sonore ponctuelle dans un environnement (champ libre) sans écho, ni obstacle, ni réverbération.
>

### 2. **Atténuation due aux obstacles**

Chaque dispositif acoustique apporte une **atténuation supplémentaire fixe** en dB, basée sur des valeurs typiques :

| Obstacle                 | Atténuation moyenne (dB) |
|--------------------------|---------------------------|
| Aucun                    | 0                         |
| Caisson insonorisé       | 10                        |
| Écran acoustique         | 20                        |
| Mur béton                | 25                        |
| Végétation dense (haie)  | 10                        |

> Ces valeurs sont des ordres de grandeur simplifiés pour une simulation pédagogique.


### 🧮 Niveau sonore final

Le niveau sonore perçu au point d’écoute est donné par :

    Niveau final (dB) = Niveau initial (dB) – Atténuation (dB)

> ### 📊 Exemple concret

Supposons les paramètres suivants :
- **Niveau initial** : 70 dB (ex. climatiseur puissant)
- **Distance** : 10 mètres
- **Obstacles sélectionnés** : Caisson + végétation dense

#### Étapes de calcul :
1. **Atténuation due à la distance** :
    20 × log10(10) = 20 dB
2. **Atténuation due aux obstacles** :
    Caisson : 10 dB
    Végétation dense : 10 dB
    Total : 10 + 10 = 20 dB
3. **Atténuation totale**:
    20 dB (distance) + 20 dB (obstacles) = 40 dB
4. **Niveau sonore final** :
    70 dB (initial) – 40 dB (atténuation) = 30 dB

> ⚠️ Remarque : Si le niveau sonore final calculé est inférieur à 0 dB, cela signifie que le bruit est complètement atténué et **inaudible** dans les conditions simulées.

## 🛠 Technologies utilisées
  - Streamlit – Interface web interactive
  - Plotly – Visualisation graphique
  - Python standard – Calculs acoustiques simplifiés

📥 Installation locale
Prérequis
Python 3.8+
pip

🤝 Contribution
Les contributions sont bienvenues !
N’hésitez pas à ouvrir une issue ou une pull request si vous souhaitez améliorer cette application.

✅ Pourquoi ce projet ?
Cette application vise à aider les particuliers ou les professionnels à estimer facilement l’impact sonore d’une installation extérieure, et à choisir les bonnes solutions d’insonorisation pour respecter les normes légales.
