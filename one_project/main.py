# git hub repository in ubuntu 20.04
class Person:
    def __init__(self,f_name,l_name,age,country):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.country = country
    
    def person_info(self):
        return f"Full name:{self.f_name} {self.l_name},\nage:{self.f_name} {self.age} years old\nCountry:{self.f_name} from {self.country}"
    

person = Person("Fayzullo","Mamajonov",21,"Fergana")

print(person.person_info())
        