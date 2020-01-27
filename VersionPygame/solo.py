#------------------------------------IMPORTS------------------------------------
from random import randint
from time import sleep # pour l'animation
import pygame
from pygame.locals import *
import webbrowser # pour les liens


#-------------------------------------CLASS-------------------------------------
class Pendu():

    def __init__(self):

        self.nbDeCoupsRestants = 7 #le nombre de coups restants
        self.lettreTappees = [] # liste vide pour lettres tappées
        self.lettreTappeesSTR = "" # lettreTappeesSTR est défini comme étant string
        self.motAAfficher = [] # liste vide pour le mot à afficher

    def creationListeDeMots(self,theme):
        "CECI BLABLABLA"
        self.themeChoisi = theme.capitalize() # tansformation du theme en majuscule
        "Création de la liste des mots en fonction du theme en attribut"
        self.affichageComplet
        self.listeDeMots = []
        self.listeImage = []
        self.listeLien = []

        self.them_path="./" + theme + "/" # stockage du chemin
        # Obtenir le path de index.csv
        theme_index="index.csv" # fichier de stockage
        fichier=self.them_path+ theme_index #assemblage du chemin complet

        # Ouvrir le fichier index
        # open() à deux params => le fichier à lire et l'encodage
        # as f utilisation d'un alias
        with open(fichier, encoding='utf-8') as f :
            for ligne in f:
                ligne_recuperee = f.readline() # Obtenir le contenu du fichier
                ligne_coupee = ligne_recuperee.split(";") #Coupe la ligne base de ";"

                mot = ligne_coupee[0]# Obtenir le mot
                imageDeFin = ligne_coupee[1] # l'image est stocké dans la colonne n°2
                lienURL  = ligne_coupee[2] # le lien est stocké dans la colonne n°3
                self.listeDeMots.append(mot)# Ajouter le mot coupee à liste
                self.listeImage.append(imageDeFin) # .append ajoute à la liste l'élément
                self.listeLien.append(lienURL)

    # récupération aléatoire avec randint par indice
    def selectionMot(self):
        "Tire un mot au hasard dans la liste listeDeMots"
        tirageAuSort = randint(0,len(self.listeDeMots)-1)
        self.motATrouver = self.listeDeMots[tirageAuSort]
        self.imageAAfficherFin = self.listeImage[tirageAuSort]
        self.lienAAfficherFin = self.listeLien[tirageAuSort]

        # print du mot à trouver dans la console pour tricher
        print(self.motATrouver,self.imageAAfficherFin,self.lienAAfficherFin )

        return self.motATrouver,self.imageAAfficherFin,self.lienAAfficherFin

    # vérification de la présence de la lettre dans le mot récupéré
    def lettreJoueePresente(self,lettreJouee):
        "Vérifie si la lettre est présente dans le mot"
        lettreJouee = lettreJouee.upper() # mise en majuscule de la lettre pour compatibilité
        if lettreJouee in "AZERTYUIOPQSDFGHJKLMWXCVBN":
            print(lettreJouee)

            if not lettreJouee in self.lettreTappees: # Vérifier si lettreJouee est été tappée
                self.lettreTappees.append(lettreJouee) # Ajouter lettreJouee à la liste dèja tapée
                self.lettreTappeesSTR += lettreJouee # transformation de la lettre en string pour l'ajouter au mot

                if lettreJouee in self.motATrouver: # Vérifier si lettreJouee exist dans le mot à trouver
                    return True
                else: # Si lettreJouee n'exist pas dans le mot à trouver
                    self.nbDeCoupsRestants -= 1 # Diminus le nombre de coups restants
                    return False


    # Témoins pour vérifier si la patie est gagnée ou perdu, utilisé en page 4
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

    # Conversion du mot en - - - avec espaces
    def affichageMot(self):
        "Crée le mot a afficher avec des '-' si la lettre n'a pas été tentée"
        self.motAAfficher = []
        for lettreMot in self.motATrouver:
            if lettreMot in self.lettreTappees: # affiche la lettre
                self.motAAfficher.append(lettreMot)
            elif lettreMot == " " or lettreMot == "-": # affiche l'espace
                self.motAAfficher.append("   ")
            else:
                self.motAAfficher.append("-") # affiche le tiret

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

#-----------------------------------FONCTIONS-----------------------------------
def affichageClavier(posXClavier,posYClavier):
    #Affichage clavier sur la fenetre (position ( X, Y)
    listeLettre = "AZERTYUIOPQSDFGHJKLMWXCVBN"

    # Définit le nombre de lettre à afficher chaque ligne, 10 lettres par ligne
    for i in range(len(listeLettre)):
        lettre = listeLettre[i]
        if not lettre in jeu.lettreTappeesSTR:
            lettre  = police.render(lettre, 1, (66,66,66))
            if i <10: # affiche les 10 premiers characteres sur une ligne
                fenetre.blit(lettre , (posXClavier +i*50                              , posYClavier+ 0))
            elif i < 20: # affiche les 10 suivant characteres sur une deuxième ligne
                fenetre.blit(lettre , (posXClavier +i%10* tailleTouche                , posYClavier+ tailleTouche))
            else: # affiche les derniers charactères sur une ligne
                fenetre.blit(lettre , (posXClavier +i%10* tailleTouche+2*tailleTouche , posYClavier+ 2*tailleTouche))


def clicToucheClavier(posXClavier,posYClavier,clicX,clicY,tailleTouche):
    # attraper un événement de clic sur le clavier de la fenetre
    listeLettre = "AZERTYUIOPQSDFGHJKLM--WXCVBN--------------------------------"

    if clicX > posXClavier and clicY > posYClavier: # Vérifier si le joueur clique sur la clavier ou pas
        clicX = (clicX - posXClavier) // tailleTouche
        clicY = (clicY - posYClavier) // tailleTouche

        lettreCliquee = listeLettre[clicX + clicY*10] # assemble les coordonnées X et Y pour définir une aire de clic

        if lettreCliquee != "-": # Si lettre cliquée n'est pas "-"
            jeu.lettreJoueePresente(lettreCliquee) # utilisé dans la boucle de jeu
            jeu.affichageComplet()


##  ----------------------------PROGRAMME PRINCIPAL-----------------------------
pygame.init()

# Initial constants
th_chien="chiens"
th_fruit="fruits"
th_instrument="instruments"
th_pays="pays"

# Definir la police
police = pygame.font.SysFont("impact", 50)
police_lien = pygame.font.SysFont("impact", 30)

# Definir la taille de la fenetre
fenetre = pygame.display.set_mode((1080,720))

# Instanciation de la class Pendu
jeu = Pendu()

#Régler position du fond
positionFond= (0, 0) # (x, y)

#Gestion des fonds des différentes fenetres
fondRegle_img="./fond/fondRegles.jpg" # fenetre 1
fondTheme_img="./fond/fondTheme.jpg" # fenetre 2
fondJeu_img="./fond/fondJeu.jpg" # fenetre 3
titre_img="./fond/titre.jpg" # titre
regle_img="./fond/regle.jpg" # régle

fondRegle=pygame.image.load(fondRegle_img)
fondTheme = pygame.image.load(fondTheme_img)
fondJeu = pygame.image.load(fondJeu_img)
titre=pygame.image.load(titre_img)
regle=pygame.image.load(regle_img)

#Définir les boutons
fondBouQuitter_img = "./fond/bouQuitter.jpg"  # bouton quiter
fondBouRejeu_img = "./fond/bouRejeu.jpg"  # bouton re-jouer
fondBouJeu_img = "./fond/bouJeu.jpg"  # bouton jouer

#Ouvrir les images
fondBouQuitter = pygame.image.load(fondBouQuitter_img)
fondBouRejeu = pygame.image.load(fondBouRejeu_img)
fondBouJeu = pygame.image.load(fondBouJeu_img)


# -----------------------------Fenêtre règles-----------------------------------
# definir position
positionTitre=(600, 50)
positionRegle=(450,150)
positionBouJouer =(680,530)

contineurJouer=True

while contineurJouer:
    # récupère les évenements
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            clicX = event.pos[0]
            clicY = event.pos[1]

            # Cliquer bouton jouer
            if 680 < clicX < 830 and 530 < clicY < 600:
                contineurJouer=False

    # Afficher le fond de fenetre 1
    fenetre.blit(fondRegle,positionFond )

    # Afficher le titre
    titre = pygame.transform.scale(titre, (300, 100))
    fenetre.blit(titre, positionTitre)

    # Afficher les règles
    fenetre.blit(regle, positionRegle )

    #Afficher le bouton jouer
    fenetre.blit(fondBouJeu, positionBouJouer)
    pygame.display.flip() # rafraichit la page

    sleep(0.2)

rejouer=True

while rejouer:
    # Placement du clavier
    posXClavier,posYClavier = 540,500
    tailleTouche = 50
    continuerChoixTheme = True

    # Fenetre choix du thème
    ##  Position sur la fenêtre (x, y)
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
            # Affectation d'un chiffre à un theme 1 2 3 4
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
        texteChoix  = police.render("Choix du thème", 1, (52, 114, 162))
        texteChiens = police.render("1:Chiens", 1, (60,60,60))
        texteFruits = police.render("2:Fruits", 1, (60,60,60))
        texteInstru = police.render("3:Instruments", 1, (60,60,60))
        textePays   = police.render("4:Pays", 1, (60,60,60))

        fenetre.blit(fondTheme,positionFond)
        fenetre.blit(texteChoix , positionTexteChoix)
        fenetre.blit(texteChiens, positionTexteChiens)
        fenetre.blit(texteFruits, positionTexteFruits)
        fenetre.blit(texteInstru, positionTexteInstru)
        fenetre.blit(textePays  , positionTextePays)

        pygame.display.flip() # rafraichit la page

        sleep(0.2)


    #   Fenetre de fin && programme principal
    ##  Position sur la fenêtre
    positionImagePendu =    (0, 50)
    positionThemeChoisi =   (720,120)
    positionLettresTappees =(500,240)
    positionAffichageMot =  (500,360)

    jeu.__init__()
    # Appel de la method selectionMot qui renvoit un mot Aléatoire
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

                # S'éxécute uniquement quand j'appuie sur une touche
                jeu.affichageComplet()

            # Cliquer la clavier sur la fenetre
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicX = event.pos[0]
                clicY = event.pos[1]
                clicToucheClavier(posXClavier,posYClavier,clicX,clicY,tailleTouche)

        # Style theme choisi
        themeChoisi = police.render(jeu.themeChoisi, 1, (52, 114, 162))
        # Style lettre tapée
        lettreTap = police.render(str(jeu.lettreTappeesSTR), 1, (255, 207, 60))
        mot = police.render(jeu.motAAfficher, 1, (60,60,60))
        # afficher le fond de la fenetre
        fenetre.blit(fondJeu,positionFond)
        # afficher le theme
        fenetre.blit(themeChoisi,positionThemeChoisi)
        # afficher la lettre tapée
        fenetre.blit(lettreTap, positionLettresTappees)
        # afficher le mot
        fenetre.blit(mot, positionAffichageMot)

        #Affichage la Clavier
        affichageClavier(posXClavier,posYClavier)

        #Affichage ImagePendu
        lienImagePendu = "./images pendu/{}.png".format(7-jeu.nbDeCoupsRestants)
        image = pygame.image.load(lienImagePendu)

        fenetre.blit(image, positionImagePendu)

        pygame.display.flip() # rafraichit la page

        # Afficher image en cas de perdu
        if jeu.nbDeCoupsRestants == 0:
            sleep(1)
            lienImagePendu = "./images pendu/8.png"
            image = pygame.image.load(lienImagePendu)
            fenetre.blit(image, positionImagePendu)
            pygame.display.flip() # rafraichit la page
            sleep(1)
            lienImagePendu = "./images pendu/9.png"
            image = pygame.image.load(lienImagePendu)
            fenetre.blit(image, positionImagePendu)
            pygame.display.flip() # rafraichit la page
            sleep(1.5)
        else:
            sleep(0.2)

        if jeu.partieGagnee() or jeu.partiePerdue() : continuerJeu = False


    #   Fenetre de fin
    ##  Position sur la fenêtre
    positionTexteDeFin =  (475,50)
    positionPhrase = (100,150)
    positionMot = (100,250)
    positionlien = (100,520)
    positionImageDeFin = (590,150)
    positionBouRejouer=(290,600)
    positionBouQuitter=(640,600)

    imageDeFin = "{}/{}".format(jeu.themeChoisi,jeu.imageAAfficherFin)
    imageDeFin = pygame.image.load(imageDeFin)

    # Afficher la texte gagne/ perdu
    continuerFin = True
    while continuerFin:
        if jeu.partieGagnee():
            fenetre.fill(0xF5F7E9)
            texteDeFin = "GAGNE !"

        if jeu.partiePerdue():
            fenetre.fill(0xF5F7E9)
            texteDeFin = "PERDU !"

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()


            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                clicX = event.pos[0]
                clicY = event.pos[1]

                #Cliquer bouton QUITTER
                if 640 < clicX < 790 and 600 < clicY < 670:
                    pygame.quit()
                    rejouer = False
                    print(clicX,clicY)

                # Cliquer bouton rejouer
                if 290 < clicX < 440 and 600 < clicY < 670:
                    continuerChoixTheme=True
                    continuerFin = False
                    print(clicX,clicY)

                # Cliquer le lien
                if 100 < clicX < 1000 and 520 < clicY < 570:
                    webbrowser.open(jeu.lienAAfficherFin) # Ouvrir le lien
                    print(clicX,clicY)

        # Afficher le mot
        phrase = police.render("Le mot était :", 1, (60,60,60))
        mot = police.render(jeu.motATrouver, 1, (255, 207, 60))
        lien= police_lien.render(jeu.lienAAfficherFin , 1, (52, 114, 162))
        texteDeFin = police.render(texteDeFin, 1, (52, 114, 162))

        # commande pour formater l'image en 350x350
        imageDeFin = pygame.transform.scale(imageDeFin, (350, 350))
        # Aficher image
        fenetre.blit(imageDeFin,positionImageDeFin)

        # Afficher les textes
        fenetre.blit(phrase, positionPhrase)
        fenetre.blit(mot, positionMot)
        fenetre.blit(lien, positionlien)
        fenetre.blit(texteDeFin, positionTexteDeFin)

        #Afficher le bouton jouer
        fenetre.blit(fondBouRejeu, positionBouRejouer)

        #Afficher le bouton quitter
        fenetre.blit(fondBouQuitter, positionBouQuitter)

        pygame.display.flip()
        sleep(0.5)

pygame.quit()
