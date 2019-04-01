# -*- coding: utf-8 -*-

# importation du module graphique 2D pygame
import pygame

# importation du module couleur et graphics
from couleur import *
from graphics import *

# Paramètres de la taille du jeu
N = 6
CASE = 100
WIDTH = N*CASE
HEIGHT = N*CASE

# Constantes du jeu
JOUEUR_1 = 1
JOUEUR_2 = -1
NON_JOUEE = 0

COULEUR_CROIX = jaune
COULEUR_CERCLE = cyan
COULEUR_GRILLE = magenta

# Variables du jeu
a_qui_de_jouer = JOUEUR_1
jeu = []

""" --------------------------------------------------------------------------- 
    Partie 1 - AFFICHAGE DE LA GRILLE
--------------------------------------------------------------------------- """

def dessine_quadrillage(couleur):
    dessine_ligne_h(couleur)
    dessine_ligne_v(couleur)
    pygame.display.flip()

#dessine les lignes puis les colonnes
    
def dessine_ligne_h(couleur):
    debut=[0,0]
    fin=[WIDTH,0]
    while debut[1] < HEIGHT:
        debut[1] += CASE
        fin[1]=debut[1]
        pygame.draw.line(screen,couleur,debut,fin,1)

def dessine_ligne_v(couleur):
    debut=[0,0]
    fin=[0,HEIGHT]
    while debut[0] < WIDTH:
        debut[0] += CASE
        fin[0]=debut[0]
        pygame.draw.line(screen,couleur,debut,fin,1)

""" --------------------------------------------------------------------------- 
    Partie 2 - AFFICHAGE DES CROIX ET CERCLES SELON LE JOUEUR
--------------------------------------------------------------------------- """

    
def trouve_centre(clic):
    centre = [0,0]
    centre[0]=(clic[0]//CASE)*CASE+CASE//2
    centre[1]=(clic[1]//CASE)*CASE+CASE//2
    return centre    

#Fonctions pour dessiner les croix et les cercles
def dessine_croix(clic):
    centre = trouve_centre(clic)
    a1=[centre[0]-CASE//2, centre[1]-CASE//2]
    a2=[centre[0]+CASE//2, centre[1]-CASE//2]
    b1=[centre[0]-CASE//2, centre[1]+CASE//2]
    b2=[centre[0]+CASE//2, centre[1]+CASE//2]
    pygame.draw.line(screen,COULEUR_CROIX,a1,b2,1)
    pygame.draw.line(screen,COULEUR_CROIX,a2,b1,1)
    pygame.display.flip()

def dessine_cercle(clic):
    centre = trouve_centre(clic)
    pygame.draw.circle(screen,COULEUR_CERCLE, centre,CASE//2,1)
    pygame.display.flip()

def dessine_action(clic):
    centre=trouve_centre(clic)
    if a_qui_de_jouer == JOUEUR_1:
        dessine_croix(clic)
    else:
        dessine_cercle(clic)
    
    
""" --------------------------------------------------------------------------- 
    Partie 3 - VALIDATION ET SAUVEGARDE DES COUPS JOUES
--------------------------------------------------------------------------- """

# *****************************************************************************
# Fonction qui initialise le tableau jeu avec des cases non jouées (des 0)
# *****************************************************************************

def init_jeu():
    i = 0
    while i<N:
        # ajout d'une ligne i dans le tableau jeu
        jeu.append([])
        j = 0   
        while j<N:
            # ajout d'une colonne j contenant un 0 dans la ligne i
            jeu[i].append(NON_JOUEE)
            j +=1
        i +=1   

# *****************************************************************************
# Fonction qui affiche le tableau jeu dans la console
# *****************************************************************************
  
def affiche_jeu_console():
    # parcours des lignes du tableau jeu
    i = 0
    while i<N:
        # parcours des colonnes du tableau jeu
        j = 0
        while j<N:
            print('{:>2}'.format(jeu[i][j]), end=" ")
            j +=1
        print("\n")
        i +=1
#Fonction qui vérifie si la case est libre
def est_valide(clic):
    valide = NON_JOUEE
    case_clic =[clic[0]//CASE,clic[1]//CASE]
    if jeu[case_clic[1]][case_clic[0]] == 0 :
        return valide
#Fonction qui inscrit dans le tableau 'jeu' les coups joués
def valider_coup(clic):
    case_clic =[clic[0]//CASE,clic[1]//CASE]
    jeu[case_clic[1]][case_clic[0]]=a_qui_de_jouer
    
""" --------------------------------------------------------------------------- 
    Partie 4 - Recherche d'un gagnant
--------------------------------------------------------------------------- """
#Fonctions qui parcourt les lignes, colonnes, diagonales à la recherche d'un gagnant
def recherche_ligne():
    i=0
    j=0
    somme=0
    while i<N:
        while j<N:
            somme = somme + jeu[i][j]
            j+=1
        if somme == N :
            return JOUEUR_1
        elif somme ==-N:
            return JOUEUR_2
        i+=1
    return 0

def recherche_colonne():
    i=0
    j=0
    somme=0
    while j<N :
        while i<N:
            somme = somme + jeu[i][j]
            i+=1
        if somme == N-1 :
            return JOUEUR_1
        elif somme == -N+1 :
            return JOUEUR_2
        j+=1
    return 0
    
def recherche_diagonale():
    i=0
    j=0
    somme=0
    while j<N:
        somme = somme + jeu[i][j]
        i+=1
        j+=1
    if somme == N :
        return JOUEUR_1
    elif somme == -N :
        return JOUEUR_2  
    return 0


def recherche_antidiagonale():
    i=N-1
    j=0
    somme=0
    while j<N:
        somme = somme + jeu[i][j]
        i-=1
        j+=1
    if somme == N :
        return JOUEUR_1
    elif somme == -N :
        return JOUEUR_2
    return 0

#Fonction qui trouve qui est le gagnant et le retourne
def qui_a_gagne():
    if recherche_ligne() == JOUEUR_1 or recherche_colonne() == JOUEUR_1 or recherche_diagonale() == JOUEUR_1 or recherche_antidiagonale() == JOUEUR_1 :
        print('Joueur 1 à gagné')
        return JOUEUR_1
    if recherche_ligne() == JOUEUR_2 or recherche_colonne() == JOUEUR_2 or recherche_diagonale() == JOUEUR_2 or recherche_antidiagonale() == JOUEUR_2 : 
        return JOUEUR_2
        print('Joueur 2 à gagné')
    

""" --------------------------------------------------------------------------- 
    Partie 5 - programme principal
--------------------------------------------------------------------------- """

# initialisation du module d'affichage 2D pygame
pygame.display.init()

# Création et affichage de la fenêtre graphique de largeur 900 et hauteur 600
size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.flip()

# Dessin du quadrillage
dessine_quadrillage(magenta)

# Initialisation et affichage du jeu dans la console
init_jeu()
affiche_jeu_console()

# Boucle principale
i = 1
while i<=N*N:
    # 1) attente d'un clic valide ... c'est à dire sur une case non jouée !
    clic = wait_clic()
    while est_valide(clic) != NON_JOUEE:
            clic = wait_clic()
    # 2) validation et affichage du coup dans la fenêtre graphique et la console
    valider_coup(clic)
    dessine_action(clic)
    affiche_jeu_console()
    
    # 3) recherche d'un gagnant
    gagnant = qui_a_gagne()
    if gagnant == JOUEUR_1 or gagnant == JOUEUR_2:
        i = N*N
    
    # 4) changement de joueur
    a_qui_de_jouer = -a_qui_de_jouer
    i +=1

# sortie du programme
wait_escape()
pygame.quit()

