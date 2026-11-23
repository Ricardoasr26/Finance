import json
import os

data_file = os.path.join("data", "transacciones.json")


def cargar_trans():
    if not os.path.exists(data_file):
        return []

    try:
        with open(data_file, "r", encoding="UTF-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def guardar_trans(transacciones):
    os.makedirs(os.path.dirname(data_file), exist_ok=True)
    with open(data_file, "w", encoding="utf-8") as file:
        return json.dump(transacciones, file, indent=4, ensure_ascii=False)


def agregar_trans(monto, tipo, categoria, descripcion):
    transacciones = cargar_trans()
    nueva = {
        "monto": float(monto),
        "tipo": tipo,
        "categoria": categoria,
        "descripcion": descripcion,
    }
    transacciones.append(nueva)
    guardar_trans(transacciones)
    return True


def balance():
    transacciones = cargar_trans()
    total = 0.0

    for t in transacciones:

        if t["tipo"].lower() == "ingreso":
            total += t["monto"]
        else:
            total -= t["monto"]

    return total


def movimientos():
    transaciones = cargar_trans()
    print("----MOVIMIENTOS----")
    if not transaciones:
        input("No hay transaciones, presiona 0 para volver.")
    else:
        for i, t in enumerate(transaciones, start=1):
            signo = "+" if t["tipo"].lower() == "ingreso" else "-"
            print(f"{i}. [{signo}] ${t['monto']:.2f} | Cat: {t['categoria']} | Desc: {t['descripcion']}")
    
