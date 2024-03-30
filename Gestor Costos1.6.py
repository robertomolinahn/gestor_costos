import tkinter
from tkinter import ttk
import random
import string
import pyperclip
#Definicio de la vantana
modulo = tkinter.Tk()
modulo.geometry("700x400")
modulo.title("Gestion de Costos Lite 1.5")

tabControl = ttk.Notebook(modulo)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text="Retirar ISV al 15%")
tabControl.add(tab2, text="Generador de passwords")
tabControl.grid(row=20, column=0)

#Contenido del Tab1
label3 = tkinter.Label(tab1, text="Ingrese costo").grid(row=0, column=0)
quitar_isv = tkinter.Entry(tab1)
quitar_isv.grid(row=0, column=1)
quitar_isv.insert(0,"0")
label4 = tkinter.Label(tab1, text="Precio sin ISV(15%): ").grid(row=1, column=0)
precio_sin_isv = tkinter.Label(tab1)
precio_sin_isv.grid(row=1, column=1)
label_contrasena = tkinter.Label(tab2, text="Contraseña").grid(row=0, column=0)
contrasena = tkinter.Entry(tab2)
contrasena.grid(row=0, column=1)
N2 = str(contrasena)

def quitar():
    global costo_isv 
    costo_isv = float(quitar_isv.get()) / 1.15
    precio_sin_isv["text"] = round(costo_isv, 2)
    return costo_isv

def enviar_costo():
    costo1.insert(0, round(costo_isv, 2))
#variable que contine la cantidad de caracteres del password a generar    
N2 = 16
def randStr(chars = string.ascii_uppercase + string.digits, N=int(N2)):
	return ''.join(random.choice(chars) for _ in range(N))
def sub_password_generator():
    N2 = 16
    contrasena.delete(0,"end")
    def password_generator(chars = string.ascii_uppercase + string.digits, N=int(N2)):
        
        return ''.join(random.choice(chars) for _ in range(N))

    valor = password_generator(chars='abcdefghñ123456ABCDEFGHJKLMNOPQRSTWÑ!"#$%/?¡¿')
    pyperclip.copy(valor)
    contrasena.insert(0, valor)

generar_contrasena = tkinter.Button(tab2, text="Generar", command=sub_password_generator).grid(row=0, column=2)
#contrasena.insert(0, randStr())
quitar_isv_boton = tkinter.Button(tab1, text="Calcular", command=quitar, bg='red').grid(row=0, column=3)
#quitar_isv_boton_us = tkinter.Button(tab1, text="Calcular $", bg="green").grid(row=1, column=3)
enviar_al_costo = tkinter.Button(tab1, text="Enviar al Costo", command=enviar_costo, bg='green').grid(row=2, column=1)
#******************************FIN DEL CONTENIDO DEL TAB1 Y 2******************************
#Ingreso de costo sin el impuesto
label1 = tkinter.Label(modulo, text="Costo(SIN ISV)")
costo1 = tkinter.Entry(modulo)
costo1.insert(0,"0")

label2 = tkinter.Label(modulo, text="Ingrese no. cotizacion")
cotizacion = tkinter.Entry(modulo)

label5 = tkinter.Label(modulo, text="Item #").grid(row=0, column=3)
item = tkinter.Entry(modulo)
item.grid(row=0, column=4)
#Realizar calculos para el calculo de los costos

label_costo_proveedor = tkinter.Label(modulo, text="Costo: ")
costo_proveedor = tkinter.Label(modulo)


valor5_label = tkinter.Label(modulo, text="Venta al 5%")
valor10_label = tkinter.Label(modulo, text="Venta al 10%")
valor15_label = tkinter.Label(modulo, text="Venta al 15%")
valor20_label = tkinter.Label(modulo, text="Venta al 20%")
valor25_label = tkinter.Label(modulo, text="Venta al 25%")
valor30_label = tkinter.Label(modulo, text="Venta al 30%")
valor5 = tkinter.Label(modulo)
valor10 = tkinter.Label(modulo)
valor15 = tkinter.Label(modulo)
valor20 = tkinter.Label(modulo)
valor25 = tkinter.Label(modulo)
valor30 = tkinter.Label(modulo)



#funcion del calculo de costos
def calc():
    costo_funcion = float(costo1.get())
    costo_proveedor["text"] = costo_funcion
    n = costo_funcion
    if n == 0:
        error01 = "El valor del costo es 0"
        costo_proveedor["text"] = error01
    elif n == "":
        error02 = "Por favor ingresa un valor!"
        costo_proveedor["text"] = error02
    elif n != 0:
        calc_costo = costo_funcion

        #calc_costo = float(calc_costo)
        valor_venta5 = calc_costo / 0.95
        valor5["text"] = f"Lps. {round(valor_venta5, 2)}"
        valor_venta10 = calc_costo / 0.90
        valor10["text"] = f"Lps. {round(valor_venta10, 2)}"
        valor_venta15 = calc_costo / 0.85
        valor15["text"] = f"Lps. {round(valor_venta15, 2)}"
        valor_venta20 = calc_costo / 0.80
        valor20["text"] = f"Lps. {round(valor_venta20, 2)}"
        valor_venta25 = calc_costo / 0.75
        valor25["text"] = f"Lps. {round(valor_venta25, 2)}"
        valor_venta30 = calc_costo / 0.70
        valor30["text"] = f"Lps. {round(valor_venta30, 2)}"

#funcion del calculo de costos
def calc_usd():
    costo_funcion = float(costo1.get())
    costo_proveedor["text"] = costo_funcion
    n = costo_funcion
    if n == 0:
        error01 = "El valor del costo es 0"
        costo_proveedor["text"] = error01
    elif n == "":
        error02 = "Por favor ingresa un valor!"
        costo_proveedor["text"] = error02
    elif n != 0:
        calc_costo = costo_funcion

        #calc_costo = float(calc_costo)
        valor_venta5 = (calc_costo / 0.95)*25
        valor5["text"] = f"USD $ {round(valor_venta5, 2)}"
        valor_venta10 = (calc_costo / 0.90)*25
        valor10["text"] = f"USD $ {round(valor_venta10, 2)}"
        valor_venta15 = (calc_costo / 0.85)*25
        valor15["text"] = f"USD $ {round(valor_venta15, 2)}"
        valor_venta20 = (calc_costo / 0.80)*25
        valor20["text"] = f"USD $ {round(valor_venta20, 2)}"
        valor_venta25 = (calc_costo / 0.75)*25
        valor25["text"] = f"USD $ {round(valor_venta25, 2)}"
        valor_venta30 = (calc_costo / 0.70)*25
        valor30["text"] = f"USD $ {round(valor_venta30, 2)}"
calcular= tkinter.Button(modulo, text="Calcular Costo", command=calc, bg='red')
calcular_usd = tkinter.Button(modulo, text="Calcular Costo USD", command=calc_usd)
guardar = tkinter.Button(modulo, text="Guardar", bg='green').grid(row=10, column=2)

label1.grid(row=0,column=0)
costo1.grid(row=0,column=1)
label_costo_proveedor.grid(row=1,column=0)
costo_proveedor.grid(row=1,column=1)
label2.grid(row=2, column=0)
cotizacion.grid(row=2, column=1)
#valor 5%
valor5_label.grid(row=3, column=0)
valor5.grid(row=3, column=1)
#valor 10%
valor10_label.grid(row=4, column=0)
valor10.grid(row=4, column=1)
#valor 15%
valor15_label.grid(row=5, column=0)
valor15.grid(row=5, column=1)
#valor 20%
valor20_label.grid(row=6, column=0)
valor20.grid(row=6, column=1)
#valor 25%
valor25_label.grid(row=7, column=0)
valor25.grid(row=7, column=1)
#valor 30%
valor30_label.grid(row=8, column=0)
valor30.grid(row=8, column=1)
calcular.grid(row=10,column=1)
calcular_usd.grid(row=10,column=0)

modulo.mainloop()