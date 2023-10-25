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
        return ['q3']

def main():    
    estados = {'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8'}
    alfabeto = {'A', 'T', 'C', 'G'}
    estado_inicial = 'q1'
    estado_final = 'q8'

    cadena = input("Ingrese un genoma, cromosoma o gen para analizar:")
    estado_actual = {estado_inicial}

    for simbolo in cadena:
        nuevos_estados = set()
        for estado in estado_actual:
          nuevos_estados.update(transiciones(estado, simbolo))
        estado_actual = nuevos_estados

    if estado_final in estado_actual:
        print("La cadena es válida")
    else:
        print("La cadena NO es válida.")

if __name__ == "__main__":
    main()