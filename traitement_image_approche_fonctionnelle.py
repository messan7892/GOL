# -*- coding: utf-8 -*-

# importation du module graphique 2D pygame
import pygame
import pygame.gfxdraw
import time
# importation des modules couleur et graphics
from couleur import *
from graphics import *

""" --------------------------------------------------------------------------
    Partie 1 - Définition des constantes
    - FICHIER_INITIAL : nom du fichier image à charger
    - FICHIER_SAUVEGARDE : nom du fichier image pour sauvegarder les modifications
    - H_CASE : hauteur du menu
    - N : Nombre de boutons dans la barre de menus
--------------------------------------------------------------------------- """

FICHIER_INITIAL = "pingouin.ppm"
FICHIER_SAUVEGARDE = "pingouin_save.ppm"
H_CASE = 40
N = 6

""" --------------------------------------------------------------------------
    Partie 2 - Définition des structures de données
    I0 est une structure (donnée constituées de plusieurs champs) qui contient
    toutes les informations de l'image :
    - L : largeur de l'image en pixels
    - H : hauteur de l'image en pixels
    - M : valeur maximale utilisée pour coder la valeur d'un pixel rouge,
    vert ou bleu (par exemple 255 pour des pixels R,V,B codés chacun sur 8 
    bits)
    - T : tableau de pixels.
    T[i][j] est donc le pixel de l'image situé à la ligne i et à la colonne j,
    T[i][j][0] est le sous-pixel rouge,
    T[i][j][1] est le sous-pixel vert
    T[i][j][2] est le sous-pixel bleu (il s'agit d'un codage RVB)
    voir la fonction lire_fichier pour comprendre comment est rempli le tableau
--------------------------------------------------------------------------- """

L = 0
H = 0
M = 0
T = []

""" --------------------------------------------------------------------------
    Partie 3 - Lecture et sauvegarde des fichiers image
--------------------------------------------------------------------------- """

def lire_fichier(nom_fichier):
    global L,H,M,T
    # 1) ouverture du fichier contenant l'image en mode lecture
    file = open(nom_fichier, "r")
    # 2) lecture de la totalité du fichier et stokage de tous les nombres 
    # dans la liste src
    src = []
    for ligne in file:
        # on supprime les caractères de fin de chaine
        ligne = ligne.rstrip('\n')
        # on splite la ligne avec le séparateur espace
        ligne = ligne.split(" ")
        # on ajoute tous les éléments dans la liste src
        for elt in ligne:
            src.append(elt)
        
    # 3) lecture du nombre magique, L, H et M
    L = int(src[1])
    H = int(src[2])
    M = int(src[3])
    del src[0] # nombre magique
    del src[0] # L
    del src[0] # H
    del src[0] # M
            
    # 4) lecture des pixels
    k = 0
    # parcours des lignes
    i = 0
    while i<H:
        T.append([])
        # parcours des colonnes
        j = 0
        while j<L:
            # lecture des 3 sous-pixels R, V et B
            T[i].append([])
            T[i][j].append(int(src[k]))
            #print(src[k])
            k+=1
            T[i][j].append(int(src[k]))
            #print(src[k])
            k+=1
            T[i][j].append(int(src[k]))
            #print(src[k])
            k+=1
            #print("\n")
            j+=1
        i+=1
        
    # 5) fermeture du fichier contenant l'image
    file.close()

def save_fichier(nom_fichier):
    global L,H,M,T
    # ouverture du fichier contenant l'image modifiée en mode écriture
    file = open(nom_fichier, "w")
    # écriture dans le fichier
    file.write("P3\n")
    file.write(str(L)+"\n")
    file.write(str(H)+"\n")
    file.write(str(M)+"\n")
    # parcours des lignes
    i = 0
    while i<H:
        # parcours des colonnes
        j = 0
        while j<L:
            file.write(str(T[i][j][0])+"\n")
            file.write(str(T[i][j][1])+"\n")
            file.write(str(T[i][j][2])+"\n")                
            j+=1
        i+=1        
        
    # fermeture du fichier contenant l'image modifiée
    file.close()

""" --------------------------------------------------------------------------
    Partie 4 - Manipulation des images
    - affichage de l'image dans la fenêtre
    - copie
--------------------------------------------------------------------------- """

def affiche_I0():
    global L,H,M,T
    #parcours en ligne    
    i=0    
    while i < H :
        #parcours en colonne
        j=0
        while j < L :
            couleur_pixel=[T[i][j][0],T[i][j][1],T[i][j][2]]
            pygame.gfxdraw.pixel(screen,j,i,couleur_pixel)
            """time.sleep(0.001)
            pygame.display.flip()"""            
            j+=1
            
        i+=1
    pygame.display.flip()

""" --------------------------------------------------------------------------
    Partie 5 - Programmes de la zone de contrôle
    - filtre rouge
    - filtre vert
    - filtre bleu
    - mise en niveaux de gris
    - mise en noir et blanc    
--------------------------------------------------------------------------- """
   
def filtre_rouge():    
    global L,H,M,T
    i=0    
    while i < H :
        #parcours en colonne
        j=0
        while j < L :
            T[i][j][1]=0
            T[i][j][2]=0
            j+=1
            
        i+=1
    pygame.display.flip()
def filtre_vert():    
    global L,H,M,T
    i=0    
    while i < H :
        #parcours en colonne
        j=0
        while j < L :
            T[i][j][0]=0
            T[i][j][2]=0
            j+=1
            
        i+=1
    pygame.display.flip()

def filtre_bleu():    
    global L,H,M,T
    i=0    
    while i < H :
        #parcours en colonne
        j=0
        while j < L :
            T[i][j][0]=0
            T[i][j][1]=0
            j+=1
            
        i+=1
    pygame.display.flip()
            
def niveau_gris():        
    global L,H,M,T
    i=0    
    while i < H :
        #parcours en colonne
        j=0
        while j < L :
            T[i][j][0]=(T[i][j][0]+T[i][j][1]+T[i][j][2])/3
            T[i][j][1]=T[i][j][0]
            T[i][j][2]=T[i][j][1]
            j+=1
            
        i+=1
    pygame.display.flip()
            
def noir_et_blanc():    
    global L,H,M,T
    


def action_controle():    
    global L,H,M,T
    clic = wait_clic()
    i = clic[0]//(L//N)
    if clic[1] > H:
        if i==0:
            filtre_rouge()
            affiche_I0()
            return 1
        if i==1:
            filtre_vert()
            affiche_I0()
            return 1
        if i==2:
            filtre_bleu()
            affiche_I0()
            return 1
        if i==3:
            niveau_gris()
            affiche_I0()
            return 1
        if i==4:
            noir_et_blanc()
            affiche_I0()
            return 1
        if i==5:
            save_fichier(FICHIER_SAUVEGARDE)
            return 0
    return 1

""" --------------------------------------------------------------------------
    Partie 6 - Affichage de la zone de contrôle
    - affiche_bouton_texte : affiche un bouton coloré avec du texte centré
    - menu : affiche le menu complet
--------------------------------------------------------------------------- """

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
    
def affiche_controle():    
    global L,H,M,T
    affiche_bouton_texte("Rouge",[0,H,L//6,H_CASE],rouge)
    affiche_bouton_texte("Vert",[L//6,H,L//6,H_CASE],vert)
    affiche_bouton_texte("Bleu",[L//3,H,L//6,H_CASE],bleu)
    affiche_bouton_texte("Gris",[L//2,H,L//6,H_CASE],gris)
    affiche_bouton_texte("N&B",[L*2//3,H,L//6,H_CASE],blanc)
    affiche_bouton_texte("Save",[L*5//6,H,L//6,H_CASE],jaune)
    pygame.display.flip()
    
""" --------------------------------------------------------------------------
    Partie 7 - programme principal
--------------------------------------------------------------------------- """
  
# Construction des images initiale I0 et modifiée IM        
lire_fichier(FICHIER_INITIAL)

# initialisation du module d'affichage 2D pygame
pygame.display.init()

# Création et affichage de la fenêtre graphique de largeur 900 et hauteur 600
screen = pygame.display.set_mode([L, H + H_CASE])
pygame.display.flip()

# Affichage du menu
affiche_controle()

# Affichage de l'image initiale
affiche_I0()

# boucle principale
encore = 1
while encore==1:
    encore = action_controle()

# sortie du programme
pygame.quit()

