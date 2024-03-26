from pyamaze import maze,agent,textLabel,COLOR

def profundidade(m,start=None):
    #este algoritmo avança o máximo possível em cada ramificação
    #antes de precisar retroceder
    if start is None:
        start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    profundidadePath={}
    procura=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        procura.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                profundidadePath[child]=currCell
        if poss>1: # indica se é uma célula de decisão. ficará vermelha no grafo
            m.markCells.append(currCell)
    cell=m._goal
    while cell!=start:
        cell=profundidadePath[cell]
    return procura,profundidadePath #retorna ordem de busca e o caminho realmente percorrido
