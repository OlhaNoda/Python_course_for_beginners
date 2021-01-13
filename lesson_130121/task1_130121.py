# task1_130121
"""
Task 1
School
Make a class structure in python representing people at school.
Make a base class called Person, a class called Student, and another one called Teacher.
Try to find as many methods and attributes as you can which belong to different classes,
and keep in mind which are common and which are not. For example, the name should be a Person attribute,
while salary should only be available to the teacher.
"""


class Person:
    person_count = 0

    def __init__(self, name, lastname, gender, birthday):
        self.name = name
        self.lastname = lastname
        self. gender = gender
        self.birthday = birthday
        self._age = 0
        self.category = ''
        Person.person_count += 1

    def age(self):
        pass

    def happy_birthday(self):
        pass

    def assign_category(self):
        if self._age < 13:
            self.category = 'child'
        elif 12 < self._age < 18:
            self.category = 'teenager'
        else:
            self.category = 'adult'
        return self.category


class Student(Person):
    student_count = 0

    def __init__(self, name, lastname, gender, birthday, group):
        super().__init__(name, lastname, gender, birthday)
        self.group = group
        self.diary = []
        Student.student_count += 1

    def change_group(self, new_group_number):
        self.group = new_group_number

    def make_mark(self, date, subject, mark):
        note = (date, subject, mark)
        self.diary.append(note)

    def show_diary(self):
        return self.diary


class Teacher(Person):
    teacher_count = 0

    def __init__(self, name, lastname, gender, birthday, subject, salary):
        super().__init__(name, lastname, gender, birthday)
        self.subject = subject
        self.salary = salary
        self.groups = set()
        Teacher.teacher_count += 1

    def change_salary(self, percent):
        self.salary = self.salary * percent

    def assign_group(self, group_number):
        self.groups.add(group_number)

    def delete_group(self, group_number):
        self.groups.remove(group_number)


if __name__ == "__main__":
    student1 = Student('Иван', 'Петренко', 'м', '22.04.12', '2')
    student2 = Student('Олена', 'Шевченко', 'ж', '03.10.10', '4')
    student3 = Student('Максим', 'Ткачук', 'м', '05.12.10', '4')
    teacher1 = Teacher('Нина', 'Иванова', 'ж', '12.03.80', 'Математика', 10000)
    teacher2 = Teacher('Олег', 'Ткаченко', 'м', '30.07.78', 'История', 10000)
    print(f'Количество сутдентов: {Student.student_count}. Количество учителей: {Teacher.teacher_count}')
    teacher1.assign_group(3)
    teacher2.assign_group(2)
    teacher2.assign_group(4)
    print(teacher1.groups)
    print(teacher2.groups)
    teacher1.change_salary(1.05)
    print(teacher1.salary)
    student3.change_group(3)
    student1.make_mark('11.01.21', 'Математика', '12')
    student1.make_mark('11.01.21', 'История', '8')
    student2.make_mark('12.01.21', 'Математика', '10')
    student3.make_mark('12.01.21', 'География', '9')
    student3.make_mark('11.01.21', 'История', '11')
    print(student1.show_diary())
    print(student2.show_diary())
    print(student3.show_diary())
