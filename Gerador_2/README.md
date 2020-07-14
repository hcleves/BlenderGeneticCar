## Generator 2

This is the second and last type of generator tested, below are its characteristics:

* Simpler neural network, with only a hidden layer of 4 neurons
* Cars are eliminated throughout the generation when they crash or if they do not reach enough points within a certain time interval (that is, if they are too slow).
* As the cars are being eliminated, the simulation starts to become lighter and can be performed at more FPS. Visually, it looks like the cars are accelerating, when in fact it is only the simulation that is getting faster.
* The simulation can be done much faster than generator 1, since given a certain generation, most cars tend to fail, and therefore the simulation runs with fewer cars the longer it runs.
