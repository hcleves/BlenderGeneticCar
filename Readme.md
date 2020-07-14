# Cars with genetic algorithm in Blender

[Leia em portugues](README.pt.md)


## Index

<! - Add later using the [site] (https://ecotrust-canada.github.io/markdown-toc/) ->
- [Introduction](#introduction)
- [How it works](#how-it-works)
- [Tracks](#tracks)
- [Genetic algorithm](#genetic-algorithm)
- [Score](#score)
- [Requirements](#requirements)
- [Usage](#usage)
- [Future works](#future-works)

## Introduction

This is a project developed for the discipline PSI 3572- Visual Computing, administered by the Polytechnic School of USP in the second semester of 2019. 
The project consists of developing an application that uses visual computing. We chose to use a genetic algorithm to teach a virtual car how to drive.

Similar applications can be found on the Internet, such as this [link](https://ashwinvaidya.com/blog/self-driving-car-using-genetic-algorithm-in-unity/) or [here](https://www.youtube.com/watch?v=8V2sX9BhAW8&feature=emb_title).
However, we could not find any such program that runs using the Blender Game Engine. So, we decided to make one. Another reason for using Blender is because it is lighter to run than Unity, in addition to being an Open Source program.

The results can be seen in the [video](https://youtu.be/K3c_hVrH8Zo)

## How it works
To apply a genetic algorithm, we thought about using a generic controller in the car and then the genetic algorithm changes the parameters of that controller, thus giving different characteristics to the cars to be selected. 
The controller of the genetic algorithm can be found in the "gerador_logic.py" scripts.

As a controller, we decided to use a neural network, and thus, the parameters that make up the genetic code of cars are the weights and biases of the network. 
The internal structure of the network is different in generator 1 and generator 2, more details can be found within the readme of these folders. 
Despite this, the network inputs and outputs are the same for both. 
The inputs are the module of the linear speed of the car and the value of 3 Ray type sensors (Exemplified by "lasers" in the visualization). 
The output is the equivalent of the WASD keys on the keyboard to control the cart. The code related to the cart controller can be found in the "network_logic.py" scripts.

![Cars riding in Interlagos](carros_in_interlagos.png)

The physical model of the cart was adapted from that [model](https://free3d.com/3d-model/low-poly-car-40967.html) found on the internet. 
To animate the cart, we first made a "car_logic.py" script, which allowed the user to control the cart more naturally using the WASD keys on the keyboard.
After that, it was enough to exchange this keyboard input for the neural network output.

There is yet another unexplained file, 'cube_logic.py'. This file only moves a cube responsible for the correct positioning of Ray type sensors.

The cars of each generation run all at the same time, but are essentially invisible to each other, as they do not collide with each other and the sensors detect only the distance from the car to the track track.

## Tracks
To train the car, we needed a test track, for that, we used Formula 1 racetracks as inspiration. First we created a cross-section of the track with side walls, as in the file "pista_pedaco.blend". Then, it is possible to make the track follow a determined curve as in this [video](https://www.youtube.com/watch?v=SDLLbKvEeBY). To create the curve we use python's Shapely library, which allows us to create a curve from a series of points. This library was also useful for calculating the distance traveled on this curve. As in the video, we designed a schematic drawing of the Interlagos track, which served as training, and we were manually finding the correct coordinates to approach this track. This process is in the file "pistaInterlagos.blend".

After training the cart, we made a track with the design of the Formula 1 monaco track, to test them on a different track and see how they worked.

It is important to note that due to the way we built the track, we disregard the differences in altitude between the sectors of the track. So, a track with slopes becomes a flat track.


## Genetic Algorithm
The Genetic Algorithm, which is described in "gerador_logic.py" works as follows. The genetic code is an array that has the weights and biases of the neural network that constitutes the car. In the first generation, cars are created with genes intialized to random values.

In generator 2, when testing a generation, when the cars fail, their genetic codes are included in one list, and their correspondent scores are included in another list. After all cars fail, or reach the end of the track (and consequently fail, since they will be stopped for a long time), the list of genes and the list of scores are joined in order to create a table (or matrix) containing on each line the car's genetic code and its score. This matrix is then ordered according to the score so that the highest score is at the top of the matrix. So, this matrix is passed to a reproduction function

In generator 1, the matrix with the genes and scores is generated only after a certain simulation time has passed, since all the cars are always on the track.

In the reproduction phase, the first x individuals to be reproduced are selected. Then, breeding pairs are generated, so that the first has priority in the reproduction, the second after it, etc. For example, if there were 4 individuals for reproduction, the pairs formed would be (1,2) (1,3) (1,4) (2,3) (2,4) (3,4), with the list of pairs is traversed from left to right. The top two are passed on to the next generation without changes. After the pairs are generated, reproduction is carried out for each pair, generating 2 children, until reaching the fixed size of the population. The reproduction part is done as follows: a random index is chosen in the gene vector, and thus the vector of the genetic code is divided into two on that index. One of the children receives the first part from one parent and the second part from the other parent, and vice versa. So, this process always generates 2 children from a pair.

After reproduction, the children go through a mutation stage, which can alter one or more elements of their genetic code according to a given probability. The change is made by adding a random number in a given range.

In the end, a new population is generated, which then transmits its characteristics to the cars and then the new generation is generated.

## Score

To be able to use the genetic algorithm, it is necessary to define how the car score will be calculated. We used the distance covered in the curve that represents the track as the basis of the score. This distance is calculated by finding the point on the curve closest to the car and traveling the curve up to that point. The calculation is performed using the line.project(point) function of the Shapely library. There are cases where the car is disqualified: in these, their score is frozen at the moment the disqualification occurred. The criteria for disqualification are as follows:

* The car fell off the track: in this case the score is 0.
* The car hit the track: that is, one of the sensors detected the distance to be to small from the car to the side of the track.
* The car has very low instantaneous speed.
* The car is at low average speed.

A criterion that would be interesting to prevent would be that the car is moving in the opposite direction of the road. However, we were unable to implement this criterion in the program. To prevent a car from reversing and cheating the scoring system by making it thinking the car was in the end of the lap, we placed blocks that physically prevent the car from passing.

## Requirements

* Blender version 2.79 (In version 2.8, Blender Game Engine has been discontinued and therefore will not work)
* Libraries
   * numpy
   * shapely
   * mathutils
   * math
   * os
   * datetime

* It is recommended to use the same operating system used to develop the program (Ubuntu 18.04). Although Blender is cross-platform, I had some trouble getting it to work on Windows 10 and I didn't have the opportunity to test on MacOs.

## Usage

To use the program, simply access the .blend file inside the Blenders folder.

##### Important: To launch the .blend file, use the command line "blender <filename>". Trying to open the file with two clicks or otherwise, will result in a defective simulation, for reasons I don't understand.

Note that it is also easy to create a new file, just place it inside the Blenders folder and copy and paste the main.py file into the scripts folder for the blender text editor and run the script. If it is a new file, it is recommended to do the following steps to improve performance:

1. Go to the Properties view, on the Render tab, look for System
2. In that location, disable "Use Frame Rate" and change Vsync to Off
3. Still in the Render tab, go to "Display", which should be right under System.
4. Check the "Debug Properties" and "Framerate and Profile" boxes. Although these boxes are not linked to performance, they offer important information about the status of the program

In both cases, whether it is a new file or an old file, it is essential to execute the following commands in the interactive python console as soon as you open the file. Otherwise, python will issue a docstring error the second time the simulation is performed.

`` python
import numpy
import importlib
importlib.reload (numpy)
``

To launch the simulation, just open a 3dView window, place the mouse over it and hit "p". Make sure that Blender is in Blender Game mode. To exit the simulation, just place the mouse over it again and press ESC.

To use the game camera in 3dView, you can use the hotkey Numpad 0

To run the simulation the second time or the nth time, is recommended to run the following command on the interactive python console

`` python
importlib.reload (numpy)
``

## Future works

We probably won't be working hard on this project in the future. However, the project is open to anyone who wants to continue. If you are interested in continuing and want to be added as a collaborator, just get in touch. Below is a list of tasks that we think would be interesting to do, in no specific order:

* Translate the variables into English, and put more suitable names in them according to some convention to facilitate the reading of the code
* Make the Shapely library functions using only numpy functions, so that the user does not need to install it, since in Windows this was one of the problems we encountered.
* Use more than one CPU core to run the simulation
* Think of ways to optimize the size of the population, rather than maintaining a fixed size
* Create new tracks
* Create tracks with variation on the z axis, that is, with slopes
* Improve scoring algorithm, to detect the car in the wrong direction, and to support the car making more than one lap
* Remove speed restrictions on the cart, and try to use the genetic algorithm to make the cart try to make the fastest lap.
* Make cars that can hit the opponent, on a starting grid as in a real race.
* Genetic algorithm: Modify Reproduction, add invasion of new individuals, etc.
