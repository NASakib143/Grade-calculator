def function_grade(number):
    if number >= 80:
        return "A+"
    elif number >= 70:
        return "A"
    elif number >= 60:
        return "A-"
    elif number >= 50:
        return "B"
    elif number >= 40:
        return "C"
    elif number >= 30:
        return "D"
    else:
        return "F"
subjects = ["Math", "Art", "English", "History", "Science"]
marks = []
for subject in subjects:
    score = float(input(f"Enter your marks in {subject} out of 100: "))
    marks.append(score)

total_marks = sum(marks)
average = total_marks / len(subjects)
grade = function_grade(average)

print("\n ------ Grade Calculator ------")
print(f"Total Marks: {total_marks} out of {len(subjects) * 100}")
print(f"Average Marks: {average:.2f}")
print(f"Your Grade: {grade}")
