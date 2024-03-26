
from pyamaze import maze, agent, textLabel, COLOR

def profundidade_limitada(m, start=None, limit=15): #limite de profundidade: 15
  if start is None:
    start = (m.rows, m.cols)
  explored = [start]
  frontier = [start]
  profundidadePath = {}
  current_depth = 0 #profundidade atual na busca

  #enquanto há nós inexplorados e a profundidade for menor que o limite, continue explorando
  while len(frontier) > 0 and current_depth <= limit:
    currCell = frontier.pop()
    current_depth += 1 #incrementa a profundidade

    if currCell == m._goal:
      break
    for d in 'ESNW':
      if m.maze_map[currCell][d] == True:
        if d =='E':
            child=(currCell[0],currCell[1]+1)
        elif d =='W':
            child=(currCell[0],currCell[1]-1)
        elif d =='N':
            child=(currCell[0]-1,currCell[1])
        elif d =='S':
            child=(currCell[0]+1,currCell[1])

        if child in explored:
          continue
        explored.append(child) #marca o proximo nó como explorado
        frontier.append(child) #adiciona o próximo nó à fila de exploração
        profundidadePath[child] = currCell

  return explored, profundidadePath