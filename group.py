from student import Student
MAX_STUDENTS = 10

class Group:
    def __init__(self, spec, entrance_year, students=None):
        self.spec = spec
        self.entrance_year = entrance_year
        self.__students = []
        for item in students:
            self.add_student(item)

    def add_student(self, student: Student):
        if len(self.__students) == MAX_STUDENTS:
            return None
         for item in self.__students:
            if (item.surname, item.name, item.date_of_birth) == (studen.surname, student.name, student.date_of_birth):
                return None
         self.__students.append(student)

    def __str__(self):
        res = '\n'.join(map(str, self.__students))
        return f'{self.spec}: {self.entrance_year}\nStudents:\n{res}'

if __name__ == '__main__':
    x = Student('Ivan','Ivanov', '1999/02/14','M')
    y = Student('Anna','Bogdanovna', '1999/02/14','G')

    group = Group('math', '2021', [x, x, x, y])
    group.add_student(x)
    group.add_student(y)

    print(group)




