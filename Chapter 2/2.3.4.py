"""
Q. The harmonic mean is defined by  H=n/n(sigma)i=1. (1/ai)
    is sometimes used as a mean of central tendency .
    Develop an algorithm to compute the harmonic mean of n data values.
"""

choice=int(input("how many number do you wan'na give : "))
list=[]
sum=0
for i in range(choice):
    num=int(input("enter the number : "))
    list.append(num)
for j in list:
    sum=sum+(1/j)

harmonic_mean= len(list)/sum

print("Harmonic Mean = ",harmonic_mean)