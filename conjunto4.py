# Abrir el archivo FASTA
#with open(r'D:\proyectos\sequence.fasta', 'r') as file:
    #Lee todo el contenido del archivo FASTA
    #content = file.read()

# Obtener la cadena ingresada por el usuario
# cadena = input("Ingrese un genoma, cromosoma o gen para analizar:")

# Extraer la cadena de un archivo FASTA
# Buscar el archivo
archivo = open(r'D:\proyectos\sequence.fasta', 'r')
# Obtener los datos
datos = archivo.read()
# Eliminar la primera línea
datos_sin_1_linea = datos[47:]
# Eliminar los saltos de línea
cadena = datos_sin_1_linea.replace("\n", "")


# Extraer el gen F8 del cromosoma X
inicio  = "tgaggagtacaagagtag"
inicio_upper = inicio.upper()
final = 'ctcgccgccccaagcactt'
final_upper = final.upper()
B_index = cadena.find(inicio_upper)
E_index = cadena.find(final_upper)

#cadena[B_index:E_index]
cadena = 'TGAGGAG'

#Agrupa cadenas de 3 
def agrupar_en_tres(cadena):
    conjuntos = [cadena[i:i+3] for i in range(0, len(cadena), 3)]
    
    # Si sobra un carácter, agruparlo con los últimos tres caracteres
    if len(cadena) % 3 == 1:
        conjuntos[-1] += cadena[-1]
    
    return conjuntos

conjuntos = agrupar_en_tres(cadena)

# Mostrar los conjuntos
for conjunto in conjuntos:
    print(conjunto)