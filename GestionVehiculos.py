# Clase Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrarInfo(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"

# Auto hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, numeroPuertas, esAutomatico):
        super().__init__(marca, modelo, año)
        self.numeroPuertas = numeroPuertas
        self.esAutomatico = esAutomatico

    def mostrar_info(self):
        base_info = super().mostrarInfo()
        return f"{base_info}, Número de Puertas: {self.numeroPuertas}, Es Automático: {'Sí' if self.esAutomatico else 'No'}"

#  Moto hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindraje, tipo):
        super().__init__(marca, modelo, año)
        self.cilindraje = cilindraje
        self.tipo = tipo

    def mostrarInfo(self):
        base_info = super().mostrarInfo()
        return f"{base_info}, Cilindraje: {self.cilindraje}, Tipo: {self.tipo}"

# Main
def main():
    # lista de vehículos
    vehiculos = [
        Auto("Volkswagen", "Golf", 2024, 1.5, True),
        Auto("Mercedes-Benz", "CLA Coupé", 2024, 2, True),
        Moto("Kawasaki", "Ninja 400", 2024, 399, "Deportiva"),
        Moto("Honda", "CB500X", 2024, 471, "Aventura")
    ]

    # información de cada vehículo
    for vehiculo in vehiculos:
        print(vehiculo.mostrarInfo())

# Ejecutar
if __name__ == "__main__":
    main()