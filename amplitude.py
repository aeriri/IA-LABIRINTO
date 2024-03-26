from pyamaze import maze, agent, textLabel, COLOR
from collections import deque

def amplitude(m, start=None):
    #este algoritmo avança pelos nós mais próximos do início e do nó corrente enquanto é executado
    if start is None: # caso inicio seja vazio, pega inicio padrao da biblioteca (canto inferior direito)
        start = (m.rows, m.cols)
    frontier = deque() #fila para armazenar nos a serem explorados    
    frontier.append(start) #joga inicio na fila
    amplitudePath = {} #vetor para armazenar nós pais de cada nó
    explored = [start] #nos explorados
    procura = [] #caminho de procura

    while len(frontier) > 0:
        currCell = frontier.popleft() #remove o nó da esquerda, que é o primeiro a ser explorado
        if currCell == m._goal: #se o nó atual é o objetivo, para de andar
            break
        for d in 'ESNW': #ESWN sao as direções de andamento possíveis. Norte, Sul, Leste, Oeste
            if m.maze_map[currCell][d]: #verifica se é possivel andar na próxima direção
                #calcula indice da próxima célula:(X, Y)
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell) #joga próximo nó a fila de exploração
                explored.append(childCell) #joga próximo nó em nós explorados
                amplitudePath[childCell] = currCell #configura o pai do próximo nó
                procura.append(childCell) #registra ordem de busca. para primeiro andamento no grafo
    cell = m._goal
    while cell != start:
        cell = amplitudePath[cell]
    return procura, amplitudePath #retorna ordem de busca e o caminho mais curto realmente percorrido
