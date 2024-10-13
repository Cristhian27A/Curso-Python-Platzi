class Vehicle:
    def __init__(self, brand, model, price):
        # Encapsulamiento
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehículo {self.brand} ha sido vendido")
        else:
            print(f"El vehículo {self.brand} no está disponible")  
    
    # Abstracción 
    def check_available(self):
        return self.is_available

    def get_price(self):  # Abstracción 
        return self.price

    # Métodos abstractos para iniciar y detener el motor
    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

# Clases hijas que heredan de Vehicle
class Car(Vehicle):  # Herencia
    def start_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} está en marcha"
        else:
            return f"El coche {self.brand} no está disponible"     

    def stop_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no está disponible"

class Bike(Vehicle):
    def start_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} no está disponible"     

    def stop_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} no está disponible"

class Truck(Vehicle):
    def start_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} está en marcha"
        else:
            return f"El camión {self.brand} no está disponible"     

    def stop_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} no está disponible"

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no está disponible")

    def inquire_vehicle(self, vehicle: Vehicle):    
        if vehicle.check_available():
            availability = "disponible"
        else:
            availability = "no disponible"
        print(f"El {vehicle.brand} está {availability} y cuesta ${vehicle.get_price()}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido agregado al inventario")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)  
        print(f"El cliente {customer.name} ha sido registrado")

    def show_available_vehicles(self):
        print("Vehículos disponibles en la tienda:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} {vehicle.model} por ${vehicle.get_price()}")

# Crear vehículos
car1 = Car("Toyota", "Corolla", 200000)
bike1 = Bike("Yamaha", "MT-07", 70000)
truck1 = Truck("Volvo", "FH16", 8000000)

# Crear cliente
customer1 = Customer("Cristhian")

# Crear concesionaria
dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

# Mostrar vehículos disponibles
dealership.show_available_vehicles()

# Cliente consulta un vehículo
customer1.inquire_vehicle(car1)

# Cliente compra un vehículo
customer1.buy_vehicle(car1)

# Mostrar vehículos disponibles después de la compra
dealership.show_available_vehicles()
