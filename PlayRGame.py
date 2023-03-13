from unidecode import unidecode
from utils.data import *


def play():
    tries = 4
    guessed = False
    jogadores_chutados = []
    
    
    jogador = df.sample()
    name = unidecode(jogador['Name'].to_string(index=False)).lower().split(' ')
    answer = jogador['Name'].to_string(index=False)
    pos = jogador['Position'].to_string(index=False)
    country = jogador['Country'].to_string(index=False)
    club = jogador['Club'].to_string(index=False)
    idx = 0

    while not guessed and tries > 0:
        if tries == 4:
            print('Welcome to PlayR! Try to guess the Premier League footballer.\n')
            print('Position: ' + pos)
        guess = input('\nGuess the PlayR: ').lower()
        if len(guess) <= 1:
            print('Your guess is invalid or too short.')


        if guess in name:
            guessed = True
        elif guess in jogadores_chutados:
            print('You already guessed that player, try again!')        
        else:
            jogadores_chutados.append(guess)    
            if tries > 2:    
                print('Wrong! Here goes another tip:\n')
            if tries == 2:
                print('Last chance!, think carefully.\n')

            if idx == 0:
                print('Position: ' + pos)
                print('Country: ' + country)                
            elif idx == 1:
                print('Position: ' + pos)
                print('Country: ' + country)
                print('Club: ' + club)
            idx += 1
            tries -= 1
    if guessed:
        print('Well done, you got it!')
    else:
        print(f'Game over! the PlayR was {answer}')



play()
