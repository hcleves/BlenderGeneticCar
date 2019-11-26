import bge

cont = bge.logic.getCurrentController()
own = cont.owner

own.worldPosition = own['carro'].worldPosition;
own.worldOrientation = own['carro'].worldOrientation;
own.applyRotation((0,0,2.5*1.5708),True)

