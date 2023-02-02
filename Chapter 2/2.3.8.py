"""
Q. Develop an algorithm to compute the sum of the first n terms (n>=1) of the series 
    s= 1 - 3 + 5 - 7 + 9 -........
"""        

num=int(input("enter the number of term : "))
list1=[1]
var=1
for i in range(1,num):
    var=var+2

    if i%2==0:
        list1.append(var)
    else:
        list1.append(-var)

print("you series is : ",list1)
print("sum of your list is : ",sum(list1))