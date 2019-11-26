import bge
import mathutils
import math
import numpy

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / numpy.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return numpy.arccos(numpy.clip(numpy.dot(v1_u, v2_u), -1.0, 1.0))

cont = bge.logic.getCurrentController()
own = cont.owner

#constants
MAX_VEL = 0.35
MAX_TURN = 0.02
BRAKE_SPEED = 0.01
ACCEL = 0.01
CRUISE = 0.001
TURN_INC = 0.0005
TURN_SPEED = 0.0005
MAX_VEL_RE = -0.15

#sensors
w = own['w']
a = own['a']
d = own['d']
s = own['s']
#Controlar forca da rede ou alguma propriedade

#motion actuator
motion = cont.actuators['Motion']

#properties
velocity = own['velocity']
turn = own['turn']

############ movement ############

#forwards
if w and velocity < MAX_VEL and s == False and a == False and d == False:
    own['velocity'] += ACCEL
    motion.dLoc = ([0.0, -(own['velocity']), 0.0])
    cont.activate(motion)

#cruise speed
elif w == False and velocity > 0:
    own['velocity'] -= CRUISE
    motion.dLoc = ([0.0, -(own['velocity']), 0.0])
    cont.activate(motion)

#braking
if s and velocity > 0.01 and w == False:
    own['velocity'] -= BRAKE_SPEED
    motion.dLoc = ([0.0, -(own['velocity']), 0.0])
    cont.activate(motion)

#stop any movement
if velocity < 0.001 and velocity > -0.001:
    motion.dLoc = ([0.0, 0.0, 0.0])
    cont.activate(motion)

# Adicionando Re
if s and velocity > MAX_VEL_RE and velocity <= 0.0 and w==False:
    own['velocity'] -= ACCEL
    motion.dLoc = ([0.0, -(own['velocity']), 0.0])
    cont.activate(motion)

elif s == False and velocity < 0:
    own['velocity'] += CRUISE
    motion.dLoc = ([0.0, -(own['velocity']), 0.0])
    cont.activate(motion)
    
if w and velocity < -0.01 and s == False:
    own['velocity'] += BRAKE_SPEED
    motion.dLoc = ([0.0, -(own['velocity']), 0.0])
    cont.activate(motion)
    
# Fim Re
#print(velocity)

########## Turning ###########

#right turning
if ((velocity > 0.03 or velocity < -0.03) and a and turn < MAX_TURN):
    own['turn'] += TURN_INC
    own['velocity'] -= TURN_SPEED
    motion.dRot = ([0.0, 0.0, (own['turn'])])
    motion.dLoc = ([0.0, -(own['velocity']), 0.0])
    cont.activate(motion)
    
elif a == False and turn > 0:
    own['turn'] -= TURN_INC
    motion.dRot = ([0.0, 0.0, (own['turn'])])
    cont.activate(motion)        
    
#stop any rotation
if turn < 0.001 and d == False:
    motion.dRot = ([0.0, 0.0, 0.0])
    cont.activate(motion)

#left turning
if ((velocity > 0.03 or velocity < -0.03) and d and turn > -MAX_TURN):
    own['turn'] -= TURN_INC
    own['velocity'] -= TURN_SPEED
    motion.dRot = ([0.0, 0.0, (own['turn'])])
    motion.dLoc = ([0.0, -(own['velocity']), 0.0])
    cont.activate(motion)

elif d == False and turn < 0:
    own['turn'] += TURN_INC
    motion.dRot = ([0.0, 0.0, (own['turn'])])
    cont.activate(motion)    


