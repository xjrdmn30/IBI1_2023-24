#ues a symbol to 
n=0
#provide a density 
den=5
#set a cycle to calculate when the density is larger than 90
while 1==1:
    den=den*2
    n +=1
    if den>=90: 
        break
#to output the time of cycles
print("the number of days is " + str(n))