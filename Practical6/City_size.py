# Define city sizes and names for the UK and China
uk_citysize = [0.56, 0.62, 0.04, 9.7]
cn_citysize = [0.58, 8.4, 29.9, 22.2]
uk_city = ['Edinburgh', 'Glasgow', 'Stirling', 'London']
cn_city = ['Haining', 'Hangzhou', 'Shanghai', 'Beijing']
# Print sorted city sizes for UK and China
print("Sorted UK City Sizes:")
print(sorted(uk_citysize))
print("Sorted China City Sizes:")
print(sorted(cn_citysize))
# Import matplotlib for plotting
import matplotlib.pyplot as plt
# Plot bar chart for UK cities
plt.figure(figsize=(8,6))
plt.bar(uk_city, uk_citysize)
plt.xlabel('UK City')
plt.ylabel('City Size')
plt.title('City Sizes in the UK')
plt.show()
# Plot bar chart for China cities
plt.figure(figsize=(8,6))
plt.bar(cn_city, cn_citysize)
plt.xlabel('China City')
plt.ylabel('City Size')
plt.title('City Sizes in China')
plt.show()
