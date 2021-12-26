import datetime

class Person:
    def __init__(self,name: str, surname: str,date_of_birth:str):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def __str__(self):
        age = datetime.datetime.now() - datetime.date(self.date_of_birth.split('/'))
        return f'{self.surname} {self.name}, {age} years'

