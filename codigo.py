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
        return []

    elif estado == 'q4' and simbolo == 'A':
        return  ['q5', 'q8']
    elif estado == 'q4' and simbolo == 'T':
        return  ['q2','q4','q5','q8']
    elif estado == 'q4' and simbolo == 'C':
        return  ['q4', 'q8']
    elif estado == 'q4' and simbolo == 'G':
        return  ['q5','q8']

    elif estado == 'q5' and simbolo == 'A':
        return  ['q3','q8']
    elif estado == 'q5' and simbolo == 'T':
        return ['q3','q8']
    elif estado == 'q5' and simbolo == 'C':
        return ['q3','q8']
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
        return  ['q8']

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

    #cadena = input("Ingrese una cadena con los digitos 0, 1, 2 o 3 en cualquier orden, para evaluar: ").upper()

    # Extraer la cadena de un archivo FASTA
    # Buscar el archivo
    archivo = open(r'D:\proyectos\sequence.fasta', 'r')
    # Obtener los datos
    datos = archivo.read()
    # Eliminar la primera línea
    datos_sin_1_linea = datos[47:]
    # Eliminar los saltos de línea
    # Obtener la cadena completa
    cadena = datos_sin_1_linea.replace("\n", "")

    #Agrupa cadenas de 3 
    def agrupar_en_tres(cadena):
        conjuntos = [cadena[i:i+3] for i in range(0, len(cadena), 3)]
        if len(conjuntos[-1]) == 1:
            conjuntos[-2] += conjuntos[-1]
            conjuntos.pop()
        return conjuntos

    conjuntos = agrupar_en_tres(cadena)

    # Mostrar los conjuntos
    for conjunto in conjuntos:
        print(conjunto)
        estado_actual = {estado_inicial}
        for simbolo in conjunto:
            nuevos_estados = set()
            for estado in estado_actual:
                nuevos_estados.update(transiciones(estado, simbolo))
                estado_actual = nuevos_estados

        if estado_final.intersection(estado_actual):
            print("La cadena es válida")
        else:
            print("La cadena NO es válida.")

if __name__ == "__main__":
    main()