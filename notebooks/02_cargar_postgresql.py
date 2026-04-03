import pandas as pd
from sqlalchemy import create_engine

# Conexión
engine = create_engine("postgresql+psycopg2://postgres:28koda@localhost:5432/inei_mercado_laboral")

CLEAN = r"D:\URP\proyecto-inei-mercado-laboral\data\cleaned"

# Cargar cada CSV como tabla
tablas = {
    "desempleo_ciudad": f"{CLEAN}/desempleo_ciudad.csv",
    "ingreso_departamento": f"{CLEAN}/ingreso_departamento.csv",
    "informalidad_departamento": f"{CLEAN}/informalidad_departamento.csv",
    "poblacion_ocupada_lima": f"{CLEAN}/poblacion_ocupada_lima.csv",
    "combinado_departamentos": f"{CLEAN}/combinado_departamentos.csv",
}

for tabla, ruta in tablas.items():
    df = pd.read_csv(ruta)
    df.to_sql(tabla, engine, if_exists="replace", index=False)
    print(f"✅ Tabla '{tabla}' cargada — {len(df)} filas")

print("\n✅ Todas las tablas cargadas en PostgreSQL")