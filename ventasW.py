import pandas as pd
from datetime import datetime

# Archivo Excel para guardar los datos
archivo_excel = "ventas.xlsx"

# Intentar cargar datos existentes o crear un DataFrame vacío si el archivo no existe
try:
    df_ventas = pd.read_excel(archivo_excel)
except FileNotFoundError:
    df_ventas = pd.DataFrame(columns=["Fecha", "Cantidad", "Monto Total", "Pagado"])

def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Ingresar Venta")
        print("2. Recibir Pago")
        print("3. Ver Ganancias")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            ingresar_venta()
        elif opcion == '2':
            recibir_pago()
        elif opcion == '3':
            ver_ganancias()
        elif opcion == '4':
            print("Guardando datos...")
            df_ventas.to_excel(archivo_excel, index=False)
            print("Datos guardados. Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def ingresar_venta():
    print("\nIngresar Venta")
    print("1. Fiado")
    print("2. Pagado")
    tipo = input("Seleccione el tipo de venta: ")
    
    cantidad = int(input("Ingrese la cantidad: "))
    monto_total = float(input("Ingrese el monto total: "))
    
    if tipo == '1':
        fecha = input("Ingrese la fecha (formato YYYY-MM-DD): ")
        df_ventas.loc[len(df_ventas)] = [fecha, cantidad, monto_total, False]
    elif tipo == '2':
        df_ventas.loc[len(df_ventas)] = [datetime.now().strftime("%Y-%m-%d"), cantidad, monto_total, True]
    else:
        print("Opción no válida")

def recibir_pago():
    print("\nVentas Fiadas")
    ventas_fiadas = df_ventas[df_ventas['Pagado'] == False]
    
    if ventas_fiadas.empty:
        print("No hay ventas fiadas pendientes de pago.")
        return
    
    print(ventas_fiadas)
    index_venta = int(input("Ingrese el número de la venta a marcar como pagada: "))
    
    if index_venta in ventas_fiadas.index:
        df_ventas.at[index_venta, 'Pagado'] = True
        print("Venta actualizada como pagada.")
    else:
        print("Número de venta no válido.")

def ver_ganancias():
    if df_ventas.empty:
        print("No hay ventas registradas.")
        return

    total_monto = df_ventas['Monto Total'].sum()
    total_cantidad = df_ventas['Cantidad'].sum()
    print(f"\nGanancias Totales:\nMonto Total: ${total_monto}\nCantidad Total Vendida: {total_cantidad}")

menu_principal()
