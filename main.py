from logica import agregar_trans, cargar_trans, balance

while True:
    
    total_actual = balance()

    print("\n--- MENÚ PRINCIPAL ---")
    print(
        f"Saldo total actual: {total_actual}"
    )  
    print("1. Agregar ingreso")
    print("2. Agregar Gasto:")
    print("3. Ver ingresos:")
    print("4. Ver Gastos:")
    print("5. Salir")

    try:
        accion = int(input("Elige que deseas realizar: "))
    except ValueError:
        print("Selecciona una opcion que aparezca en pantalla")
        continue

    if accion == 1 or accion == 2:
        tipo = "ingreso" if accion == 1 else "gasto"
        print("----------------------------------------")
        monto = float(input("Ingresa el monto: "))
        categoria = input("Categoria: ")
        descripcion = input("Descripcion: ")

        agregar_trans(monto, tipo, categoria, descripcion)

        print("----------------------------------------")
        print(f"Monto: {monto} \nCategoria: {categoria} \nDescripcion: {descripcion}")

    elif accion == 4:
        break
    else:
        print("Opcion no valida.")
