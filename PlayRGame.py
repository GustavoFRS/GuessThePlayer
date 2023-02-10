from data import *
from unidecode import unidecode


def play():
    tentativas = 4
    acertou = False
    jogadores_chutados = []
    
    jogador = df.sample()
    nome = unidecode(jogador['Nome'].to_string(index=False)).lower().split(' ')
    resposta = jogador['Nome'].to_string(index=False)
    pos = jogador['Posição'].to_string(index=False)
    country = jogador['País'].to_string(index=False)
    club = jogador['Clube'].to_string(index=False)
    idx = 0

    while not acertou and tentativas > 0:
        if tentativas == 4:
            print('Bem vindo ao PlayR! Tente adivinhar o jogador. Somente jogadores da Premier League são válidos.\n')
            print('Posição: ' + pos)
        chute = input('\nAdivinhe o Jogador: ').lower()
        if len(chute) <= 1:
            print('Seu chute é inválido ou muito curto.')


        if chute in nome:
            acertou = True
        elif chute in jogadores_chutados:
            print('Você já adivinhou esse jogador, tente novamente!')        
        else:
            jogadores_chutados.append(chute)    
            if tentativas > 2:    
                print('Errado! Aqui vai mais uma dica:\n')
            if tentativas == 2:
                print('Última chance!, pense com cuidado.\n')

            if idx == 0:
                print('Posição: ' + pos)
                print('País: ' + country)                
            elif idx == 1:
                print('Posição: ' + pos)
                print('País: ' + country)
                print('Clube: ' + club)
            idx += 1
            tentativas -= 1
    if acertou:
        print('Parabéns, você acertou!')
    else:
        print(f'Acabaram suas chances! o jogador era o {resposta}')



play()
