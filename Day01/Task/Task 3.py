
marks = int(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = 'A'
elif marks >= 75:
    grade = 'B'
elif marks >= 60:
    grade = 'C'
elif marks >= 40:
    grade = 'D'
else:
    grade = 'Fail'

print(f"Your Grade: {grade}")
