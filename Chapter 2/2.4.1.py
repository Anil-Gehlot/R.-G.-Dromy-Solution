"""
Q. For a given n, design an algorithm to compute 1/n! .
"""

# Solution 

num=int(input("enter a number : "))
fact=1
if num==0:
    print(f"Factorial of {num} : {1}")
elif num <0:
    print("There is no factorial of Negative Numbers")
else:
    for i in range(1, num+1):
        var1=i*fact
        fact=var1
    print(f"The solution of 1/{num}! : {1/fact}")