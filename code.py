   # -*- coding: utf-8 -*-

# importation du module graphique 2D pygame
import pygame
# importation du module random
import random
# importation du module time
import time
# importation des modules couleur et graphics
from couleur import *
from graphics import *

# definition de quelques constantes
CASE = 20
L = 32
H = 24
WIDTH = L*CASE 
HEIGHT = H*CASE
SIZE = [WIDTH, HEIGHT]

MORTE = 0
VIVANTE = 1
TEMPS=0.5 										#Temps attente entre 2 rafraichissements en secondes

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
#            Programme Pour le Quadrillage                 #
#                                                          #
############################################################

"""Fonction Lignes Horizontal"""

def dessine_line_H(couleur):
    debut = [0,0]
    fin = [WIDTH, 0]
    while debut[1]<HEIGHT:
        debut[1] += CASE
        fin[1] = debut[1]
        pygame.draw.line(screen, couleur, debut, fin, 1)
    pygame.display.flip()
    
"""Fonction Lignes Verticale"""  
  
def dessine_line_V(couleur):
    debut = [0,0]
    fin = [0, HEIGHT]
    while debut[0]<WIDTH:
        debut[0] += CASE
        fin[0] = debut[0]
        pygame.draw.line(screen, couleur, debut, fin, 1)
    pygame.display.flip()

def dessine_quadrillage(couleur):
    dessine_line_H(couleur)
    dessine_line_V(couleur)

############################################################
#                                                          #
#         Initialisation des structures                    #
#                                                          #
############################################################    

def init_jeu():
    i = 0
    while i<H:
        # ajout d'une ligne i dans le tableau jeu
        jeu.append([])
        j = 0   
        while j<L:
            # ajout d'une colonne j contenant un 0 dans la ligne i
            jeu[i].append(MORTE)
            j +=1
        i +=1   
    
def init_voisin():
    i = 0
    while i<H:
        # ajout d'une ligne i dans le tableau jeu
        voisin.append([])
        j = 0   
        while j<L:
            # ajout d'une colonne j contenant un 0 dans la ligne i
            voisin[i].append(MORTE)
            j +=1
        i +=1  
############################################################
#                                                          #
#         Calcul de la generation                          #
#                                                          #
############################################################    

#def calcul_voisin():
    
#def calcul_jeu():

############################################################
#                                                          #
#         Programme pour la sélection de cellules          #
#                                                          #
############################################################    

def est_vide(clic):
    vide = MORTE
    case_clic =[clic[0]//CASE,clic[1]//CASE]
    if jeu[case_clic[1]][case_clic[0]] == 0 :
        return vide
    
    
    
############################################################
#                                                          #
#               Programme pour le Menu                     #
#                                                          #
############################################################

def affiche_bouton_texte(texte, rect, couleur):
    # dessin du fond coloré du bouton
    pygame.draw.rect(screen, couleur,op", [WIDTH//1.5, HEIGHT, WIDTH//3, -3*CASE], orange)
    pygame.display.flip() rect, 0)    
    # Initialisation de la fonte
    pygame.font.init()
    font = pygame.font.SysFont("verdana", 12, bold=False, italic=False)
    # Coordonnées du centre    
    centre = [rect[0]+rect[2]//2, rect[1]+rect[3]//2]
    # création de la surface contenant le texte
    text_area = font.render(texte, 1, noir)
    # taille de la surface contenant le texte
    text_size = font.size(texte)
    # position d'ancrage du coin en haut à gauche de la surface contenant 
    # le texte
    text_pos = [centre[0]-text_size[0]/2, centre[1]-text_size[1]/2]
    # ancrage de la surface contenant le texte dans la fenêtre
    screen.blit(text_area, text_pos)
    pygame.display.flip()  
    # desinitialisation de la fonte
    pygame.font.quit()


def affiche_menu_case():
    global WIDTH, HEIGHT, CASE
    affiche_bouton_texte("Lecture", [0, HEIGHT, WIDTH//3, -3*CASE], blanc)
    affiche_bouton_texte("Pause", [WIDTH//3, HEIGHT, WIDTH//3, -3*CASE], violet)
    affiche_bouton_texte("Stop", [WIDTH//1.5, HEIGHT, WIDTH//3, -3*CASE], orange)
    
############################################################
#                                                          #
#                  Programme Principal                     #
#                                                          #
############################################################

#Initialisation du module d'affichage pygame
pygame.display.init()

#creation et affichage de la fenetre graphique
screen = pygame.display.set_mode(SIZE)
pygame.display.flip()

#Dessin du Quadrillage
dessine_quadrillage(COULEUR_0)
affiche_menu_case()

#initialisation des case dans des tableaux
init_jeu()
init_voisin()

#Boucle principale
quitter = 0
while quitter == 0:
  
  '''attente d un clic'''
  clic = wait_clic()
  
  '''Verification de la case'''
  #Si la case cliqué est vide
  if est_vide(clic) == MORTE:
    print(MORTE)
	#Si la case cliqué est rempli/vivante
  else:
    print(VIVANTE)
  time.sleep(TEMPS)
  
wait_escape()
pygame.quit()

