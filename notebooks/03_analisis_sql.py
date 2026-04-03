import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://postgres:28koda@localhost:5432/inei_mercado_laboral")

def query(sql):
    with engine.connect() as conn:
        return pd.read_sql_query(text(sql), conn)
    
print("=" * 55)
print("ANÁLISIS: MERCADO LABORAL PERÚ 2022-2024")
print("=" * 55)

# 1. Top 5 ciudades con mayor desempleo en 2024
q1 = """
SELECT ciudad, ROUND(desempleo_2024::numeric, 2) AS tasa_2024
FROM desempleo_ciudad
WHERE ciudad NOT LIKE 'Total%'
ORDER BY desempleo_2024 DESC
LIMIT 5;
"""
df1 = query(q1)
print("\n📊 Top 5 ciudades con mayor desempleo (2024):")
print(df1.to_string(index=False))

# 2. Departamentos con mayor informalidad en 2024
q2 = """
SELECT departamento, ROUND(informalidad_2024::numeric, 2) AS informalidad_pct
FROM informalidad_departamento
ORDER BY informalidad_2024 DESC
LIMIT 5;
"""
df2 = query(q2)
print("\n📊 Top 5 departamentos con mayor informalidad (2024):")
print(df2.to_string(index=False))

# 3. Departamentos que más redujeron informalidad (2022 vs 2024)
q3 = """
SELECT departamento,
       ROUND(informalidad_2022::numeric, 2) AS inf_2022,
       ROUND(informalidad_2024::numeric, 2) AS inf_2024,
       ROUND((informalidad_2024 - informalidad_2022)::numeric, 2) AS variacion
FROM informalidad_departamento
ORDER BY variacion ASC
LIMIT 5;
"""
df3 = query(q3)
print("\n📊 Departamentos que más redujeron informalidad (2022-2024):")
print(df3.to_string(index=False))

# 4. Correlación ingreso vs informalidad por departamento
q4 = """
SELECT departamento,
       ROUND(ingreso_2024::numeric, 0) AS ingreso_2024,
       ROUND(informalidad_2024::numeric, 2) AS informalidad_2024
FROM combinado_departamentos
ORDER BY ingreso_2024 DESC
LIMIT 8;
"""
df4 = query(q4)
print("\n📊 Ingreso vs Informalidad por departamento (2024):")
print(df4.to_string(index=False))

# 5. Sectores económicos con más empleo en Lima (2023)
q5 = """
SELECT categoria, ROUND("2023"::numeric, 1) AS miles_personas
FROM poblacion_ocupada_lima
WHERE categoria NOT IN ('Total')
ORDER BY "2023" DESC
LIMIT 6;
"""
df5 = query(q5)
print("\n📊 Sectores con más empleo en Lima (2023, miles de personas):")
print(df5.to_string(index=False))

print("\n✅ Análisis completado")