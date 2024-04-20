

"""closet = ["Pantalon","Camisa","harina pan"]
#closet =     0         1           2

print(closet[0])"""


netflix=["Batman","Simon","Ley de los audaces"]

running = True

while running:

    print("1.Añadir\n2.Ver lista\n3.Borrar elemento\n4.Salir\n")

    opcion=int(input("Ingrese una opcion: "))

    if opcion == 1:
        pelicula=input("Añade una pelicula: ")
        netflix.append(pelicula)

    if opcion == 2:
        print(netflix)

    if opcion == 3:
        indice= input("Ingrese el numero que desea borrar ")
        netflix.lower.remove(indice)

    if opcion == 4:
        print("Vuelva pronto")
        running = False

    print("\n")






