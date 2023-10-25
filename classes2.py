class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        print(f"{self.name} is eating")

# Create an instance of the Person class
p = Person("Joe", 21, "male")

# Access and print instance attributes
print(p.name)
print(p.age)
print(p.gender)

# Call the eat method
p.eat()
