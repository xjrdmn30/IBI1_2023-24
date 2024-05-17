# Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the DALYs data from a CSV file
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
# Extract data for every 10th row up to the 100th row for analysis
data_1 = dalys_data.iloc[0:101:10, 3]
# Extract specific columns from the dataset
entity = dalys_data["Entity"]
afghanistan = dalys_data["Entity"] == "Afghanistan"
afghanistan_data = dalys_data[afghanistan]

china_data = dalys_data[dalys_data['Entity'] == "China"]

# Calculate the mean of DALYs for China
china_mean = np.mean(china_data["DALYs"])

# Check if the mean of DALYs for China is above, below, or equal to a certain threshold
if china_mean > 22270.51:
    print("DALYs in 2019 for China were below the mean.")
elif china_mean < 22270.51:
    print("DALYs in 2019 for China were above the mean.")
else:
    print("DALYs in 2019 for China were equal to the mean.")
# Plot a scatter plot for DALYs of China
plt.figure()
plt.plot(china_data.Year, china_data.DALYs, "ro")
plt.title("DALYs of China")
plt.xticks(china_data.Year, rotation=-90)
plt.show()
plt.clf()
# Print data specific to Afghanistan and data from every 10th row up to the 100th row
print(afghanistan_data)
print(data_1)
# Print the mean of DALYs for China
print(china_mean)
# Filter countries with DALYs less than or equal to a certain threshold and print the results
dalys = dalys_data["DALYs"]
countries = dalys <= 18000
countries_data = entity[countries]
print(countries_data)
