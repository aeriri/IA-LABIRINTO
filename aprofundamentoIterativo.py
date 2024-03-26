from pyamaze import maze, agent, textLabel, COLOR

def profundidadeLimitada(m, start=None, limit=10):
    if start is None:
        start = (m.rows, m.cols)
    explorado = [start]
    fronteira = [start]
    caminho = {}
    objetivoEncontrado = False
    current_depth = 0

    while fronteira and not objetivoEncontrado: #enquanto existir nós inexplorados e o objetivo não for atingido, continue
        if current_depth == limit: #se a profundidade atual for igual ao limite, pare
            break

        current_depth += 1 #incrementa profundidade atual
        next_fronteira = [] #lista de nós da próxima profundidade (<profundidade atual)

        for currCell in fronteira: #para cada no fronteiriço, ou seja, o ultimo
            if currCell == m._goal: #verifica se encontrou o objetivo. se encontrou, pare
                objetivoEncontrado = True
                break

            for d in 'ESNW':
                if m.maze_map[currCell][d]:
                    child = (currCell[0] + (d == 'S') - (d == 'N'), currCell[1] + (d == 'E') - (d == 'W'))
                    if child not in explorado:
                        explorado.append(child)
                        next_fronteira.append(child)
                        caminho[child] = currCell

        fronteira = next_fronteira #atualiza fronteira para próxima profundidade, para passar para a próxima navegação

    return explorado, caminho, objetivoEncontrado

def aprofundamentoIterativo(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    objetivoEncontrado = False
    depth_limit = 0

    while not objetivoEncontrado: #enquanto nao atingir o objetivo, continue a navegacao em profundidade limitada na fronteira estabelecida
        explorado, caminho, objetivoEncontrado = profundidadeLimitada(m, start, limit=depth_limit)
        depth_limit += 1

    return explorado, caminho, objetivoEncontrado
