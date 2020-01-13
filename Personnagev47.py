#-------------------------------------------------------------------------------
# Name:        Personnages
# Purpose:
#
# Author:      Sonia
#
# Created:     09/01/2020
# Copyright:   (c) Administrateur 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import randint

class Personnage:
    def __init__ (self, id, nom, camp, race, classe, pv, pvMax, force, endurance, rapidite, intelligence):
        self.id = id
        self.nom = nom
        self.camp = camp
        self.race = race
        self.classe = classe
        self.pv = pv
        self.pvMax = pvMax
        self.pv = pv
        self.force = force
        self.endurance = endurance
        self.rapidite = rapidite
        self.intelligence = intelligence

    def estMort(self):
        if (self.pv > 0):
            return False
        else:
            return True

    def afficheEtat(self):
        if (self.estMort() == False):
            print(self.nom, "à", self.pv, "points de vie.")
        else:
            print(self.nom, "est mort !")

    def afficheCarac(self):
        print(" °~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~°" )
        print(" %s %s %s %s:\n \t FORCE : %i \n \t ENDURANCE: %i \n  \t RAPIDITE: %i \n \t INTELLIGENCE: %i \n "%(self.nom, self.camp, self.race, self.classe, self.force, self.endurance, self.rapidite, self.intelligence))
        print("°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~°")

    def perdVie(self, nbrPvPerdu):
        if (nbrPvPerdu >= self.pv):
            print("L'ennemi vous attaque !", self.nom, "subit une attaque mortelle !" )
            self.pv = 0
        else:
            print("L'ennemi vous attaque !", self.nom, "perd:", nbrPvPerdu, "points de vie !" )
            self.pv -= nbrPvPerdu

    def gagneVie(self, nbrPvGagne):
        if (self.estMort() != True):
            pvTmp = nbrPvGagne + self.pv
            if( pvTmp <= self.pvMax):
                self.pv += nbrPvGagne
                print(self.nom, "a été soigné, ses points de vie s'élèvent à:", self.pv, "points de vie.")
            elif (self.pv == self.pvMax):
                print(self.nom, "utilise une potion de soin mais", self.nom, "est deja à son maximum de point de vie.")
        else:
            print(self.nom, "ne peut être soigné car il est mort.")

    def attaque(self, ennemi):
        if (self.estMort() == False):
            if (ennemi.esquive(self) == False):
                self.degats = round(0.6 * self.force)
                ennemi.pv -= self.degats
                print("Vous infligez:", self.degats, "points de dégat à", ennemi.nom)
        else:
            print(self.nom, "ne peut attaquer car il/elle est mort(e).")

    def soigne(self, allie, nbrPvSoigne):
        if (self.estMort() == False and allie.estMort() == False):
            pvTmp = nbrPvSoigne + allie.pv
            if( pvTmp <= allie.pvMax):
                allie.pv += nbrPvSoigne
                print(self.nom, "soigne", allie.nom, ",", allie.nom, "récupère", nbrPvSoigne, ", il est à:", allie.pv, "points de vie.")

            elif (allie.pv == allie.pvMax):
                print(self.nom, "utilise un sort de soin mais", allie.nom, "est deja à son maximum de point de vie.")

            else:
                allie.pv += allie.pvMax
                print(allie.nom, "retoune à son maximum de point de vie:", allie.pvMax)


        elif (allie.estMort() == True):
            print(self.nom, "ne peut pas soigner", allie.nom, "car il est mort !")

        else:
            print(allie.nom, "ne peut pas être soigné car", self.nom, "est mort !")

    def esquive (self, ennemi):
        if (self.estMort() == False and ennemi.estMort() == False):
            if (self.rapidite > ennemi.rapidite):
                print(self.nom, "esquive l'attaque de", ennemi.nom)
                return True
                print("La rapidité de ",self.nom ,"est de:", self.rapidite,"contre",ennemi.nom ,"pour", ennemi.rapidite)
            else:
                print(self.nom, "a raté son esquive.")
                return False
        elif ( self.estMort() == True):
            print(self.nom, "ne peut esquiver l'attaque de", ennemi.nom, "car il est mort.")
        else:
            print(self.nom, "ne peut esquiver d'attaque car il est mort !")

    def mouvement(self, deplacement):#passer la direction : rester ou fuir
        if (self.estMort() != True):
            mouvement = input=("Voulez vous rester ou fuir")
            if (deplacement == "rester"):
                print(self.nom, "tient la position.")
            elif (deplacement == "fuir"):
                print(self.nom, "s'enfuit à toute jambes.")


##Création de personnages aléatoires par saisie utilisateur, choix du camps:
# CHOIX DU CAMP DANS LEQUEL LES PERSONNAGES SERONT CREES
choixCamp = input("Création d'un nouveau pesonnage: dans quel camps voulez-vous qu'il soit? horde alliance")

if (choixCamp =="horde"):
    print("Bravo vous avez choisi la Horde !")
    choixCamp = "horde"
    #persoRandom()
elif (choixCamp =="alliance"):
    print("Vous avez choisi l'alliance ")
    choixCamp = "alliance"
    #persoRandom()
else :
    choixCamp = input("Vous devez choisir un camp: horde ou alliance")


# CHOIX DU NOMBRE DE PERSO A CREER
#def persoRandom():

allianceux = []
hordeux = []

choixNbr = int(input("Combien de personnages voulez-vous créer ?"))

if (choixCamp == "alliance"):
    #print("allianceux")
    # CEATION DES PERSONNAGES
    for i in range(0, choixNbr):
    #id, nom, race, classe, pv, pvMax, force, endurance, rapidite, intelligence
        #Génération aléatoire des carac
        nomAlli = ["Tyrande", "Milhouse", "Varyan", "Dagran"]
        nom = nomAlli[randint(0,len(nomAlli)-1)]
        raceAlli = ["elfe de la nuit", "gnome", "humain", "nain"]
        race = raceAlli[randint(0,len(raceAlli)-1)]
        classeAlli = ["guerrier", "archer", "mage"]
        classe = classeAlli[randint(0,len(classeAlli)-1)]
        pvMax, force, endurance, rapidite, intelligence = randint(10, 40), randint(10, 40), randint(10, 40), randint(10, 40),randint(10, 40)
        pv = pvMax

    # Instanciation et ajout du personnage à la liste de camp choisit
        perso = Personnage(i, nom, choixCamp, race, classe, pv, pvMax, force, endurance, rapidite, intelligence)
        allianceux.append(perso)

    for perso in allianceux:
        print(perso.afficheCarac())

else:
    #print("hordeux")
    # CEATION DES PERSONNAGES
    for i in range(0, choixNbr):
    #id, nom, race, classe, pv, pvMax, force, endurance, rapidite, intelligence
    #Génération aléatoire des carac
        nomHorde = ["Sylvanas", "Gazleu", "Léoric", "Cairne"]
        nom = nomHorde[randint(0,len(nomHorde)-1)]
        raceHorde = ["elfe de sang", "gobelin", "mort vivant", "tauren"]
        race = raceHorde[randint(0,len(raceHorde)-1)]
        classeHorde = ["guerrier", "archer", "mage"]
        classe = classeHorde[randint(0,len(classeHorde)-1)]
        pvMax, force, endurance, rapidite, intelligence = randint(10, 40), randint(10, 40), randint(10, 40), randint(10, 40),randint(10, 40)
        pv = pvMax

    # Instanciation et ajout du personnage à la liste de camp choisit
        perso = Personnage(i, nom, choixCamp, race, classe, pv, pvMax, force, endurance, rapidite, intelligence)
        hordeux.append(perso)

    for perso in hordeux:
        print(perso.afficheCarac())




#  (import randint et uniform)


"""
### Affichages testes ####

# Instanciation :  nom, camp, race, classe, pv, pvMax, force, endurance, rapidite, intelligence
p1 = Personnage(1, "Sonia", "alliance", "humain", "archer", 20, 20, 30, 5, 25, 15) # Perso principal
e1 = Personnage(1, "Gruul", "horde", "orque", "guerrier", 35, 35, 20, 15, 10, 5) # Ennemi lamdba n°1

# Pésentation personnage
print("\t Bienvenue ! \n Votre personnage est", p1.nom)
p1.afficheCarac()

# Pésentation
print("Ennemi sauvage apparaît !")
e1.afficheCarac()

p1.afficheEtat()
e1.afficheEtat()

# Combat p1 attaque => e1
print("\n premiere attaque")
p1.attaque(e1)
e1.afficheEtat()

print("\n", e1.nom, " boit une potion")
e1.gagneVie(18)


print("\n deuxieme attaque")
p1.attaque(e1)
e1.afficheEtat()

print("\n", e1.nom, " boit une potion")
e1.gagneVie(18)

print(" \n troisieme attaque")
p1.attaque(e1)
e1.afficheEtat()

print("\n quatrieme attaque")
p1.attaque(e1)
e1.afficheEtat()

# Mouvement
p1.mouvement("rester")
p1.mouvement("fuir")

# Soins
p2 = Personnage("Gilles", "alliance", "humain", "mage",20, 20, 15, 15, 25, 55)# Allie n°1
p1.pv = p1.pv - 15
p2.soigne(p1, 20)
"""

