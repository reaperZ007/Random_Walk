import matplotlib.pyplot as plt
from refactoring import RandomWalk
# make a random walk
while True:

    rw = RandomWalk(50_000) # increase thee points
    rw.fill_walk()
    # plot the point in the walk
    plt.style.use('classic')
    fig,ax = plt.subplots(figsize =(25,25))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c = point_numbers,cmap = plt.cm.Blues,edgecolors= 'none',s = 1)
    ax.set_aspect('equal')
    #emphasize the first and last points
    ax.scatter(0,0,c= 'green',edgecolors='none',s = 50)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c = 'red',edgecolors='none',s = 50)
    #remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk ? (y/n): ")
    if keep_running == 'n':
        break 