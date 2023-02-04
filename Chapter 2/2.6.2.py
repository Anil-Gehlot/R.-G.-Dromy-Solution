"""
Q. The first few numbers of the Lucas sequence which is a variation on Fibonacci sequence are :
    1, 3, 4, 7, 11 , 18, 29
    Design an algorithm to generate the Lucas sequence.
"""

choice = int(input("Enter how many terms Do you wan'na generate of fibonacci series : "))
pre_term=2
cur_term=1

print(pre_term,end=", ")
print(cur_term,end=", ")

for i in range(1,choice-1):
    next_term=pre_term+cur_term
    print(next_term,end=", ")

    pre_term=cur_term          # This is the right way.  
    cur_term=next_term        

    # cur_term=next_term       #It will not give right output.
    # pre_term=cur_term
    
