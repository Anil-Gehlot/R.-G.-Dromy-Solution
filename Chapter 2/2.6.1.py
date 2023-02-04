"""
Q. Implement the Fibonacci algorithm as a function that accepts as input two consecutive 
    Fibonacci numbers and returns as output the next Fibonacci number.
"""

choice = int(input("Enter how many terms Do you wan'na generate of fibonacci series : "))
pre_term=int(input("Enter first term of the series : "))
cur_term=int(input("Enter second term of the series : "))

print(pre_term,end=", ")
print(cur_term,end=", ")

for i in range(1,choice-1):
    next_term=pre_term+cur_term
    print(next_term,end=", ")

    pre_term=cur_term          # This is the right way.  
    cur_term=next_term        

    # cur_term=next_term       #It will not give right output.
    # pre_term=cur_term
    
