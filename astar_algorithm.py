distancia_linha_reta = [
        [0,    10,   18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1,  16.7, 27.3, 27.6, 29.8], # Estação E1
        [10,   0,    8.5,  14.8, 26.6, 29.1, 26.1, 17.3, 10,   3.5,  15.5, 20.9, 19.1, 21.8], # Estação E2
        [18.5, 8.5,  0,    6.3,  18.2, 20.6, 17.6, 13.6, 9.4,  10.3, 19.5, 19.1, 12.1, 16.6], # Estação E3
        [24.8, 14.8, 6.3,  0,    12,   14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4], # Estação E4
        [36.4, 26.6, 18.2, 12,   0,    3,    2.4,  19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9], # Estação E5
        [38.8, 29.1, 20.6, 14.4, 3,    0,    3.3,  22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2], # Estação E6
        [35.8, 26.1, 17.6, 11.5, 2.4,  3.3,  0,    20,   23,   27.3, 34.2, 25.7, 12.4, 15.6], # Estação E7
        [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20,   0,    8.2,  20.3, 16.1, 6.4,  22.7, 27.6], # Estação E8
        [17.6, 10,   9.4,  12.6, 23.3, 25.7, 23,   8.2,  0,    13.5, 11.2, 10.9, 21.2, 26.6], # Estação E9
        [9.1,  3.5,  10.3, 16.7, 28.2, 30.3, 27.3, 20.3, 13.5, 0,    17.6, 24.2, 18.7, 21.2], # Estação E10
        [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0,    14.2, 31.5, 35.5], # Estação E11
        [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4,  10.9, 24.2, 14.2, 0,    28.8, 33.6], # Estação E12
        [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0,    5.1],  # Estação E13
        [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1,  0]     # Estação E14
    ]

# Multiplica por 2 para acharmos o tempo (2 min por km andado)
def time_min(matrix):
    return [[element * 2 for element in line] for line in matrix]

heuristic_table = time_min(distancia_linha_reta)

# Função para retornar os vizinhos
def get_neighbors(v):
    if v in matrix_dist:
        return matrix_dist[v]
    else:
        return None

def AStar(partida, destino):
    open_list = []                        
    open_list.append(partida)         
    closed_list = []

    # Valor somado das distâncias até o momento
    g_score = []
    g_score[partida] = 0 # A distância da estação inicial até ela mesma é 0              

    while len(open_list) > 0: 
        # O nódulo com menor valor de f, inicializado como "None"
        current_winner = None
        
        for v in open_list:
            # índices na matriz de heurística
            estacao_winner = current_winner[0] - 1 
            estacao_destino = destino[0] - 1
            estacao_atual = v[0] - 1

            if current_winner == None or ((g_score[v] + heuristic_table[estacao_atual][estacao_destino]) < (g_score[current_winner] + heuristic_table[estacao_winner][estacao_destino])):
                current_winner = v;
                print(f'Nó atual: {current_winner}')

        # Alterar isso daqui pra o negativo e colocar o for dentro do if 
        # Se n é o nó de destino
        if (current_winner == destino):
            print(f'Done!')

        open_list.remove(current_winner)
        closed_list.append(current_winner)

        # Número da estação atual
        estacao_current = current_winner[0]

        # Checar os vizinhos
        for (estacao, distancia, linha) in get_neighbors(estacao_current): 
            vizinho = (estacao, linha) # Pegamos somente o número da estação vizinha e a linha
            if vizinho not in open_list and vizinho not in closed_list:
                open_list.append(vizinho)  