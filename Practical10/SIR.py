import numpy as np
import matplotlib.pyplot as plt  # Import libraries

# Define variables
total = 10000
susceptible = 9999
infected = 1
recovered = 0
beta = 0.3
gamma = 0.05 
# Lists to store counts over time
all_susceptible = [susceptible]
all_infected = [infected]
all_recovered = [recovered]
# Simulate the SIR model over time
for time in range(1, 1000):
    # Calculate probabilities of infection and recovery
    probability_infected = beta * all_infected[-1] / (total - 1)
    probability_recovered = gamma
    
    # Simulate new infections and recoveries
    new_infected = np.random.choice(range(2), all_susceptible[-1], p=[1 - probability_infected, probability_infected]).sum()
    new_recovered = np.random.choice(range(2), all_infected[-1], p=[1 - probability_recovered, probability_recovered]).sum()
    # Update counts
    all_susceptible.append(all_susceptible[-1] - new_infected)
    all_infected.append(all_infected[-1] + new_infected - new_recovered)
    all_recovered.append(all_recovered[-1] + new_recovered)
# Plot the SIR model results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(range(1, 1001), all_susceptible, label="Susceptible")
plt.plot(range(1, 1001), all_infected, label="Infected")
plt.plot(range(1, 1001), all_recovered, label="Recovered")
plt.xlabel("Time")
plt.ylabel("Number")
plt.title("SIR Model")
plt.legend(["Susceptible", "Infected", "Recovered"])
plt.savefig("SIR Model.png", format="png")
plt.show()
plt.clf()  # Clear the plot to avoid overlapping figures
