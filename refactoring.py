"""The fill walk method is lengthy we will create a new method get step to determine the direction and distance for each steps"""
from random import choice
class RandomWalk:
    def __init__(self,num_points = 5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # all walks start at 0,0
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""
        #keep taking step until the walk reaches the desired length
        while len(self.x_values)< self.num_points:
            # decide which direction to go and how far to go in that direction
            x_step = self.get_step()
            y_step = self.get_step()

            # rejects moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
    def get_step(self):
        """Decide which direction to go and how far to go in that direction"""
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4,5,6,7,8,9])
        return direction*distance
