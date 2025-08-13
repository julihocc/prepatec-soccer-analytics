# ---
# marp: true
# theme: default
# paginate: true
# ---

# %% [markdown]
# # Test Sample: Notebook de Prueba
# 
# Este es un archivo de prueba para el convertidor py-to-marp.
#
# ---
#
# ## Sección 1: Variables y Tipos de Datos
#
# Vamos a explorar variables básicas:

# %%
# Variables básicas
nombre = "Pelé"
edad = 82
altura = 1.70
es_leyenda = True

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura}")
print(f"¿Es una leyenda?: {es_leyenda}")

# %% [markdown]
# ---
#
# ## Sección 2: Estructuras de Control
#
# Ejemplo de condicionales:

# %%
# Condicionales
if edad > 80:
    print("Veterano del fútbol")
elif edad > 40:
    print("Jugador maduro")
else:
    print("Jugador joven")

# %% [markdown]
# ---
#
# ## Sección 3: Listas y Bucles
#
# Trabajando con listas:

# %%
# Listas
jugadores = ["Pelé", "Maradona", "Messi", "Cristiano"]

print("Lista de grandes jugadores:")
for jugador in jugadores:
    print(f"- {jugador}")

# %% [markdown]
# ---
#
# ## Conclusión
#
# - Este es un ejemplo básico
# - Muestra diferentes tipos de celdas
# - Combina markdown y código
# - Perfecto para testing
