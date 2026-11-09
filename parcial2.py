
inventario = []

def registrar():
    id = input("ID: ")

    for c in inventario:
        if c["id"] == id:
            print("ID repetido")
            return

    nombre = input("Nombre: ")
    categoria = input("Categoria: ")
    stock = int(input("Stock: "))
    precio = float(input("Precio: "))

    if stock < 0 or precio < 0:
        print("Valores incorrectos")
        return

    inventario.append({
        "id": id,
        "nombre": nombre,
        "categoria": categoria,
        "stock": stock,
        "precio_unitario": precio
    })

    print("Componente registrado")


def consultar():
    for c in inventario:
        print(c)


def filtrar():
    cat = input("Categoria: ")

    for c in inventario:
        if c["categoria"].lower() == cat.lower():
            print(c)


def actualizar():
    id = input("ID del componente: ")

    for c in inventario:
        if c["id"] == id:
            print("Stock actual:", c["stock"])
            op = input("1. Sumar  2. Restar: ")
            cantidad = int(input("Cantidad: "))

            if cantidad <= 0:
                print("Cantidad incorrecta")
            elif op == "1":
                c["stock"] += cantidad
            elif op == "2" and cantidad <= c["stock"]:
                c["stock"] -= cantidad
            else:
                print("Operacion no permitida")

            return

    print("Componente no encontrado")


while True:
    print("\n1. Registrar")
    print("2. Consultar")
    print("3. Filtrar")
    print("4. Actualizar stock")
    print("5. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":
        registrar()
    elif opcion == "2":
        consultar()
    elif opcion == "3":
        filtrar()
    elif opcion == "4":
        actualizar()
    elif opcion == "5":
        print("Hasta pronto")
        break
    else:
        print("Opcion incorrecta")
