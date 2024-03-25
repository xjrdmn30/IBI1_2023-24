uk_citysize = [0.56, 0.62, 0.04, 9.7]
cn_citysize = [0.58, 8.4, 29.9, 22.2]
uk_city = ['Edinburgh', 'Glasgow', 'Stirling', 'London']
cn_city = ['Haining', 'Hangzhou', 'Shanghai', 'Beijing']
print (sorted(uk_citysize))
print (sorted(cn_citysize))
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.bar(uk_city,uk_citysize)
plt.xlabel('uk_city')
plt.ylabel('uk_citysize')
plt.show()
plt.figure(figsize=(8,6))
plt.bar(cn_city,cn_citysize)
plt.xlabel('cn_city')
plt.ylabel('cn_citysize')
plt.show()