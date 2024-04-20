

"""def nombre(nombre):

    print(f"Mi nombre es {nombre}")


nombr=input("Ingresa tu nombre:")

nombre(nombr)

"""


def suma(num1,num2):

    resultado = num1 + num2

    return resultado

def resta(num1,num2):

    resultado = num1 - num2

    return resultado


def matematica(num1,num2):

    resultado = (f"{suma(num1,num2)} , {resta(num1,num2)}")

    return resultado

numero1= int(input("Ingresa el nuemro 1:"))
numero2= int(input("Ingresa el nuemro 2:"))

print(f"{suma(numero1,numero2)},{resta(numero1,numero2)}")

print("\n")

print(matematica(numero1,numero2))



