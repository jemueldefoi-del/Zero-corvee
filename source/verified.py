# Caractéristiques vérifiées le 5 octobre 2026 (sites des fabricants, revendeurs et tests).
# Clé = nom du produit dans content.py. "name" renomme le produit sur un modèle précis.

OVR = {
 # Sols
 "Roborock Qrevo": {"name": "Roborock Qrevo S", "specs": [("Aspiration", "7 000 Pa"), ("Autonomie", "≈ 180 min"), ("Batterie", "5 200 mAh"), ("Navigation", "Laser + caméra")]},
 "Dreame L-series": {"name": "Dreame L40 Ultra", "specs": [("Aspiration", "11 000 Pa"), ("Autonomie", "≈ 180 min"), ("Serpillières", "Rotatives, levage auto"), ("Navigation", "Laser + caméra")]},
 "Xiaomi Robot Vacuum": {"name": "Xiaomi Robot Vacuum S20", "specs": [("Aspiration", "5 000 Pa"), ("Batterie", "2 900 mAh"), ("Bac à poussière", "400 mL"), ("Réservoir d'eau", "270 mL")]},
 "Ecovacs Deebot": {"name": "Ecovacs Deebot T30 Omni", "table": ["Vidage + lavage + remplissage", "Serpillières rotatives"],
   "specs": [("Aspiration", "11 000 Pa"), ("Station", "Mini Omni"), ("Serpillières", "Levage auto 9 mm"), ("Navigation", "Laser + détection 3D")]},
 # Pelouse
 "Husqvarna Automower": {"name": "Husqvarna Automower 310 Mark II", "table": ["Fil périmétrique", "40 %"],
   "specs": [("Surface", "1 000 m² (±20 %)"), ("Pente max", "40 %"), ("Bruit", "59 dB(A)"), ("Hauteur de coupe", "20 à 50 mm")]},
 "Gardena Sileno": {"name": "Gardena Sileno City", "table": ["Fil périmétrique", "35 %"],
   "specs": [("Surface", "250 à 600 m² selon version"), ("Pente max", "35 %"), ("Bruit", "57 dB(A)"), ("Hauteur de coupe", "20 à 50 mm")]},
 "Worx Landroid": {"name": "Worx Landroid M500", "table": ["Fil périmétrique", "35 %"], "cons": ["Navigation plus aléatoire", "Plus bruyant (67 dB)"],
   "specs": [("Surface", "500 m² (400 m² conseillés)"), ("Pente max", "35 %"), ("Largeur de coupe", "18 cm"), ("Hauteur de coupe", "30 à 60 mm")]},
 "Segway Navimow": {"name": "Segway Navimow i105E", "table": ["GPS RTK + caméra", "30 %"],
   "specs": [("Surface", "500 m²"), ("Pente max", "30 %"), ("Largeur de coupe", "18 cm"), ("Hauteur de coupe", "20 à 60 mm")]},
 # Piscine
 "Dolphin (Maytronics)": {"name": "Dolphin S300i", "pros": ["Nettoie fond, parois et ligne d'eau", "Programmation depuis l'application", "Garantie 3 ans"],
   "specs": [("Bassin", "Jusqu'à 12 m"), ("Cycle", "1 h 30 à 2 h 30"), ("Câble", "17 m"), ("Poids", "8,4 kg")]},
 "Beatbot": {"name": "Beatbot AquaSense 2 Pro",
   "specs": [("Bassin", "Jusqu'à 360 m²"), ("Autonomie", "Jusqu'à 4 h 30 (fond + parois)"), ("Poids", "11,4 kg"), ("Filtration", "150 + 250 µm")]},
 "Aiper": {"name": "Aiper Seagull Pro", "table": ["Batterie", "Fond, parois"], "cons": ["Ne nettoie pas la surface de l'eau", "Moins complet que le haut de gamme"],
   "specs": [("Bassin", "Jusqu'à 300 m²"), ("Autonomie", "180 min"), ("Charge", "90 min"), ("Poids", "≈ 9,5 kg")]},
 "Zodiac": {"name": "Zodiac Tornax Pro RT 2100", "table": ["Câble", "Fond uniquement"], "cons": ["Ne nettoie que le fond", "Bassin limité à 8 x 4 m"],
   "specs": [("Bassin", "Jusqu'à 8 x 4 m"), ("Cycle", "2 h"), ("Câble", "14 m"), ("Filtration", "100 µm, 3 L")]},
 # Vitres
 "Ecovacs Winbot": {"name": "Ecovacs Winbot W2 Omni", "pros": ["Pulvérisation automatique à 6 buses", "Station portable sur batterie", "Câble de sécurité intégré au câble d'alimentation"],
   "specs": [("Aspiration", "5 500 Pa"), ("Batterie", "5 200 mAh, ≈ 110 min"), ("Pulvérisation", "Intégrée"), ("Vitre sans cadre", "Oui")]},
 "Hobot": {"name": "Hobot 2S", "table": ["Aspiration", "Intégrée (ultrasons)"],
   "specs": [("Pulvérisation", "Ultrasons, 2 réservoirs"), ("Batterie de secours", "≈ 20 min"), ("Corde de sécurité", "4,5 m"), ("Bruit", "60 dB")]},
 "Cecotec Conga WinDroid": {"name": "Cecotec Conga WinDroid 980 Connected",
   "specs": [("Câble", "5 m avec rallonge"), ("Batterie de secours", "Oui"), ("Pulvérisation", "Manuelle"), ("Commande", "Appli + télécommande")]},
 # Litière
 "Litter-Robot 4": {"specs": [("Poids mini du chat", "1,4 kg"), ("Entrée", "40 x 40 cm"), ("Sable", "Agglomérant"), ("Connexion", "Wi-Fi 2,4 GHz")]},
 "Petkit Pura Max 2": {"specs": [("Poids du chat", "1,5 à 8 kg"), ("Bac à déchets", "7 L"), ("Dimensions", "66,5 x 57 x 58,5 cm"), ("Bruit", "< 25 dB")]},
 "PetSafe ScoopFree": {"specs": [("Format", "Bac ouvert, râteau"), ("Sable", "Cristaux en plateau jetable"), ("Dimensions", "52 x 71 x 18 cm"), ("Connexion", "Aucune")]},
 # Croquettes
 "Petkit Fresh Element": {"name": "Petkit Fresh Element Solo",
   "specs": [("Réservoir", "3 L (≈ 15 jours pour un chat)"), ("Repas", "Jusqu'à 10 par jour, 10 à 50 g"), ("Croquettes", "Moins de 12 mm"), ("Secours", "Piles")]},
 "Xiaomi Smart Pet Food Feeder": {"name": "Xiaomi Smart Pet Food Feeder 2", "pros": ["Grand réservoir de 5 L", "Application simple", "Prix bas pour un modèle connecté"],
   "cons": ["Pas d'alimentation de secours annoncée", "Moins de réglages fins"],
   "specs": [("Réservoir", "5 L (≈ 30 jours pour un chat)"), ("Connexion", "Wi-Fi 2,4 GHz"), ("Dimensions", "37 x 22 x 32 cm"), ("Animaux", "Chat")]},
 "Cat Mate (minuterie)": {"name": "Cat Mate C500",
   "specs": [("Repas", "5 compartiments de 330 g"), ("Programmation", "Minuterie"), ("Secours", "3 piles AA (≈ 1 an)"), ("Pâtée", "Oui, 2 pains de glace")]},
 # Linge
 "Miele (gamme T1)": {"specs": [("Technologie", "Pompe à chaleur"), ("Capacité", "8 à 9 kg selon modèle"), ("Anti-froissage", "Oui"), ("Classe énergie", "Généralement A++ ou A+++")]},
 "Bosch Série 6": {"specs": [("Technologie", "Pompe à chaleur"), ("Capacité", "8 à 9 kg selon modèle"), ("Anti-froissage", "Oui"), ("Classe énergie", "Généralement A++ ou A+++")]},
 "Samsung (gamme pompe à chaleur)": {"specs": [("Technologie", "Pompe à chaleur"), ("Capacité", "9 kg et plus"), ("Anti-froissage", "Vapeur selon modèle"), ("Classe énergie", "Généralement A++ ou A+++")]},
 "Beko (gamme pompe à chaleur)": {"specs": [("Technologie", "Pompe à chaleur"), ("Capacité", "8 kg selon modèle"), ("Anti-froissage", "Oui"), ("Classe énergie", "Généralement A++")]},
}

# Textes du choix rapide qui citent un produit renommé.
ALTS = [("Xiaomi Robot Vacuum</a>", "Xiaomi Robot Vacuum S20</a>"), ("Dreame L-series</a>", "Dreame L40 Ultra</a>"),
        ("Segway Navimow</a>", "Segway Navimow i105E</a>"), ("Worx Landroid</a>", "Worx Landroid M500</a>"),
        (">Aiper</a>", ">Aiper Seagull Pro</a>"), (">Zodiac</a>", ">Zodiac Tornax Pro</a>"),
        ("Cecotec Conga WinDroid</a>", "Cecotec Conga WinDroid 980</a>"), (">Cat Mate</a>", ">Cat Mate C500</a>")]

# Mini lave-vaisselle : Bob passe en tête avec ses caractéristiques vérifiées.
BOB = {"name": "Bob", "brand": "Daan Tech", "badge": "Meilleur choix", "price": "€€", "table": ["Réservoir ou robinet", "3"],
  "for": "les studios, les locations et les couples sans place pour un lave-vaisselle.",
  "pros": ["Fonctionne sur réservoir ou raccordé au robinet", "Cycle express de 20 minutes", "Accepte les assiettes jusqu'à 29 cm"],
  "cons": ["Limité à 3 couverts", "Prix élevé pour sa taille (≈ 400 €)"],
  "specs": [("Réservoir", "3,9 L"), ("Cycle express", "20 min, 2,9 L d'eau"), ("Capacité", "3 couverts"), ("Dimensions", "34 x 49 x 49 cm")]}


MAIN = {"robot-aspirateur-laveur", "robot-tondeuse", "robot-piscine", "robot-lave-vitres", "seche-linge-pompe-a-chaleur",
        "mini-lave-vaisselle", "litiere-autonettoyante", "distributeur-croquettes-automatique"}


def apply(guides):
    for g in guides:
        for p in g["products"]:
            o = OVR.get(p["name"])
            if o:
                o = dict(o)
                if g["slug"] not in MAIN:
                    o.pop("table", None)
                p.update(o)
        for a, b in ALTS:
            g["pick"]["alts"] = g["pick"]["alts"].replace(a, b)
        if g["slug"] == "mini-lave-vaisselle":
            midea = next(p for p in g["products"] if p["brand"] == "Midea")
            midea.update({"name": "Midea (lave-vaisselle de table)", "badge": "Plus de couverts", "table": ["Robinet ou réservoir selon modèle", "3 à 6"],
                          "specs": [("Raccordement", "Selon modèle"), ("Couverts", "3 à 6 selon modèle"), ("Pose", "Comptoir"), ("Cycle rapide", "Oui")]})
            candy = next(p for p in g["products"] if p["brand"] == "Candy")
            candy["badge"] = "Petit budget"
            g["products"] = [BOB, midea, candy]
            g["pick"] = {"why": "Le plus simple à installer : il fonctionne sur son propre réservoir ou raccordé au robinet, et lave en 20 minutes.",
                         "alts": 'Besoin de plus de couverts ? Voir <a href="#p2">Midea</a>. Petit budget avec raccordement ? Voir <a href="#p3">Candy compact</a>.'}
