#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      python
#
# Created:     18/12/2019
# Copyright:   (c) python 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# coding: UTF-8
from random import randint
from tkinter import *
from PIL import ImageTk, Image


def creation_fenetre():
    fenetre = Tk()
    fenetre.title("PENDU")
    fenetre.geometry("1024x720")
    fenetre.resizable(width=False, height=False)
    return fenetre


def affichage_fenetre(lien):
    #Création d'un canvas

    canvas = Canvas(fenetre, width=474, height=248)
    canvas.pack()
    #Charger image
    im = Image.open(lien)
    canvas.image = ImageTk.PhotoImage(im)
    #Coller image sur canvas
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')
    Bouton = Button(fenetre, text = 'Recharger', command = lambda :reload(i))
    Bouton.pack()
    fenetre.mainloop()

def reload(numImg):

    print(numImg)
    affichage_fenetre("{}.png".format(numImg))

fenetre = creation_fenetre()
affichage_fenetre("{}.png".format(0))
