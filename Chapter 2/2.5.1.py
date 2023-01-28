"""
Q. Design an algorithm to find the sum of the first n terms of the series.....
    f= 0!+1!+2!+3!+4!+5!..........+n!   (n>=0)
"""

def factorial(num):
    fact=1
    total=0
    for i in range(1,num+1):
        fact=fact*i
        total=total+fact
    return total+1

num=int(input("Enter how many number do you wan'na give in the series  : "))
summation=factorial(num)
print(f"The sum of the series with {num} number is :  {summation}")