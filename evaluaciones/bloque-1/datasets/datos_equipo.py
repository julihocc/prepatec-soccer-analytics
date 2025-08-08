# Datos Simples para el Caso Práctico - Bloque 1
# Análisis Básico de un Equipo de Fútbol
# =====================================

# DATOS DE PARTIDOS (listas simples)
# Resultados de 10 partidos de la temporada
resultados_partidos = ["Victoria", "Derrota", "Victoria", "Empate", "Victoria", 
                      "Derrota", "Victoria", "Empate", "Victoria", "Victoria"]

# Goles marcados por nuestro equipo en cada partido
goles_favor = [2, 0, 3, 1, 2, 0, 1, 2, 3, 2]

# Goles recibidos por nuestro equipo en cada partido
goles_contra = [1, 3, 1, 1, 0, 2, 0, 2, 1, 1]

# Nombres de los equipos rivales
rivales = ["Atlas", "América", "Pumas", "Cruz Azul", "Tigres", 
          "Monterrey", "Santos", "Chivas", "León", "Pachuca"]

# DATOS DE JUGADORES (diccionario simple)
# Información básica de los jugadores del equipo
jugadores = {
    "Carlos": {"posicion": "Delantero", "goles": 8, "edad": 23},
    "María": {"posicion": "Mediocampo", "goles": 3, "edad": 21}, 
    "Luis": {"posicion": "Defensa", "goles": 1, "edad": 25},
    "Ana": {"posicion": "Delantero", "goles": 6, "edad": 22},
    "Pedro": {"posicion": "Mediocampo", "goles": 2, "edad": 24},
    "Sofia": {"posicion": "Portero", "goles": 0, "edad": 20},
    "Diego": {"posicion": "Defensa", "goles": 0, "edad": 26},
    "Carmen": {"posicion": "Delantero", "goles": 5, "edad": 19}
}

# INFORMACIÓN ADICIONAL PARA ANÁLISIS
# Estos datos pueden usar los estudiantes para hacer cálculos adicionales

# Partidos jugados como local vs visitante (opcional)
ubicacion_partidos = ["Local", "Visitante", "Local", "Local", "Visitante",
                     "Local", "Visitante", "Local", "Visitante", "Local"]

# Meses de los partidos (para análisis temporal básico)
meses_partidos = ["Agosto", "Agosto", "Septiembre", "Septiembre", "Octubre",
                 "Octubre", "Noviembre", "Noviembre", "Diciembre", "Diciembre"]

# NOTAS PARA INSTRUCTORES:
# =========================
# - Estos datos están diseñados para ser simples y manejables para estudiantes de preparatoria
# - No requieren pandas, numpy u otras bibliotecas avanzadas
# - Los estudiantes pueden copiar y pegar estos datos directamente en su notebook
# - Los números están balanceados para obtener resultados interesantes pero no complejos
# - Total de partidos: 10 (fácil de manejar)
# - Total de jugadores: 8 (permite análisis por posición)
# - Los resultados permiten calcular: 6 victorias, 2 empates, 2 derrotas = 20 puntos totales