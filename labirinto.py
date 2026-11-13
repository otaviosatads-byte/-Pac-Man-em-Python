def prepararLabiritnto(labirinto):

# borda labirinto
    for i in range(9):
        labirinto[i][0] = '#'
        labirinto[i][27] = '#'
    for i in range(30, 31):
        for j in range(27, 28):
            labirinto[i][j] = '#'
        
    for i in range(28):
            labirinto[0][i] = '#'
            
    for i in range(19, 31):
        for j in range(1):
            labirinto[i][j] = '#'
                        
# canto superior esquerdo
    for i in range(2, 5, 1):
        for j in range(2, 6, 1):
            labirinto[i][j] = '#'
            
# canto superior esquerdo
    for i in range(6, 8):
        for j in range(2, 6):
            labirinto[i][j] = '#'
            
# canto superior esquerdo
    for i in range(2, 5, 1):
        for j in range(7, 12, 1):
            labirinto[i][j] = '#'

#inferior esquerdo

    for i in range(21, 23):
        for j in range(7, 12):
            labirinto[i][j] = '#'
    
    for i in range(21, 23):
        for j in range(2, 6):
            labirinto[i][j] = '#'
            
    for i in range(23, 26):
        for j in range(4, 6):
            labirinto[i][j] = '#'
    
    for i in range(24, 26):
        for j in range(0, 3):
            labirinto[i][j] = '#'
            
    for i in range(24, 29):
        for j in range(7, 9):
            labirinto[i][j] = '#'
    for i in range(27, 29):
        for j in range(2, 12):
            labirinto[i][j] = '#'
             
    for i in range(26, 29):
        for j in range(13, 15):
            labirinto[i][j] = '#'
            
    for i in range(24, 26):
        for j in range(10, 18):
            labirinto[i][j] = '#'

#direito central
    for i in range(9, 14):
        for j in range(22, 28):
            labirinto[i][j] = '#'

                 
#esquerdo central
    for i in range(9, 14):
        for j in range(0, 6):
            labirinto[i][j] = '#'
            
    for i in range(15, 20):
        for j in range(0, 6):
            labirinto[i][j] = '#'
            
    for i in range(15, 20):
        for j in range(7, 9):
            labirinto[i][j] = '#'
            
    for i in range(6, 14):
        for j in range(7, 9):
            labirinto[i][j] = '#'
            
    for i in range(9, 11):
        for j in range(9, 12):
            labirinto[i][j] = '#'
                       
#direito central
    for i in range(15, 20):
        for  j in range(22, 28):
            labirinto[i][j] = '#'
            
    for i in range(15, 20):
        for j in range(19, 21):
            labirinto[i][j] = '#'
            
            
# superior central
    for i in range(5):
        labirinto[i][13] = '#'
        labirinto[i][14] = '#'

# superior central
    for i in range(6, 8):
        for j in range(10,18):
            labirinto[i][j] = '#'
            
    for i in range(7, 11):
        labirinto[i][13] = '#'
        labirinto[i][14] = '#'
        
# inferior central
    for i in range(18,20):
        for j in range(10, 18):
            labirinto[i][j]= '#'
            
    for i in range(20, 23):
        for j in range(13, 15):
            labirinto[i][j] = '#'
        
        
# canto superior direito
    for i in range(2, 5):
        for j in range(16, 21):
            labirinto[i][j] = '#'
            
# canto superior direito
    for i in range(2, 5):
        for j in range(22, 26):
            labirinto[i][j] = '#'

# canto superior direito
    for i in range(6,8):
        for j in range(22, 26):
            labirinto[i][j] = '#'
            
 # canto superior direito           
    for i in range (6, 14):    
        for j in range(19, 21):
            labirinto[i][j] = '#'
    for i in range(9, 11):
        for j in range(16,20):
            labirinto[i][j] = '#' 

# inferior direito
    for i in (21, 22):
        for j in range(16, 21):
            labirinto[i][j] = '#'

    for i in range(21, 23):
        for j in range(22, 26):
            labirinto[i][j] = '#'
    
    for i in range(23, 26):
        for j in range(22, 24):
            labirinto[i][j] = '#'
    
    for i in range(24, 26):
        for j in range(25, 28):
            labirinto[i][j]= '#' 

    for i in range(24, 29):
        for j in range(19, 21):
            labirinto[i][j] = '#'
            
    for i in range(27, 29):
        for j in range(16, 26):
            labirinto[i][j] = '#'

# adiciona fundo
    for i in range(30):
        for j in range(28):
            if labirinto[i][j] == 0:
                labirinto[i][j] = ' '
                
#caixa dos fantasmas     
    for i in range(12,17):
        for j in range(10,18):
            labirinto[i][j] = '#'
            
    for i in range(13,16):
        for j in range(11,17):
            labirinto[i][j] = ' '
            
    labirinto[12][13] = '_'
    labirinto[12][14] = '_'
    
    for i in range(30, 31):
        for j in range(28):
            labirinto[i][j] = '#'
    
    for i in range(20, 31):
        for j in range(27, 28):
            labirinto[i][j] = '#'


def mostrarLabirinto(labirinto):
    tela = ''
    ANSI_AZUL = "\033[34m"
    ANSI_AMARELO = "\033[33m"
    ANSI_PADRAO = "\033[0m"
    ANSI_VERMELHO   = "\033[31m"
    ANSI_ROSA       = "\033[38;5;211m"
    ANSI_LARANJA    = "\033[38;5;214m"
    ANSI_AZUL_CLARO = "\033[36m"
    
    for i in range(31):
        for j in range(28):
            if labirinto[i][j] == '#':
                tela += ANSI_AZUL + labirinto[i][j] + " "
                       
            elif labirinto[i][j] == 'ᗧ':            
                tela += ANSI_AMARELO + labirinto[i][j] + " "
            
            elif labirinto[i][j] == 'B':
                tela += ANSI_VERMELHO + labirinto[i][j] + " "
            
            elif labirinto[i][j] == 'P':
                tela += ANSI_ROSA + labirinto[i][j] + " "
                
            elif labirinto[i][j] == 'I':
                tela += ANSI_AZUL_CLARO + labirinto[i][j] + " "
                
            elif labirinto[i][j] == 'C':
                tela += ANSI_LARANJA + labirinto[i][j] + " "
                
            elif labirinto[i][j] == '4':
                tela += ANSI_AZUL + labirinto[i][j] + " "
                
            else:
                tela += ANSI_PADRAO + labirinto[i][j] + " "
            
        tela += "\n"
    print(tela + ANSI_PADRAO, end="")


def mostrarVidas(vidas, pontos):
    while vidas >= 0:
        if vidas > 0:
            print('ᗧ', end = ' ')
        vidas -= 1    
    print('pontos:', pontos)
        
def colocarPastilhas(pastilhas, labirinto):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
# evita que que onde não deve ter pastilha não recceba pastilha 
            if(i >= 9 and i <= 19 and j >= 7 and j <= 20) and labirinto[i][j] != '#':
                if labirinto[i][j] == ' ':
                    labirinto[i][j] = ' '
                elif labirinto[i][j] == '_':
                    labirinto[i][j] = '_'
                    
# coloca pastilha
            elif labirinto[i][j] == ' ' and labirinto[i][j] != '#':
                if i == 14 and (j <= 5 or j >= 22):
                    labirinto[i][j] = ' '
                elif i == 4 and (j == 1 or j == 26):
                    labirinto[i][j] = 'O'
                    pastilhas += 1
                elif i == 23 and (j == 1 or j == 26):
                    labirinto[i][j] = 'O'
                    pastilhas += 1
                else:
                    labirinto[i][j] = 'o'
                    pastilhas += 1 
                
    return pastilhas

def limparLabirinto(labirinto, blinkAtual, pinkAtual, inkyAtual, clydAtual):
    for i in range(30):
        for j in range(27):
            if (i != 11 and j != 13) or (i != 14 and j != 11) or (i != 14 and j !=  13) or ( i != 14 and j != 15):
                
                if labirinto[i][j] == 'B':
                    labirinto[i][j] = blinkAtual
                    
                elif labirinto[i][j] == 'P':
                    labirinto[i][j] = pinkAtual

                elif labirinto[i][j] == 'I':
                     labirinto[i][j] = inkyAtual
                
                elif labirinto[i][j] == 'C':
                    labirinto[i][j] = clydAtual
                
                elif labirinto[i][j] == 'ᗧ':
                    labirinto[i][j] = ' '
                
                elif labirinto[i][j] == ':':
                    labirinto[i][j] = ' '
                    
                elif labirinto[i][j] == '4':
                    labirinto[i][j] = ' '
                    
                    
                    
def contadorPastilhas(pastilhas, labirinto):
    pastilhas = 0
    
    for i in range(31):
        for j in range(28):
            if labirinto[i][j] == 'o' or labirinto[i][j] == 'O':
                pastilhas += 1
                
    return pastilhas

