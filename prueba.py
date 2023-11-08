 # Obtener la cadena ingresada por el usuario
    # 
    # 
    # cadena = input("Ingrese un genoma, cromosoma o gen para analizar: ")
    
    # Extraer la cadena de una archivo FASTA
    # 
    # 
    # Buscar el archivo
x = open(r'D:\proyectos\sequence.fasta','r')
    # Obtener los datos
a = x.read()
    # Eliminar la primera linea
b = a[47:]
    # Eliminar los saltos de linea
c = b.replace("\n","")

    # Extraer el gen F8 del cromosoma X
inicio  = "tgaggagtacaagagtag"
inicio_upper = inicio.upper()
final = 'ctcgccgccccaagcactt'
final_upper = final.upper()
B_index = c.find(inicio_upper)
E_index = c.find(final_upper)
#c[B_index:E_index]
cadena = 'TGAGGAG'

def agrupar_en_tres(cadena):
    conjuntos = [cadena[i:i+3] for i in range(0, len(cadena), 3)]
    return conjuntos

conjuntos = agrupar_en_tres(cadena)

# Mostrar los conjuntos
for conjunto in conjuntos:
    print(conjunto)

