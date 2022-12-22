# Trabalho final - Batalha navall
#
# Arquivo principal
#
# Grupo composto por:
#
# Gabriel Messias Marques Eiras - DRE: 118143172
#
#


# Importando funções do arquivo de funções auxiliares
from funcoes import *

# #Tabuleiro dos dois jogadores para implementação
tabuleiro_inicial = [
    [["  ", "  A B C D E F G H I J"],['  1 '],['  2 '],['  3 '],['  4 '],['  5 '],['  6 '],['  7 '],['  8 '],['  9 '],['  10']],
    [["  ", "  A B C D E F G H I J"],['  1 '],['  2 '],['  3 '],['  4 '],['  5 '],['  6 '],['  7 '],['  8 '],['  9 '],['  10']]
            ]
# Tabuleiro para marcação das posições dos navios
tabuleiro_navios = [
    [["  ", "  A B C D E F G H I J"],['  1 '],['  2 '],['  3 '],['  4 '],['  5 '],['  6 '],['  7 '],['  8 '],['  9 '],['  10']],
    [["  ", "  A B C D E F G H I J"],['  1 '],['  2 '],['  3 '],['  4 '],['  5 '],['  6 '],['  7 '],['  8 '],['  9 '],['  10']]
            ]
# Tabuleiro contendo as posições livres
tabuleiro_livre = [
    [["  ", "  A B C D E F G H I J"],['  1 '],['  2 '],['  3 '],['  4 '],['  5 '],['  6 '],['  7 '],['  8 '],['  9 '],['  10']],
    [["  ", "  A B C D E F G H I J"],['  1 '],['  2 '],['  3 '],['  4 '],['  5 '],['  6 '],['  7 '],['  8 '],['  9 '],['  10']]
            ]


# Declaração das listas e dicionários
# Dicionário vazio dos navios
navios_1 = {}
navios_2 = {}

# Lista contendo as posições livres
posicoes_livres_1 = []
posicoes_livres_2 = []

# Lista contendo as marcações no tabuleiro do jogador (será imprimido na tela)
tabuleiro_jogador_1 =[]
tabuleiro_jogador_2 =[]

# Lista contendo as posições dos navios em cada tabuleiro
tabuleiro_navios_1 = []
tabuleiro_navios_2 = []


# Lista com nome dos navios
navios_lista = [
    "porta-avião",
    "navio-tanque",
    "contratorpedeiro",
    "submarino",
]

# Dicionário contendo o tamanho de cada navio
navios_tamanho = {
    "porta-avião":5 ,
    "navio-tanque":4 ,
    "contratorpedeiro":3 ,
    "submarino":2 ,
}

# Contagem de pontos dos jogadores. Cada embarcação acumula 1 ponto.
pontos_player =[
    0,
    0
]

# Informações sobre a quantidade de navios afundados pelo jogador 1
navios_afundados_1 = {
    "porta-avião":0,
    "navio-tanque":0 ,
    "contratorpedeiro":0 ,
    "submarino":0 ,
}

# Informações sobre a quantidade de navios afundados pelo jogador 2
navios_afundados_2 = {
    "porta-avião":0,
    "navio-tanque":0 ,
    "contratorpedeiro":0 ,
    "submarino":0 ,
}


# Dicionário com o nome de cada navio e a lista de suas posições em cada tabuleiro
navio_1_marcacao = {
    "porta-avião":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino":[],
}

navio_2_marcacao = {
    "porta-avião":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino":[],
}

#Adicionando as posições livre na lista posicoes_livre de cada jogador            
gerar_posicoes_livres(posicoes_livres_1)
gerar_posicoes_livres(posicoes_livres_2)

# Gerando os tabuleiros            
gerar_tabuleiros(tabuleiro_inicial,tabuleiro_navios,tabuleiro_livre)

# Tabuleiro dos jogadores
tabuleiro_jogador_1 = tabuleiro_inicial[0][:]
tabuleiro_jogador_2 = tabuleiro_inicial[1][:]

# Tabuleiro para posicionamento dos navios;
tabuleiro_navios_1 = tabuleiro_navios[0][:]
tabuleiro_navios_2 = tabuleiro_navios[1][:]

        
# Criando os dicionários para os navios no tabuleiro 1 e no tabuleiro 2 para iniciar o jogo
cria_dicionario_navios(navios_1,1,posicoes_livres_1,posicoes_livres_2)
cria_dicionario_navios(navios_2,2,posicoes_livres_1,posicoes_livres_2)

# Marcar as posições dos navios, contido no dicionario navios_1 e navios_2 nos tabuleiros dos navios 1 e 2
marcar_navios_tabuleiro(navios_1,tabuleiro_navios_1)
marcar_navios_tabuleiro(navios_2,tabuleiro_navios_2)



# Monstrando o tabuleiro na tela    
mostrar_tabuleiro(atualiza_tabuleiro(tabuleiro_jogador_1,tabuleiro_jogador_2))

# Inicio do programa
def main():
    
    nome = ""
    tamanho = 0
    n = False
    
    #informações sobre o jogo e mensagem de bem-vindo.
    bem_vindo()
    
    while True:
        
        # Caso seja a vez do jogador 1, ou seja, quando n == 0, a jogada é realizada no tabuleiro_jogador_2, para acertar o tabuleiro do oponente                
        tabuleiro_jogador = tabuleiro_jogador_1 if int(n) == 1 else tabuleiro_jogador_2
        navios_afundados = navios_afundados_1 if int(n) == 0 else navios_afundados_2
        
        # Referencia do jogador como sendo o valor inteiro do bool n
        player = int(n)    
        print('\n')
        
        # Input do usuário
        tiro = input('>> Ataque do jogador {}: '.format(int(n)+1))
        print('\n')
        
        if tiro.lower() == "sair":
            # Sair do jogo
            print("Saindo...")
            break
        
        elif tiro.lower() == "navios":
            # Mostrar as embarcações atingidas
            print("Embarcações atigindas: ")
            print("\n")
        
            for navio in navios_afundados:
                print(navio +":", end=" ")
                print(navios_afundados[navio])
        
        elif tiro.lower() == "reiniciar":
            # Reiniciar o jogo (incompleto :/)
            
            print('Reiniciando partida...')
            
            # reset_tabuleiros(tabuleiro_inicial,tabuleiro_navios,tabuleiro_livre,tabuleiro_jogador_1,tabuleiro_jogador_2)
            # reset_navios(navios_1,navios_2)
            # reset_posicoes_livre(posicoes_livres_1,posicoes_livres_2)
            # reset_tab_navios(tabuleiro_navios_1,tabuleiro_navios_2)
            # reset_marcacao(navio_1_marcacao,navio_2_marcacao)
            # reset_pontos(pontos_player)
            # reset_navios_afundados(navios_afundados_1,navios_afundados_2)
            
            # gerar_posicoes_livres(posicoes_livres_1)
            # gerar_posicoes_livres(posicoes_livres_2)
            
            # gerar_tabuleiros(tabuleiro_inicial,tabuleiro_navios,tabuleiro_livre)
            
            # atualiza_lista(tabuleiro_jogador_1,tabuleiro_jogador_2,tabuleiro_navios_1,tabuleiro_navios_2,tabuleiro_inicial,tabuleiro_navios)
            
            # cria_dicionario_navios(navios_1,1,posicoes_livres_1,posicoes_livres_2)
            # cria_dicionario_navios(navios_2,2,posicoes_livres_1,posicoes_livres_2)
            
            # marcar_navios_tabuleiro(navios_1,tabuleiro_navios_1)
            # marcar_navios_tabuleiro(navios_2,tabuleiro_navios_2)
            
            # mostrar_tabuleiro(atualiza_tabuleiro(tabuleiro_jogador_1,tabuleiro_jogador_2))
            
            # main()
            break
        else:    
            
            if valida_tiro(tiro):
                # Verifica o input informado. Tratamendo de dados
                linha = int(tiro[1:])
                coluna = str(tiro[0])
                
                if verifica_tabuleiro(tabuleiro_jogador,linha,coluna):
                    # verifica posição no tabuleiro
                    if encontrou_navio(linha,coluna,player,tabuleiro_navios_1,tabuleiro_navios_2):
                        # verifica se há um navio na posição informada
                        nome_e_tamanho = nome_e_tamanho_navio(coluna,linha,player,navios_1,navios_2)
                        
                        atinge_navio(coluna,linha,player,navios_1,navios_2)
                        modifica_tabuleiro(tabuleiro_jogador,linha,coluna)
                        mostrar_tabuleiro(atualiza_tabuleiro(tabuleiro_jogador_1,tabuleiro_jogador_2))  
                        
                        nome = str(nome_e_tamanho[0])
                        tamanho = int(nome_e_tamanho[1])-1
                        
                        if tamanho == 0:
                            # Mensagem para caso afunde totalmente uma embarcação e marcação de pontos
                            
                            print("Parabéns! Você afundou um {}!".format(nome))
                            
                            pontos_player[player] += 1
                            navios_afundados[nome] += 1
                           
                            if pontos_player[player] == 10:
                                # Vence quem derrubar 10 navios primeiro (total de navios)
                                # Cada navio derrubado é adicionado 1 ponto ao jogador.
                                
                                print(">> Vencedor: Jogador {}".format(n))
                                print("Jogador {} destruiu todas as embarcações!".format(n))
                                
                                break
                                
                        print(">>> Você atirou em {}{} e acertou uma embarcação!".format(coluna.upper(),linha)) 
                        
                        if tamanho > 0: 
                            print("Restam apenas {} parte(s) para afundá-lo totalmente!".format(tamanho))
                       
                        n = not n
                    
                    else:
                        
                        modifica_tabuleiro(tabuleiro_jogador,linha,coluna,"*")
                        mostrar_tabuleiro(atualiza_tabuleiro(tabuleiro_jogador_1,tabuleiro_jogador_2))  
                        
                        print(">>> Você atirou em {}{} (tiro na água)".format(coluna.upper(),linha))  
                    
                    n = not n


# Iniciar o jogo automaticamente
if __name__ == "__main__":
    main()
