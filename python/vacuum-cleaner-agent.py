# Name: Atharva Patil
# Github Profile link:  https://github.com/atharvapatil123 

# Vacuum Cleaner Problem: Here, we are given a grid and we need to clean each cell. 
# This algorithm consists of a Simple Reflex Agent, which chooses its next move randomly, thereby requiring more time to clean the grid.

import random, math


class ContinuumWorld:

    def __init__(self, grid_size=[2, 2], dirt=[[1, 1], [1, 1]]):

        self.grid_size = grid_size
        self.dirt = dirt

    def print_dirt(self, agent, position):

        # print(agent.position)
        part = self.dirt[:agent.position[0]]
        print()
        for row in part:
            print(*row, sep=", ")

        current = self.dirt[agent.position[0]]
        print(*current[:agent.position[1]], sep=", ", end=" ")
        print("["+str(self.dirt[agent.position[0]][agent.position[1]])
              + "]", end=" ")
        print(*current[agent.position[1]+1:], sep=", ")

        part = self.dirt[agent.position[0]+1:]
        for row in part:
            print(*row, sep=", ")
        print()
    
    def noDirt(self):
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                if(self.dirt[i][j]==1):return False
        return True

    def fillDirt(self):
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                self.dirt[i][j]=1
        print(self.dirt)




class Agent:

    def __init__(self, position=[0, 0], max_moves=30, grid_size=0, dirt=0):

        self.score = 0
        self.m=0
        self.position = position
        self.max_moves = max_moves
        self.world = ContinuumWorld(grid_size, dirt)
        self.visited = set()
        self.visited.add((self.position[0], self.position[1]))

    def crosses_boundary(self, step):

        # error = "Cannot go beyond! Change direction!\n"
        if step == 'R':
            if self.position[1]+1 > self.world.grid_size[1]-1:
                # print(error)
                return True
        if step == 'L':
            if self.position[1]-1 < 0:
                # print(error)
                return True
        if step == 'U':
            if self.position[0]-1 < 0:
                # print(error)
                return True
        if step == 'D':
            if self.position[0]+1 > self.world.grid_size[0]-1:
                # print(error)
                return True

        return False

    def perform_action(self, action):

        self.m=self.m+1
        if action == 'R':
            self.position[1] += 1
        if action == 'L':
            self.position[1] -= 1
        if action == 'U':
            self.position[0] -= 1
        if action == 'D':
            self.position[0] += 1
        if action == 'S':
            self.world.dirt[self.position[0]][self.position[1]] = 0
            
        self.score = self.m

    def print_status(self, step, counter=0):

        print(step, self.score)
        self.world.print_dirt(self, self.position)


class SimpleReflexAgent(Agent):
    def clean_grid(self):

        cnt=1
        while True:
            i=1
            while (self.world.noDirt()==False):
                if self.world.dirt[self.position[0]][self.position[1]] > 0:
                    step = 'S'
                else:
                    while(True):
                        step = random.choice(['R', 'L', 'U', 'D'])
                        if self.crosses_boundary(step):
                            continue
                        else:
                            break
                self.perform_action(step)
                # print("Step number:", i)
                self.print_status(step, i)
                i+=1
            
            inp = input("Do you want to continue again ? y/n: ")
            if(inp=='y' or inp=='Y'):
                cnt+=1
                self.world.fillDirt()
                initial2 = []
                x2=0
                y2=0
                while(True):
                    posStr2 = input("Enter initial position: ")
                    x2 = int(posStr2[0])
                    y2 = int(posStr2[-1])
                    initial2.append(x2-1)
                    initial2.append(y2-1)
                    self.position = initial2
                    if(x2<=self.world.grid_size[0] and x2>=1 and y2<=self.world.grid_size[1] and y2>=1):
                        break
                    else:
                        print("\nEnter proper row and column\n")
                        initial2=[]
                continue
            else: break
        print(f"Average performance of Simplex Reflex Aagent is : {math.ceil(self.score/cnt)} moves")
       
# Driver Function
def main():
    
    g = []
    g_s = input("Enter grid size: ")
    r = int(g_s[0])
    c = int(g_s[-1])
    g.append(r)
    g.append(c)
    print(g)
    dirt = []
    print("\nEnter grid row wise:\n")
    for i in range(r):
        line = []
        l = []
        line=(input().split())
        for j in range(len(line)):
            l.append(int(line[j]))
        dirt.append(l)

    print("\nGrid is: ")

    for i in range(r):
        for j in range(c):
            print(dirt[i][j]," ",end="")
        print()
    print("\n")
    
    initial = []
    x=0
    y=0
    while(True):
        posStr = input("Enter initial position: ")
        x = int(posStr[0])
        y = int(posStr[-1])
        initial.append(x-1)
        initial.append(y-1)
        print(initial)
        if(x<=r and x>=1 and y<=c and y>=1):
            break
        else:
            print("\nEnter proper row and column\n")
            initial = []

    
    moves = 1
    reflex_agent = SimpleReflexAgent(initial, moves, g, dirt)
    print("**Simple Reflex Agent**\n")
    reflex_agent.clean_grid()

   

if __name__ == "__main__":
    main()
