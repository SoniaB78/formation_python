#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrateur
#
# Created:     08/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
'''
dir help
'''
global choixCaburant,mettreCarburant

class Voiture:
    def __init__(self, marque, modele, couleur, carburant, reservoir, maxReservoir, reserve):
        self.moteurAllume = 0 # variable type boolean (0 1) pour vérifier que le moteur est allumé
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.carburant = carburant # permet de faire varier le prix pour complexifier
        self.reservoir = reservoir # taille du reservoir en litres
        self.maxReservoir = maxReservoir # stock le max du reservoir
        self.reserve = reserve # indicateur de reserve

    def action(self):
        action = input("Vous pouvez: avancer, arréter le moteur ou mettre du carburant. (avancer arreter carburant)")

        if action != "avancer" and action != "arreter" and action != "carburant":
            #erreur saisie
            action = input("Vous devez écrire: avancer arreter carburant")

        #Pour avancer
        elif action == "avancer":
            self.avancer()

        #Pour arreter le moteur
        elif action == "arreter":
            self.arreter()

        #Pour mettre du carburant
        elif action == "carburant":
            self.carburant()

    def demarrer(self):
        if self.reservoir > 0:
            print("*Le moteur démarre, vous avez ", self.reservoir, " litres de carburant*")
            self.moteurAllume = 1
        else:
            print("*Vous essayez de démarrer mais il n'y a pas assez de carburant*")

    def arret(self):
        print("*Le moteur s'arrète*")
        self.moteurAllume = 0

    def carburant(self):
        mettreCarburant = int(input("Combien voulez-vous en mettre ? (max {})".format(self.reservoir)))

        if mettreCarburant <= self.reservoir:
            self.reservoir += mettreCarburant
        else:
            print("Vous ne pouvez pas mettre plus de carburant que la contenance du reservoir, ça déborde!")
            self.reservoir += maxReservoir

    def avancer(self):
        if self.moteurAllume == 1:
            print("*Le véhicule commence à avancer*")
            kmParcourus = 0

            while self.reservoir > self.reserve:
                self.reservoir -= 1
                kmParcourus += 15
            print("*Vous avez parcourus ", kmParcourus, " kilomètres ,le voyant de la réserve s'allume, vous devriez vous vous arréter mettre du carburant")

            choixCaburant = input("Voulez-vous mettre du carburant? (oui non)")

            if choixCaburant != "oui" and choixCaburant != "non":
                print("Voulez-vous mettre du carburant? Vous devez taper oui ou non")
            elif choixCaburant == "oui":
                self.carburant()
            elif choixCaburant == "non":
                print("Vous continuez à rouler")
            while self.reservoir > 0:
                self.reservoir -= 1
                kmParcourus += 15
                if self.reservoir == 0:
                    print("Vous tombez en panne")
                    self.moteurAllume = 0
                    break

        else:
            print("Vous devez demarrer le moteur pour pouvoir avancer ;)")



######################## PROGRAMME PRINCIPALE ########################
maVoiture = Voiture("Audi", "A2", "grise", "diesel", 45, 45, 5)

print("Votre véhicule est de la marque :", maVoiture.marque , ",modèle :", maVoiture.modele, ". Elle est", maVoiture.couleur, ", il fonctionne avec le carburant :", maVoiture.carburant, ", son reservoir est de", maVoiture.maxReservoir ,".\n")

# ------------------ Pour demarrer le véhicule ------------------

demarrer = input("Le moteur est éteint, pour démarrer la voiture tapez oui.")

if demarrer != "oui" and demarrer != "non":
    print("Veuillez entrer oui ou non.")

elif demarrer == "non":
    while demarrer != "oui":
        demarrer = input("Le moteur reste éteint, voulez-vous démarrer la voiture?")

        if demarrer == "non":
            continue

        elif demarrer != "oui" and demarrer != "non":
            print("Veuillez entrer oui ou non.")
            continue

        else:
            maVoiture.demarrer()
            break

else:
    maVoiture.demarrer()
    maVoiture.action()



##### QUESTIONS POUR GILLES #####
"""
J'ai des soucis à mettre en place des condition  / boucles de manière logique

Comment organiser les parties du programme principal pour qu'on ne puisse pas sauter d'une condition à l'autre

Quand je suis dans le programme principale est ce que j'utilise self , comment je récupère l'info qui concerne quel instance j'utilise? param?
"""
