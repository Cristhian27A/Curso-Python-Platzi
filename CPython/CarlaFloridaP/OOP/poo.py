class Person: 
    #f funcion particular para definir un constructor 
    # "self" quiere decir que se llama a si mismo
    def __init__(self, name, age): #un constructor es una funcion propia de las clases
        self.name = name
        self.age = age


    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")
 
person1 = Person("Chester", 3)
person2 = Person("Cristhian", 20)

person1.greet()
person2.greet()

