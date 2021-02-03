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
import datetime


class Person:
    person_count = 0

    def __init__(self, name, lastname, gender, birthday):
        self.name = name
        self.lastname = lastname
        self. gender = gender
        self.birthday = birthday
        self.age = 0
        self.category = ''
        Person.person_count += 1

    def age_calculate(self):
        birth_date = datetime.datetime.strptime(self.birthday, '%Y%m%d').date()
        self.age = int((datetime.date.today() - birth_date).days / 365)
        return self.age

    def print_happy_birthday(self):
        birth_date = datetime.datetime.strptime(self.birthday, '%Y%m%d').date()
        if datetime.date.today().day == birth_date.day and datetime.date.today().month == birth_date.month:
            print('Happy birthday!')

    def assign_category(self):
        self.age_calculate()
        if self.age < 13:
            self.category = 'child'
        elif 12 < self.age < 18:
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

    def average_mark(self):
        av_mark = 0
        for i in self.diary:
            av_mark += i[2]
        av_mark = av_mark / len(self.diary)
        return av_mark


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
    student1 = Student('Иван', 'Петренко', 'м', '20120113', '2')
    student2 = Student('Олена', 'Шевченко', 'ж', '20101003', '4')
    student3 = Student('Максим', 'Ткачук', 'м', '20101205', '4')
    teacher1 = Teacher('Нина', 'Иванова', 'ж', '19800312', 'Математика', 10000)
    teacher2 = Teacher('Олег', 'Ткаченко', 'м', '19780730', 'История', 10000)
    print(f'Количество сутдентов: {Student.student_count}. Количество учителей: {Teacher.teacher_count}')
    teacher1.assign_group(3)
    teacher2.assign_group(2)
    teacher2.assign_group(4)
    print(teacher1.groups)
    print(teacher2.groups)
    teacher1.change_salary(1.05)
    print(teacher1.salary)
    student3.change_group(3)
    student1.make_mark('11.01.21', 'Математика', 12)
    student1.make_mark('11.01.21', 'История', 7)
    student2.make_mark('12.01.21', 'Математика', 10)
    student3.make_mark('12.01.21', 'География', 9)
    student3.make_mark('11.01.21', 'История', 11)
    print(student1.show_diary())
    print(student2.show_diary())
    print(student3.show_diary())
    print(student1.average_mark())
    print(student1.age_calculate())
    print(student1.assign_category())
    print(teacher1.age_calculate())
    print(teacher1.assign_category())
    print(teacher2.assign_category())
    student1.print_happy_birthday()
