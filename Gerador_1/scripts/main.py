import bpy
max_population = 1
put_on_layers = lambda x: tuple((i in x) for i in range(20))

objs = bpy.data.objects;

for o in bpy.data.objects:
    o.select =True;
    bpy.data.objects.remove(o,do_unlink=True)
    
bpy.ops.wm.append(directory='../src',filename = "Car4.blend\\Object\\Car")
bpy.data.objects.remove(objs['Car.001'])
carro = bpy.data.objects['Car']
bpy.context.scene.objects.active = carro;

bpy.ops.object.game_property_new(type='FLOAT',name = 'angulo');
bpy.ops.object.game_property_new(type='FLOAT',name = 'angulo_pista');
bpy.ops.object.game_property_new(type='FLOAT',name = 'pontuacao');
bpy.ops.object.game_property_new(type='BOOL',name = 'sentido_errado');
bpy.ops.object.game_property_new(type='BOOL',name = 'roubou');

bpy.ops.object.game_property_new(type='BOOL',name = 'w');
bpy.ops.object.game_property_new(type='BOOL',name = 'a');
bpy.ops.object.game_property_new(type='BOOL',name = 'd');
bpy.ops.object.game_property_new(type='BOOL',name = 's');


#cria controlador
if 'car_logic.py' not in bpy.data.texts:
    bpy.ops.text.open(filepath = "../scripts/car_logic.py")
        
bpy.ops.logic.controller_add(type = 'PYTHON',object='Car');
controlador = carro.game.controllers['Python'];
controlador.name = '1';
controlador.text = bpy.data.texts['car_logic.py'];

#cria controlador rede
if 'network_logic.py' not in bpy.data.texts:
    bpy.ops.text.open(filepath = "../scripts/network_logic.py")
        
bpy.ops.logic.controller_add(type = 'PYTHON',object='Car');
controlador_rede = carro.game.controllers['Python'];
controlador_rede.name = '2';
controlador_rede.text = bpy.data.texts['network_logic.py'];
controlador_rede

#cria sensor 1
bpy.ops.logic.sensor_add(type='KEYBOARD',object='Car');
sensor = carro.game.sensors['Keyboard'];
sensor.name = 'w';
sensor.key = 'W';
sensor.link(controlador)
sensor.link(controlador_rede)

#cria sensor 2
bpy.ops.logic.sensor_add(type='KEYBOARD',object='Car');
sensor = carro.game.sensors['Keyboard'];
sensor.name = 'a';
sensor.key = 'A';
sensor.link(controlador)
sensor.link(controlador_rede)

#cria sensor 3
bpy.ops.logic.sensor_add(type='KEYBOARD',object='Car');
sensor = carro.game.sensors['Keyboard'];
sensor.name = 's';
sensor.key = 'S';
sensor.link(controlador)
sensor.link(controlador_rede)

#cria sensor 4
bpy.ops.logic.sensor_add(type='KEYBOARD',object='Car');
sensor = carro.game.sensors['Keyboard'];
sensor.name = 'd';
sensor.key = 'D';
sensor.link(controlador)
sensor.link(controlador_rede)

#cria sensor 5
bpy.ops.logic.sensor_add(type='ALWAYS',object = 'Car');
sensor = carro.game.sensors['Always']
sensor.use_pulse_true_level = True
sensor.link(controlador)
sensor.link(controlador_rede)

#cria sensor Ray 1
bpy.ops.logic.sensor_add(type='RAY',object='Car');
sensor = carro.game.sensors['Ray'];
sensor.name = 'Ray1';
sensor.property = 'track'
sensor.use_x_ray = True
sensor.use_pulse_true_level = True;
sensor.axis = 'NEGYAXIS';
sensor.range = 100;
sensor.link(controlador);
sensor.link(controlador_rede)

#cria sensor Ray 2
bpy.ops.logic.sensor_add(type='RAY',object='Car');
sensor = carro.game.sensors['Ray'];
sensor.name = 'Ray2';
sensor.use_pulse_true_level = True;
sensor.property = 'track'
sensor.use_x_ray = True
sensor.axis = 'NEGXAXIS';
sensor.range = 100;
sensor.link(controlador);
sensor.link(controlador_rede)

#cria sensor Ray 3
bpy.ops.logic.sensor_add(type='RAY',object='Car');
sensor = carro.game.sensors['Ray'];
sensor.name = 'Ray3';
sensor.use_pulse_true_level = True;
sensor.property = 'track'
sensor.use_x_ray = True
sensor.axis = 'XAXIS';
sensor.range = 100;
sensor.link(controlador);
sensor.link(controlador_rede)

#cria atuador
bpy.ops.logic.actuator_add(type = 'MOTION',object = 'Car');
atuador = carro.game.actuators['Motion']
#atuador.name = '2';
#atuador.mode = 'SIMPLE_MOTION';
#atuador.offset_rotation[2] = 0.0523599;
atuador.use_local_rotation = True;
atuador.use_local_force = True;
atuador.use_local_torque = True;
atuador.use_local_location = True;
#atuador.offset_location[2] = 0;
#atuador.use_character_jump = True;
atuador.link(controlador);
#atuador.force[2] = 100;


carro_original = bpy.data.objects['Car']
carros = []
carro_original.select = True;

for i in range(0,max_population):
    bpy.ops.object.duplicate()
    bpy.data.objects[-1].location = (10*i,0,0)
    carros.append(bpy.data.objects[-1])
    
for i in range(0,len(carros)):
    carros[i].name = str(i);
    carros[i].game.use_collision_bounds = True;
    
    for j in range(0,len(carros[i].game.collision_mask)):
        if j!=0:
            carros[i].game.collision_mask[j] = False;
    
    carros[i].game.collision_group[1]=True;
    carros[i].game.collision_group[0]=False;
    
    carros[i].game.physics_type = 'RIGID_BODY';
    for j in range(i+1,len(carros)):
        carros[i].constraints.new('RIGID_BODY_JOINT')
        carros[i].constraints[-1].target = carros[j]
        carros[i].constraints[-1].pivot_type = 'GENERIC_6_DOF'
        carros[i].constraints[-1].use_linked_collision = True
    carros[i].layers[:] = put_on_layers({1})
    
bpy.ops.wm.append(directory='../src',filename = "pistaInterlagos.blend\\Object\\track")
objs['track'].game.physics_type = 'STATIC';
#objs['track'].game.use_collision_bounds = True;
objs['track'].game.collision_group[0]=True;
objs['track'].game.collision_mask[1]=True;
bpy.context.scene.objects.active = objs['track']
bpy.ops.object.game_property_new(type='FLOAT',name='track')

#cria gerador
bpy.ops.mesh.primitive_monkey_add(location=(0,0,0));
gerador = objs['Suzanne']
gerador.name = 'Deus'
bpy.context.scene.objects.active = gerador;
bpy.ops.object.game_property_new(type='TIMER',name='tempo');
bpy.ops.object.game_property_new(type='BOOL',name='init');
bpy.ops.object.game_property_new(type='INT',name= 'geracao');
bpy.ops.object.game_property_new(type='FLOAT',name = 'pontuacao');

objs['Deus'].game.properties['geracao'].show_debug = True;
objs['Deus'].game.properties['pontuacao'].show_debug = True;

#cria sensor do gerador
bpy.ops.logic.sensor_add(type='ALWAYS',object = 'Deus');
sensor = gerador.game.sensors['Always']
sensor.use_pulse_true_level = True

#cria controlador do gerador
bpy.ops.logic.controller_add(type = 'PYTHON',object='Deus');
controlador = gerador.game.controllers['Python'];

if 'gerador_logic.py' not in bpy.data.texts:
    bpy.ops.text.open(filepath = "../scripts/gerador_logic.py");

controlador.text = bpy.data.texts['gerador_logic.py'];
controlador.link(sensor);

carro_original.layers[:] = put_on_layers({1})
bpy.context.scene.objects.active = carro;

bpy.ops.object.camera_add(location=(0,0,0))
bpy.ops.logic.sensor_add(type='ALWAYS',object = 'Camera');
sensor = objs['Camera'].game.sensors['Always']
sensor.use_pulse_true_level = True

bpy.ops.logic.controller_add(type='LOGIC_AND', object = 'Camera');
sensor.link(objs['Camera'].game.controllers['And'])

bpy.ops.logic.actuator_add(type='CAMERA',object = 'Camera')
objs['Camera'].game.actuators['Camera'].height = 50;
objs['Camera'].game.actuators['Camera'].min = 50;
objs['Camera'].game.actuators['Camera'].max = 50;
objs['Camera'].game.actuators['Camera'].axis = 'POS_Y'
objs['Camera'].game.actuators['Camera'].damping = 0.03;
objs['Camera'].game.actuators['Camera'].object = objs['Deus'];
objs['Camera'].game.actuators['Camera'].link(objs['Camera'].game.controllers['And'])

#cria objeto empty para ser usado como sensor

bpy.ops.object.empty_add(type='CUBE');
cubo = objs['Empty']
bpy.context.scene.objects.active = cubo; 

bpy.ops.logic.controller_add(type = 'PYTHON',object='Empty');
controlador = cubo.game.controllers['Python'];

if 'cube_logic.py' not in bpy.data.texts:
    bpy.ops.text.open(filepath = "../scripts/cube_logic.py");

controlador.text = bpy.data.texts['cube_logic.py'];

bpy.ops.logic.sensor_add(type='RAY',object='Empty');
sensor = cubo.game.sensors['Ray'];
sensor.name = 'Ray';
sensor.property = 'track'
sensor.use_x_ray = True
sensor.use_pulse_true_level = True;
sensor.axis = 'XAXIS';
sensor.range = 100;
sensor.link(controlador);

bpy.ops.logic.sensor_add(type='RAY',object='Empty');
sensor = cubo.game.sensors['Ray.001'];
sensor.name = 'Ray2';
sensor.property = 'track'
sensor.use_x_ray = True
sensor.use_pulse_true_level = True;
sensor.axis = 'YAXIS';
sensor.range = 100;
sensor.link(controlador);

bpy.ops.logic.sensor_add(type='ALWAYS',object = 'Empty');
sensor = cubo.game.sensors['Always']
sensor.use_pulse_true_level = True
sensor.link(controlador)

cubo.layers[:]=put_on_layers({1})
