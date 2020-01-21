from random import randint
from time import sleep
import pygame
from pygame.locals import *
pygame.init()
fenetre = pygame.display.set_mode((1080,720))
police = pygame.font.SysFont("impact", 40)

#Couleur de la fenetre
fenetre.fill((255,0,0))

posX,posY =100,250

listeLettre = "AZERTYUIOPQSDFGHJKLMWXCVBN"
for i in range(len(listeLettre)):
        lettre = listeLettre[i]
        lettre  = police.render(lettre, 1, (0,255,0))
        if i <10:
            fenetre.blit(lettre , (posX+i * 40,posY+0))
        elif i < 20:
            fenetre.blit(lettre , (posX+i%10 * 40,posY+40))
        else:
            fenetre.blit(lettre , (posX+i%10 * 40 + 80,posY+80))


"""
        A	Z	E	R	T	Y	U	I	O	P
        Q	S	D	F	G	H	J	K	L	M
		W	X	C	V	B	N


"""



pygame.display.flip()
sleep(3.0)
pygame.quit()
