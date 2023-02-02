"""
Q. Generate the first n terms of the sequence 
    1   2   4   8   16  32............
"""


num=int(input("Enter a number : "))
var=1
print(var,end=" ")
for i in range(1, num+1):
    var=var+var
    print(var,end=" ")