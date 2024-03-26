from pyamaze import maze, agent, textLabel, COLOR

def buscaBidirecional(m, start=None, goal=None):
    #algoritmo para realizar busca para os dois lados simultaneamente
    #retorna o ponto de encontro de ambos os caminhos (nao sei se esta correto)
    if start is None:
        start = (m.rows, m.cols)
    if goal is None:
        goal = m._goal

    frontier_forward = [start] #fronteira sentido partida -> objetivo
    fronteira_fim_inicio = [goal] #fronteira sentido objetivo -> partida
    exploradoInicioFim = [start] #nos explorados sentido partida -> objetivo
    exploradoFimInicio = [goal] #nos explorados sentido objetivo -> partida
    pontoEncontro = None

    while frontier_forward and fronteira_fim_inicio: #enquanto houver fronteiras em ambos os sentidos
        next_frontier_forward = []
        for currCell in frontier_forward:
            for d in 'ESNW':
                if m.maze_map[currCell][d]:
                    child = (currCell[0] + (d == 'S') - (d == 'N'), currCell[1] + (d == 'E') - (d == 'W'))
                    if child not in exploradoInicioFim: #verifica se o proximo nó ainda nao foi explorado (sentido partida -> objetivo)
                        exploradoInicioFim.append(child) #coloca proximo no na lista de explorados (sentido partida -> objetivo)
                        next_frontier_forward.append(child) #coloca proximo no na lista da proxima fronteira (sentido partida -> objetivo)
                        if child in exploradoFimInicio: #se o próximo nó não está na lista de explorados do sentido objetivo -> partida, define que o estado comum é o próximo nó
                            pontoEncontro = child
                            break

        frontier_forward = next_frontier_forward #atribui a proxima fronteira do proximo nivel a fronteira atual

        if pontoEncontro: # se houver estado comum, ou seja, se os caminhos se encontrarem, finaliza a busca
            break

        #realiza mesmas ações de busca porém no sentido objetivo->partida
        prox_fronteira_fim_inicio = []
        for currCell in fronteira_fim_inicio:
            for d in 'ESNW':
                if m.maze_map[currCell][d]:
                    child = (currCell[0] + (d == 'S') - (d == 'N'), currCell[1] + (d == 'E') - (d == 'W'))
                    if child not in exploradoFimInicio:
                        exploradoFimInicio.append(child)
                        prox_fronteira_fim_inicio.append(child)
                        if child in exploradoInicioFim:
                            pontoEncontro = child
                            break

        fronteira_fim_inicio = prox_fronteira_fim_inicio

        if pontoEncontro:
            break

    return pontoEncontro, exploradoInicioFim, exploradoFimInicio
