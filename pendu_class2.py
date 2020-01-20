#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      haya_
#
# Created:     10/01/2020
# Copyright:   (c) haya_ 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
import pandas as pd
import numpy as np
from random import randint

data=pd.read_csv("fruits.csv",sep=";")#tableau on met ; car les colonnes sont sont separées par ;

from PIL import Image





class Jeu():

    global lettre_trouve
    global s
    global erreur
    global window
    global root2

    global photo_selectionner
    photo_selectionner=0

    lettre_trouve=0
    s=0
    erreur=0


    def __init__(self,data):

        window=Tk()
        window.config(background="black")
        window.geometry("700x700")
        window.minsize(700,700)
        frame2=Frame(window,height=20,width=20)
        frame2.pack(side=TOP,expand=YES)
        frame=Frame(window,bg="black",height=10,width=10)

        frame55=Frame(window,height=20,width=20,bg="black")
        frame55.pack(side=BOTTOM,expand=YES)


        frame.pack(expand=YES)




        self.photo0=PhotoImage(file='0.png').subsample(3)


        self.photo11=PhotoImage(file='2.png').subsample(3)
        self.photo22=PhotoImage(file='4.png').subsample(3)
        self.photo33=PhotoImage(file='6.png').subsample(3)
        self.photo44=PhotoImage(file='8.png').subsample(3)
        self.photo55=PhotoImage(file='9.png').subsample(3)

        self.A=Button(frame,text="A",fg="white",bg="black",padx=10,pady=10,command=lambda:self.lettre("A",self.A,self.frame2))

        self.Z=Button(frame,text="Z",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("Z",self.Z,self.frame2))
        self.E=Button(frame,text="E",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("E",self.E,self.frame2))
        self.R=Button(frame,text="R",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("R",self.R,self.frame2))
        self.T=Button(frame,text="T",fg="white",bg="black",padx=10,pady=10,command=lambda:self.lettre("T",self.T,self.frame2))
        self.Y=Button(frame,text="Y",fg="white",bg="black",padx=10,pady=10,command=lambda:self.lettre("Y",self.Y,self.frame2))
        self.U=Button(frame,text="U",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("U",self.U,self.frame2))
        self.I=Button(frame,text="I",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("I",self.I,self.frame2))
        self.O=Button(frame,text="O",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("O",self.O,self.frame2))
        self.P=Button(frame,text="P",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("P",self.P,self.frame2))
        self.Q=Button(frame,text="Q",fg="white",bg="black",padx=10,pady=10,command=lambda:self.lettre("Q",self.Q,self.frame2))
        self.S=Button(frame,text="S",fg="white",bg="black",padx=10,pady=10,command=lambda:self.lettre("S",self.S,self.frame2))
        self.D=Button(frame,text="D",fg="white",bg="black",padx=10,pady=10,command=lambda:self.lettre("D",self.D,self.frame2))
        self.F=Button(frame,text="F",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("F",self.F,self.frame2))
        self.G=Button(frame,text="G",fg="white",bg="black",padx=10,pady=10,command=lambda:self.lettre("G",self.G,self.frame2))
        self.H=Button(frame,text="H",fg="white",bg="black",padx=10,pady=10,command=lambda:self.lettre("H",self.H,self.frame2))
        self.J=Button(frame,text="J",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("J",self.J,self.frame2))
        self.K=Button(frame,text="K",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("K",self.K,self.frame2))
        self.L=Button(frame,text="L",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("L",self.L,self.frame2))
        self.M=Button(frame,text="M",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("M",self.M,self.frame2))
        self.W=Button(frame,text="W",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("W",self.W,self.frame2))
        self.X=Button(frame,text="X",fg="white",bg="black",padx=10,pady=10,command=lambda:self.lettre("X",self.X,self.frame2))
        self.C=Button(frame,text="C",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("C",self.C,self.frame2))
        self.V=Button(frame,text="V",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("V",self.V,self.frame2))
        self.B=Button(frame,text="B",bg="black",fg="white",padx=10,pady=10,command=lambda:self.lettre("B",self.B,self.frame2))
        self.N=Button(frame,text="N",fg="white",bg="black",padx=10,pady=10,command=lambda:self.lettre("N",self.N,self.frame2))
        self.espace=Button(frame,text="espace",fg="white",bg="black",padx=14,pady=10)#juste pour faire beau




        self.A.grid(column=0,row=0)
        self.Z.grid(column=1,row=0)
        self.E.grid(column=2,row=0)
        self.R.grid(column=3,row=0)
        self.T.grid(column=4,row=0)
        self.Y.grid(column=5,row=0)
        self.U.grid(column=6,row=0)
        self.I.grid(column=7,row=0)
        self.O.grid(column=8,row=0)
        self.P.grid(column=9,row=0)
        self.Q.grid(column=0,row=1)
        self.S.grid(column=1,row=1)
        self.D.grid(column=2,row=1)
        self.F.grid(column=3,row=1)
        self.G.grid(column=4,row=1)
        self.H.grid(column=5,row=1)
        self.J.grid(column=6,row=1)

        self.K.grid(column=7,row=1)
        self.L.grid(column=8,row=1)
        self.M.grid(column=9,row=1)

        self.W.grid(column=0,row=2)
        self.X.grid(column=1,row=2)
        self.C.grid(column=2,row=2)
        self.V.grid(column=3,row=2)
        self.B.grid(column=4,row=2)
        self.N.grid(column=5,row=2)
        self.espace.grid(column=6,row=2,columnspan=2)


        self.data=data
        self.mot='aaa'
        self.c="A"
        self.window=window
        self.frame2=frame2
        self.frame55=frame55





    def choix_mot(self):
        """choix du mots"""
        a=randint(0,data.shape[0]-1)
        self.mot=self.data.iloc[a,0]
        return self.mot

    def longueur_mot(self):
        espace=0

        for i,t in enumerate (self.mot):
            if t==" ":

                espace=espace+1
            longueur_mot=len(self.mot)-espace
        return(longueur_mot)




    def changer_image(self):



        global photo_selectionner

        if photo_selectionner == 0:
            photo_selectionner = self.photo11
        elif photo_selectionner == self.photo11:
            photo_selectionner = self.photo22
        elif  photo_selectionner == self.photo22:
            photo_selectionner = self.photo33
        elif photo_selectionner == self.photo33:
            photo_selectionner = self.photo44
        elif photo_selectionner == self.photo55:
            photo_selectionner = self.photo55



    def quitter(self):
        self.window.destroy()


    def changer_image2(self):
        self.window.after(50, self.changer_image())



    def envoi(self):


        root2=Toplevel()
        root2.geometry("600x300")

        root2.title("choix du thème")


        photo = PhotoImage(file='chiens.png')

        photo3= PhotoImage(file='fruits2.png')
        photo4= PhotoImage(file='ferme2.png')
        photo5= PhotoImage(file='pays2.png')
        button = Button(root2, image=photo)
        button.grid(row=1,column=0)
        button = Button(root2, image=photo3)
        button.grid(row=1,column=1)
        button = Button(root2, image=photo4)
        button.grid(row=0,column=0)
        button = Button(root2, image=photo5)
        button.grid(row=0,column=1)

        root2.mainloop()






    def lettre(self,c,bouton,root2):



        global lettre_trouve

        global erreur
        global photo_selectionner

        mot=self.mot.upper()

        s=0
        for t,i in enumerate(mot):

            if c in i:

                e=Entry(self.frame2,bg="black",fg="red",width=3,bd=0,font=('Helveticia', '12', 'bold'))

                e.grid(row=200,column=t)
                e.delete(0,END)
                e.insert(0,c)

                lettre_trouve=lettre_trouve+1


                bouton.destroy()
            else:


                s=s+1
                if s==len(mot):

                    erreur=erreur+1
                    if erreur==1 :



                        canvas=Canvas(self.frame55,width=200,height=200,bg="black",bd=0,highlightthickness=0)
                        canvas.create_image(100,100,image=self.photo11)
                        id_im=canvas.grid(row=0,column=0)
                        canvas.itemconfig(id_im, image=photo_selectionner)
                        self.changer_image2()

                    if erreur==2:
                        photo_selectionner=self.photo11
                        canvas=Canvas(self.frame55,width=200,height=200,bg="black",bd=0,highlightthickness=0)
                        canvas.create_image(100,100,image=self.photo22)
                        id_im=canvas.grid(row=0,column=0)
                        canvas.itemconfig(id_im, image=photo_selectionner)
                        self.changer_image2()
                    if erreur==3:
                        photo_selectionner=self.photo22
                        canvas=Canvas(self.frame55,width=200,height=200,bg="black",bd=0,highlightthickness=0)
                        canvas.create_image(100,100,image=self.photo33)
                        id_im=canvas.grid(row=0,column=0)
                        canvas.itemconfig(id_im, image=photo_selectionner)
                        self.changer_image2()
                    if erreur==4:
                        photo_selectionner=self.photo33
                        canvas=Canvas(self.frame55,width=200,height=200,bg="black",bd=0,highlightthickness=0)
                        canvas.create_image(100,100,image=self.photo44)
                        id_im=canvas.grid(row=0,column=0)
                        canvas.itemconfig(id_im, image=photo_selectionner)
                        self.changer_image2()
                    if erreur==5:
                        photo_selectionner=self.photo44
                        canvas=Canvas(self.frame55,width=200,height=200,bg="black",bd=0,highlightthickness=0)
                        canvas.create_image(100,100,image=self.photo55)
                        id_im=canvas.grid(row=0,column=0)
                        canvas.itemconfig(id_im, image=photo_selectionner)
                        self.changer_image2()

                bouton.destroy()





        if lettre_trouve==self.longueur_mot():

            root=Toplevel()
            root.config(background="black")
            root.geometry("800x800")



            frame5=Frame(root,bg="black")
            frame5.pack(side=TOP)
            Label2=Label(frame5,text="Super, le mot est ",font=('Times', '40', 'bold italic'),bg="black" ,fg="blue")
            Label3=Label(frame5,text=self.mot,font=('Times', '40', 'bold '),bg="black" ,fg="white")
            Label2.grid(row=0,column=0)
            Label3.grid(row=1,column=0)
            photo5= PhotoImage(file="{}.png".format(mot)).subsample(3)
            canvas=Canvas(frame5,width=200,height=200,bg="black",bd=0,highlightthickness=0)
            canvas.create_image(100,100,image=photo5)
            canvas.grid(row=2,column=0)
            photo4= PhotoImage(file='bravo.png').subsample(2)

            canvas=Canvas(frame5,width=200,height=200,bg="black",bd=0,highlightthickness=0)
            canvas.create_image(100,100,image=photo4)
            canvas.grid(row=5,column=0)
            titre=Label(frame5,text="Bravo tu as gagné!!!",font=("Helveticia",25,'bold italic'),bg="black",fg="red")
            titre.grid(row=6,column=0)
            bouton7=Button(root,text="Quitter",font=("Times","20","bold"),overrelief=RIDGE,bg="blue",fg="white",command=lambda:self.quitter())
            bouton7.pack(side=RIGHT)
            bouton2=Button(root,text="Rejouer",font=("Times","20","bold"),overrelief=RIDGE,bg="blue",fg="white",command=lambda:self.envoi())
            bouton2.pack(side=LEFT)



            root.mainloop()








        if erreur>4:

            root=Toplevel()

            root.config(background="black")
            root.geometry("800x800")



            frame5=Frame(root,bg="black")
            frame5.pack(side=TOP)
            Label2=Label(frame5,text="Pfff, le mot était ",font=('Times', '40', 'bold italic'),bg="black" ,fg="blue")
            Label3=Label(frame5,text=self.mot,font=('Times', '40', 'bold '),bg="black" ,fg="white")
            Label2.grid(row=0,column=0)
            Label3.grid(row=1,column=0)
            photo5= PhotoImage(file="{}.png".format(self.mot)).subsample(3)
            canvas=Canvas(frame5,width=200,height=200,bg="black",bd=0,highlightthickness=0)
            canvas.create_image(100,100,image=photo5)
            canvas.grid(row=2,column=0)
            photo4= PhotoImage(file='bidon2.png').subsample(2)

            canvas=Canvas(frame5,width=200,height=200,bg="black",bd=0,highlightthickness=0)
            canvas.create_image(100,100,image=photo4)
            canvas.grid(row=5,column=0)
            titre=Label(frame5,text="Gros Nazzzz!!!",font=("Helveticia",25,'bold italic'),bg="black",fg="red")
            titre.grid(row=6,column=0)


            bouton7=Button(root,text="Quitter",font=("Times","20","bold"),overrelief=RIDGE,bg="blue",fg="white",command=lambda:self.quitter())
            bouton7.pack(side=RIGHT)
            bouton2=Button(root,text="Rejouer",font=("Times","20","bold"),overrelief=RIDGE,bg="blue",fg="white",command=lambda:self.envoi())
            bouton2.pack(side=LEFT)


            root.mainloop()





    def tiret(self) :


        espace=0
        mot=self.mot.upper()
        for i,t in enumerate (mot):
            if t==" ":
                label=Label(self.frame2,text='          ',bg='black',fg='white')
                label.grid(row=200,column=i)
                espace=espace+1

            else:


                label=Label(self.frame2,text='____',bg='black',fg='white')
                label.grid(row=200,column=i)
        longueur_mot=len(mot)-espace









        self.window.mainloop()













Jeu=Jeu(data)
mot=Jeu.choix_mot()
print(mot)
Jeu.tiret()