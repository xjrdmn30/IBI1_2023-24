#Recursive
#the next number is 3 larger than the twice of last number 
#thefirst one is 4
count=0.5
#5 cycles in total
for i in range(1,6):
    count=count*2+3
    print(count)