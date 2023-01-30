"""
Q. Redesign the algorithm so that it only needs to perform n-1 addition to sum n numbers.
"""

#Solution.

choice=int(input("how many number do you wan'na add : "))
list=[]

for i in range(choice):
    num=int(input("enter the number : "))
    list.append(num)

sum=list[0]

for j in range(1,len(list)):
    sum=sum+list[j]

print(f"The sum of given {choice} number is : {sum}")