# dashboard_temperaturas.py

import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# ---- CONEXIÓN A MYSQL ----
engine = create_engine("mysql+mysqlconnector://root:PepeArgento21.@localhost/dataset_db")

# ---- CARGA DE TABLAS ----
estaciones = pd.read_sql("SELECT * FROM estacion", engine)
temp_prom = pd.read_sql("SELECT * FROM temperatura", engine)
temp_max = pd.read_sql("SELECT * FROM temperatura_max", engine)
temp_min = pd.read_sql("SELECT * FROM temperatura_min", engine)

# ---- JOIN CON INFORMACIÓN DE ESTACIONES ----
df_prom = temp_prom.merge(estaciones, on="COD_ESTACION", how="left")
df_max = temp_max.merge(estaciones, on="COD_ESTACION", how="left")
df_min = temp_min.merge(estaciones, on="COD_ESTACION", how="left")

# ---- REFORMATEO DE LOS DATOS (de ancho a largo) ----
df_prom_largo = df_prom.melt(
    id_vars=["COD_ESTACION", "estacion", "provincia", "region"],
    var_name="Mes",
    value_name="Temp_Promedio"
)

# ---- Mapa de meses para ordenarlos correctamente ----
orden_meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
               "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
df_prom_largo["Mes"] = pd.Categorical(df_prom_largo["Mes"], categories=orden_meses, ordered=True)

# ---- DASHBOARD ----
fig = px.line(
    df_prom_largo,
    x="Mes",
    y="Temp_Promedio",
    color="provincia",
    line_group="estacion",
    hover_name="estacion",
    title="Evolución de Temperaturas Promedio por Provincia"
)

fig.update_layout(
    xaxis_title="Mes",
    yaxis_title="Temperatura (°C)",
    legend_title="Provincia"
)

fig.show()