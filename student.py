from person import Person
class Student(Person):
    def __init__(self,name:str, surname:str, date_of_birth: str, sex: str):
        super().__init__(name, surname, date_of_birth)
        self.sex = sex

    def __str__(self):
        res = super().__str__()
        return f'{res}: {self.sex}'

if __name__ == '__main__':
    x = Student('Ivan','Ivanov', '1999/02/14','M')
    print(x)