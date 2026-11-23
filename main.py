from logica import agregar_trans, balance, balance_en_bs, movimientos
from tasa import tasa_dia

tasas = tasa_dia()  # una sola consulta al abrir el programa


def preguntar_otro():
    """Pregunta si quiere repetir la acción. True = añadir otro, False = menú."""
    while True:
        respuesta = input("\n¿Qué deseas hacer? [A] Añadir otro  [M] Volver al menú: ").lower()
        if respuesta == "a":
            return True
        if respuesta == "m":
            return False
        print("Escribe A o M.")


def registrar_transaccion(tipo, tasa_dolar):
    """Pide los datos de una transacción y la guarda."""
    print("----------------------------------------")
    try:
        monto = float(input("Ingresa el monto en $: "))
    except ValueError:
        print("El monto debe ser un número.")
        return
    categoria = input("Categoria: ")
    descripcion = input("Descripcion: ")

    agregar_trans(monto, tipo, categoria, descripcion, tasa_dolar)

    print("----------------------------------------")
    print(f"Monto: ${monto:,.2f} (≈ {monto * tasa_dolar:,.2f} Bs)")
    print(f"Categoria: {categoria} \nDescripcion: {descripcion}")
    print(f"Saldo actual: ${balance():,.2f} (≈ {balance_en_bs(tasa_dolar):,.2f} Bs)")


while True:
    tasa_dolar = tasas["dolar"]
    total_usd = balance()

    print("\n--- MENÚ PRINCIPAL ---")
    print(f"Tasa dólar: {tasa_dolar:,.2f} Bs | Euro: {tasas['euro']:,.2f} Bs")
    print(f"Saldo total actual: ${total_usd:,.2f} (≈ {balance_en_bs(tasa_dolar):,.2f} Bs)")
    print("1. Agregar ingreso")
    print("2. Agregar gasto")
    print("3. Ver movimientos")
    print("4. Actualizar tasas")
    print("5. Salir")

    try:
        accion = int(input("Elige que deseas realizar: "))
    except ValueError:
        print("Selecciona una opcion que aparezca en pantalla")
        continue

    if accion == 1 or accion == 2:
        tipo = "ingreso" if accion == 1 else "gasto"
        while True:
            registrar_transaccion(tipo, tasa_dolar)
            if not preguntar_otro():
                break

    elif accion == 3:
        movimientos()
        input("\nPresiona Enter para volver al menú.")

    elif accion == 4:
        tasas = tasa_dia()
        print("Tasas actualizadas.")

    elif accion == 5:
        salir = input("Estas seguro que quieres salir?: [S] [N]: \n").lower()
        if salir == "s":
            break

    else:
        print("Opcion no valida.")