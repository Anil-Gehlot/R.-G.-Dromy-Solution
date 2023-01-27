"""
Q. Design an algorithm to compute the average of n numbers.
"""
#Solution.

choice=int(input("how many number do you wan'na add : "))
list=[]
sum=0
if choice==0:
    print("You can not find the average of 0 numbers.")
    quit()
for i in range(choice):
    num=int(input("enter the number : "))
    list.append(num)

for j in list:
    sum=sum+j
print("Average of given no. is : ",sum/choice)