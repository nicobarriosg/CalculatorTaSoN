import tkinter as tk
from tkinter import messagebox

def menu():
    while True:
        try:
            print("Calculadora TaSoN")
            print("1) Ingresar un triángulo a calcular")
            print("2) Salir")
            opcion = int(input("\nIngrese la opción deseada: "))
            if opcion >= 1 and opcion <= 2:
                return opcion
            else:
                print("\nIngrese solo opciones válidas")
        except ValueError:
            print("\nIngrese solo números")

def leerLados():
    while True:
        try:
            lado_a = float(input("\nIngrese la longitud del lado a: "))
            lado_b = float(input("Ingrese la longitud del lado b: "))
            lado_c = float(input("Ingrese la longitud del lado c: "))
            if lado_a + lado_b > lado_c and lado_b + lado_c > lado_a and lado_a + lado_c > lado_b:
                return lado_a, lado_b, lado_c
            else:
                print("Los lados no forman un triángulo válido")
        except ValueError:
            print("Ingrese solo números válidos")

def calculadora_trigonometrica_lados(a, b, c):
    seno = b / c
    coseno = a / c
    tangente = seno / coseno
    cosecante = 1 / seno
    secante = 1 / coseno
    cotangente = coseno / seno

    return (
        "\nSeno: "
        + str(seno)
        + "\n"
        + "Coseno: "
        + str(coseno)
        + "\n"
        + "Tangente: "
        + str(tangente)
        + "\n"
        + "Secante: "
        + str(secante)
        + "\n"
        + "Cosecante: "
        + str(cosecante)
        + "\n"
        + "Cotangente: "
        + str(cotangente)
        + "\n"
    )

def on_calculate():
    try:
        a, b, c = float(entry_a.get()), float(entry_b.get()), float(entry_c.get())
        if a + b > c and b + c > a and a + c > b:
            result_text.set(calculadora_trigonometrica_lados(a, b, c))
        else:
            messagebox.showerror("Error", "Los lados no forman un triángulo válido.")
    except ValueError:
        messagebox.showerror("Error", "Ingrese solo números válidos.")

def on_exit():
    root.destroy()

# Interfaz gráfica
root = tk.Tk()
root.title("Calculadora TaSoN")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Título en grande
title_label = tk.Label(frame, text="Calculadora TaSoN", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

label_a = tk.Label(frame, text="Longitud del lado A:")
label_a.grid(row=1, column=0, padx=5, pady=5)
entry_a = tk.Entry(frame)
entry_a.grid(row=1, column=1, padx=5, pady=5)

label_b = tk.Label(frame, text="Longitud del lado B:")
label_b.grid(row=2, column=0, padx=5, pady=5)
entry_b = tk.Entry(frame)
entry_b.grid(row=2, column=1, padx=5, pady=5)

label_c = tk.Label(frame, text="Longitud del lado C:")
label_c.grid(row=3, column=0, padx=5, pady=5)
entry_c = tk.Entry(frame)
entry_c.grid(row=3, column=1, padx=5, pady=5)

calculate_button = tk.Button(frame, text="Calcular", command=on_calculate)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_text = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_text)
result_label.grid(row=5, column=0, columnspan=2, pady=10)

exit_button = tk.Button(frame, text="Salir", command=on_exit)
exit_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
