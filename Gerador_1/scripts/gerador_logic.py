import bge
import numpy
import os
import datetime
import shapely.geometry as geom
import mathutils

tamanho_gene = 60    
max_populacao = 100
tamanho_parceiros = 15;
posicao_inicial = (-200,297,2.5);

scene = bge.logic.getCurrentScene()
obj = bge.logic.getCurrentController().owner

coords = [(-128,297),(-420,294),(-442,289),(-469,277),(-481,257),(-482,238),(-469,217),(-448,184),(-455,157),(-475,134),(-499,102),(-514,40),(-499,-31),(-443,-91),(98,-380),(119,-383),(144,-376),(162,-357),

(204,-260),(202,-210),(182,-166),
(-41,99),
(-48,143),(-34,186),(-13,214),(18,233),(48,236),(117,235),
(164,224),(177,210),(181,197),(175,182),
(139,149),(130,128),(133,106),(143,89),(162,80),(189,80),(235,106),
(290,131),(310,135),(360,134),(383,130),(392,123),(397,114),(398,104),(394,96),(387,89),
(289,36),(259,-7),(252,-42),(259,-80),(279,-108),
(397,-228),(403,-233),(413,-236),(428,-236),(441,-226),
(495,-146),(506,-88),(506,-20),(487,60),(467,109),(423,155),
(185,279),(123,296),(83,301),
(-126,297)
]
line = geom.LineString(coords)

for i in range(0,len(line.coords)-1):
    from_pos = mathutils.Vector([line.coords[i][0], line.coords[i][1], 2])    # The start position is the cube's position (which is a vector)
    to_pos = mathutils.Vector([line.coords[i+1][0], line.coords[i+1][1], 2]) # Add another vector (1 over on the X axis) to the cube's position
    color = [1, 0, 0]   # Color of the line (Red, Green, Blue)
    bge.render.drawLine(from_pos, to_pos, color)    

def cria_novos_carros(populacao):
    altura = 700;
    largura = 100;
    a = 0;
    b = 0;
    numero = 1;
    carros = []
    cenario = []
    i = 0;
    bge.logic.getCurrentController().owner.worldPosition = posicao_inicial;
    for a in range(0,max_populacao):
        carro=scene.addObject('0',obj,0)
        cubo = scene.addObject('Empty',obj,0)
        carro['cubo'] = cubo;
        carro['sensor1'] = cubo.sensors['Ray']
        carro['sensor2'] = cubo.sensors['Ray2']
        cubo['carro'] = carro;
        cubo.applyRotation((0,0,1.5*1.5708),True)
        carro['force'] = a*5;
        carro.applyRotation((0,0,3*1.5708),True)
        carros.append(carro)
        cenario.append(cubo)
        carro['gene'] = populacao[i].tolist();
        carro['line'] = line;
        i=i+1;
        carro['pontuacao'] = 0;
        carro['init'] = False;
        
    bge.logic.getCurrentController().owner.worldPosition = (0,0,-22)
    return carros,cenario

def add_populacao(populacao,filho_1,filho_2):
    populacao = numpy.vstack((populacao,filho_1))
    populacao = numpy.vstack((populacao,filho_2))
    return populacao;

def cria_10_carros():
    altura = 700;
    largura = 100;
    a = 0;
    b = 0;
    numero = 1;
    carros = []
    cenario = []
    bge.logic.getCurrentController().owner.worldPosition = posicao_inicial;
    
    for a in range(0,max_populacao):
        carro = scene.addObject('0',obj,0)
        cubo = scene.addObject('Empty',obj,0)
        carro['cubo'] = cubo;
        carro['sensor1'] = cubo.sensors['Ray']
        carro['sensor2'] = cubo.sensors['Ray2']
        cubo['carro'] = carro;
        cubo.applyRotation((0,0,1.5*1.5708),True)
        carro.applyRotation((0,0,3*1.5708),True)
        carro['force'] = a*5;
        carros.append(carro)
        cenario.append(cubo)
        carro['line'] = line;
        carro['gene'] = (numpy.random.rand(tamanho_gene)*2-1).tolist()
        carro['pontuacao'] = 0;
        carro['init'] = False;
    
    bge.logic.getCurrentController().owner.worldPosition = (0,0,-22)
    return carros,cenario

def gera_lista_indices(inteiro):
    lista = []
    for i in range(0,inteiro):
        lista.append(i)
    return lista

def extrai_pontuacoes(carros):
    pontuacoes = []
    for carro in carros:
        pontuacoes.append(carro['pontuacao'])
    
    return pontuacoes

def gera_matrix_ganhos(carros,pontuacoes):
    matrix = numpy.asarray(carros[0]['gene'])
    for i in range(1,len(carros)):
        matrix = numpy.vstack((matrix,numpy.asarray(carros[i]['gene'])))
        
    matrix = numpy.hstack((matrix, numpy.asarray(pontuacoes).reshape(len(carros),1)))
    matrix = numpy.hstack((matrix, numpy.asarray(gera_lista_indices(len(carros))).reshape(len(carros),1)))
    return matrix

def mutacao(individuo):
    probabilidade_de_mutacao = 0.1;
    for i in range(len(individuo)):
        if(numpy.random.rand(1)<probabilidade_de_mutacao):
            individuo[i] = individuo[i] + (numpy.random.rand(1)[0]-0.5)*10 
    
    return individuo

def reproducao(matrix_ordenada):
    populacao = matrix_ordenada[0:2,:-2];
    parceiros = matrix_ordenada[0:tamanho_parceiros+1,:-2];
    duplas = []
    for i in range(0,tamanho_parceiros):
        for j in range(i+1,tamanho_parceiros):
            duplas.append([i,j])
    
    for i,j in duplas:
        if len(populacao)<=(max_populacao-2):
            [filho_1,filho_2] = cruza(parceiros[i],parceiros[j])
            filho_1 = mutacao(filho_1)
            filho_2 = mutacao(filho_2)
            populacao = add_populacao(populacao,filho_1,filho_2)
    
    return populacao

def cruza(pai,mae):
    ponto_de_troca = numpy.random.randint(len(pai))
    filho_1 = numpy.concatenate((pai[:ponto_de_troca],mae[ponto_de_troca:]))
    filho_2 = numpy.concatenate((mae[:ponto_de_troca],pai[ponto_de_troca:]))
    return filho_1,filho_2

scene = bge.logic.getCurrentScene()        # Get the current game scene
cont = bge.logic.getCurrentController() # Get the controller executing this script
obj = cont.owner                         # Get this object

if 'lista_carros' not in obj:
    obj['lista_carros'] = []
    obj['lista_cenarios'] = []

if  not obj['init']:
    obj['init']= True;
    obj['geracao'] = 1;
    [carros,obj['lista_cenarios']] = cria_10_carros();
    obj['lista_carros']=carros;
    scene.objects['Camera'].actuators[0].object = carros[0];
    print(scene.objects['Camera'].actuators)
    data = datetime.datetime.now()
    diretorio = str(data.year) + '-' + str(data.month) + '-' + str(data.day) + '-' + str(data.hour) + '-' + str(data.minute) + '-' + str(data.second)
    diretorio = os.path.join('../data',diretorio)
    if not os.path.exists(diretorio):
        os.mkdir(diretorio)
    obj['diretorio'] = diretorio;
    
for object in scene.objects:
    if object.name == "Text":
        object.text = 'Geracao: ' + str(obj['geracao'])

if obj['geracao'] < 5:
    tempo_limite = 15;
elif obj['geracao'] < 20:
    tempo_limite = 20;
elif obj['geracao'] < 80:
    tempo_limite = 30;
elif obj['geracao'] < 120:
    tempo_limite = 70;
elif obj['geracao'] <130:
    tempo_limite = 100;
else:
    tempo_limite = 200;        

if obj['tempo'] > tempo_limite:
    obj['geracao'] += 1;
    print(obj['tempo']);
    obj['tempo'] = 0;
    
    pontuacoes = extrai_pontuacoes(obj['lista_carros']);
    matrix_desordenada = gera_matrix_ganhos(obj['lista_carros'],pontuacoes)
    matrix_ordenada = matrix_desordenada[matrix_desordenada[:,-2].argsort()[::-1]]
    populacao = reproducao(matrix_ordenada)
    pontuacao_max = matrix_ordenada[0][-2]
    obj['pontuacao'] = pontuacao_max
    
    for carro in obj['lista_carros']:  
        carro.endObject()
        
    for cubo in obj['lista_cenarios']:
        cubo.endObject()
        
    arquivo = os.path.join(obj['diretorio'],str(obj['geracao']-1) + '.csv')
    with open(arquivo,'wt') as file:
        for i in range(0,len(matrix_ordenada)):
            line = matrix_ordenada[i]
            for j in range(0,len(line)):
                file.write(str(line[j]))
                file.write(' ,')
            file.write('\n')
    
    [obj['lista_carros'],obj['lista_cenarios']]=cria_novos_carros(populacao)    
    scene.objects['Camera'].actuators[0].object = obj['lista_carros'][0];


