import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation 

#fills the grid with NN random tiles.
def fillGrid(N): 
    return np.random.choice([1,0], N*N, p=[0.25, 0.75]).reshape(N, N) 

#updates each tile in the grid
def update(frameNum, img, grid, N):
    updatedGrid = grid.copy() 
    for x in range(N): 
        for y in range(N):
            # calculates the number of alive neighbor cells
            # using modulus N so that the x and y values wrap around.
            aliveNeighbors = (grid[x,(y-1)%N] + grid[x,(y+1)%N] + grid[(x-1)%N,y] + grid[(x+1)%N,y] + 
                              grid[(x-1)%N,(y-1)%N] + grid[(x-1)%N,(y+1)%N] + grid[(x+1)%N,(y-1)%N]+
                              grid[(x+1)%N,(y+1)%N])

            # apply Conway's rules based on the number calculated above
            if grid[x, y] == 1 and ((aliveNeighbors < 2) or (aliveNeighbors > 3)): 
                updatedGrid[x, y] = 0 
            elif aliveNeighbors == 3: 
                updatedGrid[x, y] = 1 

    # update data 
    img.set_data(updatedGrid) 
    grid[:] = updatedGrid[:] 
    return img,

def main():
    #initializes the grid with 50 x 50 random tiles.
    N=50
    grid = np.array([])
    grid = fillGrid(N)

    #animates the grid
    fig, ax = plt.subplots() 
    img = ax.imshow(grid, interpolation='nearest') 
    ani = FuncAnimation(fig, update, fargs=(img, grid, N, ), frames=10, interval=100, save_count=50) 
    plt.show()

if __name__ == '__main__':
    main()
