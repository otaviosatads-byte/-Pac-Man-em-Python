import random

def movimentoBlink(passadoBlinkX, passadoBlinkY, blinkX, blinkY, pacmanX, pacmanY, labirinto, poder, blinkAtual, blinkVivo):
    caminho = [0, 0, 0, 0]
    indiciCaminho = 0
    menor = 1000
    posicaoX = 0
    posicaoY = 0
    #faz o caucluo dos possiveis caminhos do blink
    
    if blinkVivo == False:
        posicaoX = 13
        posicaoY = 14
        for i in range(4):   
            diferenca = 1000
            if i == 0 and (labirinto[blinkY][blinkX - 1] != '#') and ((blinkX - 1) != passadoBlinkX or blinkY != passadoBlinkY):
                deltaX = (blinkX - 1) - posicaoX
                deltaY = blinkY - posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1) 
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY
                else:
                    diferenca = deltaX + deltaY
                              
            if i == 1 and (labirinto[blinkY][blinkX + 1] != '#') and ((blinkX + 1) != passadoBlinkX or blinkY != passadoBlinkY):
                deltaX = (blinkX + 1) - posicaoX
                deltaY = blinkY - posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY
                  
                else:
                    diferenca = deltaX + deltaY   
                              
            if i == 2 and (labirinto[blinkY - 1][blinkX] != '#') and ((blinkY - 1) != passadoBlinkY or blinkX != passadoBlinkX):
                deltaX = blinkX - posicaoX
                deltaY = (blinkY - 1) - posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                      diferenca = (deltaX * -1) + deltaY
                else:
                      diferenca = deltaX + deltaY
              
            if i == 3 and (labirinto[blinkY + 1][blinkX] != '#') and  ((blinkY + 1) != passadoBlinkY or blinkX != passadoBlinkX):
                deltaX = blinkX - posicaoX
                deltaY = (blinkY + 1)- posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY    
                  
                else:
                    diferenca = deltaX + deltaY
  
            caminho[i] = diferenca
        
    elif poder == True:
        posicaoX = random.randint(1, 26)
        posicaoY = random.randint(1, 29)
        
        for i in range(4):
            diferenca = 1000
            if i == 0 and (labirinto[blinkY][blinkX - 1] != '#') and ((blinkX - 1) != passadoBlinkX or blinkY != passadoBlinkY) and (labirinto[blinkY][blinkX - 1] != '_'):
                deltaX = (blinkX - 1) - posicaoX
                deltaY = blinkY - posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1) 
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY
                else:
                    diferenca = deltaX + deltaY
                              
            if i == 1 and (labirinto[blinkY][blinkX + 1] != '#') and ((blinkX + 1) != passadoBlinkX or blinkY != passadoBlinkY) and (labirinto[blinkY][blinkX + 1] != '_'):
                deltaX = (blinkX + 1) - posicaoX
                deltaY = blinkY - posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY
                  
                else:
                    diferenca = deltaX + deltaY   
                              
            if i == 2 and (labirinto[blinkY - 1][blinkX] != '#') and ((blinkY - 1) != passadoBlinkY or blinkX != passadoBlinkX) and (labirinto[blinkY - 1][blinkX] != '_'):
                deltaX = blinkX - posicaoX
                deltaY = (blinkY - 1) - posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                      diferenca = (deltaX * -1) + deltaY
                else:
                      diferenca = deltaX + deltaY
              
            if i == 3 and (labirinto[blinkY + 1][blinkX] != '#') and  ((blinkY + 1) != passadoBlinkY or blinkX != passadoBlinkX) and (labirinto[blinkY + 1][blinkX] != '_'):
                deltaX = blinkX - posicaoX
                deltaY = (blinkY + 1)- posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY    
                  
                else:
                    diferenca = deltaX + deltaY
  
            caminho[i] = diferenca
            
    elif poder == False:     
        for i in range(4):
            diferenca = 1000
            if i == 0 and (labirinto[blinkY][blinkX - 1] != '#') and ((blinkX - 1) != passadoBlinkX or blinkY != passadoBlinkY) and (labirinto[blinkY][blinkX - 1] != '_'):
                deltaX = (blinkX - 1) - pacmanX
                deltaY = blinkY - pacmanY
            
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1) 
                
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY
                else:
                    diferenca = deltaX + deltaY
                            
            if i == 1 and (labirinto[blinkY][blinkX + 1] != '#') and ((blinkX + 1) != passadoBlinkX or blinkY != passadoBlinkY) and (labirinto[blinkY][blinkX + 1] != '_'):
                deltaX = (blinkX + 1) - pacmanX
                deltaY = blinkY - pacmanY
            
                if deltaY <= 0 and deltaX <= 0:
                   diferenca = (deltaX * -1) + (deltaY * -1)
                
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY
                
                else:
                    diferenca = deltaX + deltaY   
                            
            if i == 2 and (labirinto[blinkY - 1][blinkX] != '#') and ((blinkY - 1) != passadoBlinkY or blinkX != passadoBlinkX) and (labirinto[blinkY - 1][blinkX] != '_'):
                deltaX = blinkX - pacmanX
                deltaY = (blinkY - 1) - pacmanY
            
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY
                else:
                    diferenca = deltaX + deltaY
            
            if i == 3 and (labirinto[blinkY + 1][blinkX] != '#') and  ((blinkY + 1) != passadoBlinkY or blinkX != passadoBlinkX) and (labirinto[blinkY + 1][blinkX] != '_'):
                deltaX = blinkX - pacmanX
                deltaY = (blinkY + 1)- pacmanY
            
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY    
                
                else:
                    diferenca = deltaX + deltaY

            caminho[i] = diferenca
            
    for i in range(4):
        if caminho[i] < menor:
            menor = caminho[i]
            indiciCaminho = i
            
    # reliaza a escolha do caminho mais curto
    if indiciCaminho == 0:          
        labirinto[blinkY][blinkX] = blinkAtual
        passadoBlinkX = blinkX
        passadoBlinkY = blinkY
        blinkX -= 1
        if labirinto[blinkY][blinkX] != 'P' and labirinto[blinkY][blinkX] != 'I' and labirinto[blinkY][blinkX] != 'C' and labirinto[blinkY][blinkX] != '4' and labirinto[blinkY][blinkX] != ':' and labirinto[blinkY][blinkX] != 'ᗧ':
            blinkAtual = labirinto[blinkY][blinkX]
            
        if blinkX == 0 and blinkY == 14:
            blinkX = 26
            
    elif indiciCaminho == 1:    
        labirinto[blinkY][blinkX] = blinkAtual
        passadoBlinkX = blinkX
        passadoBlinkY = blinkY
        blinkX += 1
        if labirinto[blinkY][blinkX] != 'P' and labirinto[blinkY][blinkX] != 'I' and labirinto[blinkY][blinkX] != 'C' and labirinto[blinkY][blinkX] != '4' and labirinto[blinkY][blinkX] != ':' and labirinto[blinkY][blinkX] != 'ᗧ':    
            blinkAtual = labirinto[blinkY][blinkX]
            
        if blinkX == 27 and blinkY == 14:
            blinkX = 1
                
    elif indiciCaminho == 2:
        labirinto[blinkY][blinkX] = blinkAtual
        passadoBlinkX = blinkX
        passadoBlinkY = blinkY
        blinkY -= 1
        if labirinto[blinkY][blinkX] != 'P' and labirinto[blinkY][blinkX] != 'I' and labirinto[blinkY][blinkX] != 'C' and labirinto[blinkY][blinkX] != '4' and labirinto[blinkY][blinkX] != ':' and labirinto[blinkY][blinkX] != 'ᗧ':    
            blinkAtual = labirinto[blinkY][blinkX]

    elif indiciCaminho == 3:
        labirinto[blinkY][blinkX] = blinkAtual
        passadoBlinkX = blinkX
        passadoBlinkY = blinkY
        blinkY += 1
        if labirinto[blinkY][blinkX] != 'P' and labirinto[blinkY][blinkX] != 'I' and labirinto[blinkY][blinkX] != 'C' and labirinto[blinkY][blinkX] != '4' and labirinto[blinkY][blinkX] != ':' and labirinto[blinkY][blinkX] != 'ᗧ':    
            blinkAtual = labirinto[blinkY][blinkX]
                      
    return blinkY, blinkX, passadoBlinkY, passadoBlinkX, blinkAtual, blinkVivo
    
def movimentoPink(pinkX, pinkY, pacmanX, pacmanY, labirinto, passadoPinkX, passadoPinkY, opcao, pinkAtual, poder, pinkVivo):
    caminho = [0, 0, 0, 0]
    menor = 1000
    indiceCaminho = 0
    posicaoX = 0
    posicaoY = 0
    
    if pinkVivo == False:
        posicaoX = 13
        posicaoY = 14
        for i in range(4):   
            diferenca = 1000
            if i == 0 and (labirinto[pinkY][pinkX - 1] != '#') and ((pinkX - 1) != passadoPinkX or pinkY != passadoPinkY):
                deltaX = (pinkX - 1) - posicaoX
                deltaY = pinkY - posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1) 
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY
                else:
                    diferenca = deltaX + deltaY
                              
            if i == 1 and (labirinto[pinkY][pinkX + 1] != '#') and ((pinkX + 1) != passadoPinkX or pinkY != passadoPinkY):
                deltaX = (pinkX + 1) - posicaoX
                deltaY = pinkY - posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY
                  
                else:
                    diferenca = deltaX + deltaY   
                              
            if i == 2 and (labirinto[pinkY - 1][pinkX] != '#') and ((pinkY - 1) != passadoPinkY or pinkX != passadoPinkX):
                deltaX = pinkX - posicaoX
                deltaY = (pinkY - 1) - posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                      diferenca = (deltaX * -1) + deltaY
                else:
                      diferenca = deltaX + deltaY
              
            if i == 3 and (labirinto[pinkY + 1][pinkX] != '#') and  ((pinkY + 1) != passadoPinkY or pinkX != passadoPinkX):
                deltaX = pinkX - posicaoX
                deltaY = (pinkY + 1)- posicaoY
              
                if deltaY <= 0 and deltaX <= 0:
                    diferenca = (deltaX * -1) + (deltaY * -1)
                  
                elif deltaY <= 0:
                    diferenca = deltaX + (deltaY * -1)
                  
                elif deltaX <= 0:
                    diferenca = (deltaX * -1) + deltaY    
                  
                else:
                    diferenca = deltaX + deltaY
  
            caminho[i] = diferenca
    
    elif poder == True:
        posicaoX = random.randint(1, 26)
        posicaoY = random.randint(1, 29)
        for i in range(4):
            diferenca = 1000    
            if i == 0 and (labirinto[pinkY][pinkX - 1] != '#') and (labirinto[pinkY][pinkX - 1] != '_') and ((pinkX - 1) != passadoPinkX or pinkY != passadoPinkY):
                deltaX = (pinkX - 1) - posicaoX
                deltaY = pinkY - posicaoY
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
            
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX
            
                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)  
                
                else:  
                    diferenca = deltaY + deltaX
                            
            elif i == 1 and (labirinto[pinkY][pinkX + 1] != '#') and (labirinto[pinkY][pinkX + 1] != '_') and ((pinkX + 1) != passadoPinkX or pinkY != passadoPinkY):
                deltaX = (pinkX + 1) - posicaoX
                deltaY = pinkY - posicaoY
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
                
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX

                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)  

                else:  
                    diferenca = deltaY + deltaX                
        
            elif i == 2 and (labirinto[pinkY - 1][pinkX] != '#') and (labirinto[pinkY - 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY - 1) != passadoPinkY):
                deltaX =  pinkX - posicaoX
                deltaY = (pinkY - 1) - posicaoY
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
                
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX

                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)  

                else:  
                    diferenca = deltaY + deltaX
                        
            elif i == 3 and (labirinto[pinkY + 1][pinkX] != '#') and (labirinto[pinkY + 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY + 1) != passadoPinkY):
                deltaX =  pinkX - posicaoX
                deltaY = (pinkY + 1) - posicaoY
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
            
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX
                
                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)  
                
                else:  
                    diferenca = deltaY + deltaX
        
            caminho[i] = diferenca

    elif poder == False:    
        if opcao == 'A' or opcao == 'a':
            for i in range(4):
                #faz o caucluo dos possiveis caminhos do pink
                diferenca = 1000
                if i == 0 and (labirinto[pinkY][pinkX - 1] != '#') and (labirinto[pinkY][pinkX - 1] != '_') and ((pinkX - 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX - 1) - (pacmanX - 5)
                    deltaY = pinkY - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
                            
                elif i == 1 and (labirinto[pinkY][pinkX + 1] != '#') and (labirinto[pinkY][pinkX + 1] != '_') and ((pinkX + 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX + 1) - (pacmanX - 5)
                    deltaY = pinkY - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX                
        
                elif i == 2 and (labirinto[pinkY - 1][pinkX] != '#') and (labirinto[pinkY - 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY - 1) != passadoPinkY):
                    deltaX =  pinkX - (pacmanX - 5)
                    deltaY = (pinkY - 1) - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX
                        
                elif i == 3 and (labirinto[pinkY + 1][pinkX] != '#') and (labirinto[pinkY + 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY + 1) != passadoPinkY):
                    deltaX =  pinkX - (pacmanX - 5)
                    deltaY = (pinkY + 1) - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
        
                caminho[i] = diferenca
                
        elif opcao == 'd' or opcao == 'D':
            for i in range(4):
                #faz o caucluo dos possiveis caminhos do pink
                diferenca = 1000
                if i == 0 and (labirinto[pinkY][pinkX - 1] != '#') and (labirinto[pinkY][pinkX - 1] != '_') and ((pinkX - 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX - 1) - (pacmanX + 5)
                    deltaY = pinkY - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
                            
                elif i == 1 and (labirinto[pinkY][pinkX + 1] != '#') and (labirinto[pinkY][pinkX + 1] != '_') and ((pinkX + 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX + 1) - (pacmanX + 5)
                    deltaY = pinkY - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX                
        
                elif i == 2 and (labirinto[pinkY - 1][pinkX] != '#') and (labirinto[pinkY - 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY - 1) != passadoPinkY):
                    deltaX =  pinkX - (pacmanX + 5)
                    deltaY = (pinkY - 1) - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX
                        
                elif i == 3 and (labirinto[pinkY + 1][pinkX] != '#') and (labirinto[pinkY + 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY + 1) != passadoPinkY):
                    deltaX =  pinkX - (pacmanX + 5)
                    deltaY = (pinkY + 1) - pacmanY
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
        
                caminho[i] = diferenca
        elif opcao == 'W' or opcao == 'w':
            for i in range(4):
                #faz o caucluo dos possiveis caminhos do pink
                diferenca = 1000
                if i == 0 and (labirinto[pinkY][pinkX - 1] != '#') and (labirinto[pinkY][pinkX - 1] != '_') and ((pinkX - 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX - 1) - pacmanX
                    deltaY = pinkY - (pacmanY - 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
                            
                elif i == 1 and (labirinto[pinkY][pinkX + 1] != '#') and (labirinto[pinkY][pinkX + 1] != '_') and ((pinkX + 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX + 1) - pacmanX
                    deltaY = pinkY - (pacmanY - 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX                
        
                elif i == 2 and (labirinto[pinkY - 1][pinkX] != '#') and (labirinto[pinkY - 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY - 1) != passadoPinkY):
                    deltaX =  pinkX - pacmanX
                    deltaY = (pinkY - 1) - (pacmanY - 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX
                        
                elif i == 3 and (labirinto[pinkY + 1][pinkX] != '#') and (labirinto[pinkY + 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY + 1) != passadoPinkY):
                    deltaX =  pinkX - pacmanX
                    deltaY = (pinkY + 1) - (pacmanY - 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
        
                caminho[i] = diferenca
        elif opcao == 'S' or opcao == 's':
            for i in range(4):
                #faz o caucluo dos possiveis caminhos do pink
                diferenca = 1000
                if i == 0 and (labirinto[pinkY][pinkX - 1] != '#') and (labirinto[pinkY][pinkX - 1] != '_') and ((pinkX - 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX - 1) - pacmanX 
                    deltaY = pinkY - (pacmanY + 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
                            
                elif i == 1 and (labirinto[pinkY][pinkX + 1] != '#') and (labirinto[pinkY][pinkX + 1] != '_') and ((pinkX + 1) != passadoPinkX or pinkY != passadoPinkY):
                    deltaX = (pinkX + 1) - pacmanX
                    deltaY = pinkY - (pacmanY + 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX                
        
                elif i == 2 and (labirinto[pinkY - 1][pinkX] != '#') and (labirinto[pinkY - 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY - 1) != passadoPinkY):
                    deltaX =  pinkX - pacmanX
                    deltaY = (pinkY - 1) - (pacmanY + 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
                
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX

                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  

                    else:  
                        diferenca = deltaY + deltaX
                        
                elif i == 3 and (labirinto[pinkY + 1][pinkX] != '#') and (labirinto[pinkY + 1][pinkX] != '_') and (pinkX != passadoPinkX or (pinkY + 1) != passadoPinkY):
                    deltaX =  pinkX - pacmanX
                    deltaY = (pinkY + 1) - (pacmanY + 5)
                    if deltaY < 0 and deltaX < 0:
                        diferenca = (deltaY * -1) + (deltaX * -1)
            
                    elif deltaY < 0:
                        diferenca = (deltaY * -1) + deltaX
                
                    elif deltaX < 0:
                        diferenca = deltaY + (deltaX * -1)  
                
                    else:  
                        diferenca = deltaY + deltaX
        
                caminho[i] = diferenca            

    for i in range(4):
        if caminho[i] < menor:
            menor = caminho[i]
            indiceCaminho = i
# reliaza a escolha do caminho mais curto
            
    if indiceCaminho == 0:   
        labirinto[pinkY][pinkX] = pinkAtual 
        passadoPinkX = pinkX
        passadoPinkY = pinkY
        pinkX -= 1
        if labirinto[pinkY][pinkX] != 'B' and labirinto[pinkY][pinkX] != 'I' and labirinto[pinkY][pinkX] != 'C' and labirinto[pinkY][pinkX] != '4' and labirinto[pinkY][pinkX] != ':' and labirinto[pinkY][pinkX] != 'ᗧ':
            pinkAtual = labirinto[pinkY][pinkX] 
                    
        if pinkX == 0 and pinkY == 14:
            pinkX = 26
                    
    elif indiceCaminho == 1:
        labirinto[pinkY][pinkX] = pinkAtual
        passadoPinkX = pinkX
        passadoPinkY = pinkY                        
        pinkX += 1
        if labirinto[pinkY][pinkX] != 'B' and labirinto[pinkY][pinkX] != 'I' and labirinto[pinkY][pinkX] != 'C' and labirinto[pinkY][pinkX] != '4' and labirinto[pinkY][pinkX] != ':' and labirinto[pinkY][pinkX] != 'ᗧ':    
            pinkAtual = labirinto[pinkY][pinkX]

        if pinkX == 27 and pinkY == 14:
            pinkX = 1
                
    elif indiceCaminho == 2:
        labirinto[pinkY][pinkX] = pinkAtual   
        passadoPinkX = pinkX
        passadoPinkY = pinkY
        pinkY -= 1
        if labirinto[pinkY][pinkX] != 'B' and labirinto[pinkY][pinkX] != 'I' and labirinto[pinkY][pinkX] != 'C' and labirinto[pinkY][pinkX] != '4' and labirinto[pinkY][pinkX] != ':' and labirinto[pinkY][pinkX] != 'ᗧ':
            pinkAtual = labirinto[pinkY][pinkX]
                        
    elif indiceCaminho == 3:
        labirinto[pinkY][pinkX] = pinkAtual                 
        passadoPinkX = pinkX
        passadoPinkY = pinkY 
        pinkY += 1
        if labirinto[pinkY][pinkX] != 'B' and labirinto[pinkY][pinkX] != 'I' and labirinto[pinkY][pinkX] != 'C' and labirinto[pinkY][pinkX] != '4' and labirinto[pinkY][pinkX] != ':' and labirinto[pinkY][pinkX] != 'ᗧ':        
            pinkAtual = labirinto[pinkY][pinkX]
                        
    return pinkY, pinkX, passadoPinkY, passadoPinkX, pinkAtual, pinkVivo
            
def movimentoInky(inkyX, inkyY, blinkX, blinkY, pacmanX, pacmanY, labirinto, passadoinkyX, passadoinkyY, inkyAtual, poder, inkyVivo):
    caminho = [0, 0, 0, 0]
    menor = 1000
    indicieCaminho = 0
    posicaoX = 0
    posicaoY = 0

    if inkyVivo == False:
        posicaoX = 13
        posicaoY = 14
       
        for i in range(4):
            diferenca = 1000
            if i == 0 and labirinto[inkyY][inkyX - 1] != '#' and (labirinto[inkyY][inkyX - 1] != '_') and (inkyY != passadoinkyY or (inkyX - 1)!= passadoinkyX): #esquerda
                deltaX = (inkyX - 1) - posicaoX
                deltaY = inkyY - posicaoY
            
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
                        
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX
                        
                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)
                        
                else:
                    diferenca = deltaY + deltaX
                        
                diferenca *= 2
            
            elif i == 1 and labirinto[inkyY][inkyX + 1] != '#' and (labirinto[inkyY][inkyX + 1] != '_') and (inkyY != passadoinkyY or (inkyX + 1) != passadoinkyX):#  direita
                deltaX = (inkyX + 1) - posicaoX
                deltaY = inkyY - posicaoY
                        
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
                                    
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX
                                    
                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)
                                    
                else:
                    diferenca = deltaY + deltaX
                                    
                diferenca *= 2
        
            elif i == 2 and (labirinto[inkyY - 1][inkyX] != '#') and (labirinto[inkyY - 1][inkyX] != '_') and ((inkyY - 1) != passadoinkyY or inkyX != passadoinkyX):# para cima 
                deltaX = inkyX - posicaoX
                deltaY = (inkyY - 1) - posicaoY

                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
            
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX

                elif deltaX < 0: 
                    diferenca = deltaY + (deltaX * -1)
            
                else: 
                    diferenca = deltaY + deltaX
            
                diferenca *= 2   
        
            elif i == 3 and labirinto[inkyY + 1][inkyX] != '#' and (labirinto[inkyY + 1][inkyX] != '_') and ((inkyY + 1) != passadoinkyY or inkyX != passadoinkyX):#para baixo
                deltaX = inkyX - posicaoX
                deltaY = (inkyY + 1) - posicaoY
            
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
            
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX
            
                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)
            
                else:
                    diferenca = deltaY + deltaX
            
                diferenca *= 2
            caminho[i] = diferenca
    
    elif poder == True:
        posicaoX = random.randint(1, 26)
        posicaoY = random.randint(1, 29)
        for i in range(4):
            diferenca = 1000
            if i == 0 and labirinto[inkyY][inkyX - 1] != '#' and (labirinto[inkyY][inkyX - 1] != '_') and (inkyY != passadoinkyY or (inkyX - 1)!= passadoinkyX): #esquerda
                deltaX = (inkyX - 1) - posicaoX
                deltaY = inkyY - posicaoY
            
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
                        
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX
                        
                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)
                        
                else:
                    diferenca = deltaY + deltaX
                        
                diferenca *= 2
            
            elif i == 1 and labirinto[inkyY][inkyX + 1] != '#' and (labirinto[inkyY][inkyX + 1] != '_') and (inkyY != passadoinkyY or (inkyX + 1) != passadoinkyX):#  direita
                deltaX = (inkyX + 1) - posicaoX
                deltaY = inkyY - posicaoY
                        
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
                                    
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX
                                    
                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)
                                    
                else:
                    diferenca = deltaY + deltaX
                                    
                diferenca *= 2
        
            elif i == 2 and (labirinto[inkyY - 1][inkyX] != '#') and (labirinto[inkyY - 1][inkyX] != '_') and ((inkyY - 1) != passadoinkyY or inkyX != passadoinkyX):# para cima 
                deltaX = inkyX - posicaoX
                deltaY = (inkyY - 1) - posicaoY

                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
            
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX

                elif deltaX < 0: 
                    diferenca = deltaY + (deltaX * -1)
            
                else: 
                    diferenca = deltaY + deltaX
            
                diferenca *= 2   
        
            elif i == 3 and labirinto[inkyY + 1][inkyX] != '#' and (labirinto[inkyY + 1][inkyX] != '_') and ((inkyY + 1) != passadoinkyY or inkyX != passadoinkyX):#para baixo
                deltaX = inkyX - posicaoX
                deltaY = (inkyY + 1) - posicaoY
            
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
            
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX
            
                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)
            
                else:
                    diferenca = deltaY + deltaX
            
                diferenca *= 2
            caminho[i] = diferenca        
   
    #faz o caucluo dos possiveis caminhos do inky
    elif poder == False:
        for i in range(4):
            diferenca = 1000
            if i == 0 and labirinto[inkyY][inkyX - 1] != '#' and (labirinto[inkyY][inkyX - 1] != '_') and (inkyY != passadoinkyY or (inkyX - 1)!= passadoinkyX): #esquerda
                deltaX = blinkX - (pacmanX - 2)
                deltaY = blinkY - pacmanY
            
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
                        
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX
                        
                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)
                        
                else:
                    diferenca = deltaY + deltaX
                        
                diferenca *= 2
            
            elif i == 1 and labirinto[inkyY][inkyX + 1] != '#' and (labirinto[inkyY][inkyX + 1] != '_') and (inkyY != passadoinkyY or (inkyX + 1) != passadoinkyX):#  direita
                deltaX = blinkX - (pacmanX + 2)
                deltaY = blinkY - pacmanY
                        
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
                                    
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX
                                    
                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)
                                    
                else:
                    diferenca = deltaY + deltaX
                                    
                diferenca *= 2
        
            elif i == 2 and (labirinto[inkyY - 1][inkyX] != '#') and (labirinto[inkyY - 1][inkyX] != '_') and ((inkyY - 1) != passadoinkyY or inkyX != passadoinkyX):# para cima 
                deltaX = blinkX - pacmanX
                deltaY = blinkY - (pacmanY - 2)

                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
            
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX

                elif deltaX < 0: 
                    diferenca = deltaY + (deltaX * -1)
            
                else: 
                    diferenca = deltaY + deltaX
            
                diferenca *= 2   
        
            elif i == 3 and labirinto[inkyY + 1][inkyX] != '#' and (labirinto[inkyY + 1][inkyX] != '_') and ((inkyY + 1) != passadoinkyY or inkyX != passadoinkyX):#para baixo
                deltaX = blinkX - pacmanX
                deltaY = blinkY - (pacmanY + 2)
            
                if deltaY < 0 and deltaX < 0:
                    diferenca = (deltaY * -1) + (deltaX * -1)
            
                elif deltaY < 0:
                    diferenca = (deltaY * -1) + deltaX
            
                elif deltaX < 0:
                    diferenca = deltaY + (deltaX * -1)
            
                else:
                    diferenca = deltaY + deltaX
            
                diferenca *= 2
            caminho[i] = diferenca
        
    for i in range(4):
        if caminho[i] < menor:
            menor = caminho[i]
            indicieCaminho = i
    # reliaza a escolha do caminho mais curto
    
    if indicieCaminho == 0:      
        labirinto[inkyY][inkyX] = inkyAtual
        passadoinkyX = inkyX
        passadoinkyY = inkyY
        inkyX -= 1
        if labirinto[inkyY][inkyX] != 'B' and labirinto[inkyY][inkyX] != 'P' and labirinto[inkyY][inkyX] != 'C' and labirinto[inkyY][inkyX] != '4' and labirinto[inkyY][inkyX] != ':' and labirinto[inkyY][inkyX] != 'ᗧ':
            inkyAtual = labirinto[inkyY][inkyX]
        
        if inkyY == 14 and inkyX == 0:
            inkyX = 26
            
    elif indicieCaminho == 1:
        labirinto[inkyY][inkyX] = inkyAtual
        passadoinkyX = inkyX
        passadoinkyY = inkyY
        inkyX += 1
        if labirinto[inkyY][inkyX] != 'B' and labirinto[inkyY][inkyX] != 'P' and labirinto[inkyY][inkyX] != 'C' and labirinto[inkyY][inkyX] != '4' and labirinto[inkyY][inkyX] != ':' and labirinto[inkyY][inkyX] != 'ᗧ':
            inkyAtual = labirinto[inkyY][inkyX]    
        
        if inkyY == 14 and inkyX == 27:
            inkyX = 1
    
    elif indicieCaminho == 2:    
        labirinto[inkyY][inkyX] = inkyAtual
        passadoinkyX = inkyX
        passadoinkyY = inkyY
        inkyY -= 1
        if labirinto[inkyY][inkyX] != 'B' and labirinto[inkyY][inkyX] != 'P' and labirinto[inkyY][inkyX] != 'C' and labirinto[inkyY][inkyX] != '4' and labirinto[inkyY][inkyX] != ':' and labirinto[inkyY][inkyX] != 'ᗧ':
            inkyAtual = labirinto[inkyY][inkyX]  
        
    elif indicieCaminho == 3:
        labirinto[inkyY][inkyX] = inkyAtual
        passadoinkyX = inkyX
        passadoinkyY = inkyY
        inkyY += 1
        if labirinto[inkyY][inkyX] != 'B' and labirinto[inkyY][inkyX] != 'P' and labirinto[inkyY][inkyX] != 'C' and labirinto[inkyY][inkyX] != '4' and labirinto[inkyY][inkyX] != ':' and labirinto[inkyY][inkyX] != 'ᗧ':
            inkyAtual = labirinto[inkyY][inkyX]        
    
    return inkyY, inkyX, passadoinkyY, passadoinkyX, inkyAtual

def movimentoClyd(clydX, clydY, passadoClydX, passadoClydY, clydAtual, clydVivo, poder, pacmanX, pacmanY, labirinto):
    caminho = [0, 0, 0, 0]
    menor = 1000
    posicaoX = 0
    posicaoY = 0
     
    if clydVivo == False:
        posicaoX = 13
        posicaoY = 14
        for i in range(4):
            diferenca = 1000
            
            if i == 0 and labirinto[clydY][clydX - 1] != '#' and ((clydX - 1) != passadoClydX or clydY != passadoClydY):
                deltaX = (clydX - 1) - posicaoX
                deltaY = clydY - posicaoY
                if deltaX < 0 and deltaY < 0:
                    diferenca = (deltaX * -1) +  (deltaY * -1)
                
                elif deltaX < 0:
                    diferenca = (deltaX * -1) + deltaY
                
                elif deltaY < 0:
                
                    diferenca = deltaX + (deltaY * -1)
                
                else:
                    diferenca = deltaX + deltaY
            
            elif i == 1 and labirinto[clydY][clydX + 1] != '#' and ((clydX + 1) != passadoClydX or clydY != passadoClydY):
                deltaX = (clydX + 1) - posicaoX
                deltaY = clydY - posicaoY
                if deltaX < 0 and deltaY < 0:
                    diferenca = (deltaX * -1) +  (deltaY * -1)                
                
                elif deltaX < 0:
                    diferenca = (deltaX * -1) + deltaY
                
                elif deltaY < 0:
                    diferenca = deltaX + (deltaY * -1)
                
                else:
                    diferenca = deltaX + deltaY
            
            elif i == 2 and labirinto[clydY - 1][clydX] != '#' and (clydX != passadoClydX or (clydY - 1) != passadoClydY):
                deltaX = clydX- posicaoX
                deltaY = (clydY - 1) - posicaoY
        
                if deltaX < 0 and deltaY < 0:
                    diferenca = (deltaX * -1) +  (deltaY * -1)
                
                elif deltaX < 0:
                    diferenca = (deltaX * -1) + deltaY
                
                elif deltaY < 0:
                    diferenca = deltaX + (deltaY * -1)
                
                else:
                    diferenca = deltaX + deltaY
            
            elif i == 3 and labirinto[clydY + 1][clydX] != '#' and (clydX != passadoClydX or (clydY + 1) != passadoClydY):
                deltaX = clydX - posicaoX
                deltaY = (clydY + 1) - posicaoY
                
                if deltaX < 0 and deltaY < 0:
                    diferenca = (deltaX * -1) +  (deltaY * -1)                
                
                elif deltaX < 0:
                    diferenca = (deltaX * -1) + deltaY
                
                elif deltaY < 0:
                    diferenca = deltaX + (deltaY * -1)

                else:
                    diferenca = deltaX + deltaY
                            
            caminho[i] = diferenca        
    elif poder == True:
        posicaoX = random.randint(1, 26)
        posicaoY = random.randint(1, 29)
        
        for i in range(4):
            diferenca = 1000    
            if i == 0 and labirinto[clydY][clydX - 1] != '#' and ((clydX - 1) != passadoClydX or clydY != passadoClydY) and labirinto[clydY][clydX - 1] != '_':
                deltaX = (clydX - 1) - posicaoX
                deltaY = clydY - posicaoY
                
                if deltaX < 0 and deltaY < 0:
                    diferenca = (deltaX * -1) +  (deltaY * -1)
                
                elif deltaX < 0:
                    diferenca = (deltaX * -1) + deltaY
                
                elif deltaY < 0:
                    diferenca = deltaX + (deltaY * -1)
                    
                else:
                    diferenca = deltaX + deltaY
            
            elif i == 1 and labirinto[clydY][clydX + 1] != '#' and ((clydX + 1) != passadoClydX or clydY != passadoClydY) and labirinto[clydY][clydX + 1] != '_':
                deltaX = (clydX + 1) - posicaoX
                deltaY = clydY - posicaoY
                
                if deltaX < 0 and deltaY < 0:
                    diferenca = (deltaX * -1) +  (deltaY * -1)
                
                elif deltaX < 0:
                    diferenca = (deltaX * -1) + deltaY
                
                elif deltaY < 0:
                    diferenca = deltaX + (deltaY * -1)
                
                else:
                    diferenca = deltaX + deltaY
            
            elif i == 2 and labirinto[clydY - 1][clydX] != '#' and (clydX != passadoClydX or (clydY - 1) != passadoClydY) and labirinto[clydY - 1][clydX] != '_' :
                deltaX = clydX- posicaoX
                deltaY = (clydY - 1) - posicaoY
                
                if deltaX < 0 and deltaY < 0:
                    diferenca = (deltaX * -1) +  (deltaY * -1)
                
                elif deltaX < 0:
                    diferenca = (deltaX * -1) + deltaY
                    
                elif deltaY < 0:
                    diferenca = deltaX + (deltaY * -1)
                
                else:
                    diferenca = deltaX + deltaY
            
            elif i == 3 and labirinto[clydY + 1][clydX] != '#' and (clydX != passadoClydX or (clydY + 1) != passadoClydY) and labirinto[clydY + 1][clydX] != '_':
                deltaX = clydX - posicaoX
                deltaY = (clydY + 1) - posicaoY
                
                if deltaX < 0 and deltaY < 0:
                    diferenca = (deltaX * -1) +  (deltaY * -1)
                                    
                elif deltaX < 0:
                    diferenca = (deltaX * -1) + deltaY
                
                elif deltaY < 0:
                    diferenca = deltaX + (deltaY * -1)
                
                else:
                    diferenca = deltaX + deltaY
                            
            caminho[i] = diferenca         
                
    elif poder == False:
        #Calculo para verificar se clyd esta dentro do raio de alcance do pacman
        raio = 7
        deltaX = clydX - pacmanX
        deltaY = clydY - pacmanY
        
        raio *= raio
        deltaX *= deltaX
        deltaY *= deltaY
        posicao = deltaX + deltaY
        #se a posição for maior que o raio o fantasma esta fora da area de alcance do pacman
        if posicao > raio:        
            #faz o calculo das possiveis possições para cehgar ate o pacman 
            for i in range(4):
                diferenca = 1000
                #verefica a esquerda
                if i == 0 and labirinto[clydY][clydX - 1] != '#' and ((clydX - 1) != passadoClydX or clydY != passadoClydY) and labirinto[clydY][clydX - 1] != '_':
                    deltaX = (clydX - 1) - pacmanX
                    deltaY = clydY - pacmanY

                    if deltaX < 0 and deltaY < 0:
                        diferenca = (deltaX * -1) + (deltaY * -1)
                    
                    elif deltaX < 0:
                        diferenca = (deltaX * -1) + deltaY
                    
                    elif deltaY < 0:
                        diferenca = deltaX + (deltaY * -1)
                    
                    else:
                        diferenca = deltaX + deltaY    
                #verefica a direita
                elif i == 1 and labirinto[clydY][clydX + 1] != '#' and ((clydX + 1) != passadoClydX or clydY != passadoClydY) and labirinto[clydY][clydX + 1] != '_':
                    deltaX = (clydX + 1) - pacmanX
                    deltaY = clydY - pacmanY

                    if deltaX < 0 and deltaY < 0:
                        diferenca = (deltaX * -1) + (deltaY * -1)
                    
                    elif deltaX < 0:
                        diferenca = (deltaX * -1) + deltaY
                    
                    elif deltaY < 0:
                        diferenca = deltaX + (deltaY * -1)
                    
                    else:
                        diferenca = deltaX + deltaY
                #Verefica para cima
                elif i == 2 and labirinto[clydY - 1][clydX] != '#' and (clydX != passadoClydX or (clydY - 1) != passadoClydY) and labirinto[clydY - 1][clydX] != '_':
                    deltaX = clydX - pacmanX
                    deltaY = (clydY - 1) - pacmanY

                    if deltaX < 0 and deltaY < 0:
                        diferenca = (deltaX * -1) + (deltaY * -1)
                    
                    elif deltaX < 0:
                        diferenca = (deltaX * -1) + deltaY
                    
                    elif deltaY < 0:
                        diferenca = deltaX + (deltaY * -1)
                    
                    else:
                        diferenca = deltaX + deltaY
                #Verefica em baixo
                elif i == 3 and labirinto[clydY + 1][clydX] != '#' and (clydX != passadoClydX or (clydY + 1) != passadoClydY) and labirinto[clydY + 1][clydX] != '_':
                    deltaX  = clydX - pacmanX
                    deltaY = (clydY + 1)- pacmanY

                    if deltaX < 0 and deltaY < 0:
                        diferenca = (deltaX * -1) + (deltaY * -1)
                    
                    elif deltaX < 0:
                        diferenca = (deltaX * -1) + deltaY
                    
                    elif deltaY < 0:
                        diferenca = deltaX + (deltaY * -1)
                    
                    else:
                        diferenca = deltaX + deltaY                
                #Guarda e diferençã entre de distacia do fantasmas e do pacman
                caminho[i] = diferenca                
        
        #caso o fantamas esteja dentro da area de alcançe do pacman
        else:
            #faz o calculo das possiveis possições para cehgar ate o pacman 
            for i in range(4):
                posicaoX = random.randint(1, 26)
                posicaoY = random.randint(1, 29)
                diferenca = 1000
                #verefica a esquerda
                if i == 0 and labirinto[clydY][clydX - 1] != '#' and ((clydX - 1) != passadoClydX or clydY != passadoClydY) and labirinto[clydY][clydX - 1] != '_':
                    deltaX = (clydX - 1) - posicaoX
                    deltaY = clydY - posicaoY

                    if deltaX < 0 and deltaY < 0:
                        diferenca = (deltaX * -1) + (deltaY * -1)
                    
                    elif deltaX < 0:
                        diferenca = (deltaX * -1) + deltaY
                    
                    elif deltaY < 0:
                        diferenca = deltaX + (deltaY * -1)
                    
                    else:
                        diferenca = deltaX + deltaY    
                #verefica a direita
                elif i == 1 and labirinto[clydY][clydX + 1] != '#' and ((clydX + 1) != passadoClydX or clydY != passadoClydY) and labirinto[clydY][clydX + 1] != '_':
                    deltaX = (clydX + 1) - posicaoX
                    deltaY = clydY - posicaoY

                    if deltaX < 0 and deltaY < 0:
                        diferenca = (deltaX * -1) + (deltaY * -1)
                    
                    elif deltaX < 0:
                        diferenca = (deltaX * -1) + deltaY
                    
                    elif deltaY < 0:
                        diferenca = deltaX + (deltaY * -1)
                    
                    else:
                        diferenca = deltaX + deltaY
                #Verefica para cima
                elif i == 2 and labirinto[clydY - 1][clydX] != '#' and (clydX != passadoClydX or (clydY - 1) != passadoClydY) and labirinto[clydY - 1][clydX] != '_':
                    deltaX = clydX - posicaoX
                    deltaY = (clydY - 1) - posicaoY

                    if deltaX < 0 and deltaY < 0:
                        diferenca = (deltaX * -1) + (deltaY * -1)
                    
                    elif deltaX < 0:
                        diferenca = (deltaX * -1) + deltaY
                    
                    elif deltaY < 0:
                        diferenca = deltaX + (deltaY * -1)
                    
                    else:
                        diferenca = deltaX + deltaY
                #Verefica em baixo
                elif i == 3 and labirinto[clydY + 1][clydX] != '#' and (clydX != passadoClydX or (clydY + 1) != passadoClydY) and labirinto[clydY + 1][clydX] != '_':
                    deltaX = clydX - posicaoX
                    deltaY = (clydY + 1) - posicaoY

                    if deltaX < 0 and deltaY < 0:
                        diferenca = (deltaX * -1) + (deltaY * -1)
                    
                    elif deltaX < 0:
                        diferenca = (deltaX * -1) + deltaY
                    
                    elif deltaY < 0:
                        diferenca = deltaX + (deltaY * -1)
                    
                    else:
                        diferenca = deltaX + deltaY                
                #Guarda e diferençã entre de distacia do fantasmas e do pacman
                caminho[i] = diferenca
                
        #Escolhe o menor caminho calculado
    menor = 1000
    for  i in range(4):
        if caminho[i] < menor:
            menor = caminho[i]
            indiceCaminho = i
                
    #realiza a mudaça de coordana escolhida
    #Para a esquerda
    if indiceCaminho == 0:
        labirinto[clydY][clydX] = clydAtual
        passadoClydX = clydX
        passadoClydY = clydY
        clydX -= 1
        if labirinto[clydY][clydX] != 'B' and labirinto[clydY][clydX] != 'P' and labirinto[clydY][clydX] != 'I' and labirinto[clydY][clydX] != '4' and labirinto[clydY][clydX] != ':' and labirinto[clydY][clydX] != 'ᗧ':
            clydAtual = labirinto[clydY][clydX]
        
        if clydY == 14 and clydX == 0:
            clydX = 26

        #Para a direita
    elif indiceCaminho == 1:
        labirinto[clydY][clydX] = clydAtual
        passadoClydX = clydX
        passadoClydY = clydY
        clydX += 1
        if labirinto[clydY][clydX] != 'B' and labirinto[clydY][clydX] != 'P' and labirinto[clydY][clydX] != 'I' and labirinto[clydY][clydX] != '4' and labirinto[clydY][clydX] != ':'  and labirinto[clydY][clydX] != 'ᗧ' :
            clydAtual = labirinto[clydY][clydX]
        
        if clydY == 14 and clydX == 26:
            clydX = 1            
    #Para a cima
    elif indiceCaminho == 2:
        labirinto[clydY][clydX] = clydAtual
        passadoClydX = clydX
        passadoClydY = clydY
        clydY -= 1
        if labirinto[clydY][clydX] != 'B' and labirinto[clydY][clydX] != 'P' and labirinto[clydY][clydX] != 'I' and labirinto[clydY][clydX] != '4' and labirinto[clydY][clydX] != ':' and labirinto[clydY][clydX] != 'ᗧ':
            clydAtual = labirinto[clydY][clydX]            

    #Para a baixo 
    elif indiceCaminho == 3:
        labirinto[clydY][clydX] = clydAtual
        passadoClydX = clydX
        passadoClydY = clydY
        clydY += 1
        if labirinto[clydY][clydX] != 'B' and labirinto[clydY][clydX] != 'P' and labirinto[clydY][clydX] != 'I' and labirinto[clydY][clydX] != '4' and labirinto[clydY][clydX] != ':' and labirinto[clydY][clydX] != 'ᗧ':
            clydAtual = labirinto[clydY][clydX]        
                
    return clydY, clydX, clydAtual, passadoClydY, passadoClydX
