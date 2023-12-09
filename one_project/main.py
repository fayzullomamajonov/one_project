# git hub repository in ubuntu 20.04
# Person nomli class yaratildi
class Person:
    # Person clasiga atributlar kiritildi 
    def __init__(self,f_name,l_name,age,country):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.country = country
    # person_info() nomli funksiya yaratildi
    def person_info(self):
        return f"Full name:{self.f_name} {self.l_name},\nage:{self.f_name} {self.age} years old\nCountry:{self.f_name} from {self.country}"
    
# Person classi orqali person obyekti yaratildi
person = Person("Fayzullo","Mamajonov",21,"Fergana")

# person obyektining ma`lumotlarini olish uchun person_info() f-yasiga murojat qilindi
print(person.person_info())
        