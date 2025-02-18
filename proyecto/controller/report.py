from config.app import *
import pandas as pd
from datetime import datetime
import os

def GenerateReportVentas(app: App):
    """Genera un reporte de ventas por país y producto"""
    conn = app.bd.getConection()
    query = """
        SELECT 
            p.pais,
            v.product_id,
            SUM(v.quantity) AS total_vendido
        FROM 
            VENTAS v
        JOIN 
            POSTALCODE p
        ON 
            v.postal_code = p.code
        GROUP BY 
            p.pais, v.product_id
        ORDER BY 
            total_vendido DESC;
    """
    df = pd.read_sql_query(query, conn)
    
    if df.empty:
        print("⚠ No hay datos para generar el reporte de ventas.")
        return

    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    path = f"/workspaces/workspacepy0125vteoria/proyecto/files/Reporte1-{fecha_actual}.csv"
    df.to_csv(path, index=False)
    
    if os.path.exists(path):
        print(f"✅ Reporte de ventas guardado en {path}")
        sendMail(app, path, "Reporte de Ventas", "Adjunto reporte de ventas por país y producto.")
    else:
        print("❌ Error al guardar el reporte de ventas.")

def GenerateReportVentas2(app: App):
    """Genera un reporte de ventas por país y producto"""
    # Cargar los datos en un DataFrame de pandas desde el origen adecuado
    ventas_df = pd.read_sql_query("SELECT * FROM VENTAS", app.bd.getConection())
    postalcode_df = pd.read_sql_query("SELECT * FROM POSTALCODE", app.bd.getConection())
    
    # Si los DataFrames están vacíos, terminamos la función
    if ventas_df.empty or postalcode_df.empty:
        print("⚠ No hay datos para generar el reporte de ventas.")
        return

    # Hacemos un merge de las tablas 'VENTAS' y 'POSTALCODE' por el código postal
    df = ventas_df.merge(postalcode_df, left_on='postal_code', right_on='code')

    # Agrupamos por país y producto y sumamos la cantidad vendida
    grouped_df = df.groupby(['pais', 'product_id']).agg({'quantity': 'sum'}).reset_index()

    # Ordenamos el DataFrame por la cantidad vendida en orden ascendente (menos cantidad vendida primero)
    sorted_df = grouped_df.sort_values(by='quantity', ascending=True)

    # Si no hay datos, regresamos
    if sorted_df.empty:
        print("⚠ No hay ventas para generar el reporte.")
        return

    # Guardamos el reporte en un archivo CSV
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    path = f"/workspaces/workspacepy0125vteoria/proyecto/files/Reporte2-{fecha_actual}.csv"
    sorted_df.to_csv(path, index=False)

    # Verificamos si el archivo se guardó correctamente
    if os.path.exists(path):
        print(f"✅ Reporte de ventas guardado en {path}")
        sendMail(app, path, "Reporte de Ventas", "Adjunto reporte de ventas por país y producto.")
    else:
        print("❌ Error al guardar el reporte de ventas.")


def sendMail(app: App, file_path: str, subject: str, message: str):
    """Envía un correo con el reporte adjunto"""
    if os.path.exists(file_path):
        app.mail.send_email('from@example.com', subject, message, file_path)
        print(f"📧 Correo enviado con el archivo {file_path}")
    else:
        print("❌ No se pudo enviar el correo porque el archivo no existe.")
        