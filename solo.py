from random import randint

class Pendu:

    def __init__(self):
        self.listeDeMots = ['MAISON','BATEAU','CHAMPIGNON']
        self.nbDeCoupsRestants = 7
        self.lettreTappees = []
        self.motAAfficher = []

    def selectionMot(self):
        self.motATrouver = self.listeDeMots[randint(0,len(self.listeDeMots)-1)]
        print(self.motATrouver)
        return self.motATrouver

    def lettreJoueePresente(self,lettreJouee):

        self.lettreTappees.append(lettreJouee)
        if lettreJouee in self.motATrouver:
            print("Il reste",self.nbDeCoupsRestants,"coups")
            print('-----------Lettre présente')
            return True
        else:
            print("Il reste",self.nbDeCoupsRestants,"coups")
            print('-----------Lettre absente')
            self.nbDeCoupsRestants -= 1
            return False

    def partiePerdue(self):
        if self.nbDeCoupsRestants <= 0:
            print("------------PERDU !!!")
            return True
        else:
            print('------------Pas perdu')
            return False

    def partieGagnee(self):
        if "-" in self.motAAfficher:
            print('-------------Pas gagner')
            return False
        else:
            print('-------------Gagner !')
            return True

    def afficheLettresTappees(self):
        print("Lettre tapées :",self.lettreTappees)

    def affichageMot(self):
        self.motAAfficher = []
        for lettreMot in self.motATrouver:
            if lettreMot in self.lettreTappees:
                self.motAAfficher.append(lettreMot)
            else:
                self.motAAfficher.append("-")

        print("mot",self.motAAfficher)
        return self.motAAfficher

jeu = Pendu()

jeu.selectionMot()

while not jeu.partiePerdue() or not jeu.partieGagnee():

    jeu.affichageMot()
    jeu.afficheLettresTappees()

    lettreATester = input("Quelle lettre ?").upper()
    jeu.lettreJoueePresente(lettreATester)
    jeu.partieGagnee()
    jeu.partiePerdue()