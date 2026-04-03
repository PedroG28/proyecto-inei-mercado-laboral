import pandas as pd
import numpy as np
import os

RAW = r"D:\URP\proyecto-inei-mercado-laboral\data\raw"
CLEAN = r"D:\URP\proyecto-inei-mercado-laboral\data\cleaned"
os.makedirs(CLEAN, exist_ok=True)

# ─────────────────────────────────────────────
# 1. TASA DE DESEMPLEO POR CIUDAD (2022-2024)
# ─────────────────────────────────────────────
print("Procesando: Tasa de desempleo...")

df_desem = pd.read_excel(
    f"{RAW}/desem-cuad-2_5.xlsx",
    skiprows=4,        # salta títulos
    usecols=[0, 1, 2, 3],
    names=["ciudad", "desempleo_2022", "desempleo_2023", "desempleo_2024"]
)

# Eliminar filas vacías, notas al pie y subtotales
df_desem = df_desem[df_desem["ciudad"].notna()]
df_desem = df_desem[~df_desem["ciudad"].str.startswith(("1/", "2/", "Fuente", "Total"), na=False)]
df_desem = df_desem[df_desem["ciudad"] != "Total 1/"]

# Reemplazar "-" por NaN y convertir a float
for col in ["desempleo_2022", "desempleo_2023", "desempleo_2024"]:
    df_desem[col] = pd.to_numeric(df_desem[col], errors="coerce")

df_desem["ciudad"] = df_desem["ciudad"].str.strip()
df_desem = df_desem.reset_index(drop=True)

print(f"  {len(df_desem)} ciudades | columnas: {list(df_desem.columns)}")
df_desem.to_csv(f"{CLEAN}/desempleo_ciudad.csv", index=False, encoding="utf-8-sig")


# ─────────────────────────────────────────────
# 2. INGRESO PROMEDIO POR DEPARTAMENTO (2022-2024)
# ─────────────────────────────────────────────
print("Procesando: Ingreso promedio...")

df_ing = pd.read_excel(
    f"{RAW}/ing-cuad-1_7.xlsx",
    skiprows=3,
    usecols=[0, 1, 2, 3],
    names=["departamento", "ingreso_2022", "ingreso_2023", "ingreso_2024"]
)

df_ing = df_ing[df_ing["departamento"].notna()]
df_ing = df_ing[~df_ing["departamento"].str.startswith(("1/", "2/", "Fuente", "Área"), na=False)]
df_ing = df_ing[df_ing["departamento"] != "Total"]

for col in ["ingreso_2022", "ingreso_2023", "ingreso_2024"]:
    df_ing[col] = pd.to_numeric(df_ing[col], errors="coerce")

df_ing = df_ing.dropna(subset=["ingreso_2022"])
df_ing["departamento"] = df_ing["departamento"].str.strip()
df_ing = df_ing.reset_index(drop=True)

print(f"  {len(df_ing)} departamentos | columnas: {list(df_ing.columns)}")
df_ing.to_csv(f"{CLEAN}/ingreso_departamento.csv", index=False, encoding="utf-8-sig")


# ─────────────────────────────────────────────
# 3. TASA DE INFORMALIDAD POR DEPARTAMENTO (2022-2024)
# ─────────────────────────────────────────────
print("Procesando: Tasa de informalidad...")

df_inf = pd.read_excel(
    f"{RAW}/peao-cuad-7_6.xlsx",
    skiprows=2,
    usecols=[0, 1, 2, 3],
    names=["departamento", "informalidad_2022", "informalidad_2023", "informalidad_2024"]
)

df_inf = df_inf[df_inf["departamento"].notna()]
df_inf = df_inf[~df_inf["departamento"].str.startswith(("1/", "2/", "Fuente", "Área", "Total", "Depart"), na=False)]

for col in ["informalidad_2022", "informalidad_2023", "informalidad_2024"]:
    df_inf[col] = pd.to_numeric(df_inf[col], errors="coerce")

df_inf = df_inf.dropna(subset=["informalidad_2022"])
df_inf["departamento"] = df_inf["departamento"].str.strip()
df_inf = df_inf.reset_index(drop=True)

print(f"  {len(df_inf)} departamentos | columnas: {list(df_inf.columns)}")
df_inf.to_csv(f"{CLEAN}/informalidad_departamento.csv", index=False, encoding="utf-8-sig")


# ─────────────────────────────────────────────
# 4. POBLACIÓN OCUPADA POR RAMAS (Lima, 2007-2023)
# ─────────────────────────────────────────────
print("Procesando: Población ocupada por ramas...")

df_lima_raw = pd.read_excel(
    f"{RAW}/lima-cuad-3_5.xlsx",
    skiprows=2,
    header=None
)

# La fila 1 (índice 1) tiene los encabezados reales
header_row = df_lima_raw.iloc[1]
headers = ["categoria"] + [str(int(v)) if isinstance(v, float) and not pd.isna(v) else str(v) for v in header_row[1:]]
df_lima = df_lima_raw.iloc[2:].copy()
df_lima.columns = headers
df_lima = df_lima[df_lima["categoria"].notna()]
df_lima = df_lima[~df_lima["categoria"].astype(str).str.startswith(("1/", "2/", "Fuente"), na=False)]

# Filtrar solo filas de datos reales
df_lima = df_lima[pd.to_numeric(df_lima["2022"], errors="coerce").notna()]
df_lima["categoria"] = df_lima["categoria"].str.strip()

# Quedarnos solo con columnas relevantes: categoría + últimos 5 años
cols_años = ["2019", "2020", "2021", "2022", "2023"]
df_lima = df_lima[["categoria"] + cols_años]

for col in cols_años:
    df_lima[col] = pd.to_numeric(df_lima[col], errors="coerce").round(1)

df_lima = df_lima.reset_index(drop=True)

print(f"  {len(df_lima)} categorías | columnas: {list(df_lima.columns)}")
df_lima.to_csv(f"{CLEAN}/poblacion_ocupada_lima.csv", index=False, encoding="utf-8-sig")


# ─────────────────────────────────────────────
# 5. TABLA COMBINADA: Ingreso + Informalidad por departamento
# ─────────────────────────────────────────────
print("Creando tabla combinada departamentos...")

df_combined = pd.merge(df_ing, df_inf, on="departamento", how="inner")
df_combined["variacion_ingreso"] = (
    (df_combined["ingreso_2024"] - df_combined["ingreso_2022"]) / df_combined["ingreso_2022"] * 100
).round(2)
df_combined["variacion_informalidad"] = (
    df_combined["informalidad_2024"] - df_combined["informalidad_2022"]
).round(2)

df_combined.to_csv(f"{CLEAN}/combinado_departamentos.csv", index=False, encoding="utf-8-sig")
print(f"  {len(df_combined)} departamentos combinados")

print("\nLimpieza completada. Archivos en data/cleaned/:")
for f in os.listdir(CLEAN):
    print(f"  - {f}")