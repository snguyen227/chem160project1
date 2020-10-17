import random
from random import choice
density=float(input("density"))
maxsteps=10000
npart=500
perc=0
side=41
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]
for ipart in range(npart):
    x,y=side//2,side//2
    for x in range(side):
        for y in range(side):
            grid[x][y]=random.randint(0,100)
            if grid[x][y] <= (density*100):
                grid[x][y]=1
            else:
                grid[x][y]=0
    x,y=side//2,side//2
    for i in range(maxsteps):
        grid[x][y] = 0
        sx,sy=choice(steps)
        y += sy
        x += sx
        if x<0 or y<0 or x==side or y==side:
            perc += 1
            break
        if grid[x][y] == 1 :
            y -= sy
            x -= sx
        continue
print("Probability of the Particle Percolating=%5.2f"%(perc/npart))