import pygame
import WConio2 as Wc
# import random
import time
import os
pygame.mixer.init()
from labirinto import *
from ghosts import *
from movimentos import *

# main
os.system("cls")
labirinto = []
pastilhas = 0
vidaAtual = False
loop = 0
pontos = 0
poder = False
temporizador = 0
opcaoMenu = 1000
#personagens
pacman = 'ᗧ'
blink = 'B'
pink = 'P'
inky = 'I'
opcao = ' '
listajogadores = []
jogador = {"nome": " ", "pontos": 0}
melhorPontos = [jogador]

# esta criando o labirinto
for i in range(31):
    labirinto.append([])
    for j in range(28):
        labirinto[i].append(0)
while opcaoMenu != 0:
    indiciePontuacao = 0
    print("""
  ########      ######      ##########        ##       ##     ######      ##       ##
  ##     ##    ##    ##     ##                ###     ###    ##    ##     ###      ##
  ##     ##    ##    ##     ##                ####   ####    ##    ##     ####     ##
  ########     ########     ##       ######   ## ## ## ##    ########     ## ##    ##
  ##           ##    ##     ##                ##  ###  ##    ##    ##     ##  ##   ##
  ##           ##    ##     ##                ##       ##    ##    ##     ##   ##  ##
  ##           ##    ##     ##########        ##       ##    ##    ##     ##    #####
""")
    print("="*50)
    print("0 - Sair do jogo")
    print("1 - jogar")
    print("2 - Melhores Pontuções")
    print("="*50)
    opcaoMenu = int(input("Digite sua opção: "))
    
    if opcaoMenu == 1:
        print("="*50)
        print("0 - voltar")
        print("1 - Normal")
        print("2 - dificil")
        print("="*50)
        opcaoMenu = int(input("Digite sua opção: "))        
        
        if opcaoMenu ==  1:
            prepararLabiritnto(labirinto)
            pastilhas = colocarPastilhas(pastilhas, labirinto)
            vidas = 3
            pontos = 0
            temporizador = 0
            poder = False
            pacmanX = 13
            pacmanY = 23
            blinkX = 13
            blinkY = 11
                
            passadoBlinkX = blinkX
            passadoBlinkY = blinkY
            blinkAtual = ' '
            blinkVivo = True
            blink = 'B'
            
            pinkX = 11
            pinkY = 14
        
            passadoPinkX = pinkX
            passadoPinkY = pinkY
            pinkAtual = ' '
            pinkVivo = True
            pink = 'P'
            inkyX = 13
            inkyY = 14
            inky = 'I'
            passadoinkyX = inkyX
            passadoinkyY = inkyY
            inkyAtual = ' '
            inkyVivo = True
            clyd = 'C'
            clydY = 14
            clydX = 15
            passadoClydY = clydY
            passadoClydX = clydX
            clydAtual = ' '
            clydVivo = True
            loop = 0
            
            labirinto[pacmanY][pacmanX] = pacman
            labirinto[blinkY][blinkX] = blink
            labirinto[pinkY][pinkX] = pink
            labirinto[inkyY][inkyX] = inky
            labirinto[clydY][clydX] = clyd

            
            while pastilhas > 0 and vidas >= 0:
                #Renicia os personagens apos a morte da pacman
                if vidas >= 0 and  vidaAtual == False:
                    poder = False
                    temporizador = 0
                    vidaAtual = True
                    vidas -= 1
                    somInicio = pygame.mixer.Sound(r'audios\02. Start Music.mp3')
                    somMorte =  pygame.mixer.Sound(r"audios\13. PAC-MAN - Eating The Ghost.mp3")
                    pacmanX = 13
                    pacmanY = 23

                    blinkX = 13
                    blinkY = 11
        
                    passadoBlinkX = blinkX
                    passadoBlinkY = blinkY
                    blinkAtual = ' '
                    blinkVivo = True
                    blink = 'B'

                    pinkX = 11
                    pinkY = 14
        
                    passadoPinkX = pinkX
                    passadoPinkY = pinkY
                    pinkAtual = ' '
                    pinkVivo = True
                    pink = 'P'
        
                    inkyX = 13
                    inkyY = 14

                    inky = 'I'
                    passadoinkyX = inkyX
                    passadoinkyY = inkyY
                    inkyAtual = ' '
                    inkyVivo = True
        
                    clyd = 'C'
                    clydY = 14
                    clydX = 15
                    passadoClydY = clydY
                    passadoClydX = clydX
                    clydAtual = ' '
                    clydVivo = True
                
                    labirinto[pacmanY][pacmanX] = pacman
                    labirinto[blinkY][blinkX] = blink
                    labirinto[pinkY][pinkX] = pink
                    labirinto[inkyY][inkyX] = inky
                    labirinto[clydY][clydX] = clyd
                    
                    #limpa qualquer anomalia dentro do labrinto
                    limparLabirinto(labirinto, blinkAtual, pinkAtual, inkyAtual, clydAtual)
                    mostrarLabirinto(labirinto)
                    mostrarVidas(vidas, pontos)
                    loop = 0
                    opcao = 'a'
                    somInicio.play()
                    time.sleep(4)
    
                else:
                    #Temporiza o tempo que a pastilha grande esta funcionando 
                    if temporizador == 50:
                        poder = False
                        temporizador = 0
                        blink = 'B'
                        pink = 'P'
                        inky = 'I'
                        clyd = 'C'
        
                    # ressusita os fantasmas comidos
                    if blinkVivo == False or pinkVivo == False or inkyVivo == False: 
                        if blinkY == 14 and blinkX == 13:
                            blinkVivo = True
                            blink = 'B'
                            labirinto[blinkY][blinkX] = ' '
                            blinkY = 11
                
                        if pinkY == 14 and pinkX == 13:
                            pinkVivo = True
                            pink ='P'
                            labirinto[passadoPinkY][pinkX] = ' '
                            pinkY = 11
                
                        if inkyY == 14 and inkyX == 13:
                            inkyVivo = True
                            inky = 'I'
                            labirinto[inkyY][inkyX] = ' '
                            inkyY = 11
                        
                        if clydY == 14 and clydX == 13:
                            clydVivo = True
                            clyd = 'C'
                            labirinto[clydY][clydX] = ' '
                            clydY = 11

            # mostra os labirinto e as vidas para o jogador
                    mostrarLabirinto(labirinto)
                    mostrarVidas(vidas, pontos)
        
                    time.sleep(0.2)
                    if(Wc.kbhit()):  #verifica se uma tecla foi apertada
                        codigo, opcao = Wc.getch()  #captura a tecla apertada 
        
                #Faz o pacman se mover
                    pacmanY, pacmanX, pastilhas, pontos, poder = movientacao(opcao, pacmanY, pacmanX, pacman, pastilhas, labirinto, pontos, poder)
                    
                    blink, pink, inky, clyd, blinkVivo, pinkVivo, inkyVivo, clydVivo, vidaAtual ,pontos= interacoes(poder, pacmanY, pacmanX, blinkY, blinkX, pinkY, pinkX, inkyY, inkyX, clydY, clydX, blink, pink, inky, clyd, blinkVivo, pinkVivo, inkyVivo, clydVivo, vidaAtual, pontos)

                #Escolhe onde o proximo movento do Fantasma  
                    blinkY, blinkX, passadoBlinkY, passadoBlinkX, blinkAtual, blinkVivo = movimentoBlink(passadoBlinkX, passadoBlinkY, blinkX, blinkY, pacmanX, pacmanY, labirinto, poder, blinkAtual, blinkVivo)
                    
                    #libera os fantasmas de acordo com o tempo 
                    if loop >= 10:
                        
                        #coloca o fantamas fora da caixa
                        if loop == 10:
                            labirinto[pinkY][pinkX] = ' '
                            pinkY = 11
                            pinkX = 13
                            
                        #Escolhe onde o proximo movento do Fantasma
                        pinkY, pinkX, passadoPinkY, passadoPinkX, pinkAtual, pinkVivo = movimentoPink(pinkX, pinkY, pacmanX, pacmanY, labirinto, passadoPinkX, passadoPinkY, opcao, pinkAtual, poder, pinkVivo)
                    
                    #libera os fantasmas de acordo com o tempo 
                    if loop >= 15:    
                        
                        #coloca o fantamas fora da caixa
                        if loop == 15:
                            labirinto[inkyY][inkyX] = ' '
                            inkyY = 11
                            inkyX = 13
                            
                        #Escolhe onde o proximo movento do Fantasma    
                        inkyY, inkyX, passadoinkyY, passadoinkyX, inkyAtual = movimentoInky(inkyX, inkyY, blinkX, blinkY, pacmanX, pacmanY, labirinto, passadoinkyX, passadoinkyY,inkyAtual, poder, inkyVivo)
                    
                    #libera os fantasmas de acordo com o tempo 
                    if loop >= 20:
                        
                        #coloca o fantamas fora da caixa
                        if loop == 20:
                            labirinto[clydY][clydX] = ' '
                            clydY = 11
                            clydX = 13
                            
                        #Escolhe onde o proximo movento do Fantasma
                        clydY, clydX, clydAtual, passadoClydY, passadoClydX = movimentoClyd(clydX, clydY, passadoClydX, passadoClydY, clydAtual, clydVivo, poder, pacmanX, pacmanY, labirinto)
                    
                    #Realiza todas as intereções dos fantasmas e pacman
                    blink, pink, inky, clyd, blinkVivo, pinkVivo, inkyVivo, clydVivo, vidaAtual, pontos = interacoes(poder, pacmanY, pacmanX, blinkY, blinkX, pinkY, pinkX, inkyY, inkyX, clydY, clydX, blink, pink, inky, clyd, blinkVivo, pinkVivo, inkyVivo, clydVivo, vidaAtual, pontos)

                    #faz a movimentação do fantasmas
                    labirinto[pacmanY][pacmanX] = pacman
                    labirinto[blinkY][blinkX] = blink 
                    labirinto[pinkY][pinkX] = pink
                    labirinto[inkyY][inkyX] = inky
                    labirinto[clydY][clydX] = clyd
                                  
                #Atualiza o temporizador
                    loop += 1
                    if poder == True:
                        temporizador += 1
                        
                    pastilhas = contadorPastilhas(pastilhas, labirinto)
                # Som do quando o pacman morre
                    if vidaAtual == False:
                        mostrarLabirinto(labirinto)
                        somMorte.play()
                        time.sleep(3)
                    print(temporizador)
                    print(blinkAtual, pinkAtual, inkyAtual, clydAtual)
            
            print("Game-Over") 
            for i in range(30):
                for j in range(28):
                    labirinto[i][j] = ' '
                    
            #Quando o jogo acaba pergunta o nome de jogador e guarda a pontuaçãllo na lisa de jogadores
            for i in range(len(melhorPontos)):
                #vereica se o jogador esta entre os dez melhores
                if pontos > melhorPontos[i]['pontos']:
                    nome = input("digite seu nome: ")
                    jogador = {"nome":nome, "pontos": pontos}
                    listajogadores.append(jogador)
                    continue     
                        
        elif opcaoMenu == 2:
            prepararLabiritnto(labirinto)
            pastilhas = 0
            pastilhas = colocarPastilhas(pastilhas, labirinto)
            vidas = 1
            pontos = 0
            temporizador = 0
            poder = False
            pacmanX = 13
            pacmanY = 23
            blinkX = 13
            blinkY = 11
                
            passadoBlinkX = blinkX
            passadoBlinkY = blinkY
            blinkAtual = ' '
            blinkVivo = True
            blink = 'B'
            
            pinkX = 11
            pinkY = 14
        
            passadoPinkX = pinkX
            passadoPinkY = pinkY
            pinkAtual = ' '
            pinkVivo = True
            pink = 'P'
            inkyX = 13
            inkyY = 14
            inky = 'I'
            passadoinkyX = inkyX
            passadoinkyY = inkyY
            inkyAtual = ' '
            inkyVivo = True
            clyd = 'C'
            clydY = 14
            clydX = 15
            passadoClydY = clydY
            passadoClydX = clydX
            clydAtual = ' '
            clydVivo = True
            loop = 0
            labirinto[pacmanY][pacmanX] = pacman
            labirinto[blinkY][blinkX] = blink
            labirinto[pinkY][pinkX] = pink
            labirinto[inkyY][inkyX] = inky
            labirinto[clydY][clydX] = clyd
            
            while pastilhas > 0 and vidas >= 0:
                #Renicia os personagens apos a morte da pacman
                if vidas >= 0 and  vidaAtual == False:
                    poder = False
                    temporizador = 0
                    vidaAtual = True
                    vidas -= 1
                    somInicio = pygame.mixer.Sound(r'audios\02. Start Music.mp3')
                    somMorte =  pygame.mixer.Sound(r"audios\15. Fail.mp3")
                    pacmanX = 13
                    pacmanY = 23

                    blinkX = 13
                    blinkY = 11
        
                    passadoBlinkX = blinkX
                    passadoBlinkY = blinkY
                    blinkAtual = ' '
                    blinkVivo = True
                    blink = 'B'

                    pinkX = 11
                    pinkY = 14
        
                    passadoPinkX = pinkX
                    passadoPinkY = pinkY
                    pinkAtual = ' '
                    pinkVivo = True
                    pink = 'P'
        
                    inkyX = 13
                    inkyY = 14

                    inky = 'I'
                    passadoinkyX = inkyX
                    passadoinkyY = inkyY
                    inkyAtual = ' '
                    inkyVivo = True
        
                    clyd = 'C'
                    clydY = 14
                    clydX = 15
                    passadoClydY = clydY
                    passadoClydX = clydX
                    clydAtual = ' '
                    clydVivo = True
                
                    labirinto[pacmanY][pacmanX] = pacman
                    labirinto[blinkY][blinkX] = blink
                    labirinto[pinkY][pinkX] = pink
                    labirinto[inkyY][inkyX] = inky
                    labirinto[clydY][clydX] = clyd
                    
                    #limpa qualquer anomalia dentro do labrinto
                    limparLabirinto(labirinto, blinkAtual, pinkAtual, inkyAtual, clydAtual)
                    mostrarLabirinto(labirinto)
                    mostrarVidas(vidas, pontos)
                    loop = 0
                    opcao = 'a'
                    somInicio.play()
                    time.sleep(4)
    
                else:
                    #Temporiza o tempo que a pastilha grande esta funcionando 
                    if temporizador == 25:
                        poder = False
                        temporizador = 0
                        blink = 'B'
                        pink = 'P'
                        inky = 'I'
                        clyd = 'C'
        
                    # ressusita os fantasmas comidos
                    if blinkVivo == False or pinkVivo == False or inkyVivo == False: 
                        if blinkY == 14 and blinkX == 13:
                            blinkVivo = True
                            blink = 'B'
                            labirinto[blinkY][blinkX] = ' '
                            blinkY = 11
                
                        if pinkY == 14 and pinkX == 13:
                            pinkVivo = True
                            pink ='P'
                            labirinto[passadoPinkY][pinkX] = ' '
                            pinkY = 11
                
                        if inkyY == 14 and inkyX == 13:
                            inkyVivo = True
                            inky = 'I'
                            labirinto[inkyY][inkyX] = ' '
                            inkyY = 11
                        
                        if clydY == 14 and clydX == 13:
                            clydVivo = True
                            clyd = 'C'
                            labirinto[clydY][clydX] = ' '
                            clydY = 11

            # mostra os labirinto e as vidas para o jogador
                    mostrarLabirinto(labirinto)
                    mostrarVidas(vidas, pontos)
        
                    time.sleep(0.2)
                    if(Wc.kbhit()):  #verifica se uma tecla foi apertada
                        codigo, opcao = Wc.getch()  #captura a tecla apertada 
        
                #Faz o pacman se mover
                    pacmanY, pacmanX, pastilhas, pontos, poder = movientacao(opcao, pacmanY, pacmanX, pacman, pastilhas, labirinto, pontos, poder)
                    
                    blink, pink, inky, clyd, blinkVivo, pinkVivo, inkyVivo, clydVivo, vidaAtual ,pontos= interacoes(poder, pacmanY, pacmanX, blinkY, blinkX, pinkY, pinkX, inkyY, inkyX, clydY, clydX, blink, pink, inky, clyd, blinkVivo, pinkVivo, inkyVivo, clydVivo, vidaAtual, pontos)

                #Escolhe onde o proximo movento do Fantasma  
                    blinkY, blinkX, passadoBlinkY, passadoBlinkX, blinkAtual, blinkVivo = movimentoBlink(passadoBlinkX, passadoBlinkY, blinkX, blinkY, pacmanX, pacmanY, labirinto, poder, blinkAtual, blinkVivo)
                    
                    #libera os fantasmas de acordo com o tempo 
                    if loop >= 10:
                        
                        #coloca o fantamas fora da caixa
                        if loop == 10:
                            labirinto[pinkY][pinkX] = ' '
                            pinkY = 11
                            pinkX = 13
                            
                        #Escolhe onde o proximo movento do Fantasma
                        pinkY, pinkX, passadoPinkY, passadoPinkX, pinkAtual, pinkVivo = movimentoPink(pinkX, pinkY, pacmanX, pacmanY, labirinto, passadoPinkX, passadoPinkY, opcao, pinkAtual, poder, pinkVivo)
                    
                    #libera os fantasmas de acordo com o tempo 
                    if loop >= 15:    
                        
                        #coloca o fantamas fora da caixa
                        if loop == 15:
                            labirinto[inkyY][inkyX] = ' '
                            inkyY = 11
                            inkyX = 13
                            
                        #Escolhe onde o proximo movento do Fantasma    
                        inkyY, inkyX, passadoinkyY, passadoinkyX, inkyAtual = movimentoInky(inkyX, inkyY, blinkX, blinkY, pacmanX, pacmanY, labirinto, passadoinkyX, passadoinkyY,inkyAtual, poder, inkyVivo)
                    
                    #libera os fantasmas de acordo com o tempo 
                    if loop >= 20:
                        
                        #coloca o fantamas fora da caixa
                        if loop == 20:
                            labirinto[clydY][clydX] = ' '
                            clydY = 11
                            clydX = 13
                            
                        #Escolhe onde o proximo movento do Fantasma
                        clydY, clydX, clydAtual, passadoClydY, passadoClydX = movimentoClyd(clydX, clydY, passadoClydX, passadoClydY, clydAtual, clydVivo, poder, pacmanX, pacmanY, labirinto)
                    
                    #Realiza todas as intereções dos fantasmas e pacman
                    blink, pink, inky, clyd, blinkVivo, pinkVivo, inkyVivo, clydVivo, vidaAtual, pontos = interacoes(poder, pacmanY, pacmanX, blinkY, blinkX, pinkY, pinkX, inkyY, inkyX, clydY, clydX, blink, pink, inky, clyd, blinkVivo, pinkVivo, inkyVivo, clydVivo, vidaAtual, pontos)

                    #faz a movimentação do fantasmas
                    labirinto[pacmanY][pacmanX] = pacman
                    labirinto[blinkY][blinkX] = blink 
                    labirinto[pinkY][pinkX] = pink
                    labirinto[inkyY][inkyX] = inky
                    labirinto[clydY][clydX] = clyd
                                  
                #Atualiza o temporizador
                    loop += 1
                    if poder == True:
                        temporizador += 1
                        
                    pastilhas = contadorPastilhas(pastilhas, labirinto)
                # Som do quando o pacman morre
                    if vidaAtual == False:
                        mostrarLabirinto(labirinto)
                        somMorte.play()
                        time.sleep(3)
                    print(temporizador)
                    print(blinkAtual, pinkAtual, inkyAtual, clydAtual)
            pontos *= 2
            print("Game-Over") 
            for i in range(30):
                for j in range(28):
                    labirinto[i][j] = ' '            
            #Quando o jogo acaba pergunta o nome de jogador e guarda a pontuaçãllo na lisa de jogadores
            for i in range(len(melhorPontos)):
                #vereica se o jogador esta entre os dez melhores
                if pontos > melhorPontos[i]['pontos']:
                    nome = input("digite seu nome: ")
                    jogador = {"nome":nome, "pontos": pontos}
                    listajogadores.append(jogador)
                    continue

        elif opcaoMenu == 0:
            opcaoMenu = 1000        

    elif opcaoMenu == 2:
        print(listajogadores) 
        copiaLista = listajogadores.copy()
        indice = 0
        print("====================\n")
        print("Melhores Pontuações\n")            
        print("====================\n")  
        print("Jogador          Pontuação\n", end = " ")
        
        for i in range(11):
            maior = 0
            nome = " "
            for j in range(len(copiaLista)):
                if copiaLista[j]['pontos'] > maior:
                    maior = copiaLista[j]['pontos']
                    nome = copiaLista[j]['nome']
                    indice = i
                    jogador = {"nome": nome, "pontos": maior}
                    melhorPontos.append(jogador) 
            copiaLista[indice]['pontos'] = 0            
        
        if len(melhorPontos) == 1:
            for i in range(len(melhorPontos)):
                if melhorPontos[i]['pontos'] == 0 and melhorPontos[i]['nome'] == ' ':
                    del melhorPontos[i] 
                                          
        for i in range(len(melhorPontos)):
            print(f"{melhorPontos[i]['nome']}              {melhorPontos[i]['pontos']}")
    else:
        print("Opção invalida") 
               
print("Obrigado por jogar :}!!!!")
print("Criadores: Joâo Luiz Francisco, Mateus Damaceno Bueno e Otavio Magnenti de Sá")
