from config.app import *
from modelos.model import *
# 
import pandas as pd

def IngestDataProducts(app:App):
    bd=app.bd
    conn=bd.getConection()
    dataPais=GetDataSourcePais()
    CreateTablesPais(conn)
    InsertDataPais(bd,dataPais)
    dataPostalCode=GetDatoSourcePostalCode()
    CreateTablePostalCode(conn)
    InsertDataPostalCode(bd,dataPostalCode)
    dataCategories=GetDataSourceCategories()
    createTableCategories(conn)
    InsertManyCategories(bd,dataCategories)
    dataProducts=GetDataSourceProductos(conn)
    createTableProducts(conn)
    InsertManyProducts(bd,dataProducts)
    dataVentas=GetDatasourceOrders(conn)
    createTableVentas(conn)
    insertManyVentas(bd,dataVentas)

    dataSegmentos = GetDataSourceSegmentos()
    CreateTableSegmentos(conn)
    InsertDataSegmentos(bd, dataSegmentos)

    dataMercados = GetDataSourceMercados()
    CreateTableMercados(conn)
    InsertDataMercados(bd, dataMercados)

    dataRegiones = GetDataSourceRegiones()
    CreateTableRegiones(conn)
    InsertDataRegiones(bd, dataRegiones)



def GetDataSourcePais():
    pathData="/workspaces/workspacepy0125vteoria/proyecto/files/datafuente.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    print(df.shape)
    print(df.keys())
    df_country=df['Country'].unique()
    print(df_country.shape)
    country_tuples = [(country,) for country in df_country] # hacer una lista de tuplas simplificado
    return country_tuples

def CreateTablesPais(conn:Connection):
    pais=Pais()
    pais.create_table(conn)
    
def InsertDataPais(bd:Database,data):
    bd.insert_many('PAIS',['name'],data)


def GetDatoSourcePostalCode():
    pathData="/workspaces/workspacepy0125vteoria/proyecto/files/datafuente.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    df['Postal Code'] = df['Postal Code'].astype(str)
    df_postalCode=df[['Postal Code','Country','State']]
    df_postalCode=df_postalCode.dropna()
    df_postalCode=df_postalCode.drop_duplicates()

    print(df_postalCode.head())
    postal_code_tuples=[tuple(x) for x in df_postalCode.to_records(index=False)]
    return postal_code_tuples

def CreateTablePostalCode(conn:Connection):
    postalCode=PostalCode()
    postalCode.create_table(conn)

def InsertDataPostalCode(bd:Database,data):
    bd.insert_many('POSTALCODE',['code','pais','state'],data)

def GetDataSourceCategories():
    pathData="/workspaces/workspacepy0125vteoria/proyecto/files/datafuente.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    df_categories=df[['Category','Sub-Category']].dropna().drop_duplicates()
    categories_tuples=[tuple(x) for x in df_categories.to_records(index=False)]
    return categories_tuples

def createTableCategories(conn:Connection):
    categories=Categorias()
    categories.create_table(conn)

def InsertManyCategories(bd:Database,data):
    bd.insert_many('CATEGORIAS',['name','subcategory'],data)


def GetDataSourceProductos(conn):
    pathData="/workspaces/workspacepy0125vteoria/proyecto/files/datafuente.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    df_products=df[['Product ID','Product Name','Category']].dropna().drop_duplicates()
    df_categoria=pd.read_sql_query("SELECT id,name FROM CATEGORIAS",conn)
    #df_newProducts=df_products.merge(df_categoria,how="left",left_on='Category',right_on='name')
    #print(df_newProducts.head())
    df_newProducts=df_products.merge(df_categoria,how="left",left_on='Category',right_on='name')
    df_newProducts=df_newProducts[['Product ID','Product Name','id']]
    df_newProducts=[tuple(x) for x in df_products.to_records(index=False)]
    return df_newProducts

def createTableProducts(conn:Connection):
    productos=Productos()
    productos.create_table(conn)

def InsertManyProducts(bd:Database,data):
    bd.insert_many('PRODUCTOS',['product_id','name','category_id'],data)


def GetDatasourceOrders(conn):
    pathData="/workspaces/workspacepy0125vteoria/proyecto/files/datafuente.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    df_products=pd.read_sql_query("SELECT id,name,product_id FROM PRODUCTOS",conn)
    df_orders=df[['Order ID','Postal Code','Product ID','Sales','Quantity','Discount','Profit','Shipping Cost','Order Priority']].dropna().drop_duplicates()
    df_orders['Postal Code'] = df_orders['Postal Code'].astype(str)
    print('shape orders',df_orders.shape)
    df_newOrders=df_orders.merge(df_products,how="left",left_on="Product ID",right_on="product_id")
    df_newOrders=df_newOrders.drop_duplicates()
    print('shape orders 1',df_newOrders.shape)
    df_newOrders=df_newOrders[['Order ID','Postal Code','id','Sales','Quantity','Discount','Profit','Shipping Cost','Order Priority']]
    list_tuples=[tuple(x) for x in df_newOrders.to_records(index=False)]
    return list_tuples

def createTableVentas(conn):
    ventas=Ventas()
    ventas.create_table(conn)

def insertManyVentas(bd:Database,data):
    bd.insert_many('VENTAS',['order_id','postal_code','product_id','sales_amount','quantity','discount','profit','shipping_cost','order_priority'],data)



def GetDataSourceSegmentos():
    pathData = "/workspaces/workspacepy0125vteoria/proyecto/files/datafuente.xls"
    df = pd.read_excel(pathData, sheet_name="Orders")
    df_segmentos = df['Segment'].dropna().unique()  # Extraer los segmentos únicos
    segmentos_tuples = [(segment,) for segment in df_segmentos]  # Convertir a lista de tuplas
    return segmentos_tuples

def CreateTableSegmentos(conn: Connection):
    segmentos = Segmentos()
    segmentos.create_table(conn)

def InsertDataSegmentos(bd: Database, data):
    bd.insert_many('SEGMENTOS', ['name'], data)


def GetDataSourceMercados():
    pathData = "/workspaces/workspacepy0125vteoria/proyecto/files/datafuente.xls"
    df = pd.read_excel(pathData, sheet_name="Orders")
    df_mercados = df['Market'].dropna().unique()  # Extraer mercados únicos
    mercados_tuples = [(market,) for market in df_mercados]
    return mercados_tuples

def CreateTableMercados(conn: Connection):
    mercados = Mercados()
    mercados.create_table(conn)

def InsertDataMercados(bd: Database, data):
    bd.insert_many('MERCADOS', ['name'], data)


def GetDataSourceRegiones():
    pathData = "/workspaces/workspacepy0125vteoria/proyecto/files/datafuente.xls"
    df = pd.read_excel(pathData, sheet_name="Orders")
    df_regiones = df['Region'].dropna().unique()  # Extraer regiones únicas
    regiones_tuples = [(region,) for region in df_regiones]
    return regiones_tuples

def CreateTableRegiones(conn: Connection):
    regiones = Regiones()
    regiones.create_table(conn)

def InsertDataRegiones(bd: Database, data):
    bd.insert_many('REGIONES', ['name'], data)

    