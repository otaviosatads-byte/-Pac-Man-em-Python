import pygame          
def interacoes(poder, pacmanY, pacmanX, blinkY, blinkX, pinkY, pinkX, inkyY, inkyX, clydY, clydX, blink, pink, inky, clyd, blinkVivo, pinkVivo, inkyVivo, clydVivo, vidaAtual, pontos):
    #verefica se os fantasmas pegaram o pacman    
    if poder == False:
        if (blinkY == pacmanY and blinkX == pacmanX )and blinkVivo == True:
            vidaAtual = False
                          
        if (pinkY == pacmanY and pinkX == pacmanX) and pinkVivo == True:
            vidaAtual = False
            
        if (inkyY == pacmanY and inkyX == pacmanX) and inkyVivo == True:
            vidaAtual = False        
        
        if (clydY == pacmanY and clydX == pacmanX) and clydVivo == True:
            vidaAtual = False
            
    #Deixa os fantasmas fracos            
    if poder == True:
        if blinkVivo == True:
            blink = '4'
        
        if pinkVivo == True:
            pink = '4'
        
        if inkyVivo == True:
            inky = '4'
            
        if clydVivo == True:
            clyd = '4'
                  
    #Verifica se o pacman comeu algun fantasma
    if poder == True:
        if blinkX == pacmanX and blinkY == pacmanY and blinkVivo == True:
            blinkVivo = False
            pontos += 200
        if pinkX == pacmanX and pinkY == pacmanY and pinkVivo == True:
            pinkVivo = False
            pontos += 200

        if inkyX == pacmanX and inkyY == pacmanY and inkyVivo == True:
            inkyVivo = False
            pontos += 200

        if clydX == pacmanX and clydY == pacmanY and clydVivo == True:
            clydVivo =  False
            pontos += 200
            
    #transforma os fantasmas comido em apenas olhos                
    if blinkVivo == False:
        blink = ':'
    if pinkVivo == False:
        pink = ':'
    if inkyVivo == False:
        inky = ':'
    if clydVivo == False:
        clyd = ':'
        
    return blink, pink, inky, clyd, blinkVivo, pinkVivo, inkyVivo, clydVivo, vidaAtual, pontos

def movientacao(opcao, pacmanY, pacmanX, pacman, pastilhas, labirinto, pontos, poder):
    # A movimentacao que pacman fez de acordo com o usuario
    
    if opcao == 'w' or opcao == 'W':
        if labirinto[pacmanY - 1][pacmanX] == '#':
               labirinto[pacmanY][pacmanX] = pacman
        else:
            if labirinto[pacmanY -  1][pacmanX] == 'O':
                somMastigar.play()
                poder = True
                labirinto[pacmanY][pacmanX] = ' '
                pastilhas -= 1
                pacmanY -= 1
                labirinto[pacmanY][pacmanX] = pacman
                
            
            elif labirinto[pacmanY - 1][pacmanX] == 'o':
                somMastigar.play()
                labirinto[pacmanY][pacmanX] = ' '
                pacmanY -= 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
                pontos += 10
            
            elif labirinto[pacmanY][pacmanX] == '4':
                labirinto[pacmanY][pacmanX] = ' '
                pacmanY -= 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
                pontos += 10
            
            elif labirinto[pacmanY - 1][pacmanX] == ':':
                labirinto[pacmanY][pacmanX] = ' '
                pacmanY -= 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
                pontos += 10
            else: 
                labirinto[pacmanY][pacmanX] = ' '
                pacmanY -= 1
                labirinto[pacmanY][pacmanX] = pacman

    #usar alguma biblioteca para ignorar o camel case
    #transformar a entrada em minusculo ou maiusculo
    elif opcao == 'd' or opcao == 'D':
        if pacmanY == 14 and pacmanX == 27:
            labirinto[pacmanY][pacmanX] = ' '
            pacmanX = 1
            labirinto[pacmanY][pacmanX] = pacman        
        
        elif labirinto[pacmanY][pacmanX + 1] == '#':
            labirinto[pacmanY][pacmanX] = pacman        
                 
        else:
            if labirinto[pacmanY][pacmanX + 1] == 'O':
                somMastigar.play()
                poder = True
                labirinto[pacmanY][pacmanX] = ' '                
                pastilhas -= 1
                pacmanX += 1
                labirinto[pacmanY][pacmanX] = pacman
                
            elif labirinto[pacmanY][pacmanX + 1] == 'o':
                somMastigar.play()
                labirinto[pacmanY][pacmanX] = ' '
                pacmanX += 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
                pontos += 10
            elif labirinto[pacmanY][pacmanX + 1] == '4':
                labirinto[pacmanY][pacmanX] = ' '
                pacmanX += 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
                pontos += 10
            
            elif labirinto[pacmanY][pacmanX + 1] == ':':
                labirinto[pacmanY][pacmanX] = ' '
                pacmanX += 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
                pontos += 10
                
            else:
                labirinto[pacmanY][pacmanX] = ' '
                pacmanX += 1
                labirinto[pacmanY][pacmanX] = pacman
    
    elif opcao == 'a' or opcao == 'A':
        if labirinto[pacmanY][pacmanX - 1] == '#':
            labirinto[pacmanY][pacmanX] = pacman
        
        elif pacmanY == 14 and pacmanX == 0:
            labirinto[pacmanY][pacmanX] = ' '
            pacmanX = 26
            labirinto[pacmanY][pacmanX] = pacman                
            
        else:
            if labirinto[pacmanY][pacmanX - 1] == 'O':
                somMastigar.play()
                poder = True
                labirinto[pacmanY][pacmanX] = ' '
                pastilhas -= 1
                pacmanX -= 1
                labirinto[pacmanY][pacmanX] = pacman
                labirinto[pacmanY][pacmanX] = pacman
                
            elif labirinto[pacmanY][pacmanX - 1] == 'o':
                somMastigar.play()
                labirinto[pacmanY][pacmanX] = ' '
                pacmanX -= 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
                pontos += 10
            
            elif labirinto[pacmanY][pacmanX - 1] == '4':
                labirinto[pacmanY][pacmanX] = ' '
                pacmanX -= 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
                pontos += 10
            
            elif labirinto[pacmanY][pacmanX - 1] == ':':
                labirinto[pacmanY][pacmanX] = ' '
                pacmanX -= 1
                pastilhas -= 1
                labirinto[pacmanY][pacmanX] = pacman
                pontos += 10

            else:   
                labirinto[pacmanY][pacmanX] = ' '
                pacmanX -= 1
                labirinto[pacmanY][pacmanX] = pacman
    
    elif opcao == 's' or opcao == 'S':
        if labirinto[pacmanY + 1][pacmanX] == '#':
           labirinto[pacmanY][pacmanX] = pacman
        else:
            if labirinto[pacmanY + 1][pacmanX] == 'O':
                somMastigar.play()
                poder = True
                labirinto[pacmanY][pacmanX] = ' '                
                pastilhas -= 1
                pacmanY += 1
                labirinto[pacmanY][pacmanX] = pacman

            elif labirinto[pacmanY + 1][pacmanX] == 'o':
                somMastigar.play()
                labirinto[pacmanY][pacmanX] = ' '
                pacmanY += 1
                labirinto[pacmanY][pacmanX] = pacman
                pastilhas -=  1
                pontos += 10
            
            elif labirinto[pacmanY + 1][pacmanX] == '4':
                labirinto[pacmanY][pacmanX] = ' '
                pacmanY += 1
                labirinto[pacmanY][pacmanX] = pacman
                pastilhas -=  1
                pontos += 10
                
            elif labirinto[pacmanY + 1][pacmanX] == ':':
                labirinto[pacmanY][pacmanX] = ' '
                pacmanY += 1
                labirinto[pacmanY][pacmanX] = pacman
                pastilhas -=  1
                pontos += 10
        
            else:
                labirinto[pacmanY][pacmanX] = ' '
                pacmanY += 1
                labirinto[pacmanY][pacmanX] = pacman

    if labirinto[pacmanY][pacmanX] == '4' or labirinto[pacmanY][pacmanX] == ':': 
        labirinto[pacmanY][pacmanX] == ' ' 
    return pacmanY, pacmanX, pastilhas, pontos, poder 
 
