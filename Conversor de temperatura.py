from tkinter import Tk, Label, Button, Entry, StringVar, messagebox  
  
def convert_temperature():  
    try:  
        celsius = float(entry_celsius.get())  
        fahrenheit = celsius * 9/5 + 32  
        result.set(f"{fahrenheit:.2f} °F")  
    except ValueError:  
        messagebox.showerror("Error", "Debe ingresar solo numeros")  
  
# Se crea la pantalla principal  
root = Tk()  
root.title("Convertidor de Temperatura")  
  
# Se crea un StringVar para el resultado  
result = StringVar()  
  
# Se crean y customizan el entorno y pantalla principal 
Label(root, text="Celsius:").grid(row=0, column=0, padx=10, pady=10)  
entry_celsius = Entry(root)  
entry_celsius.grid(row=0, column=1, padx=10, pady=10)  
  
Button(root, text="Convertir a Fahrenheit", command=convert_temperature).grid(row=1, column=0, columnspan=2, pady=10)  
  
Label(root, text="Fahrenheit:").grid(row=2, column=0, padx=10, pady=10)  
Label(root, textvariable=result).grid(row=2, column=1, padx=10, pady=10)  
  
# Arranca el loop  
root.mainloop()  

