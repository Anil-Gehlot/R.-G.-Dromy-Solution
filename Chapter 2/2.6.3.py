"""
Q. Given a=0, b=1, and c=1, are the first three numbers of some sequence.
    all the other numbers in the sequence are generated from the sum of 
    their three most recent predecessors.
    Design an algorithm that will refute or confirm this conjecture."""


choice=int(input("Enter how many term do you wan'na generate of this series : "))
a = 0
b = 1
c = 1

print(f'{a}, {b}, {c},',end=" ")

for i in range(0,choice-3):
    next_term=a+b+c
    print(next_term,end=", ")
    a = b
    b = c
    c = next_term

