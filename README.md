# 📘 Evaluación en Contacto con el Docente – Piedra, Papel o Tijera (Python)

Juego clásico entre **usuario** y **computadora** programado en **Python 3**.  
Versión mejorada: incluye menú principal, validación de entradas, estadísticas acumuladas e historial de jugadas.

---

## 📋 Requisitos
- 🐍 Python **3.8+**  
- 📦 No requiere librerías externas (usa `random` de la biblioteca estándar)  

---

## 🧠 Funcionalidades implementadas
- 🎮 Menú por consola con opciones:  
  1. Jugar contra la computadora  
  2. Ver estadísticas  
  3. Ver reglas  
  4. Salir  
- 🎲 Elección aleatoria de la computadora con `random.choice()`  
- ⚖️ Lógica de resultado: **empate / gana jugador / gana PC**  
- 📊 Estadísticas acumuladas: partidas jugadas, victorias jugador, victorias PC, empates  
- 📜 Historial de jugadas (últimas 5 rondas mostradas en pantalla)  
- 🔁 Repetición de rondas hasta que el jugador decida salir  

---

## 🧩 Diagramas
- 🔹 **Diagrama de casos de uso** (Jugador y, opcionalmente, Computadora como actor)  
- 🔹 **Diagrama de flujo – Flujo principal**  
- 🔹 **Diagrama de flujo – Estadisticas**
- 🔹 **Diagrama de flujo – Reglas**   

---

## 🧾 Explicación breve del código
- **`OPCIONES` (tupla)** → jugadas válidas del juego (`("piedra", "papel", "tijera")`).  
- **`REGLAS` (diccionario)** → define qué jugada vence a cuál.  
- **`ESTADISTICAS` (diccionario)** → registra partidas, victorias y empates.  
- **`HISTORIAL` (lista de tuplas)** → guarda cada jugada con el formato `(jugador, pc, resultado)`.  
- **Funciones principales**:  
  - `pedir_jugada()` → lee y valida la jugada del jugador  
  - `elegir_pc()` → genera la jugada aleatoria de la computadora  
  - `determinar_ganador()` → decide el resultado de la ronda  
  - `actualizar_estadisticas()` → incrementa estadísticas y guarda en el historial  
  - `menu_principal()` → organiza la navegación por el juego  

**Comparación de jugadas:**  
- Si son iguales → **Empate**  
- Reglas: piedra > tijera, tijera > papel, papel > piedra  
- Si no se cumple la regla del jugador → **gana la PC**   

---

## 🔎 Problemas encontrados y soluciones (Implicaciones y limitaciones)

- ⚠️ **Problema 1: Validación de entradas del usuario**  
  - El programa fallaba cuando el jugador escribía algo distinto a `1, 2 o 3`.  
  ✅ **Solución:** Implementé la función `normalizar_entrada_jugada()` que convierte la entrada en minúsculas y valida, aceptando tanto números como palabras.  

- ⚠️ **Problema 2: Registro de estadísticas**  
  - Al inicio solo se contaban las partidas, sin diferenciar entre victorias, derrotas o empates.  
  ✅ **Solución:** Usé un diccionario (`ESTADISTICAS`) para acumular los resultados y una lista (`HISTORIAL`) para guardar cada jugada como tupla `(jugador, pc, resultado)`, lo que permitió mostrar estadísticas completas y el historial de rondas.

---

## 👤 Autor
**Glemer Jair Estupiñán Valencia**  

