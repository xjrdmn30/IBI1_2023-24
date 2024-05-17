import numpy as np
import matplotlib.pyplot as plt #import libraries

total=10000
infected=1
recovered=0
beta=0.3
gamma=0.05 
vaccination_rate =[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1] #define variables 

all_infected=[]

for rate in vaccination_rate :
    
    susceptible=int(9999-rate*(total-1))
    rate_infected=[infected] #loop of vaccination rate
    
    for time in range(1,1001) :
        probability_infected=beta*rate_infected[-1]/(total-1)
        probability_recovered=gamma
        new_infected=np.random.choice(range(2), susceptible, p=[1-probability_infected,probability_infected]).sum()
        new_recovered=np.random.choice(range(2), rate_infected[-1], p=[1-probability_recovered,probability_recovered]).sum()

        susceptible -= new_infected
        rate_infected.append(rate_infected[-1]+new_infected-new_recovered)  #write down numbers of infected people
    all_infected.append(rate_infected)

for i,rate in enumerate(vaccination_rate):
    plt.plot(range(1, 1002), all_infected[i], label=f"Vaccination Percentage={rate*100}%") 

plt.xlabel("Time")
plt.ylabel("Number of infected people")
plt.title("SIR Moedel with different vaccination rates")
plt.legend(["0", "10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"])
plt.savefig("SIR Vaccination.png", format="png")
plt.show()
plt.clf() #show the figure