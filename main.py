from logica import agregar_trans, cargar_trans

total = 0.0
while True:
    print("Que deseas hacer:")
    print(f"total: {total}")
    print("1. Agregar ingreso:")
    print("2. Agregar Gasto:")
    print("3. Ver ingresos :")
    print("4. Ver Gastos:")
    print("5.salir")

    try:
        accion = int(input("Elige que deseas realizar:"))
    except ValueError:
        print("Seleciona una opcion que aparezca en pantalla")
        continue
    if accion == 1 or accion == 2:
        tipo = "ingreso" if accion == 1 else "gasto"
        print("-------------------------------------")
        monto = float(input("Ingresa el monto:"))
        categoria = input("Categoria:")
        descripcion= input("Descipcion:")
        print("-------------------------------------")
        print(f" Monto: {monto} \n Categoria:{categoria} \n Descripcion: {descripcion}")
        
        agregar_trans(monto, tipo, categoria,descripcion)
        

