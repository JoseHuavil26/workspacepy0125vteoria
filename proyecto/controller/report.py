from config.app import *
import pandas as pd
from datetime import datetime
import os

def GenerateReportVentas(app: App):
    """Genera un reporte de ventas por país y producto usando SQL"""
    try:
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

        save_and_send_report(app, df, "Reporte1", "Reporte de Ventas por País y Producto")

    except Exception as e:
        print(f"❌ Error en GenerateReportVentas: {e}")


def GenerateReportPaisesMenosCompraron(app: App):
    """Genera un reporte de los países que compraron menos usando Pandas"""
    try:
        conn = app.bd.getConection()

        # Cargar las tablas en DataFrames
        ventas_df = pd.read_sql_query("SELECT * FROM VENTAS", conn)
        postalcode_df = pd.read_sql_query("SELECT * FROM POSTALCODE", conn)

        if ventas_df.empty or postalcode_df.empty:
            print("⚠ No hay datos para generar el reporte de países que compraron menos.")
            return

        # Realizar el merge en Pandas (en lugar de SQL)
        df = ventas_df.merge(postalcode_df, left_on='postal_code', right_on='code')

        # Agrupar por país y producto, sumando las cantidades vendidas
        grouped_df = df.groupby(['pais', 'product_id'])['quantity'].sum().reset_index()

        # Ordenar por cantidad vendida (menor a mayor)
        sorted_df = grouped_df.sort_values(by='quantity', ascending=True)

        # Guardar y enviar reporte
        save_and_send_report(app, sorted_df, "Reporte2", "Reporte de Países con Menos Compras")

    except Exception as e:
        print(f"❌ Error en GenerateReportPaisesMenosCompraron: {e}")


def save_and_send_report(app: App, df: pd.DataFrame, report_name: str, subject: str):
    """Guarda un DataFrame en CSV y envía un correo con el archivo adjunto"""
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    path = f"/workspaces/workspacepy0125vteoria/proyecto/files/{report_name}-{fecha_actual}.csv"
    
    df.to_csv(path, index=False)

    if os.path.exists(path):
        print(f"✅ Reporte guardado en {path}")
        sendMail(app, path, subject, f"Adjunto {subject}.")
    else:
        print(f"❌ Error al guardar el reporte {report_name}")


def sendMail(app: App, file_path: str, subject: str, message: str):
    """Envía un correo con el reporte adjunto"""
    if os.path.exists(file_path):
        app.mail.send_email('from@example.com', subject, message, file_path)
        print(f"📧 Correo enviado con el archivo {file_path}")
    else:
        print("❌ No se pudo enviar el correo porque el archivo no existe.")
        