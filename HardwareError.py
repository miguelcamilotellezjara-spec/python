#Notes on POOP course:
from pyclbr import Class


Class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 30)
person1.greet()

person2 = Person("Bob", 25)
person2.greet()

#accesing and modyfying data 
Class User:

def __init__(self, username, email, password):
    self.username = username #atribute
    self._email = email #protected atribute
    self.password = password

def say_hi_touser(self, user):
    print(f"Sending message to {user.username}... Hi {user.username}!", it´s {self.username} )"

user1 = User("dantheman", "dan@gmail.com", "123")

print(user1._email)

user1._email = "newemail@gmail.com" #not recommended to change protected atribute directly
print(user1._email)    

def get_email(self): #yes, we can create a method to access the protected atribute
    return self._email

user1.:email = "12322179846"
print(user1.get_email())    #not recommended to change protected atribute directly, but we can create a method to access it

def set_email(self, new_email):
    self._email = new_email #yes, we can create a method to change the protected atribute

user1.set_email("danny@outlook.com"

#python way with property decorator
@property
def email(self):    
    return  self._email #Getter property

@email.setter
def email(self, new_email): 
    self._email = new_email #Setter property

##Static attributes
#Static attributes are shared among all instances of a class. They are defined at the class level and can be accessed using the class name or an instance of the class.

##Static method
#belongs to the class rather than an instance of the class, and can be called without creating an instance of the class. They are defined using the @staticmethod decorator.
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b    
result = MathUtils.add(5, 3)
print(result)  # Output: 8  
