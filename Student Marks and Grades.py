print("===== STUDENT GRADES SYSTEM =====")

name = input("Enter student name: ")

maths = float (input("Enter Mathematics marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer Studies marks: "))
science = float(input("Enter Science marks: "))


total = maths + english + computer + science
average = total / 4


if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "E"



print("\n===== STUDENT REPORT =====")
print("Student:", name)
print("Total marks:", total, "out of 400")
print("Average:", round(average, 2))
print("Grade:", grade)