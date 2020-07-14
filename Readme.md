# Cars with genetic algorithm in Blender

[Leia em portugues](README.pt.md)


## Index

<! - Add later using the [site] (https://ecotrust-canada.github.io/markdown-toc/) ->
- [Introduction] (# introduction)
- [How it works] (# how-it works)
- [Tracks] (# tracks)
- [Genetic algorithm] (# genetic-algorithm)
- [Score] (# score)
- [Requirements] (# requirements)
- [Usage] (# usage)
- [Future works] (# future-works)

## Introduction

This is a project developed for the discipline PSI 3572- Visual Computing, administered by the Polytechnic School of USP in the second semester of 2019. 
The project consists of developing an application that uses visual computing. We chose to use a genetic algorithm to teach a virtual car how to drive.

Similar applications can be found on the Internet, such as this [link] (https://ashwinvaidya.com/blog/self-driving-car-using-genetic-algorithm-in-unity/) or [here] (https: // www.youtube.com/watch?v=8V2sX9BhAW8&feature=emb_title).
However, we could not find any such program that runs using the Blender Game Engine. So, we decided to make one. Another reason for using Blender is because it is lighter to run than Unity, in addition to being an Open Source program.

The results can be seen in the [video] (https://youtu.be/K3c_hVrH8Zo)

## How it works
To apply a genetic algorithm, we thought about using a generic controller in the car and then the genetic algorithm changes the parameters of that controller, thus giving different characteristics to the cars to be selected. 
The controller of the genetic algorithm can be found in the "gerador_logic.py" scripts.

As a controller, we decided to use a neural network, and thus, the parameters that make up the genetic code of cars are the weights and biases of the network. 
The internal structure of the network is different in generator 1 and generator 2, more details can be found within the readme of these folders. 
Despite this, the network inputs and outputs are the same for both. 
The inputs are the module of the linear speed of the car and the value of 3 Ray type sensors (Exemplified by "lasers" in the visualization). 
The output is the equivalent of the WASD keys on the keyboard to control the cart. The code related to the cart controller can be found in the "network_logic.py" scripts.

! [Cars riding in Interlagos] (Carros_in_interlagos.png)

The physical model of the cart was adapted from that [model] (https://free3d.com/3d-model/low-poly-car-40967.html) found on the internet. 
To animate the cart, we first made a "car_logic.py" script, which allowed the user to control the cart more naturally using the WASD keys on the keyboard.
After that, it was enough to exchange this keyboard input for the neural network output.

There is yet another unexplained file, 'cube_logic.py'. This file only moves a cube responsible for the correct positioning of Ray type sensors.

The cars of each generation run all at the same time, but are essentially invisible to each other, as they do not collide with each other and the sensors detect only the distance from the track.

## Clues
To train the cart, we needed a test track, for that, we used Formula 1 racetracks as inspiration. First we created a side section of the track with side walls, as in the file "pista_pedaco.blend". Then, it is possible to make the track follow a determined curve as in this [video] (https://www.youtube.com/watch?v=SDLLbKvEeBY). To create the curve we use python's Shapely library, which allows us to create a curve from a series of points. This library was also useful for calculating the distance traveled on this curve. As in the video, we designed a schematic drawing of the Interlagos track, which served as training, and we were manually finding the correct coordinates to approach this track. This process is in the file "pistaInterlagos.blend".

After training the cart, we made a track with the design of the Formula 1 monaco track, to test them on a different track and see how they worked.

It is important to note that due to the way we built the track, we disregard the differences in altitude between the sectors of the track. Soon a track with slopes becomes a flat track.


## Genetic Algorithm
The Genetic Algorithm, which is described in "generator_logic.py" works as follows. The genetic code is an array that has the weights and biases of the neural network that constitutes the car. In the first generation, cars are created with genes started at random.

In generator 2, when testing a generation, as cars fail, their genetic codes are included in one list, just as their scores are included in another list. After all cars fail, or reach the end of the track (and consequently fail, as they will be stopped for a long time), the list of genes and the list of scores are joined in order to create a table (or matrix) containing on each line the code
