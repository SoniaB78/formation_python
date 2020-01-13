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
global liste_clientes

class Compte_Bancaire:
     # définition de la méthode spéciale __init__
    def __init__(self,nom,solde):
        self.nom=nom
        self.solde=solde

    # définition de la méthode spéciale __add__(surcharge de l'opérateur)
    def __add__(self,valeur):
        """ x.__add__(valeur) <=> x+ valeur
        crédite le compte de valeur de "valeur"
        """
        self.solde+=valeur
        print("Noueau solde: {:+.2f} € ".format(self.solde))

        return self

  # définition de la méthode spéciale __add__(surcharge de l'opérateur) #substract
    def __sub__(self,valeur):
        """ x.__add__(valeur) <=> x- valeur
        Débit le compte de valeur de "valeur"
        """
        self.solde-=valeur
        print("Noueau solde: {:+.2f} € ".format(self.solde))

        return self

    def Depot(self,valeur):
        self.solde+=valeur
        #return self.solde

    def Retrait(self,valeur):
        self.solde-=valeur
        #return self.solde

    def Affiche_Solde(self):
        print("Solde de client ", self.nom, "est",self.solde)

    def Register_Cliente(self,nom,solde):
        cliente=Compte_Bancaire(nom,solde)
        liste_clientes[cliente.nom]=cliente.solde
        return liste_clientes

    def Cherche_Cliente(self,nom):
        if cliente_nom in liste_clientes:
            return True
        else:
            return False


liste_clientes={}
for i in range(100):
    continu=input("Vous voulez register nouvelle cliente?")
    if continu.upper()=="OUI":
        nom=input("Saisi nom de client: ")
        solde=float(input("Saisi solde de client: "))
        cliente=Compte_Bancaire(nom,solde)
        liste_clientes[cliente.nom]=cliente.solde
    else:
        break

print(liste_clientes)
"""

action=input("Quelle est l'action que vous voulez faire? (1:Ajouter client/ 2: Déposer/3: Retrait) ")

if action=="1":
    self.


elif action=="2":
    cliente_nom=input("Saisi nom de cliente:")

    depose_valeur=float(input("Combien vous voulez déposer?"))
"""


