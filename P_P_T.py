import random  # Biblioteca estándar para generar elecciones aleatorias de la computadora.

# --- ESTRUCTURAS DE DATOS ---

# TUPLA (inmutable): jugadas válidas del juego.
OPCIONES = ("piedra", "papel", "tijera")

# DICCIONARIO: reglas de victoria. Clave = jugada; Valor = jugada a la que vence.
REGLAS = {
    "piedra": "tijera",
    "tijera": "papel",
    "papel": "piedra",
}

# DICCIONARIO: estadísticas acumuladas de la sesión.
ESTADISTICAS = {
    "partidas": 0,
    "j1_gano": 0,
    "pc_gano": 0,
    "empates": 0,
}

# LISTA: historial de rondas. Cada elemento es una tupla (jugador, pc, resultado).
HISTORIAL = []


# --- UTILIDADES DE ENTRADA/SALIDA (FUNCIONES) ---

def leer_opcion(mensaje, opciones_validas):
    while True:
        try:
            valor = int(input(mensaje).strip())
            if valor in opciones_validas:
                return valor
            print("→ Opción fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("→ Entrada inválida. Escribe un número.")


def normalizar_entrada_jugada(entrada):
    texto = entrada.strip().lower()
    mapa = {"1": "piedra", "2": "papel", "3": "tijera"}  # DICCIONARIO local de mapeo
    if texto in mapa:
        return mapa[texto]
    if texto in OPCIONES:
        return texto
    return None


def pedir_jugada(nombre="Jugador"):
    while True:
        print(f"\n{nombre}, elige tu opción:")
        print("  1) piedra")
        print("  2) papel")
        print("  3) tijera")
        entrada = input("→ ").strip()
        jugada = normalizar_entrada_jugada(entrada)
        if jugada:
            return jugada
        print("→ Opción no válida. Escribe 1, 2, 3 o piedra/papel/tijera.")


# --- LÓGICA DEL JUEGO (FUNCIONES) ---

def elegir_pc():
    return random.choice(OPCIONES)  # Usa la TUPLA OPCIONES


def determinar_ganador(j1, pc):
    if j1 == pc:
        return "empate"
    if REGLAS[j1] == pc:  # Consulta al DICCIONARIO REGLAS
        return "j1"
    return "pc"


def explicar_resultado(resultado, j1, pc):
    if resultado == "empate":
        return f"Empate: ambos eligieron {j1}."
    if resultado == "j1":
        return f"¡Ganaste! {j1} vence a {pc}."
    return f"La computadora gana. {pc} vence a {j1}."


def actualizar_estadisticas(resultado, j1, pc):
    ESTADISTICAS["partidas"] += 1
    HISTORIAL.append((j1, pc, resultado))  # LISTA con tupla (jugador, pc, resultado)
    if resultado == "empate":
        ESTADISTICAS["empates"] += 1
    elif resultado == "j1":
        ESTADISTICAS["j1_gano"] += 1
    else:
        ESTADISTICAS["pc_gano"] += 1


# --- ACCIONES (FUNCIONES) ---

def jugar_contra_pc():
    while True:
        j1 = pedir_jugada("Jugador")
        pc = elegir_pc()

        print(f"Tú elegiste: {j1}")
        print(f"La computadora eligió: {pc}")

        resultado = determinar_ganador(j1, pc)
        print(explicar_resultado(resultado, j1, pc))
        actualizar_estadisticas(resultado, j1, pc)

        if not desea_continuar():
            break


def ver_estadisticas():
    print("\nEstadísticas de partidas:")
    print(f"Partidas jugadas: {ESTADISTICAS['partidas']}")
    print(f"Jugador ganó:     {ESTADISTICAS['j1_gano']}")
    print(f"PC ganó:          {ESTADISTICAS['pc_gano']}")
    print(f"Empates:          {ESTADISTICAS['empates']}")

    if HISTORIAL:
        print("\nÚltimas 5 rondas:")
        for idx, (j1, pc, res) in enumerate(HISTORIAL[-5:], start=max(1, len(HISTORIAL)-4)):
            print(f"{idx}. Jugador: {j1} | PC: {pc} → {res}")


def ver_reglas():
    print("\nReglas del juego:")
    print(" - piedra vence a tijera")
    print(" - tijera vence a papel")
    print(" - papel vence a piedra")
    print(" - Si ambas elecciones son iguales → Empate.")



def desea_continuar():
    r = input("¿Jugar otra vez? (s/n): ").strip().lower()
    return r in ("s", "si", "sí")


# --- MENÚ PRINCIPAL ---

def menu_principal():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Jugar (1 jugador vs PC)")
        print("2. Ver estadísticas")
        print("3. Reglas del juego")
        print("4. Salir")
        op = leer_opcion("Selecciona una opción (1-4): ", range(1, 5))
        if op == 1:
            jugar_contra_pc()
        elif op == 2:
            ver_estadisticas()
        elif op == 3:
            ver_reglas()
        else:
            print("Gracias por jugar. ¡Hasta pronto!")
            break


# --- EJECUCIÓN DIRECTA DEL PROGRAMA ---

print("=== Piedra, Papel o Tijera ===")
menu_principal()
