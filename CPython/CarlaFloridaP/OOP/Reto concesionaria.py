#Ejercicio concesionaria: compra y venta, el usuario pregunta cuales estan disponibles y comprar
class Vehiculo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.available = True

    def estado(self):   
        if self.available:
            self.available = False
            print(f"El vehiculo marca {self.marca} modelo {self.modelo} ha sido vendido")
        else:
            print(f"El vehiculo de marca {self.marca} modelo {self.modelo} no esta disponible")

class Usuario:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.vender_autos = [] # esto almacenara los autos comprados

    def vender_auto(self, auto):
        if auto.available:
            auto.estado()
            self.vender_autos.append(auto)
        else:
            print(f"El vehiculo de marca {auto.marca} no esta disponible")    
    
    def mostrar_autos_comprados(self):
        if self.vender_autos:
            print(f"{self.name} ha comprado los siguientes autos:")
            for auto in self.vender_autos:
                print(f"{auto.marca} {auto.modelo} - Precio: ${auto.precio}")
        else:
            print(f"{self.name} no ha comprado ningún auto")

    def comprar_auto(self, concesionaria, marca, modelo):
        # Buscar el auto por marca y modelo
        for auto in concesionaria.autos:
            if auto.marca == marca and auto.modelo == modelo:
                if auto.available:
                    self.vender_auto(auto)  # Realizar la compra
                    return
                else:
                    print(f"El vehículo {marca} {modelo} no está disponible.")
                    return
        print(f"El vehículo {marca} {modelo} no se encuentra en la concesionaria.")        

class Concecionaria:
    def __init__(self):
        self.autos = []
        self.users = []

    def add_auto(self, auto):   
        self.autos.append(auto)
        print(f"El vehiculo marca {auto.marca} ha sido agregado")

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def autos_disponibles(self):
        print("Autos disponibles:")
        for auto in self.autos:
            if auto.available:
                print(f"{auto.marca} por {auto.modelo} - Precio: ${auto.precio}")

# se crea los vehiculos
v1 = Vehiculo("Ferrari", "250 GTO", 5000000)
v2 = Vehiculo("MacLaren", "P1", 1000000)  
v3 = Vehiculo("Lamborgini", "Huracan", 6000000 )

# crear usuario 
us = Usuario("Cristhian", "001")

#Se crea la concesionaria y registra el vehiculo y usuario
concesion = Concecionaria()
concesion.add_auto(v1)
concesion.add_auto(v2)
concesion.add_auto(v3)
concesion.register_user(us)

# Mostrar autos disponibles
concesion.autos_disponibles()

# Usuario realiza una compra
us.comprar_auto(concesion, "Ferrari", "250 GTO")

#Mostrar autos disponibles despues de la compra
concesion.autos_disponibles()

# Mostrar autos comprados por el usuario
us.mostrar_autos_comprados()


