student_name = "Sarah"
student_score = 76

print("STUDENT RESULTS MANAGER")
print("-----------------------")

print("Name:", student_name)
print("Score:", student_score)

if student_score >= 70:
    grade = "A"
elif student_score >= 60:
    grade = "B"
elif student_score >= 50:
    grade = "C"
elif student_score >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if student_score >= 50:
    print("Status: Pass")
else:
    print("Status: Fail")

student_name = input("Enter student name: ")
student_score = float(input("Enter student score: "))

print()
print("STUDENT RESULTS MANAGER")
print("-----------------------")
print("Name:", student_name)
print("Score:", student_score)

if student_score >= 70:
    grade = "A"
elif student_score >= 60:
    grade = "B"
elif student_score >= 50:
    grade = "C"
elif student_score >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if student_score >= 50:
    print("Status: Pass")
else:
    print("Status: Fail")

students = [
    {"name": "David", "score": 64},
    {"name": "Jane", "score": 38},
    {"name": "Sarah", "score": 76}
]

print(students)

for student in students:
    print("Name:", student["name"])
    print("Score:", student["score"])
    print()

for student in students:
    score = student["score"]

    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Name:", student["name"])
    print("Score:", score)
    print("Grade:", grade)
    print()

for student in students:
    score = student["score"]

    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 40:
        grade = "D"
    else:
        grade = "F"

    if score >= 50:
        status = "Pass"
    else:
        status = "Fail"

    print("Name:", student["name"])
    print("Score:", score)
    print("Grade:", grade)
    print("Status:", status)
    print("--------------------")

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"

print(calculate_grade(76))
print(calculate_grade(64))
print(calculate_grade(38))

def calculate_status(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"

students = [
    {"name": "David", "score": 64},
    {"name": "Jane", "score": 38},
    {"name": "Sarah", "score": 76}
]

for student in students:
    score = student["score"]

    grade = calculate_grade(score)
    status = calculate_status(score)

    print("Name:", student["name"])
    print("Score:", score)
    print("Grade:", grade)
    print("Status:", status)
    print("--------------------")

def calculate_average(students):
    total = 0

    for student in students:
        total = total + student["score"]

    average = total / len(students)

    return average

class_average = calculate_average(students)

print("Class average:", class_average)

class_average = calculate_average(students)

print("Class average:", round(class_average, 2))

students = [
    {"name": "David", "score": 64},
    {"name": "Jane", "score": 38},
    {"name": "Sarah", "score": 76}
]


def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def calculate_status(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"


def calculate_average(students):
    total = 0

    for student in students:
        total = total + student["score"]

    average = total / len(students)

    return average


print("STUDENT RESULTS MANAGER")
print("=======================")

for student in students:
    score = student["score"]

    print("Name:", student["name"])
    print("Score:", score)
    print("Grade:", calculate_grade(score))
    print("Status:", calculate_status(score))
    print("-----------------------")


class_average = calculate_average(students)

print("Class average:", round(class_average, 2))
highest_score = max(student["score"] for student in students)
print("Highest score:", highest_score)