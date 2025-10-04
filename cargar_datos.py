import pandas as pd
import mysql.connector

# ---------- CONEXIÓN A MYSQL ----------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PepeArgento21.",
    database="dataset_db"
)
cursor = conn.cursor()

tablas = ["estacion", "temperatura", "temperatura_max", "temperatura_min"]

for tabla in tablas:
    df = pd.read_excel("datos_clima.xlsx", sheet_name=tabla, header=0, index_col=None)
    
    columnas = ", ".join([f"`{str(c)}`" for c in df.columns])
    placeholders = ", ".join(["%s"] * len(df.columns))
    sql = f"INSERT INTO `{tabla}` ({columnas}) VALUES ({placeholders})"
    
    for i, row in df.iterrows():
        valores = tuple(None if pd.isna(x) else x for x in row)
        try:
            cursor.execute(sql, valores)
        except mysql.connector.Error as e:
            print(f"Error en tabla '{tabla}', fila {i+2}: {e}")  # +2 porque pandas empieza en 0 y fila 1 es encabezado

    print(f"Intento de carga finalizado en tabla {tabla}")

conn.commit()
cursor.close()
conn.close()
print("Carga de datos completada con revisión ✅")