from pyamaze import maze,agent,textLabel,COLOR
import amplitude as amp
import profundidade as prof
import profundidadeLimitada as profLim
import aprofundamentoIterativo as aprofIterative
import bidirecional as bi
import PySimpleGUI as sg
import multiprocessing

def labirintoNav(tipoBusca='AMPLITUDE',origem='', destino=''):
    m=maze(10,10)
    
    if origem == '':
        input_origem = '1,1'
    else:
        input_origem = origem

    if destino == '':
        input_destino = '10,10'
    else:
        input_destino = destino

    # splita string na virgula para passar como parametros para funcoes de busca
    x_orig, y_orig = map(int, input_origem.split(','))
    x_dest, y_dest = map(int, input_destino.split(','))
    
    m.CreateMaze(x_dest,y_dest) #cria labirinto com objetivo final na célula x_dest, y_dest

    if tipoBusca.upper() == 'AMPLITUDE':

        procura,amplitudePath=amp.amplitude(m,(x_orig,y_orig)) # ex: (x: 5, y: 1) => inicio da caminhada

        caminhadaInicial = agent(m,x_orig,y_orig,goal=(destino),footprints=True,shape='square',color=COLOR.green)  #procura do caminho certo
        caminho          = agent(m,x_dest,y_dest,goal=(origem),footprints=True,filled=True)
        
        m.tracePath({caminhadaInicial:procura},showMarked=True) #procura do caminho certo
        m.tracePath({caminho:amplitudePath})
        

        m.run()

    elif tipoBusca.upper() == 'PROFUNDIDADE':

        procura,profundidadePath=prof.profundidade(m,(x_orig,y_orig)) # ex: (x: 5, y: 1) => inicio da caminhada

        caminhadaInicial = agent(m,x_orig,y_orig,goal=(destino),footprints=True,shape='square',color=COLOR.green)  #procura do caminho certo
        caminho          = agent(m,x_dest,y_dest,goal=(origem),footprints=True,filled=True)
        
        m.tracePath({caminhadaInicial:procura},showMarked=True) #procura do caminho certo
        m.tracePath({caminho:profundidadePath})
        
        m.run()


    elif tipoBusca.upper() == 'PROFUNDIDADE LIMITADA':

        procura, profundidadePath = profLim.profundidade_limitada(m, (x_orig, y_orig), limit=15)

        caminhadaInicial = agent(m, x_orig, y_orig, goal=(x_dest, y_dest), footprints=True, shape='square', color=COLOR.green)
        caminho = agent(m, x_dest, y_dest, goal=(x_orig, y_orig), footprints=True, filled=True)
        inicioAoFim = agent(m, x_orig, y_orig, footprints=True, color=COLOR.yellow)
        m.tracePath({caminhadaInicial: procura}, showMarked=True)
        m.tracePath({caminho: profundidadePath})
        m.run()

    elif tipoBusca.upper() == 'APROFUNDAMENTO ITERATIVO':

        explorado, caminho, objetivoEncontrado = aprofIterative.aprofundamentoIterativo(m, (x_orig, y_orig))

        caminhoExplorado = agent(m, x_orig, y_orig, goal=(x_dest, y_dest), footprints=True, shape='square', color=COLOR.green)
        caminho2 = agent(m, x_dest, y_dest, goal=(x_orig, y_orig), footprints=True, filled=True)
        m.tracePath({caminhoExplorado: explorado})
        m.tracePath({caminho2: caminho})
        m.run()

    elif tipoBusca.upper() == 'BIDIRECIONAL':

        pontoEncontro, exploradoFrente, exploradoVolta = bi.buscaBidirecional(m, (x_orig, y_orig), (x_dest, y_dest))

        caminho1Frente = agent(m, x_orig, y_orig, goal=(x_dest, y_dest), footprints=True, shape='square', color=COLOR.green)
        caminho2Volta = agent(m, x_dest, y_dest, goal=(x_orig, y_orig), footprints=True, filled=True)
        m.tracePath({caminho1Frente: exploradoFrente})
        m.tracePath({caminho2Volta: exploradoVolta})
        m.run()


def main():
    #cria o layout com combo e inputs de origem e destino
    layout = [
        [sg.Text('Escolha o algoritmo de busca:')],
        [sg.Combo(['AMPLITUDE', 'PROFUNDIDADE', 'PROFUNDIDADE LIMITADA', 'APROFUNDAMENTO ITERATIVO', 'BIDIRECIONAL'], key='-ALGORITMO-')],
        [sg.Text('Origem:'), sg.InputText(key='-ORIGEM-')],
        [sg.Text('Destino:'), sg.InputText(key='-DESTINO-')],
        [sg.Button('OK'), sg.Button('Cancelar')]
    ]

    # cria janela que terá o layout
    window = sg.Window('Selecione o Algoritmo de Busca', layout)

    while True:
        # le os inputs do usuario
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
        elif event == 'OK': # utiliza os inputs para poder chamar as buscas.
                            # necessario utilizar multiprocessing para evitar colisao com janela da biblioteca pyamaze
                            # desse modo, a primeira janela aberta é fechada antes de abrir a segunda para renderizar o grafo

            algoritmo = values['-ALGORITMO-']
            origem = values['-ORIGEM-']
            destino = values['-DESTINO-']
            window.close()
            maze_process = multiprocessing.Process(target=labirintoNav, args=(algoritmo,origem,destino))
            maze_process.start()


    #fecha janela
    window.close()

if __name__ == '__main__':
    main() #chama main