# 📊 Análisis del Mercado Laboral Perú 2022-2024
**Fuente de datos:** Instituto Nacional de Estadística e Informática (INEI)

## 🗂️ Descripción
Análisis end-to-end del mercado laboral peruano utilizando datos públicos del INEI. El proyecto abarca la extracción y limpieza de datos con Python, almacenamiento en PostgreSQL y visualización en Power BI.

**Variables analizadas:**
- Tasa de desempleo por ciudad
- Tasa de empleo informal por departamento
- Ingreso promedio mensual por departamento
- Población ocupada por sectores económicos en Lima Metropolitana

---

## 🛠️ Stack Tecnológico
- **Python** (Pandas, NumPy, SQLAlchemy) — limpieza y transformación de datos
- **PostgreSQL** — almacenamiento y consultas analíticas
- **Power BI** — dashboard interactivo
- **Git / GitHub** — control de versiones

---

## 📁 Estructura del Proyecto
```
proyecto-inei-mercado-laboral/
├── data/
│   ├── raw/          # Archivos originales del INEI (.xlsx)
│   └── cleaned/      # Datos limpios (.csv)
├── notebooks/
│   ├── 01_limpieza_datos.py
│   ├── 02_cargar_postgresql.py
│   └── 03_analisis_sql.py
├── images/           # Capturas del dashboard
└── README.md
```

---

## 🔄 Flujo del Proyecto

```
Datos INEI (.xlsx) → Limpieza con Python → PostgreSQL → Consultas SQL → Dashboard Power BI
```

---

## 🔍 Hallazgos Principales

1. **Huancavelica lidera el desempleo** con 11.98% en 2024, casi el doble del promedio nacional
2. **Lima tiene el ingreso más alto** (S/ 2,269) pero aún con 56.9% de informalidad — más de la mitad del empleo es informal incluso en la capital
3. **Moquegua redujo más la informalidad** — bajó 6 puntos porcentuales entre 2022 y 2024, la mayor mejora del país
4. **El 62% del empleo en Lima** es en empresas de 1 a 10 trabajadores — predominan las microempresas
5. **Patrón claro:** a mayor ingreso, menor informalidad — Lima, Moquegua y Arequipa lideran en ambos indicadores

---

## 📈 Dashboard

### Desempleo por Ciudad (2024)
![Desempleo por ciudad](images/Desempleo%20por%20ciudad%20(2024).png)

### Informalidad por Departamento (2024)
![Informalidad por departamento](images/Informalidad%20por%20departamento%20(2024).png)

### Ingreso vs Informalidad
![Ingreso vs Informalidad](images/Ingreso%20vs%20Informalidad.png)

### Evolución Informalidad 2022 vs 2024
![Evolución informalidad](images/Evolución%20informalidad%202022%20vs%202024.png)

### Sectores Económicos Lima (2023)
![Sectores económicos](images/Sectores%20económicos%20Lima%20(2023).png)

---

## ▶️ Cómo reproducir el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/PedroG28/proyecto-inei-mercado-laboral.git
cd proyecto-inei-mercado-laboral
```

### 2. Instalar dependencias
```bash
pip install pandas numpy matplotlib psycopg2-binary sqlalchemy openpyxl
```

### 3. Crear la base de datos en PostgreSQL
```sql
CREATE DATABASE inei_mercado_laboral;
```

### 4. Ejecutar los scripts en orden
```bash
python notebooks/01_limpieza_datos.py
python notebooks/02_cargar_postgresql.py
python notebooks/03_analisis_sql.py
```

### 5. Abrir el dashboard
Conectar Power BI Desktop a PostgreSQL:
- Servidor: `localhost`
- Base de datos: `inei_mercado_laboral`

---

## 👤 Autor
**Pedro Gaitan Olivares**
- GitHub: [github.com/PedroG28](https://github.com/PedroG28)
- LinkedIn: [linkedin.com/in/pedro-gaitan28](https://www.linkedin.com/in/pedro-gaitan28)