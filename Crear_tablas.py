import mysql.connector

# 1️⃣ Conexión inicial al servidor MySQL (sin base específica)
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PepeArgento21."
)

cursor = conexion.cursor()

# 2️⃣ Crear la base de datos si no existe
cursor.execute("CREATE DATABASE IF NOT EXISTS dataset_db;")
print("✅ Base de datos 'dataset_db' verificada o creada correctamente.")

# 3️⃣ Conectarse a la base de datos recién creada
conexion.database = "dataset_db"

# 4️⃣ Eliminar tablas si existen (en orden por dependencias)
tablas = ["temperatura", "temperatura_max", "temperatura_min", "estacion"]
for tabla in tablas:
    cursor.execute(f"DROP TABLE IF EXISTS {tabla};")

print("Tablas anteriores eliminadas (si existían).")

# 5️⃣ Crear tabla 'estacion'
cursor.execute("""
CREATE TABLE estacion (
    COD_ESTACION INT PRIMARY KEY,
    estacion VARCHAR(100),
    provincia VARCHAR(100),
    region VARCHAR(100)
);
""")

# 6️⃣ Estructura común para las tablas de temperaturas
estructura_temperaturas = """
CREATE TABLE {nombre_tabla} (
    COD_ESTACION INT,
    Ene FLOAT,
    Feb FLOAT,
    Mar FLOAT,
    Abr FLOAT,
    May FLOAT,
    Jun FLOAT,
    Jul FLOAT,
    Ago FLOAT,
    Sep FLOAT,
    Oct FLOAT,
    Nov FLOAT,
    Dic FLOAT,
    PRIMARY KEY (COD_ESTACION),
    FOREIGN KEY (COD_ESTACION) REFERENCES estacion(COD_ESTACION)
);
"""

# Crear tablas de temperatura, temperatura_max y temperatura_min
cursor.execute(estructura_temperaturas.format(nombre_tabla="temperatura"))
cursor.execute(estructura_temperaturas.format(nombre_tabla="temperatura_max"))
cursor.execute(estructura_temperaturas.format(nombre_tabla="temperatura_min"))

# 7️⃣ Confirmar cambios
conexion.commit()
print("✅ Tablas creadas correctamente.")

# 8️⃣ Cerrar conexión
cursor.close()
conexion.close()
