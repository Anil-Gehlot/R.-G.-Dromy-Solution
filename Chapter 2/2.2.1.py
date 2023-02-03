"""
Q. Modify the algorithm above so that marks are read until an end of file is encountered. 
For this set of marks determine the total number of marks, the number of passes, and the percentage pass rate.

"""

# Solution.

list=[55,42,77,63,29,57,89]     #marks are taken according to the example given in the book.
count_pass=0
total_no_of_marks=len(list)

for i in list:
    if i>=50:
        count_pass+=1

percentage= (count_pass*100)/total_no_of_marks


print("Total no. of marks = ",total_no_of_marks)
print("the no. of pass student = ", count_pass)
print("percentage pass rate = ", percentage)