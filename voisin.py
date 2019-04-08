def calcul_voisin():
    # parcours des lignes    
    i = 0    
    while i<H :
        # parcours des colonnes
        j = 0
        while j<L :
            voisin_case = 0
            # bord haut
            if i==0:
                voisin_case = jeu[0][j-1] + jeu[0][j+1] + jeu[1][j-1] + jeu[1][j] + jeu[1][j+1]
            # bord bas
            elif i == H-1:
                voisin_case = jeu[H-2][j-1] + jeu[H-2][j] + jeu[H-2][j] + jeu[H-1][j-1] + jeu[H-1][j+1]

            #bord gauche
            elif j == 0:
                voisin_case = jeu[i-1][0] + jeu[i-1][1] + jeu[i][1] + jeu[i+1][0] + jeu[i+1][1]

            #bord droit
            elif j == L-1:
                voisin_case = jeu[i-1][L-2] + jeu[i-1][L-1] + jeu[i][L-2] + jeu[i+1][L-2] + jeu[i+1][L-1]
                    
            #coin haut gauche
            elif i == 0 and j==0 :
                voisin_case = jeu[1][0] + jeu[0][1] + jeu[1][1]
    
            #coin haut droit
            elif i == 0 and j== L-1 :
                voisin_case = jeu[0][L-2] + jeu[1][L-2] + jeu[1][L-1]
    
            if  jeu[j] != 0
    
                if jeu[i][j-1]==1
                    voisin-case +=1
    
            if jeu[j] != L-1
     
                if jeu[i][j+1]==1
                    voisin-case +=1
    
            if jeu[i] != H-1 or jeu[j] != 0
     
                if jeu[i+1][j-1]==1
                    voisin-case +=1
            if jeu[i] != H-1
                if jeu[i+1][j]==1
                    voisin-case +=1 
            if jeu[i] != H-1 or jeu[j] != L-1
                if jeu[i+1][j+1]==1
                    voisin-case +=1 
            voisin[i][j]=voisin_case
            j +=1
        i+=1
