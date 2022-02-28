import csv 
import math

with open("data.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data  = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total+=int(x)    
    mean = total/n
    return mean

squaredList = []

for no in data:
    a = int(no)-mean(data)
    a = a**2
    squaredList.append(a)

sum = 0

for i in squaredList:
    sum = sum+i 
    
res =  sum/(len(data)-1)

sd = math.sqrt(res)
print("The Standard Deviation is:", sd)