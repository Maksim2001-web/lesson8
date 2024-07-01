grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
def calculate_average_grade(grades):
    return sum(grades) / len(grades)


def create_student_grades_dict(grades, students):
    student_grades = {}
    for student, grade_list in zip(sorted(students), grades):
        student_grades[student] = calculate_average_grade(grade_list)
    return student_grades

student_grades = create_student_grades_dict(grades, students)
print(student_grades)