import numpy as np
import matplotlib.pyplot as plt

population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)
population[outbreak[0], outbreak[1]]=1
plt.figure(figsize=(6,4), dpi=150)
plt.imshow(population, cmap="viridis", interpolation="nearest")
plt.title("Initial State")
plt.close() #the initial state

beta=0.3
gamma=0.05
a=0 #define variables

for i in range(1,101):
    infectedIndex = np.where(population==1)
    a+=1
    
    if a%30==0 :
        plt.figure(figsize=(6,4), dpi=150)
        plt.imshow(population, cmap="viridis", interpolation="nearest")
        plt.title(f"{i} times")
        plt.close()  #show the figure each 30 times
        

    for i in range(len(infectedIndex[0])):   
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
    
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y):
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0] #for infected people


    for i in range(len(infectedIndex[0])):   
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        population[x,y]=np.random.choice(range(2), 1, p=[gamma, 1-gamma])[0] #for recovered people
    


