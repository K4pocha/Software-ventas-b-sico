import tkinter as tk
from tkinter import messagebox, simpledialog
import pandas as pd
from datetime import datetime

# Archivo Excel para guardar los datos
archivo_excel = "ventas.xlsx"

# Intentar cargar datos existentes o crear un DataFrame vacío si el archivo no existe
try:
    df_ventas = pd.read_excel(archivo_excel)
except FileNotFoundError:
    df_ventas = pd.DataFrame(columns=["Fecha", "Cantidad", "Monto Total", "Pagado"])

# Funciones del programa
def ingresar_venta():
    tipo = simpledialog.askstring("Tipo de Venta", "Ingrese 'fiado' o 'pagado':")
    cantidad = simpledialog.askinteger("Cantidad", "Ingrese la cantidad:")
    monto_total = simpledialog.askfloat("Monto Total", "Ingrese el monto total:")
    
    if tipo.lower() == 'fiado':
        fecha = simpledialog.askstring("Fecha", "Ingrese la fecha (formato YYYY-MM-DD):")
        df_ventas.loc[len(df_ventas)] = [fecha, cantidad, monto_total, False]
    elif tipo.lower() == 'pagado':
        df_ventas.loc[len(df_ventas)] = [datetime.now().strftime("%Y-%m-%d"), cantidad, monto_total, True]
    else:
        messagebox.showerror("Error", "Tipo de venta no válido")

def recibir_pago():
    ventas_fiadas = df_ventas[df_ventas['Pagado'] == False]
    if ventas_fiadas.empty:
        messagebox.showinfo("Recibir Pago", "No hay ventas fiadas pendientes de pago.")
        return

    index_venta = simpledialog.askinteger("Recibir Pago", f"Seleccione el número de la venta a marcar como pagada:\n{ventas_fiadas}")
    if index_venta in ventas_fiadas.index:
        df_ventas.at[index_venta, 'Pagado'] = True
        messagebox.showinfo("Pago", "Venta actualizada como pagada.")
    else:
        messagebox.showerror("Error", "Número de venta no válido")

def ver_ganancias():
    if df_ventas.empty:
        messagebox.showinfo("Ganancias", "No hay ventas registradas.")
        return

    total_monto = df_ventas['Monto Total'].sum()
    total_cantidad = df_ventas['Cantidad'].sum()
    messagebox.showinfo("Ganancias Totales", f"Monto Total: ${total_monto}\nCantidad Total Vendida: {total_cantidad}")

def guardar_salir():
    df_ventas.to_excel(archivo_excel, index=False)
    window.quit()

# Configuración de la ventana principal
window = tk.Tk()
window.title("Sistema de Ventas")

# Botones
btn_ingresar_venta = tk.Button(window, text="Ingresar Venta", command=ingresar_venta)
btn_recibir_pago = tk.Button(window, text="Recibir Pago", command=recibir_pago)
btn_ver_ganancias = tk.Button(window, text="Ver Ganancias", command=ver_ganancias)
btn_salir = tk.Button(window, text="Salir", command=guardar_salir)

# Posicionamiento de los botones
btn_ingresar_venta.pack(pady=10)
btn_recibir_pago.pack(pady=10)
btn_ver_ganancias.pack(pady=10)
btn_salir.pack(pady=10)

# Ejecutar la GUI
window.mainloop()
