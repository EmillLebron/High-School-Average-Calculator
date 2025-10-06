#Aquí están las funciones y formulas
def celsius_a_fahrenheit (Celsius):
    return (Celsius * 1.8) + 32
def celsius_a_kelvin (celsius):
    return celsius + 273.15
def celsius_a_rankine (celsius):
    return celsius * 1.8 + 491.67
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 0.555555555555555555556
def fahrenheit_a_kelvin (fahrenheit):
    return (fahrenheit - 32) * 0.5555555555555555555556 + 273.15
def fahrenheit_a_rankine (fahrenheit):
    return fahrenheit + 459.67
def kelvin_a_celsius(kelvin):
    return kelvin - 273.15
def kelvin_a_fahrenheit(kelvin):
    return (kelvin - 273.15) * 1.8 + 32
def kelvin_a_rankine (kelvin):
    return kelvin * 1.8
def rankine_a_celsius(rankine):
    return (rankine - 491.67) * 0.555555555555555555556
def rankine_a_fahrenheit (rankine):
    return rankine - 459.67
def rankine_a_kelvin(rankine):
    return rankine * 0.555555555555555555556

#Aquí es donde pregunta el nombre y muestra las opciones a elegir
name = input("Cuál es tu nombre?: ")
def conversor_de_temperaturas():
    print(f"{name}, Seleccione la conversión que desea realizar:")
    print("1. Celsius a Fahrenheit")
    print("2. celsius a kelvin")
    print("3. celsius a rankine")
    print("4. fahrenheit a celsius")
    print("5. fahrenheit a kelvin")
    print("6. fahrenheit a rankine")
    print("7. kelvin a celsius")
    print("8. kelvin a fahrenheit")
    print("9. kelvin a rankine")
    print("10. rankine a celsius")
    print("11. rankine a fahrenheit")
    print("12. rankine a kelvin")
if name == "Brayan":
    print("Hey, klk Ingeniero Brayan")
elif name == "Emill":
    print(f"klk {name} patrón")
elif name == "emill":
    print(f"klk {name} patrón")
elif name == "brayan":
    print("Hey, klk Ingeniero Brayan")

#Aquí está donde llama a la función de mostrar las opciones y dónde se seleccionan las opciones
conversor_de_temperaturas()   
elección = input(f"{name}, Seleccione la conversión que desea realizar: ")

#Aquí empieza la magia jajaja, aquí es donde están las funciones de qué pasa si eliges los números del 1 al 12 y si no eliges un número y donde da los resultados de las fórmulas 
if elección == "1":
    celsius = float(input(f"{name}, ingrese la cantidad de grados celsius: "))
    print(f"{celsius}grados celsius = {celsius_a_fahrenheit(celsius)} grados fahrenheit")
elif elección == "2":
    celsius = float(input(f"{name}, ingrese la cantidad de grados celsius: "))
    print(f"{celsius} grados celsius = {celsius_a_kelvin(celsius)} grados kelvin")
elif elección == "3":
    celsius = float(input(f"{name}, ingrese la cantidad de grados celsius: "))
    print(f"{celsius} grados celsius = {celsius_a_rankine(celsius)} grados rankine")
elif elección == "4":
    fahrenheit = float(input(f"{name}, ingrese la cantidad de grados fahrenheit: "))
    print(f"{fahrenheit} grados fahrenheit = {fahrenheit_a_celsius(fahrenheit)} grados celsius")
elif elección == "5":
    fahrenheit = float(input(f"{name}, ingrese la cantidad de grados fahrenheit: "))
    print(f"{fahrenheit} grados fahrenheit = {fahrenheit_a_kelvin(fahrenheit)} grados kelvin")
elif elección == "6":
    fahrenheit = float (input(f"{name}, ingrese la cantidad de grados fahrenheit: "))
    print(f"{fahrenheit} grados fahrenheit = {fahrenheit_a_rankine(fahrenheit)} grados rankine")
elif elección == "7":
    kelvin = float(input(f"{name}, ingrese la cantidad de grados kelvin: "))
    print(f"{kelvin} grados kelvin = {kelvin_a_celsius(kelvin)} grados celsius")
elif elección == "8":
    kelvin = float(input(f"{name}, ingrese la cantidad de grados kelvin: "))
    print(f"{kelvin} grados kelvin = {kelvin_a_fahrenheit(kelvin)} grados fahrenheit")
elif elección == "9":
    kelvin = float(input(f"{name}, ingrese la cantidad de grados kelvin: "))
    print(f"{kelvin} grados kelvin = {kelvin_a_rankine(kelvin)} grados rankine")
elif elección == "10":
    rankine = float(input(f"{name}, ingrese la cantidad de grados rankine: "))
    print(f"{rankine} grados rankine = {rankine_a_celsius(rankine)} grados celsius")
elif elección == "11":
    rankine = float(input(f"{name}, ingrese la cantidad de grados rankine: "))
    print(f"{rankine} grados rankine = {rankine_a_fahrenheit(rankine)} grados fahrenheit")
elif elección == "12":
    rankine = float(input(f"{name}, ingrese la cantidad de grados rankine: "))
    print (f"{rankine} grados rankine = {rankine_a_kelvin(rankine)} grados kelvin")
else:
    print("incorrecto, intenta de nuevo")
    
#el else es por si no se eligen los números del 1 al 12 o por si se eligen letras/palabras