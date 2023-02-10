""""
Q. Generate the sequence where each member is the sum of adjacent factorials I.e.

        f3 = 1! + 0!
        f4 = 2! + 1!
        f5 = 3! + 2!
    Note that by definition 0!=1.
"""

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

choice=int(input("Enter how many numbers Do you wan'na generate of the series : "))
pre_term=int(input("Enter first number : "))
curr_term=int(input("Enter second number : "))

print(pre_term, curr_term, end=", ")

for i in range(choice):
    next_term=factorial(pre_term) + factorial(curr_term)
    print(next_term,end=",")

    pre_term=curr_term
    curr_term=next_term
