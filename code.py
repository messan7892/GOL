# -*- coding: utf-8 -*-

# importation du module graphique 2D pygame
import pygame
# importation du module random
import random
# importation des modules couleur et graphics
from couleur import *
from graphics import *

# definition de quelques constantes
CASE = 20
L = 16
H = 12
WIDTH = L*CASE 
HEIGHT = H*CASE
SIZE = [WIDTH, HEIGHT]

MORTE = 0
VIVANTE = 1
COULEUR_0 = gris
COULEUR_1 = rouge
COULEUR_2 = vert
COULEUR_3 = bleu
COULEUR_4 = jaune
COULEUR_5 = magenta
COULEUR_6 = cyan
COULEUR_7 = orange
COULEUR_8 = violet
COULEUR_VIDE = noir

# Variables globales
jeu = []
voisin = []







############################################################
#                                                          #
#                  Programme Principal                     #
#                                                          #
############################################################

#Initialisation du module d'affichage pygame
pygame.display.init()

#
screen = pygame.display.set_mode(SIZE)
pygame.display.flip()

