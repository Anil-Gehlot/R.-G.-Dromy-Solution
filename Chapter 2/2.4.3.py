""" Design an algorithm to determine whether or not a number n is a fatorial number """

num=int(input("Enter the number : "))
fact=1
for i in range(1,num+1):
    fact=fact*i
    if fact==num:
        print(f"{num} is the factorial of : {i}")
        break
else:
    print(f"{num} is not the factorial of any number.")