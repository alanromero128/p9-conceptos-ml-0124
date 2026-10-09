print("Alan Romero nc = 0124")
import pandas as pd
print(pd.__version__) # Output: 1.5.2
# 21.
datos21 = {
    'distancia_km': [2.2, 4.6, 1.6, 5.3, 3.7],
    'trafico_nivel': [2, 1, 3, 2, 1],
    'edad_repartidor': [26, 35, 24, 41, 30],
    'tiempo_entrega_min': [18, 32, 15, 45, 25]
}

df = pd.DataFrame(datos21)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))
print("Alan Romero nc = 0124")