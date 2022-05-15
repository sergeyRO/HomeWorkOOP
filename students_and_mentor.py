class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grading(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        comment = f"Имя: {self.name}\nФамилия: {self.surname}"
        for key in self.grades:
            i = 0.0
            for item in self.grades[key]:
                i += item
            comment += f"\nСредняя оценка за домашнее задание по {key}: {round(i / len(self.grades[key]), 2)}"
        comment += f"\nКурсы в процессе изучения: {','.join(self.courses_in_progress)}"
        comment += f"\nЗавершённые курсы: {','.join(self.finished_courses)}"
        return comment

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Не студент")
            return
        else:
            comment = ''
            for key in self.grades:
                i = 0.0
                k = 0.0
                for item in self.grades[key]:
                    i += item
                if key in other.grades:
                    for item in other.grades[key]:
                        k += item
                comment += f"{key}: {round(k / len(other.grades[key]), 2)} < {round(i / len(self.grades[key]), 2)} ({round(i / len(self.grades[key]), 2) > round(k / len(other.grades[key]), 2)})\n"
        return comment


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        comment = f"Имя: {self.name}\nФамилия: {self.surname}"
        for key in self.grades:
            i = 0.0
            for item in self.grades[key]:
                i += item
            comment += f"\nСредняя оценка за лекцию по {key}: {round(i / len(self.grades[key]), 2)}"
        return comment

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Не лектор")
            return
        else:
            comment = ''
            for key in self.grades:
                i = 0.0
                k = 0.0
                for item in self.grades[key]:
                    i += item
                if key in other.grades:
                    for item in other.grades[key]:
                        k += item
                comment += f"{key}: {round(k / len(other.grades[key]), 2)} < {round(i / len(self.grades[key]), 2)} ({round(i / len(self.grades[key]), 2) > round(k / len(other.grades[key]), 2)})\n"
        return comment


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


best_student = Student('Roy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['Python']
best_student.finished_courses += ['C#']
best_student.finished_courses += ['C++']

best_student1 = Student('Soso', 'Man', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student1.courses_in_progress += ['C++']
best_student1.finished_courses += ['Python']
best_student1.finished_courses += ['C#']
best_student1.finished_courses += ['C++']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['C++']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'C++', 1)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(best_student1, 'C++', 10)
cool_reviewer.rate_hw(best_student1, 'Python', 2)
cool_reviewer.rate_hw(best_student1, 'Python', 10)

some_lecturer = Lecturer('Sergey', 'R')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['C++']
some_lecturer.courses_attached += ['C#']

some_lecturer1 = Lecturer('Alex', 'RD')
some_lecturer1.courses_attached += ['Python']
some_lecturer1.courses_attached += ['C++']
some_lecturer1.courses_attached += ['F++']

best_student.grading(some_lecturer, 'C++', 5)
best_student.grading(some_lecturer, 'Python', 2)
best_student.grading(some_lecturer, 'C++', 10)

best_student.grading(some_lecturer1, 'Python', 10)
best_student.grading(some_lecturer1, 'C++', 1)
best_student.grading(some_lecturer1, 'Python', 10)

print(best_student.grades)

print(cool_reviewer)
print()
print(some_lecturer)
print()
print(best_student)

print()
print("Лекторы")
print(some_lecturer > some_lecturer1)
print("Студенты")
print(best_student > best_student1)

print('---------------------------')
list_student = [best_student, best_student1]
list_lecturer = [some_lecturer, some_lecturer1]


#Задание 4 Средняя оценка всех студентов за ДЗ по определенному курсу
def student_grades(list_student, course):
    _sum = 0
    i = 0
    for item in list_student:
        if course in item.grades:
            for val in item.grades[course]:
                _sum += val
                i += 1
    return round(_sum/i,2)

#Задание 4 Средняя оценка всех лекторов за лекции по определенному курсу
def lecturer_grades(list_lecturer, course):
    _sum = 0
    i = 0
    for item in list_lecturer:
        if course in item.grades:
            for val in item.grades[course]:
                _sum += val
                i += 1
    return round(_sum/i,2)

course = input("Введите название курса: ")
print(student_grades(list_student, course))
print(lecturer_grades(list_lecturer, course))