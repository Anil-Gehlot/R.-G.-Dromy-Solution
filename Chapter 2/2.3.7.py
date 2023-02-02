"""
Q. Develop an algorithm that prints out n values of the sequence 
        1  -1  1  -1  1  -1  1..............
"""

num=int(input("Enter the number : "))
first_term=int(input("Enter first of the series (1 OR -1) : "))
list=[]
list.append(first_term)
for i in range(num-1):
    if first_term == -1:
        first_term=first_term+2
        list.append(first_term)
    else:
        first_term=first_term-2
        list.append(first_term)
print(list)