s ={
    'Sleep': 8,
    'Classes': 6,
    'Studying': 3.5,
    'TV': 2,
    'Music': 1,
    'Other' : 3.5
}
print (s)
#import visualization tools
import matplotlib.pyplot as plt
labels=list(s.keys())
time=list(s.values())
plt.figure()
plt.pie(time, labels=labels)
plt.show()