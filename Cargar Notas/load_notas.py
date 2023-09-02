import csv

def cargarYCalcularEvaluacion(archivo, puntos_maximo, exigencia):
    lista = []
    
    nota_maxima = 7.0
    nota_minima = 1.0

    with open(archivo) as dato:
        lector = csv.reader(dato, delimiter=';')
        next(lector, None)
        
        for fila in lector:
            rut = fila[0]
            nombre = fila[1]
            puntajes = [int(valor) for valor in fila[2:]]
            suma_puntajes = sum(puntajes)

            # Calcular la nota en base a la fórmula
            nota = ((suma_puntajes / puntos_maximo) * (nota_maxima - nota_minima)) + nota_minima
            
            # Redondea la nota a un decimales
            nota = round(nota, 1)
            
            if nota >= 4.0:
                estado = 'Aprobado'
            else:
                estado = 'Reprobado'

            orden = {
                'Rut': rut,
                'Nombres': nombre,
                'Puntaje': suma_puntajes,
                'Nota': nota,
                'Estado': estado
            }

            lista.append(orden)

    return lista

# Solicitar valores
archivo = input('Ingrese el Nombre del Archivo: ')
puntos_maximo = int(input('Ingrese el total de puntos de la evaluación (60): '))

while True:
    exigencia_str = input('Ingrese la exigencia (0.6 o 0.5): ')
    try:
        exigencia = float(exigencia_str)
        if exigencia == 0.6 or exigencia == 0.5:
            break
        else:
            print("La exigencia debe ser 0.6 o 0.5. Por favor, ingrese un valor válido.")
    except ValueError:
        print("Entrada no válida. Ingrese un valor numérico (0.6 o 0.5).")
        

print('='*60)

#Llamar funcion

mostrar = cargarYCalcularEvaluacion(archivo, puntos_maximo, exigencia)

for result in mostrar:
    for clave, valor in result.items():
        print(f"{clave}: {valor}")
    print()



    



