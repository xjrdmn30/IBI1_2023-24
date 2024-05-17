# Define a dictionary representing activities and time spent on each activity
s = {
    'Sleep': 8,
    'Classes': 6,
    'Studying': 3.5,
    'TV': 2,
    'Music': 1,
    'Other': 3.5
}

# Print the dictionary
print(s)
# Import the matplotlib library for visualization
import matplotlib.pyplot as plt
# Extract labels and time values from the dictionary
labels = list(s.keys())
time = list(s.values())
# Create a new figure for the pie chart
plt.figure()
# Plot a pie chart with time values, using labels for the corresponding activities
plt.pie(time, labels=labels)
# Display the plot
plt.show()
