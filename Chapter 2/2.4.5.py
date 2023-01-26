"""
Q. Design an algorithm to simulate multiplication by addition.
    Your program should accept as input two integers(they may be zero,positive or negative).
    
"""
# Solution 1

num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
sum=0

if num1==0 or num2==0:
    print("Multiplication of both number by addition is : ",0)
    quit()

for i in range(abs(num1)):
    sum=sum+(abs(num2))

if num1<0 and num2>0:
    print("Multiplication of both number by addition is : ",-sum)
elif num1>0 and num2<0:
    print("Multiplication of both number by addition is : ",-sum)
elif num1<0 and num2<0:
    print("Multiplication of both number by addition is : ",sum)
else:
    print("Multiplication of both number by addition is : ",sum)



# Solution 2

def numadd(num1,num2):
    sum = 0
    if num1 == 0 :
        for i in range(abs(num2)):
            sum = abs(num2) + sum
            return 0
    elif num2 == 0 :
        for i in range(abs(num1)):
            sum = abs(num1) + sum
            return 0
    else:
        for i in range(abs(num1)):
            sum = abs(num2) + sum
    if num1 < 0 and num2 < 0:
        return  sum
    if num1 > 0 and num2 > 0:
        return  sum
    if num1 < 0 or num2 < 0:
        return  -sum
    if num1 ==  0 and num2 == 0:
        return  0
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
c =numadd(num1,num2)
print("Multiplication of both number by addition is : ",c)