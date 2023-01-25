""""
Q. For a given x and a given n, design an algorithm to compute x^n/n!(x to the power n / factorial of n).
"""

# Solution  

x=float(input("Enter a number for Exponent : "))                
num=int(input("enter a number for factorial : "))
fact=1
exponent=x**num
if num==0:
    print(f"Factorial of {num} : {1}")
elif num <0:
    print("There is no factorial of Negative Numbers")
else:
    for i in range(1, num+1):
        fact=fact*i
        
    print(f"The solution of {x}^{num}/{num}!: {exponent/fact}")