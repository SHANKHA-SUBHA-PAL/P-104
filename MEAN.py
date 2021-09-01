import csv
from os import read
from collections import Counter

with open('Data-visualization-master\csv files\height-weight.csv',newline='')as f:
    reader = csv.reader(f)
    file_data=list(reader)


# removing the heading
file_data.pop(0)

new_data=[]

# going through the entire list and taking only height value and creating a new list
for i in range(len(file_data)):
    num= file_data[i][2]
    new_data.append(float(num))


# calculate the mean
length= len(new_data)
total =0
for x in new_data:
    total+=x

mean = total/length
print("Mean: ",mean)

# the section in which we find median
length = len(new_data)
new_data.sort()

if length%2 == 0:
    #getting the first number1
    median1 = float(new_data[length//2])

    # getting the second number
    median2= float(new_data[length//2-1])

    median = (median1+median2)/2

else:
    median = new_data[length//2]

print("Median: ",median)

# the section in which we find mode
data = Counter(new_data)

mode_data_for_range={
    "75-85": 0,
    "85-95": 0,
    "95-105": 0,
    "105-115":0,
    "115-125":0
}

for weight,occurrence in data.items():
    if 75 < float(weight) <85:
        mode_data_for_range["75-85"]+=occurrence
    elif 85< float(weight) <95:
        mode_data_for_range["85-95"]+=occurrence
    elif 95 < float(weight) < 105:
        mode_data_for_range["95-105"]+=occurrence
    elif 105 < float(weight) < 115:
        mode_data_for_range["105-115"]+=occurrence
    elif 115 < float(weight) < 125:
        mode_data_for_range["115-125"]+=occurrence

print(mode_data_for_range)

mode_range, mode_occurrence = 0,0

for range,occurrence in mode_data_for_range.items():
    if occurrence> mode_occurrence:
        mode_range,mode_occurrence = [int(range.split("-")[0]),int(range.split("-")[1])],occurrence

print(mode_range)
# [60,70]

mode = float((mode_range[0]+mode_range[1])/2)
print(mode)