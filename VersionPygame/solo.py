from random import randint
from time import sleep
import pygame
from pygame.locals import *

class Pendu():

    def __init__(self):

        self.nbDeCoupsRestants = 7 #le nombre de coups restants
        self.lettreTappees = []
        self.lettreTappeesSTR = ""
        self.motAAfficher = []

    def creationListeDeMots(self,theme):
        self.themeChoisi = theme.capitalize()
        "Création de la liste des mots en fonction du theme en attribut"
        self.affichageComplet
        self.listeDeMots = []
        self.them_path=".\\" + theme + "\\"
        # Obtenir le path de index.csv
        theme_index="index.csv"
        fichier=self.them_path+ theme_index

        """ Phuong améliorer code
        if theme == "chiens":
            fichier = ".\\chiens\\index.csv"
        elif theme == "pays":
            fichier = ".\\pays\\index.csv"
        elif theme == "instruments":
            fichier = ".\\instruments\\index.csv"
        elif theme == "fruits":
            fichier = ".\\fruits\\index.csv"
        """
        with open(fichier, encoding='utf-8') as f : # Ouvrir le fichier index
            for ligne in f:
                ligne_recuperee = f.readline() # Obtenir la contente du fichier
                ligne_coupee = ligne_recuperee.split(";") #Coupe la ligne base de ";"


                mot = ligne_coupee[0] # Obtenir le mot
                #self.imageDeFin = ligne_coupee[1]
                #self.lienURL  = ligne_coupee[2]
                self.listeDeMots.append(mot) # Ajouter lo mot coupee à liste


    def selectionMot(self):
        "Tire un mot au hasard dans la liste listeDeMots"
        self.motATrouver = self.listeDeMots[randint(0,len(self.listeDeMots)-1)]

        return self.motATrouver

    def lettreJoueePresente(self,lettreJouee):
        "Vérifie si la lettre est présente dans le mot"


        if not lettreJouee in self.lettreTappees: # Vérifier si lettreJouee est été tappée
            self.lettreTappees.append(lettreJouee) # Ajouter lettreJouee à la liste dèja tapée
            self.lettreTappeesSTR += lettreJouee

            if lettreJouee in self.motATrouver: # Vérifier si lettreJouee exist dans le mot à trouver
                return True
            else: # Si lettreJouee n'exist pas dans le mot à trouver
                self.nbDeCoupsRestants -= 1 # Diminus le nombre de coups restants
                return False

    def partiePerdue(self):
        "Vérifie si perdu"
        if self.nbDeCoupsRestants <= 0: #Vérifier si il reste le coup à tapper
            return True
        else:
            return False

    def partieGagnee(self):
        "Vérifie si gagné"
        if "-" in self.motAAfficher: # vérifier si toutes les lettres sont trouvées
            return False
        else:
            return True

    def affichageMot(self):
        "Crée le mot a afficher avec des '-' si la lettre n'a pas été tentée"
        self.motAAfficher = []
        for lettreMot in self.motATrouver:
            if lettreMot in self.lettreTappees:
                self.motAAfficher.append(lettreMot)
            elif lettreMot == " " or lettreMot == "-":
                self.motAAfficher.append("   ")
            else:
                self.motAAfficher.append("-")

        # Convertir la liste de lettre jouee à chaine de caractères
        motEnStr = ""
        for lettre in self.motAAfficher:
            motEnStr += lettre

        self.motAAfficher = motEnStr
        print(self.motAAfficher)

        return self.motAAfficher

    def affichageComplet(self):
        print("Il reste",self.nbDeCoupsRestants,"coups")
        print("Lettre jouées :",self.lettreTappees)
        print(self.affichageMot())


def affichageClavier(posXClavier,posYClavier):
    #Affichage clavier sur la fenetre
    listeLettre = "AZERTYUIOPQSDFGHJKLMWXCVBN"

    # Difinir le nombre de lettre à affichager chaque ligne, 10 lettres par ligne
    for i in range(len(listeLettre)):
        lettre = listeLettre[i]
        if not lettre in jeu.lettreTappeesSTR:
            lettre  = police.render(lettre, 1, (66,66,66))
            if i <10:
                fenetre.blit(lettre , (posXClavier +i*50                              , posYClavier+ 0))
            elif i < 20:
                fenetre.blit(lettre , (posXClavier +i%10* tailleTouche                , posYClavier+ tailleTouche))
            else:
                fenetre.blit(lettre , (posXClavier +i%10* tailleTouche+2*tailleTouche , posYClavier+ 2*tailleTouche))


def clicToucheClavier(posXClavier,posYClavier,clicX,clicY,tailleTouche):
    #attraper un événement de clicher sur la clavier de la fenetre
    listeLettre = "AZERTYUIOPQSDFGHJKLM--WXCVBN--------------------------------"

    if clicX > posXClavier and clicY > posYClavier: # Vérifier si le joueur clique sur la clavier ou pas
        print(clicX, clicY)
        clicX = (clicX - posXClavier) // tailleTouche
        clicY = (clicY - posYClavier) // tailleTouche

        lettreCliquee = listeLettre[clicX + clicY*10]

        if lettreCliquee != "-": # Si lettre cliquée n'est pas "-"
            jeu.lettreJoueePresente(lettreCliquee)
            jeu.affichageComplet()


##  Programme Principal
pygame.init()

# Initial constants
th_chien="chiens"
th_fruit="fruits"
th_instrument="instruments"
th_pays="pays"

# Definir la police
police = pygame.font.SysFont("impact", 50)

# Definir la taille de la fenetre
fenetre = pygame.display.set_mode((1080,720))
jeu = Pendu()

#Gestion des fonds des différentes fenetres
fondTheme = pygame.image.load(".\\fond\\fondTheme.jpg")
fondJeu = pygame.image.load(".\\fond\\fondJeu.jpg")

#   Placement du clavier
posXClavier,posYClavier = 540,500
tailleTouche = 50
continuerChoixTheme = True
#   Fenetre choix du thème
##  Position sur la fenêtre
positionTexteChoix =    (380,20)
positionTexteChiens =   (450,150)
positionTexteFruits =   (460,250)
positionTexteInstru =   (410,350)
positionTextePays =     (470,450)


while continuerChoixTheme:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        #Gestion des appuis touche (+ conversion QWERTY => AZERTY)
        # Tapper la clavier d'ordinateur
        if event.type == KEYDOWN:
            carac= event.dict['unicode']
            if carac == '1' :
                jeu.creationListeDeMots(th_chien)
                continuerChoixTheme = False
            elif carac == '2':
                jeu.creationListeDeMots(th_fruit)
                continuerChoixTheme = False
            elif carac == '3':
                jeu.creationListeDeMots(th_instrument)
                continuerChoixTheme = False
            elif carac == '4':
                jeu.creationListeDeMots(th_pays)
                continuerChoixTheme = False

        # Cliquer la clavier sur la fenetre
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            clicX = event.pos[0]
            clicY = event.pos[1]

            if 450 < clicX < 620 and 150 < clicY < 200:
                jeu.creationListeDeMots(th_chien)
                continuerChoixTheme = False
            elif 460 < clicX < 610 and 250 < clicY < 300:
                jeu.creationListeDeMots(th_fruit)
                continuerChoixTheme = False
            elif 410 < clicX < 700 and 350 < clicY < 400:
                jeu.creationListeDeMots(th_instrument)
                continuerChoixTheme = False
            elif 470 < clicX < 600 and 450 < clicY < 500:
                jeu.creationListeDeMots(th_pays)
                continuerChoixTheme = False

            print(clicX)

    # afficher les themes
    texteChoix  = police.render("Choix du thème", 1, (255,0,255))
    texteChiens = police.render("1:Chiens", 1, (255,0,0))
    texteFruits = police.render("2:Fruits", 1, (255,0,0))
    texteInstru = police.render("3:Instruments", 1, (255,0,0))
    textePays   = police.render("4:Pays", 1, (255,0,0))

    fenetre.blit(fondTheme,(0,0))
    fenetre.blit(texteChoix , positionTexteChoix)
    fenetre.blit(texteChiens, positionTexteChiens)
    fenetre.blit(texteFruits, positionTexteFruits)
    fenetre.blit(texteInstru, positionTexteInstru)
    fenetre.blit(textePays  , positionTextePays)

    pygame.display.flip()

    sleep(0.2)


#   Fenetre de fin && programme principal
##  Position sur la fenêtre
positionImagePendu =    (0, 50)
positionThemeChoisi =   (720,120)
positionLettresTappees =(500,240)
positionAffichageMot =  (500,360)

# Appler le method à Prendre le mot Aléatoire
jeu.selectionMot()

# Appler le method à affichageComplet
jeu.affichageComplet()
lettreATester = list()
#BOUCLE DE JEU
continuerJeu = True
while continuerJeu :
    #Gestion des évenement (fermer et appui touche)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        #Gestion des appuis touche (+ conversion QWERTY => AZERTY)
        if event.type == KEYDOWN:
            carac= event.dict['unicode']
            carac = carac.upper() # Convertir la lettre à majuscul
            jeu.lettreJoueePresente(carac)


            #   S'éxécute uniquement quand j'appuie sur une touche
            jeu.affichageComplet()

        # Cliquer la clavier sur la fenetre
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            clicX = event.pos[0]
            clicY = event.pos[1]
            clicToucheClavier(posXClavier,posYClavier,clicX,clicY,tailleTouche)

    #Prendre le theme choisi
    themeChoisi = police.render(jeu.themeChoisi, 1, (255,255,255))
    #Prendre la lettre tapée
    lettreTap = police.render(str(jeu.lettreTappeesSTR), 1, (255,255,0))
    mot = police.render(jeu.motAAfficher, 1, (66,255,66))
    # afficher le fond de la fenetre
    fenetre.blit(fondJeu,(0,0))
    # afficher le theme
    fenetre.blit(themeChoisi,positionThemeChoisi)
    # afficher la lettre tapée
    fenetre.blit(lettreTap, positionLettresTappees)
    # afficher le mot
    fenetre.blit(mot, positionAffichageMot)


    #Affichage la Clavier
    affichageClavier(posXClavier,posYClavier)

    #Affichage ImagePendu
    lienImagePendu = ".\\images pendu\\{}.png".format(7-jeu.nbDeCoupsRestants)
    image = pygame.image.load(lienImagePendu)

    fenetre.blit(image, positionImagePendu)


    pygame.display.flip()

    # Afficher image en cas de perdu
    if jeu.nbDeCoupsRestants == 0:
        sleep(1)
        lienImagePendu = ".\\images pendu\\8.png"
        image = pygame.image.load(lienImagePendu)
        fenetre.blit(image, positionImagePendu)
        pygame.display.flip()
        sleep(1)
        lienImagePendu = ".\\images pendu\\9.png"
        image = pygame.image.load(lienImagePendu)
        fenetre.blit(image, positionImagePendu)
        pygame.display.flip()
        sleep(1.5)
    else:
        sleep(0.2)


    if jeu.partieGagnee() or jeu.partiePerdue() : continuerJeu = False



#   Fenetre de fin
##  Position sur la fenêtre
positionTexteDeFin = (400,500)
positionPhrase = (400,150)
positionMot = (400,250)

# Afficher la texte gagne/ perdu
continuerFin = True
while continuerFin:
    if jeu.partieGagnee():
        fenetre.fill(0x00FF00)
        texteDeFin = "GAGNE"

    if jeu.partiePerdue():
        fenetre.fill(0xFF0000)
        texteDeFin = "PERDU"

    for event in pygame.event.get():
        if event.type == QUIT:
            continuerFin = False


    # Afficher le mot
    phrase = police.render("Le mot était", 1, (255,0,255))
    mot = police.render(jeu.motATrouver, 1, (255,0,255))
    texteDeFin = police.render(texteDeFin, 1, (255,255,255))

    fenetre.blit(phrase, positionPhrase)
    fenetre.blit(mot, positionMot)
    fenetre.blit(texteDeFin, positionTexteDeFin)

    pygame.display.flip()
    sleep(0.5)

pygame.quit()







