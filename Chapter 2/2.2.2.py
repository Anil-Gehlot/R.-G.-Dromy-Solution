"""
Q. Design an algorithm that reads a list of numbers and makes a count of the number of the number of negative and
     the number of non-negative members in the set. 
"""
# Solution 

list= []
total=int(input("Enter how many numbers Do you wan'na give : "))

for j in range(total):
    num=int(input("Enter the number : "))
    list.append(num)
print(list)

positive=0
negative=0

for i in list:
    if i > 0:
        positive += 1
    elif i<0 :
        negative += 1
    else:
        pass
print(f"\n There are {positive} positive number in list \n and {negative} negative numbers in list")