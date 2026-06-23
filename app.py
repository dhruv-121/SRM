def get_marks():
    while True:
        marks = int(input("Enter marks : "))
        if 10 <= marks <= 99:
            return marks
        print("Invalid! Enter only 2-digit marks.")

sub1 = get_marks()
sub2 = get_marks()
sub3 = get_marks()
sub4 = get_marks()
sub5 = get_marks()

total = (sub1 + sub2 + sub3 + sub4 + sub5)
percentage = (total / 500) * 100

print("Total Marks:", total)
print("Percentage:", percentage, "%")

# Grade
if percentage >= 80:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)

# Division
if percentage >= 60:
    division = "First Division"
elif percentage >= 45:
    division = "Second Division"
elif percentage >= 33:
    division = "Third Division"
else:
    division = "Fail"

print("Division:", division)

# Rank
if percentage >= 90:
    rank = 1
elif percentage >= 80:
    rank = 2
elif percentage >= 70:
    rank = 3
elif percentage >= 60:
    rank = 4
else:
    rank = "Not Ranked"

print("Rank:", rank)