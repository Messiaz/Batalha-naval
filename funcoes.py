from random import *

#referencia das colunas para associar a coluna em string com o seu número correspondente
letras_dicionario = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
}

# Referencia das colunas 2
colunas_tabuleiro = ["a","b","c","d","e","f","g","h","i","j"]

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


def gerar_posicoes_livres(tab_pos):
        """Função para gerar uma lista com posições livres para o tabuleiro informad (jogador 1 ou jogador 2)"""
        """list -> list"""
        """A função não gera retorno"""
        
        for c in range(0,10):
            for l in range(1,11):
                tab_pos.append(str(c)+str(l))
                
# Gerando os tabuleiros 
def gerar_tabuleiros(tabuleiro_inicial,tabuleiro_navios,tabuleiro_livre):
    """Função que gera uma lista de dois tabuleiros para print na tela"""
    """A função não gera retorno"""
    for x in range(1,11):
        for j in range(0,2):
            tabuleiro_inicial[j][x] = tabuleiro_inicial[j][x] + (["~"] * 10)
            tabuleiro_navios[j][x] = tabuleiro_navios[j][x] + (["~"] * 10)
            tabuleiro_livre[j][x] = tabuleiro_livre[j][x] + (["~"] * 10)
            
def mostrar_tabuleiro(tabuleiro):
    """Função que imprime na tela os dois tabuleiros"""
    """A função não gera retorno"""
    
    c = 0
    for linha in tabuleiro:
        # Concatenação das linhas com espaço em branco
        print(" ".join(linha))
        
        c+=1
        if c == 11:
            #Caso seja a última linha, adiciona o jogador do respectivo tabuleiro
            print((" "*9)+ "Jogador 1"+(" "*16)+"Jogador 2")
            print('\n')


def atualiza_tabuleiro(tabuleiro_1,tabuleiro_2):
    """Função que atualiza a marcação do tabuleiro_1 e tabuleiro_2 e retorna"""
    """uma lista contento as linhas dos dois tabuleiros em uma só"""
    """list, list -> list"""
    
    
    lista = []
    for i in range(11):
        lista = lista + [tabuleiro_1[i] + tabuleiro_2[i],]
    return lista

def modifica_tabuleiro(tabuleiro,linha,col,char="X"):
    """Função para marcação dos tiros nos tabuleiros"""
    """O argumento default é para caso acerte uma embarcação"""
    """A função não gera retorno"""
    

    # coluna = letra_para_numero(col.lower())
    coluna = letras_dicionario[col.lower()]
    tabuleiro[linha][coluna] = char
    
def verifica_tabuleiro(tabuleiro,linha,coluna):
    """Função que verifica a disponibilidade da posição [linha][coluna] e retorna True se não houver nenhuma marcação e False caso o espaço esteja ocupado """
    """list,int,str -> bool"""
    
    col = colunas_tabuleiro.index(coluna.lower()) + 1 
    if tabuleiro[linha][col] == "X" or tabuleiro[linha][col] == "*":
        
        print("Você já jogou nesse lugar, escolha outro!")
        return False
    return True

def valida_tiro(tiro):
    # Função de tratamento de dados do usuário
    """str -> bool"""
    
    if len(tiro) <2:
        #verifica se há mais de dois caracteres informados (linha e coluna)
    
        print("Informe um valor válido. (ex.: B6)")
        return False
    
    # Definição do valor da coluna (str)
    coluna = tiro[0].lower()
    
    # Definição do valor da linha (int)
    linha = tiro[1:]
    
    if len(linha) >1:
        if str(linha[1]) != "0":
            print("Valor inválido para linha. Informe um valor de 1-10")    
            return False
    
    if linha[0:].isalpha():
        print("Valor inválido para linha. Informe um valor de 1-10")
        return False
    
    if coluna not in "abcdefghij":
        if linha[0:].isalpha() or len(linha) == 0 or linha[0:] == " ":
            print("Informe uma entrada válida.(ex.: B6)")
            return False
        elif not linha[0:].isalpha() and linha[0:] not in range(1,11):
            print("Valor inválido para linha. Informe um valor de 1-10")
            return False
        print("Valor inválido para coluna. Informe um valor de A-J")
        return False
    elif int(linha[0:]) not in range(1,11):
        print("Valor inválido para linha. Informe um valor de 1-10")
        return False
    return True


def nome_e_tamanho_navio(coluna,linha,player,navios_1,navios_2):
    """Função que, dado os valores de coluna e linha, retorna o valor do nome e o tamanho da embarcação que o usuário (player) acertou"""
    """str,int,list,list,list -> tuple"""
    
    
    # analisa os navios do oponete, logo se player == 0 (jogador 1) analisará os navios_2
    pos_navios = navios_1 if player == 1 else navios_2
    
    coluna_informada = str(coluna).lower()
    linha_informada = int(linha)
    
    for nome_navio in navios_lista:
        if nome_navio != "porta-avião":
            for num_navio in range(len(pos_navios[nome_navio])):
                for posicao in range(len(pos_navios[nome_navio][num_navio])):
        
                    coluna_navio = str(pos_navios[nome_navio][num_navio][posicao][0])
                    linha_navio = int(pos_navios[nome_navio][num_navio][posicao][1:])
                    
                    if coluna_informada == coluna_navio and linha_informada == linha_navio:
                        return nome_navio,len(pos_navios[nome_navio][num_navio])
        
        else:
            
            for posicao in range(len(pos_navios[nome_navio])):
                coluna_navio = str(pos_navios[nome_navio][posicao][0])
                linha_navio = int(pos_navios[nome_navio][posicao][1:])
                
                if coluna_informada == coluna_navio and linha_informada == linha_navio:
                    return nome_navio, len(pos_navios[nome_navio])
                
    return " ",-1    

def atinge_navio(coluna,linha,player,navios_1,navios_2):
    """Função que atualiza o dicionário contendo as posições dos navios, deletando a sua respectiva posição depois de um acerto feito pelo usuário"""
    """Função não gera retorno"""
    
    pos_navio = navios_1 if player == 1 else navios_2
    
    coluna_informada = str(coluna).lower()
    linha_informada = int(linha)
    coluna_linha = str(coluna_informada) + str(linha_informada)
    
    for nome_navio in navios_lista:
        if nome_navio != "porta-avião":
            for num_navio in range(len(pos_navio[nome_navio])):
            
                if coluna_linha in pos_navio[nome_navio][num_navio]:
                    pos_navio[nome_navio][num_navio].remove(coluna_linha)
    
        else:
            if coluna_linha in pos_navio[nome_navio]:
                pos_navio[nome_navio].remove(coluna_linha)
                
def encontrou_navio(linha,coluna,player,tabuleiro_navios_1,tabuleiro_navios_2):
    # Função que retorna se o usuário encontrou um navio ou não no seu palpite de linah e coluna
    """int,str,list,list,list -> bool"""
    
    
    # tabuleiro a ser analisado é do oponente, logo se for o player 0 (jogador 1), analisa o tabuleiro_navios_2
    tabuleiro = tabuleiro_navios_1 if player == 1 else tabuleiro_navios_2
    
    col = str(coluna).lower()
    coluna_palpite = colunas_tabuleiro.index(col) + 1
    
    if tabuleiro[linha][coluna_palpite] == "X":
        return True
    else:
        return False

def marcar_navios_tabuleiro(dic,tabuleiro):
    """Função que gera o dicionário de posições para cada navio. O número de listas é igual a quantidade de navios que precisamos ter"""
    """Função não gera retorno"""
    
    for navio in dic:
        
        for i in range(len(dic[navio])):
            
            if navio != "porta-avião":
        
                for j in range(len(dic[navio][i])):
                    coluna = str(dic[navio][i][j][0])
                    linha = int(dic[navio][i][j][1:])
                    modifica_tabuleiro(tabuleiro,linha,coluna)
        
            else:
                coluna = str(dic[navio][i][0])
                linha = int(dic[navio][i][1:])
                modifica_tabuleiro(tabuleiro,linha,coluna)
                
def verifica_disponivel_vertical(tabuleiro,coluna,inicio,fim,posicoes_livres_1,posicoes_livres_2):
    """Função que verifica disponibilidade de marcar o tabuleiro dos navios na vertical. Retorna False se o espaço em questão já está ocupado """
    """list,str,int,int,list,list -> bool"""
    
    tabuleiro_posicoes = posicoes_livres_1 if tabuleiro == 1 else posicoes_livres_2

    for linha in range(inicio-1,fim+1):
        posicao = str(coluna) + str(linha)
        if posicao not in tabuleiro_posicoes:
            return False
    return True

def verifica_disponivel_horizontal(tabuleiro,linha,inicio,fim,posicoes_livres_1,posicoes_livres_2):
    """Função que verifica a disponibilidade de marcar o tabuleiro dos navios na Horizontal"""
    """list,int,int,int,list,list -> bool"""
    
    tabuleiro_posicoes = posicoes_livres_1 if tabuleiro == 1 else posicoes_livres_2

    for coluna in range(inicio-1,fim+1):
        posicao = str(coluna) + str(linha) 
        if posicao not in tabuleiro_posicoes:
            return False
    return True 

def atualiza_valores_vertical(tamanho):
    #Função que atualiza os valores de coluna, linha de começo e linha final para caso o espaço analisado esteja ocupado
    """int -> tuple(int,int,int)"""
    
    coluna = randint(0,9)
    começo = randint(1,10-tamanho)
    final = começo + tamanho
    return coluna,começo,final

def atualiza_valores_horizontal(tamanho):
    #Função que atualiza os valores de coluna, linha de começo e linha final para caso o espaço analisado esteja ocupado
    """int -> tuple(int,int,int)"""
    
    linha = randint(1,10)
    começo = randint(0,9-tamanho)
    final = começo + tamanho
    return linha,começo,final

def gerar_pos_navios(navio,tab_navio,posicoes_livres_1,posicoes_livres_2):
    """Função que gera uma lista contendo as posições possíveis para posicionar os navios. As posições são avaliadas a cada execução, avaliando sempre se o espaço analisado está ocupado."""
    """Função não gera retorno, apenas modifica a lista posicao_livre e posicao_lista""" 
    
    
    posicao_livre = posicoes_livres_1 if tab_navio == 1 else posicoes_livres_2
    
    tamanho = navios_tamanho[navio]
    horizontal = bool(randint(0,1))
    posicao_lista = []
    
    if not horizontal:
        
        # Gera barcos na vertical
        coluna,linha_comeco,linha_final = atualiza_valores_vertical(tamanho)
        while not verifica_disponivel_vertical(tab_navio,coluna,linha_comeco,linha_final,posicoes_livres_1,posicoes_livres_2):
            coluna,linha_comeco,linha_final = atualiza_valores_vertical(tamanho)
        
        for i in range(linha_comeco,linha_final):
            
            valor = str(coluna) + str(i)
            posicao_lista = posicao_lista + [str(colunas_tabuleiro[coluna]) + str(i)]
            posicao_livre.remove(valor)
                
    else:
        
        # Gera barcos na horizontal
        linha, coluna_comeco,coluna_final = atualiza_valores_horizontal(tamanho)
        while not verifica_disponivel_horizontal(tab_navio,linha,coluna_comeco,coluna_final,posicoes_livres_1,posicoes_livres_2):
            linha, coluna_comeco,coluna_final = atualiza_valores_horizontal(tamanho)    
        
        for i in range(coluna_comeco,coluna_final):
            valor = str(i) + str(linha)
            posicao_lista = posicao_lista + [str(colunas_tabuleiro[i]) + str(linha)]     
            posicao_livre.remove(valor)
            
    return posicao_lista

def bem_vindo():
    # Função de mensagem de bem-vindo e de informações inicias do jogo
    
    print("-"*10+"BATALHA NAVAL"+"-"*10)
    print("O objetivo é derrubar os 10 navios espalhados pelo tabuleiro. Cada navio afundado completamente vale 1 ponto.")
    print("\n")
    print("Os navios estão dividos em:\n>>> porta-avião, 1 unidade\n>>> navio-tanque, 2 unidades\n>>> contratorpedeiro, 3 unidades\n>>> submarino, 4 unidades")
    print("\n")
    print("O jogo é dado por turnos, cada jogador tem uma chance de acertar uma embarcação. Ao acertar, o jogador continua a jogada até errar.")
    print("Por favor, insira valores de coluna e linha, exemplo B3 ou b3.")
    
def cria_dicionario_navios(dicionario,tab_navio,posicoes_livres_1,posicoes_livres_2):
    """Função que criar o dicionário contento o nome do navio e a lista com a suas respectivas posições. O tamanho da lista é a quantidade de navios e o tamanho das sub-listas contidas nas listas é o tamanho de cada navio"""
    
    for i in navios_lista:
        dicionario[i] = gerar_pos_navios(i,tab_navio,posicoes_livres_1,posicoes_livres_2)
        
        if i == "navio-tanque":
            dicionario[i] = [gerar_pos_navios(i,tab_navio,posicoes_livres_1,posicoes_livres_2)]
            dicionario[i] = dicionario[i] + [gerar_pos_navios(i,tab_navio,posicoes_livres_1,posicoes_livres_2)]
            
        elif i == "contratorpedeiro":
            dicionario[i] = [gerar_pos_navios(i,tab_navio,posicoes_livres_1,posicoes_livres_2)]
            dicionario[i] = dicionario[i] + [gerar_pos_navios(i,tab_navio,posicoes_livres_1,posicoes_livres_2)]
            dicionario[i] = dicionario[i] + [gerar_pos_navios(i,tab_navio,posicoes_livres_1,posicoes_livres_2)]
            
        elif i == "submarino":
            dicionario[i] = [gerar_pos_navios(i,tab_navio,posicoes_livres_1,posicoes_livres_2)]
            dicionario[i] = dicionario[i] +[gerar_pos_navios(i,tab_navio,posicoes_livres_1,posicoes_livres_2)]
            dicionario[i] = dicionario[i] +[gerar_pos_navios(i,tab_navio,posicoes_livres_1,posicoes_livres_2)]
            dicionario[i] = dicionario[i] +[gerar_pos_navios(i,tab_navio,posicoes_livres_1,posicoes_livres_2)]
            

#Funções para resetar as listas inicias (incompleto)
def reset_tabuleiros(tabuleiro_inicial,tabuleiro_navios,tabuleiro_livre,tabuleiro_jogador_1,tabuleiro_jogador_2):
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
    
    tabuleiro_jogador_1 =[]
    tabuleiro_jogador_2 =[]
    
def reset_navios(navios_1,navios_2):
    navios_1 = {}
    navios_2 = {}
    
def reset_posicoes_livre(posicoes_livres_1,posicoes_livres_2):
    posicoes_livres_1 = []
    posicoes_livres_2 = []
    
    
def reset_tab_navios(tabuleiro_navios_1,tabuleiro_navios_2):
    tabuleiro_navios_1 = []
    tabuleiro_navios_2 = []
    
def reset_marcacao(navio_1_marcacao,navio_2_marcacao):    
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

def reset_pontos(pontos_player):
    pontos_player =[
        0,
        0
    ]

def reset_navios_afundados(navios_afundados_1,navios_afundados_2):
    navios_afundados_1 = {
    "porta-avião":0,
    "navio-tanque":0 ,
    "contratorpedeiro":0 ,
    "submarino":0 ,
    }

    navios_afundados_2 = {
        "porta-avião":0,
        "navio-tanque":0 ,
        "contratorpedeiro":0 ,
        "submarino":0 ,
    }

def atualiza_lista(tabuleiro_jogador_1,tabuleiro_jogador_2,tabuleiro_navios_1,tabuleiro_navios_2,tabuleiro_inicial,tabuleiro_navios):
    tabuleiro_jogador_1 = tabuleiro_inicial[0][:]
    tabuleiro_jogador_2 = tabuleiro_inicial[1][:]

    tabuleiro_navios_1 = tabuleiro_navios[0][:]
    tabuleiro_navios_2 = tabuleiro_navios[1][:]
