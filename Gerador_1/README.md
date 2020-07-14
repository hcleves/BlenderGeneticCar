## Generator 1

This is the first type of generator tested. It was implemented with a more complex neural network. It is a fully-connected neural network with 2 hidden layers of 4 neurons each and with a sigmoid activation function. The features of this program are listed below:
* In a given Generation, all cars run for the same period of time, regardless of their performance during this generation
* The camera follows the car that performed best in the previous generation. In the first generation, a car is chosen at random
* Uses a more complex neural network
* Was able to walk in Interlagos, in Training, and in Monaco, in the test, on the first attempt
* Training time is much longer, as all cars are active throughout the generation, resulting in a higher computational cost and lower and constant FPS.
