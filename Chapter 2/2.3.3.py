"""
Q. Design an algorithm to compute the sum of the squares of n numbers.
"""

#Solution 

choice=int(input("how many number do you wan'na add : "))
list=[]
sum=0
for i in range(choice):
    num=int(input("enter the number : "))
    sqr=num*num
    list.append(sqr)

for j in list:
    sum=sum+j
print(sum)