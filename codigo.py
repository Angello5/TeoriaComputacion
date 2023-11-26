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
        return ['q3','q6']

    elif estado == 'q3' and simbolo == 'A':
        return  ['q8']
    elif estado == 'q3' and simbolo == 'T':
        return  ['q8']
    elif estado == 'q3' and simbolo == 'C':
        return ['q8']
    elif estado == 'q3' and simbolo == 'G':
        return ['q8']

    elif estado == 'q4' and simbolo == 'A':
        return  ['q5', 'q8']
    elif estado == 'q4' and simbolo == 'T':
        return  ['q2','q4','q5','q8']
    elif estado == 'q4' and simbolo == 'C':
        return  ['q4', 'q8']
    elif estado == 'q4' and simbolo == 'G':
        return  ['q5','q8']

    elif estado == 'q5' and simbolo == 'A':
        return  ['q8']
    elif estado == 'q5' and simbolo == 'T':
        return ['q8']
    elif estado == 'q5' and simbolo == 'C':
        return ['q8']
    elif estado == 'q5' and simbolo == 'G':
        return ['q8']

    elif estado == 'q6' and simbolo == 'A':
        return ['q8']
    elif estado == 'q6' and simbolo == 'T':
        return  ['q8']
    elif estado == 'q6' and simbolo == 'C':
        return  ['q8']
    elif estado == 'q6' and simbolo == 'G':
        return ['q8']

    elif estado == 'q7' and simbolo == 'A':
        return  ['q7','q8']
    elif estado == 'q7' and simbolo == 'T':
        return  ['q3','q8']
    elif estado == 'q7' and simbolo == 'C':
        return  ['q7','q8']
    elif estado == 'q7' and simbolo == 'G':
        return  ['q7','q8']

    elif estado == 'q8' and simbolo == 'A':
        return  [ ]
    elif estado == 'q8' and simbolo == 'T':
        return  [ ]
    elif estado == 'q8' and simbolo == 'C':
        return  [ ]
    elif estado == 'q8' and simbolo == 'G':
        return  [ ]

    return [ ]

def main():
    estados = {'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'}
    alfabeto = {'A', 'T', 'C', 'G'}
    estado_inicial = 'q1'
    estado_final = {'q8'}    

    # cadena = input("Ingrese una cadena con los digitos 0, 1, 2 o 3 en cualquier orden, para evaluar: ").upper()

    # Leer el archivo FASTA y separar el encabezado de la secuencia
    with open(r'D:\proyectos\sequence.fasta', 'r') as archivo:
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

    # ESTO SIRVE PARA VERIFICAR QUE ESTAMOS LEYENDO CON LA FUNCION agrupar_en_tres():
    # Abrir el archivo en modo de escritura
    with open('D:/proyectos/archivo.txt', 'w') as archivo:
        # Escribir el contenido de la variable en el archivo
        archivo.write(secuencia)

    secuencia += '1'
    # Agrupa cadenas de 3 
    def agrupar_en_tres(cadena):
        conjuntos = [cadena[i:i+3] for i in range(0, len(cadena), 3)]
        if len(conjuntos[-1]) == 1:
            conjuntos[-2] += conjuntos[-1]
            conjuntos.pop()
        return conjuntos

    conjuntos = agrupar_en_tres(secuencia)
    
    # Mostrar los conjuntos
    esValida = True
    for conjunto in conjuntos:
        estado_actual = {estado_inicial}
        for simbolo in conjunto:
            nuevos_estados = set()
            for estado in estado_actual:
                nuevos_estados.update(transiciones(estado, simbolo))
            estado_actual = nuevos_estados

        if not estado_final.intersection(estado_actual):
            esValida = False
            break

    if esValida:
        print("La cadena completa es válida")
    else:
        print("La cadena completa NO es válida.")

if __name__ == "__main__":
    main()