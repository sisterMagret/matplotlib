import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.y_values=[0]
        self.x_values=[0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:

            #decide which direction to ho and how far to go
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4,5,6,7,8,9,12])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4,5,6,7,8,9,45])
            y_step = y_direction * y_distance

            #filter and reject zero values
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    #Set the size of plotting window
    plt.figure(dpi=128,figsize=(15,8))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    plt.scatter(0,0, c='green',edgecolor='none',s=15)
    plt.scatter(rw.x_values[-1],rw.y_values[-1], c='red',edgecolor='none',s=15)

    #Remove the axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.savefig('randomwalk.jpg',bbox_inches='tight')
    plt.show()

    keep_runing = input("Make Another Walk? (y/n) ")
    if keep_runing == 'n':
        break

