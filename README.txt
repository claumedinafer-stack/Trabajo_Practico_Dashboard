# Trabajo Práctico 2 - Dashboard con MySQL y Plotly

## Dataset
- Fuente: [Datos Abiertos de Clima](https://www.smn.gob.ar/descarga-de-datos)
- "Estadísticas normales Datos abiertos 1991-2020.txt"
- Se utilizó como base el archivo para generar el archivo "datos_clima.xlxs" con 4 solapas:
	- estacion:
		- COD_ESTACION
		- estación
		- provincia (columna nueva)
		- region  (columna nueva)
	- temperatura/temperatura_max/temperatura_min las tres con campos:
	        - COD_ESTACION
	        - Ene
		- Feb
		- Mar
		- Abr
		- May
		- Jun
		- Jul
		- Ago
		- Sep
		- Oct
		- Nov
		- Dic

		
## Base de datos
- Motor: MySQL
- Instalar MySQL community para programador

## Visual Studio Code
# Ejecutar
pip install mysql-connector-python pandas plotly streamlit 

#Ejecutar script para la creación de la base de datos con las tablas "Crear_tablas.py"
pip install pandas openpyxl mysql-connector-python

#Ejecutar script para la carga de los datos en las tablas desde archivos excel
python cargar_datos.py

#Preparo para ejecutar el dashboard
pip install SQLAlchemy

#Ejecuto dashborad para visualizar la evolución de temperaturas promedio por provincia
python dashboard_temperaturas.py