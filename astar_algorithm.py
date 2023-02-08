def reconstruct_path(closed_list, current, partida):
  total_path = []
  #print(closed_list)

  total_path.append(current)

  while current != partida:
    total_path.append(closed_list[current])
    current = closed_list[current]
  #total_path.append(partida)
  for i in range (0,len(total_path),1):
    print(total_path[len(total_path)- 1 - i])

  #while current in closed_list:
   # current = closed_list[current]
   # total_path.prepend(current)
  #print(total_path)
  #print('foi')
  #return total_path

def failure():
  print("Não há caminho possível")

distancia_linha_reta = { 
    1: {1: 0,     2: 10,   3: 18.5, 4: 24.8, 5: 36.4, 6: 38.8, 7: 35.8, 8: 25.4, 9: 17.6,  10: 9.1,  11: 16.7, 12: 27.3, 13: 27.6, 14: 29.8}, # Partindo da Estação E1
    2: {1: 10,    2: 0,    3: 8.5,  4: 14.8, 5: 26.6, 6: 29.1, 7: 26.1, 8: 17.3, 9: 10,    10: 3.5,  11: 15.5, 12: 20.9, 13: 19.1, 14: 21.8}, # Partindo da Estação E2
    3: {1: 18.5,  2: 8.5,  3: 0,    4: 6.3,  5: 18.2, 6: 20.6, 7: 17.6, 8: 13.6, 9: 9.4,   10: 10.3, 11: 19.5, 12: 19.1, 13: 12.1, 14: 16.6}, # Partindo da Estação E3
    4: {1: 24.8,  2: 14.8, 3: 6.3,  4: 0,    5: 12,   6: 14.4, 7: 11.5, 8: 12.4, 9: 12.6,  10: 16.7, 11: 23.6, 12: 18.6, 13: 10.6, 14: 15.4}, # Partindo da Estação E4
    5: {1: 36.4,  2: 26.6, 3: 18.2, 4: 12,   5: 0,    6: 3,    7: 2.4,  8: 19.4, 9: 23.3, 10: 28.2,  11: 34.2, 12: 24.8, 13: 14.5, 14: 17.9}, # Partindo da Estação E5
    6: {1: 38.8,  2: 29.1, 3: 20.6, 4: 14.4, 5: 3,    6: 0,    7: 3.3,  8: 22.3, 9: 25.7, 10: 30.3,  11: 36.7, 12: 27.6, 13: 15.2, 14: 18.2}, # Partindo da Estação E6
    7: {1: 35.8,  2: 26.1, 3: 17.6, 4: 11.5, 5: 2.4,  6: 3.3,  7: 0,    8: 20,   9: 23,   10: 27.3,  11: 34.2, 12: 25.7, 13: 12.4, 14: 15.6}, # Partindo da Estação E7
    8: {1: 25.4,  2: 17.3, 3: 13.6, 4: 12.4, 5: 19.4, 6: 22.3, 7: 20,   8: 0,    9: 8.2,  10: 20.3,  11: 16.1, 12: 6.4,  13: 22.7, 14: 27.6}, # Partindo da Estação E8
    9: {1: 17.6,  2: 10,   3: 9.4,  4: 12.6, 5: 23.3, 6: 25.7, 7: 23,   8: 8.2,  9: 0,    10: 13.5,  11: 11.2, 12: 10.9, 13: 21.2, 14: 26.6}, # Partindo da Estação E9
    10: {1: 9.1,  2: 3.5,  3: 10.3, 4: 16.7, 5: 28.2, 6: 30.3, 7: 27.3, 8: 20.3, 9: 13.5, 10: 0,     11: 17.6, 12: 24.2, 13: 18.7, 14: 21.2}, # Partindo da Estação E10
    11: {1: 16.7, 2: 15.5, 3: 19.5, 4: 23.6, 5: 34.2, 6: 36.7, 7: 34.2, 8: 16.1, 9: 11.2, 10: 17.6,  11: 0,    12: 14.2, 13: 31.5, 14: 35.5}, # Partindo da Estação E11
    12: {1: 27.3, 2: 20.9, 3: 19.1, 4: 18.6, 5: 24.8, 6: 27.6, 7: 25.7, 8: 6.4,  9: 10.9, 10: 24.2,  11: 14.2, 12: 0,    13: 28.8, 14: 33.6}, # Partindo da Estação E12
    13: {1: 27.6, 2: 19.1, 3: 12.1, 4: 10.6, 5: 14.5, 6: 15.2, 7: 12.4, 8: 22.7, 9: 21.2, 10: 18.7,  11: 31.5, 12: 28.8, 13: 0,    14: 5.1},  # Partindo da Estação E13
    14: {1: 29.8, 2: 21.8, 3: 16.6, 4: 15.4, 5: 17.9, 6: 18.2, 7: 15.6, 8: 27.6, 9: 26.6, 10: 21.2,  11: 35.5, 12: 33.6, 13: 5.1,  14: 0},    # Partindo da Estação E14
    
}

#distancia_linha_reta = [
#        [0,    10,   18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1,  16.7, 27.3, 27.6, 29.8], # Estação E1
#        [10,   0,    8.5,  14.8, 26.6, 29.1, 26.1, 17.3, 10,   3.5,  15.5, 20.9, 19.1, 21.8], # Estação E2
#        [18.5, 8.5,  0,    6.3,  18.2, 20.6, 17.6, 13.6, 9.4,  10.3, 19.5, 19.1, 12.1, 16.6], # Estação E3
#        [24.8, 14.8, 6.3,  0,    12,   14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4], # Estação E4
#        [36.4, 26.6, 18.2, 12,   0,    3,    2.4,  19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9], # Estação E5
#        [38.8, 29.1, 20.6, 14.4, 3,    0,    3.3,  22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2], # Estação E6
#        [35.8, 26.1, 17.6, 11.5, 2.4,  3.3,  0,    20,   23,   27.3, 34.2, 25.7, 12.4, 15.6], # Estação E7
#        [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20,   0,    8.2,  20.3, 16.1, 6.4,  22.7, 27.6], # Estação E8
#        [17.6, 10,   9.4,  12.6, 23.3, 25.7, 23,   8.2,  0,    13.5, 11.2, 10.9, 21.2, 26.6], # Estação E9
#        [9.1,  3.5,  10.3, 16.7, 28.2, 30.3, 27.3, 20.3, 13.5, 0,    17.6, 24.2, 18.7, 21.2], # Estação E10
#        [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0,    14.2, 31.5, 35.5], # Estação E11
#        [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4,  10.9, 24.2, 14.2, 0,    28.8, 33.6], # Estação E12
#        [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0,    5.1],  # Estação E13
#        [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1,  0]     # Estação E14
#]

distancia_real = {
#   e : [(n, d, l), (n', d', l')]
    #   e - a estação da qual se parte
    #   n - a estação na qual se pode chegar a partir de n
    #   d - o tempo que leva de n até e
    #   l - a linha que vai de n até e
    1 : [(2, 20, 'azul')],
    2 : [(3, 17, 'azul'), (1, 20, 'azul'), (9, 20, 'amarela'), (10, 7, 'amarela')],
    3 : [(2, 17, 'azul'), (4, 12.6, 'azul'), (9, 18.8, 'vermelha'), (13, 37.4, 'vermelha')],
    4 : [(3, 12.6, 'azul'), (5, 26, 'azul'), (8, 30.6, 'verde'), (13, 25.6, 'verde')],
    5 : [(4, 26, 'azul'), (6, 6, 'azul'), (7, 4.8, 'amarela'), (8, 60, 'amarela')],
    6 : [(5, 6, 'azul')],
    7 : [(5, 4.8, 'amarela')],
    8 : [(5, 60, 'amarela'), (4, 30.6, 'verde'), (9, 19.2, 'amarela'), (12, 12.8, 'verde')],
    9 : [(8, 19.2, 'amarela'), (2, 20, 'amarela'), (3, 18.8, 'vermelha'), (11, 24.4, 'vermelha')],
    10: [(2, 7, 'amarela')],
    11: [(9, 24.4, 'vermelha')],
    12: [(8, 12.8, 'verde')],
    13: [(3, 37.4, 'vermelha'), (4, 25.6, 'verde'), (14, 10.2, 'verde')],
    14: [(13, 10.2, 'verde')]
}


# Multiplica por 2 para acharmos o tempo (2 min por km andado)
def time_min(dict):
  dict_tempos = {1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}, 9: {}, 10: {}, 11: {}, 12: {}, 13: {}, 14: {}}
  for i in range (1,15,1):
    for j in range (1,15,1):
      dict_tempos[i][j] = dict[i][j] * 2
  return dict_tempos

heuristic_table = time_min(distancia_linha_reta)

# Função para retornar os vizinhos
def get_neighbors(v):
    if v in distancia_real:
        return distancia_real[v]
    else:
        return None

def AStar(partida, destino):
    # partida é o número da estação inicial
    # destino é o número da estaçãoo final
    # linha é a linha na qual se encontra no início

    open_list = []            
    open_list.append(partida) #Acrescentando o nó de partida

    closed_list = {} # Para cada nó "n", closed_list[n] é o nó que imediatamente o precedeu no caminho mais "barato" a partir do início
                     # closed_list[n] = (estacao, linha), tupla com estação da qual partiu e linha pela qual chegou

    # Valor somado das distâncias até o momento
    g_score = {} # Para cada nó "n", g_score[n] é o custo do caminho mais barato do início até n que se conhece atualmente
    for i in range(1,15,1):
        g_score[i] = float('inf')
    g_score[partida] = 0 # A distância da estação inicial até ela mesma é 0

    f_score = {} # Para cada nó "n", f_score[n] é o custo do nó calculado da seguinte maneira: f_score[n] = g_score[n] + heuristic_table[n - 1][destino - 1]
    for i in range(1,15,1):
        f_score[i] = float('inf')
    f_score[partida] = heuristic_table[partida][destino]
  
    while len(open_list) > 0: 
        current = None
        # O nódulo com menor valor de f, inicializado como "None"
        #####current_winner = None

        for no_inexplorado in open_list:
            # índices na matriz de heurística
            #####estacao_winner = current_winner[0] - 1 
            #####estacao_destino = destino[0] - 1
            #####estacao_atual = v[0] - 1

            #print(f'f_score[no_inexplorado] = {f_score[no_inexplorado]} e f_score[current] {f_score[current]}')
            if current == None or f_score[no_inexplorado] < f_score[current]:
                current = no_inexplorado;
                print(f'Nó atual: {current}')

        # Alterar isso daqui pra o negativo e colocar o for dentro do if 
        # Se n é o nó de destino
        if (current == destino):
            print(f'Done!')
            return reconstruct_path(closed_list, current, partida) # função de reconstruir o caminho do nó de partida até o nó de chegada

        open_list.remove(current)
        
        #####closed_list[current_winner[0]] = .
        #####closed_list.append(current_winner)

        # Número da estação atual
        #####estacao_current = current_winner[0]

        # Checar os vizinhos
        for (estacao_vizinho, tempo_vizinho, linha_vizinho) in get_neighbors(current):
          tentative_g_score = g_score[current] + tempo_vizinho
          if tentative_g_score < g_score[estacao_vizinho]:
            closed_list[estacao_vizinho] = current
            #print(closed_list)
            g_score[estacao_vizinho] = tentative_g_score
            f_score[estacao_vizinho] = tentative_g_score + heuristic_table[estacao_vizinho - 1][destino - 1]
            if estacao_vizinho not in open_list:
              open_list.append(estacao_vizinho)

    return failure()

def main():
    AStar(1,14)

main()
