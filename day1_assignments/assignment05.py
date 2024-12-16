# The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
# ulate the average of subjects and display the grade. The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

sub1 =int(input("Enter MATH Obtained marks out of 100 : "))
sub2 =int(input("Enter SCIENCE Obtained marks out of 100 : "))
sub3 =int(input("Enter ENGLISH Obtained marks out of 100 : "))
sum = (sub1+sub2+sub3)
avg = sum/3
if avg>=90:
    print(f"Average of 3 subjects : {(avg)} and Grade is A")
elif avg>=80:
    print(f"Average of 3 subjects : {(avg)} and Grade is B")
elif avg>=70:
    print(f"Average of 3 subjects : {(avg)} and Grade is C")
elif avg>=60:
    print(f"Average of 3 subjects : {(avg)} and Grade is D")
else:
    print(f"Average of 3 subjects : {(avg)} and Grade is F")  