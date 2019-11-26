import bge;
import numpy;
import mathutils;
import math
import shapely.geometry as geom

class NeuralNetwork:
    def __init__(self, x, y, gene):
        self.input      = x
        self.weights1   = numpy.asarray(gene[0:self.input.shape[1]*4]).reshape(self.input.shape[1],4);#numpy.random.rand(self.input.shape[1],4) 
        gene = gene[self.input.shape[1]*4:]
        self.bias1 = numpy.asarray(gene[0:4]).reshape(1,4);
        gene = gene[4:]
        self.weights2   = numpy.asarray(gene[0:4*y.shape[1]]).reshape(4,y.shape[1])
        gene = gene[4:]
        self.bias2 = numpy.asarray(gene[0:y.shape[1]])
        self.y          = y
        self.output     = numpy.zeros(self.y.shape)

    def calcula(self,x):
        self.input = x;
        self.layer1 = self.sigmoid(numpy.dot(self.input, self.weights1) + self.bias1)
        self.output = self.sigmoid(numpy.dot(self.layer1, self.weights2)+ self.bias2)
        return self.output
        
    def sigmoid(self,z):
        return 1/(1+numpy.exp(-z))

cont = bge.logic.getCurrentController()
carro  = cont.owner
own = carro

if not carro['init']:
    carro['init']=True;
    x = numpy.zeros((1,4))
    y = numpy.zeros((1,4))
    carro['rede'] = NeuralNetwork(x,y,carro['gene']);
    own['distancia_anterior'] = 0;
    
if carro['init']:
    ray1 = cont.sensors['Ray1']
    ray2 = carro['sensor1']
    ray3 = carro['sensor2']
    if ray1.positive:
        hitPosition = ray1.hitPosition
        distance1 = own.getDistanceTo(hitPosition)
        color = [1, 0, 0]
        bge.render.drawLine(own.worldPosition,ray1.hitPosition,color)
    else:
        distance1 = 100;
        xyz = own.localOrientation.to_euler()
        rotz = math.degrees(xyz[2])
        from_pos = own.worldPosition    # The start position is the cube's position (which is a vector)
        to_pos = from_pos + mathutils.Vector([distance1*math.sin(xyz[2]), -distance1*math.cos(xyz[2]), 0]) # Add another vector (1 over on the X axis) to the cube's position
        color = [1, 0, 0]   # Color of the line (Red, Green, Blue)
        bge.render.drawLine(from_pos, to_pos, color)
        
    if ray2.positive:
        hitPosition = ray2.hitPosition
        distance2 = own.getDistanceTo(hitPosition)
        color = [0, 1, 0]
        bge.render.drawLine(own.worldPosition,ray2.hitPosition,color)
    else:
        distance2 = 100;
        xyz = own.localOrientation.to_euler()
        rotz = math.degrees(xyz[2])
        from_pos = own.worldPosition    # The start position is the cube's position (which is a vector)
        to_pos = from_pos + mathutils.Vector([-distance2*math.cos(xyz[2]), -distance2*math.sin(xyz[2]), 0]) # Add another vector (1 over on the X axis) to the cube's position
        color = [0, 1, 0]   # Color of the line (Red, Green, Blue)
        bge.render.drawLine(from_pos, to_pos, color)
        
    if ray3.positive:
        hitPosition = ray3.hitPosition
        distance3 = own.getDistanceTo(hitPosition)
        color = [1, 1, 0]
        bge.render.drawLine(own.worldPosition,ray3.hitPosition,color)
    else:
        distance3 = 100;
        xyz = own.localOrientation.to_euler()
        rotz = math.degrees(xyz[2])
        from_pos = own.worldPosition    # The start position is the cube's position (which is a vector)
        to_pos = from_pos + mathutils.Vector([distance3*math.cos(xyz[2]), distance3*math.sin(xyz[2]), 0]) # Add another vector (1 over on the X axis) to the cube's position
        color = [1, 1, 0]   # Color of the line (Red, Green, Blue)
        bge.render.drawLine(from_pos, to_pos, color)

    
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
    (185,279),(123,296),(83,301)
    ]
    line = geom.LineString(coords)
    point = geom.Point(own.worldPosition[0],own.worldPosition[1])
    
    own['angulo_pista']  = line.project(point)
    
    if own['angulo_pista'] < 50:
        own['roubou'] = True;
        own['pontuacao'] = 0;
    
    if own.worldPosition[2] < -2: # caiu da pista
        if not own['roubou']:
            own['roubou'] = True;
            own['pontuacao'] = 0;
    
    if distance2 < 2.5 or distance3<2.5 or distance1<5:
        if not own['roubou']: 
            own['roubou'] = True;
            own['pontuacao'] = own['angulo_pista']
        
    #calcula pontuacao
    if not own['roubou']:
        own['pontuacao'] = own['angulo_pista']; 
        
    inputs = [ 
        distance1,
        distance2,
        distance3,
        numpy.linalg.norm(carro.getLinearVelocity())
        ]
    
    [w,a,d,s] = carro['rede'].calcula(numpy.asarray(inputs)).tolist()[0]
    
    carro['w'] = w>0.5
    carro['a'] = a>0.5
    carro['d'] = d>0.5
    carro['s'] = s>0.5
