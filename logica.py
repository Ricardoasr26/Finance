import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(BASE_DIR, "data", "transacciones.json")


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
        json.dump(transacciones, file, indent=4, ensure_ascii=False)


def agregar_trans(monto, tipo, categoria, descripcion, tasa_dolar=0.0):
    """Guarda la transacción (en $) junto con la tasa del momento."""
    transacciones = cargar_trans()
    nueva = {
        "monto": float(monto),
        "tipo": tipo,
        "categoria": categoria,
        "descripcion": descripcion,
        "tasa_dolar": float(tasa_dolar),
    }
    transacciones.append(nueva)
    guardar_trans(transacciones)
    return True


def balance():
    """Saldo total en dólares."""
    total = 0.0
    for t in cargar_trans():
        if t["tipo"].lower() == "ingreso":
            total += t["monto"]
        else:
            total -= t["monto"]
    return total


def balance_en_bs(tasa_dolar):
    """Saldo total convertido a bolívares con la tasa que le pases."""
    return balance() * tasa_dolar


def movimientos():
    transacciones = cargar_trans()
    print("----MOVIMIENTOS----")
    if not transacciones:
        input("No hay transacciones, presiona Enter para volver.")
        return

    for i, t in enumerate(transacciones, start=1):
        signo = "+" if t["tipo"].lower() == "ingreso" else "-"
        # .get() evita errores con transacciones viejas que no tienen tasa
        tasa = t.get("tasa_dolar", 0.0)
        en_bs = f" | Bs {t['monto'] * tasa:,.2f}" if tasa else ""
        print(
            f"{i}. [{signo}] ${t['monto']:.2f}{en_bs} | "
            f"Cat: {t['categoria']} | Desc: {t['descripcion']}"
        )
