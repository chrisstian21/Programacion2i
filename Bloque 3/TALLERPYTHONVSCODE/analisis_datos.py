import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Librerías importadas correctamente")
df = pd.read_csv("LifeExpectancyData.csv")
print(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas.")

print(df.head())
print(df.info())
print(df.describe())

# Rellenar valores nulos en 'Life expectancy'
df['Life expectancy'].fillna(df['Life expectancy'].mean(), inplace=True)
df.drop_duplicates(inplace=True)
print(df.info())

# Filtrar datos de Ecuador
df_ecuador = df[df['Country'] == 'Ecuador']

# Calcular promedio de esperanza de vida por región
avg_life_by_region = df.groupby('Region')['Life expectancy'].mean().sort_values(ascending=False)

# Gráfico de línea para Ecuador
plt.figure(figsize=(10,6))
sns.lineplot(data=df_ecuador, x='Year', y='Life expectancy', marker='o')
plt.title('Esperanza de Vida en Ecuador')
plt.xlabel('Año')
plt.ylabel('Esperanza de Vida')
plt.show()

# Gráfico de barras por región
plt.figure(figsize=(12,6))
avg_life_by_region.plot(kind='bar', color=sns.color_palette('coolwarm', len(avg_life_by_region)))
plt.title('Esperanza de Vida Promedio por Región')
plt.ylabel('Esperanza de Vida')
plt.xlabel('Región')
plt.show()

# Gráfico de dispersión PIB vs Esperanza de Vida para 2014
df_2014 = df[df['Year'] == 2014].dropna(subset=['GDP', 'Life expectancy'])
plt.figure(figsize=(10,7))
sns.scatterplot(data=df_2014, x='GDP', y='Life expectancy', hue='Region', alpha=0.7)
plt.xscale('log')
plt.title('PIB vs. Esperanza de Vida (2014)')
plt.xlabel('PIB')
plt.ylabel('Esperanza de Vida')
plt.show()
