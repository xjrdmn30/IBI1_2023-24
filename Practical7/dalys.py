import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv")
data_1=dalys_data.iloc[0:101:10,3]

entity=dalys_data["Entity"]
afghanistan=dalys_data["Entity"]=="Afghanistan"
afghanistan_data=dalys_data[afghanistan]

china_data = dalys_data[dalys_data['Entity']=="China"]
china_mean=np.mean(china_data["DALYs"])


if china_mean>22270.51 :
    print("DALYs in 2019 for China were below the mean.")
elif china_mean<22270.51 :
    print("DALYs in 2019 for China were above the mean.")
else :
    print("DALYs in 2019 for China were equal to the mean.")
            

plt.figure()
plt.plot(china_data.Year, china_data.DALYs, "ro")
plt.title("dalys of china")
plt.xticks(china_data.Year, rotation=-90)
plt.show()
plt.clf()

print(afghanistan_data)
print(data_1)
print(china_mean)
#question

dalys=dalys_data["DALYs"]
countries=dalys<=18000
countries_data=entity[countries]
print(countries_data)

