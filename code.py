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
L = 15
H = 10
WIDTH = L*CASE 
HEIGHT = H*CASE
SIZE = [(WIDTH+5*CASE), (HEIGHT+3*CASE)]

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
population = 0
periode = 0
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

def affiche_jeu_console():
    print("jeu :")    
    # parcours des lignes du tableau jeu
    i = 0
    while i<H:
        # parcours des colonnes du tableau jeu
        j = 0
        while j<L:
            print('{:>2}'.format(jeu[i][j]), end=" ")
            j +=1
        print("\n")
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
        
def affiche_voisin_console():
    print("voisin = ")    
    # parcours des lignes du tableau jeu
    i = 0
    while i<H:
        # parcours des colonnes du tableau jeu
        j = 0
        while j<L:
            print('{:>2}'.format(voisin[i][j]), end=" ")
            j +=1
        print("\n")
        i +=1
        
def affichage_population_depart():
    
    pygame.font.init()
    font = pygame.font.SysFont("verdana" , 15)
    afficher = font.render("Population :", 1, blanc)
    screen.blit(afficher,(WIDTH, CASE//2))  
    pygame.draw.rect(screen, noir, [WIDTH+1,2*CASE+1,WIDTH+5*CASE,4*CASE])
    
    pygame.font.init()
    font = pygame.font.SysFont("verdana" , 22)
    afficher = font.render(str(population), 1, blanc)
    screen.blit(afficher,(WIDTH+2*CASE, 2*CASE))
    
    pygame.font.init()
    font = pygame.font.SysFont("verdana" , 15)
    afficher = font.render("Période(s) :", 1, blanc)
    screen.blit(afficher,(WIDTH, 4*CASE))
    
############################################################
#                                                          #
#         Calcul de la generation                          #
#                                                          #
############################################################    

def calcul_voisin():
    # parcours des lignes    
    i = 0    
    while i<H :
        # parcours des colonnes
        j = 0
        while j<L :
            voisin_case = 0
            
                    
            #coin haut gauche
            if i == 0 and j==0 :
                voisin_case = jeu[1][0] + jeu[0][1] + jeu[1][1]
    
            #coin haut droit
            elif i == 0 and j== L-1 :
                voisin_case = jeu[0][L-2] + jeu[1][L-2] + jeu[1][L-1]
    

            #coin bas gauche
            elif i == H-1 and j == 0 :
                voisin_case = jeu[H-2][0] + jeu[H-2][1] + jeu[H-1][1]

 
            #coin bas droit
            elif i == H-1 and j == L-1 :
                voisin_case = jeu[H-2][L-2] + jeu[H-2][L-1] + jeu[H-1][L-2]
            
            # bord haut
            elif i==0:
                voisin_case = jeu[0][j-1] + jeu[0][j+1] + jeu[1][j-1] + jeu[1][j] + jeu[1][j+1]
            # bord bas
            elif i == H-1:
                voisin_case = jeu[H-2][j-1] + jeu[H-2][j] + jeu[H-2][j+1] + jeu[H-1][j-1] + jeu[H-1][j+1]

            #bord gauche
            elif j == 0:
                voisin_case = jeu[i-1][0] + jeu[i-1][1] + jeu[i][1] + jeu[i+1][0] + jeu[i+1][1]

            #bord droit
            elif j == L-1:
                voisin_case = jeu[i-1][L-2] + jeu[i-1][L-1] + jeu[i][L-2] + jeu[i+1][L-2] + jeu[i+1][L-1]

            #reste des cases
            else :
                voisin_case = jeu[i-1][j-1]+jeu[i-1][j]+jeu[i-1][j+1]+jeu[i][j-1]+jeu[i][j+1]+jeu[i+1][j-1]+jeu[i+1][j]+jeu[i+1][j+1]
            voisin[i][j]=voisin_case
            j+=1
        i+=1

def calcul_jeu():
    i = 0
    # parcours des lignes
    while i<H :
        # parcours des colonnes
        j = 0
        while j<L :
          # Attribution des variables 1 ou 0 en fonction des lois du jeu
            if voisin[i][j] <= 1 or voisin[i][j] >= 4:
                jeu[i][j] = 0
            elif voisin[i][j] == 3:
                jeu[i][j] = 1
            j += 1
        i += 1
        
def calcul_population_totale():
    population = 0    
    i = 0
    # parcours des lignes
    while i<H :
        # parcours des colonnes
        j = 0
        while j<L :
          # Attribution des variables 1 ou 0 en fonction des lois du jeu
            if jeu[i][j] == 1 :
                population += 1
            else:
                population +=0
            j += 1
        i += 1
    pygame.draw.rect(screen, noir, [WIDTH+1,2*CASE+1,WIDTH+5*CASE,2*CASE])
    pygame.display.flip()
    pygame.font.init()
    font = pygame.font.SysFont("verdana" , 22)
    afficher = font.render(str(population), 1, blanc)
    screen.blit(afficher,(WIDTH+2*CASE, 2*CASE))
    
def Affichage_periode():
    
    pygame.draw.rect(screen, noir, [WIDTH+1,5*CASE+1,WIDTH+5*CASE,7*CASE])
    pygame.display.flip()
    pygame.font.init()
    font = pygame.font.SysFont("verdana" , 22)
    afficher = font.render(str(periode), 1, blanc)
    screen.blit(afficher,(WIDTH+2*CASE, 5.5*CASE))
############################################################
#                                                          #
#         Programme pour la sélection de cellules          #
#                                                          #
############################################################    

def est_vide(clic):
  # Vérification de l'état de la cellule clické
    case_clic =[clic[0]//CASE,clic[1]//CASE]
    if jeu[case_clic[1]][case_clic[0]] == 0 :
        return MORTE
    else:
        return VIVANTE
    
    
    
############################################################
#                                                          #
#               Programme pour le Menu                     #
#                                                          #
############################################################

def affiche_bouton_texte(texte, rect, couleur):
    # dessin du fond coloré du bouton
    pygame.draw.rect(screen, couleur, rect, 0)   
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
    affiche_bouton_texte("Lecture", [0, HEIGHT, WIDTH//3, 3*CASE], blanc)
    affiche_bouton_texte("Pause", [WIDTH//3, HEIGHT, WIDTH//3, 3*CASE], violet)
    affiche_bouton_texte("Stop", [WIDTH//1.5, HEIGHT, WIDTH//3, 3*CASE], orange)
    
    
    
############################################################
#                                                          #
#          Programme pour remplir les cellules             #
#                                                          #
############################################################


def remplir_case_clic(clic):
  # Dessiné un cercle de couleur si une case vide est cliqué au début
    if jeu[i][j] == 1:
        centre = [((clic[0]//CASE)*CASE+CASE//2),((clic[1]//CASE)*CASE+CASE//2)]
        pygame.draw.circle(screen, COULEUR_6, centre, CASE//2-1)
        
  # Déssiné un rond noir par dessus le rond de couleur pour remettre une cellule à l'état initial en cliquant
    else:
        centre = [((clic[0]//CASE)*CASE+CASE//2),((clic[1]//CASE)*CASE+CASE//2)]
        pygame.draw.circle(screen, COULEUR_VIDE, centre, CASE//2-1)
        
        
def remplir_case():
    #parcours des lignes
    i = 0    
    while i<H :
        # parcours des colonnes
        j = 0
        while j<L :
          # Mettre à jour les cases avec des ronds de couleurs pour les cellules vivantes
            if jeu[i][j] == VIVANTE:
                centre = [((j*CASE)+(CASE//2)),((i*CASE)+(CASE//2))]
                pygame.draw.circle(screen, COULEUR_6, centre, CASE//2-1)
                
          # Et inversement
            else:
                centre = [((j*CASE)+(CASE//2)),((i*CASE)+(CASE//2))]
                pygame.draw.circle(screen, COULEUR_VIDE, centre, CASE//2-1)
                
            j += 1
        i += 1    
        
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
affichage_population_depart()
#initialisation des case dans des tableaux
init_jeu()
affiche_jeu_console()
init_voisin()
affiche_voisin_console()
#Boucle principale

lecture = 0
while quitter != 0:
    if lecture == 0:
        while lecture == 0:
            clic = wait_clic()
            #Si la case cliqué est vide
            if clic[1] < HEIGHT :
                if est_vide(clic) == MORTE:
                    j = clic[0]//CASE
                    i = clic[1]//CASE
                    jeu[i][j] = VIVANTE
                    remplir_case_clic(clic)
                    population += 1
                    affichage_population_depart()
                    pygame.display.flip()
                #Si la case cliqué est rempli/vivante
                elif est_vide(clic) == VIVANTE :
                    j = clic[0]//CASE
                    i = clic[1]//CASE
                    jeu[i][j] = MORTE
                    remplir_case_clic(clic)
                    population -= 1
                    affichage_population_depart()
                    pygame.display.flip()
                # Si le clic intervient en dehors du jeu, soit sur le menu
            elif clic[1] > HEIGHT :
                # Si le clic est pour lancé le programme
                if clic[0] < (WIDTH//3):
                   lecture = 1
                # Si le clic est pour mettre en pause le programme
                elif clic[0] > (WIDTH//3) and clic[0] < (WIDTH//1.5):
                   lecture = 0
                # Si le clic est pour arréter le programme 
                elif clic[0] > (WIDTH//1.5):
                   pygame.quit()
                """affiche_jeu_console()
                calcul_voisin()
                affiche_voisin_console()"""
    periode += 1        
    time.sleep(TEMPS)
    print("***")
    affiche_jeu_console()
    calcul_voisin()
    affiche_voisin_console()
    calcul_jeu()
    calcul_population_totale()
    Affichage_periode()
    affiche_jeu_console()
    remplir_case()
    pygame.display.flip()
    for event in pygame.event.get():
        
        if event.type == KEYDOWN:
            lecture = 1
        else:
            print("Clic non actifs")
  
wait_escape()
pygame.quit()
