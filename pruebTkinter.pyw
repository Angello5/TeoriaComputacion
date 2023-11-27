import tkinter as tk
from tkinter import filedialog, messagebox


def transiciones(estado, simbolo):
    if estado == 'q1' and simbolo == 'A':
        return ['q7']
    elif estado == 'q1' and simbolo == 'T':
        return ['q4']
    elif estado == 'q1' and simbolo == 'C':
        return ['q4']
    elif estado == 'q1' and simbolo == 'G':
        return ['q2', 'q4', 'q7']

    elif estado == 'q2' and simbolo == 'A':
        return ['q3', 'q6']
    elif estado == 'q2' and simbolo == 'T':
        return ['q6']
    elif estado == 'q2' and simbolo == 'C':
        return ['q2', 'q4']
    elif estado == 'q2' and simbolo == 'G':
        return ['q3', 'q6']

    elif estado == 'q3' and simbolo == 'A':
        return ['q8']
    elif estado == 'q3' and simbolo == 'T':
        return ['q8']
    elif estado == 'q3' and simbolo == 'C':
        return ['q8']
    elif estado == 'q3' and simbolo == 'G':
        return ['q8']

    elif estado == 'q4' and simbolo == 'A':
        return ['q5', 'q8']
    elif estado == 'q4' and simbolo == 'T':
        return ['q2', 'q4', 'q5', 'q8']
    elif estado == 'q4' and simbolo == 'C':
        return ['q4', 'q8']
    elif estado == 'q4' and simbolo == 'G':
        return ['q5', 'q8']

    elif estado == 'q5' and simbolo == 'A':
        return ['q8']
    elif estado == 'q5' and simbolo == 'T':
        return ['q8']
    elif estado == 'q5' and simbolo == 'C':
        return ['q8']
    elif estado == 'q5' and simbolo == 'G':
        return ['q8']

    elif estado == 'q6' and simbolo == 'A':
        return ['q8']
    elif estado == 'q6' and simbolo == 'T':
        return ['q8']
    elif estado == 'q6' and simbolo == 'C':
        return ['q8']
    elif estado == 'q6' and simbolo == 'G':
        return ['q8']

    elif estado == 'q7' and simbolo == 'A':
        return ['q7', 'q8']
    elif estado == 'q7' and simbolo == 'T':
        return ['q3', 'q8']
    elif estado == 'q7' and simbolo == 'C':
        return ['q7', 'q8']
    elif estado == 'q7' and simbolo == 'G':
        return ['q7', 'q8']

    elif estado == 'q8' and simbolo == 'A':
        return []
    elif estado == 'q8' and simbolo == 'T':
        return []
    elif estado == 'q8' and simbolo == 'C':
        return []
    elif estado == 'q8' and simbolo == 'G':
        return []

    return []
def agrupar_en_tres(cadena):
    conjuntos = [cadena[i:i + 3] for i in range(0, len(cadena), 3)]
    if len(conjuntos[-1]) == 1:
        conjuntos[-2] += conjuntos[-1]
        conjuntos.pop()
    return conjuntos


def validar_secuencia(secuencia):
    estados = {'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'}
    estado_inicial = 'q1'
    estado_final = {'q8'}

    conjuntos = agrupar_en_tres(secuencia)

    es_valida = True
    for conjunto in conjuntos:
        estado_actual = {estado_inicial}
        for simbolo in conjunto:
            nuevos_estados = set()
            for estado in estado_actual:
                nuevos_estados.update(transiciones(estado, simbolo))
            estado_actual = nuevos_estados

        if not estado_final.intersection(estado_actual):
            es_valida = False
            break

    return es_valida


def cargar_secuencia():
    archivo_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Archivos FASTA", "*.fasta")])
    if archivo_path:
        with open(archivo_path, 'r') as archivo:
            encabezado = ""
            secuencia = ""
            en_encabezado = True

            for linea in archivo:
                if en_encabezado:
                    encabezado += linea.strip() + "\n"
                    if linea.strip().endswith('.') or linea.strip()[-1].islower():
                        en_encabezado = False
                else:
                    secuencia += linea.strip()

        label_encabezado.config(text=f"Información del archivo:\n{encabezado}")

        texto.delete(1.0, tk.END)
        texto.insert(tk.END, f"Información completa del archivo:\n\n")

        texto.insert(tk.END, f"{encabezado}\n{secuencia[:800]}\n")

        resultado = "La cadena es válida." if validar_secuencia(secuencia) else "La cadena NO es válida."
        messagebox.showinfo("Resultado", resultado)


ventana = tk.Tk()
ventana.title("Validador de Secuencia FASTA")

label_encabezado = tk.Label(ventana, text="Información del archivo:\n")
label_encabezado.grid(row=0, column=0, pady=10)

label_informacion = tk.Label(ventana, text="Información")
label_informacion.grid(row=1, column=0, pady=10)

texto = tk.Text(ventana, height=15, width=80)
texto.grid(row=2, column=0, padx=10, pady=10)

boton_cargar = tk.Button(ventana, text="Cargar Secuencia", command=cargar_secuencia)
boton_cargar.grid(row=3, column=0, pady=10)

cargar_secuencia()

ventana.mainloop()
