#Bloque 1: En este primer bloque se solicita el nombre completo del usuario.
#Solicita el nombre y valida que la respuesta no sea en blanco
while True:
    nombre = input('¿Cuál es tu nombre(s)? ')
    if not nombre.strip():
        print('Este apartado no puede estar en blanco')
    else:
        break

#Solicita el apellido paterno y valida que la respuesta no esté en blanco
while True:
    apellidoPaterno = input('¿Cuál es tu apellido paterno? ')
    if not apellidoPaterno.strip():
        print('Este apartado no puede estar en blanco')
    else:
        break

#Solicita el apellido materno y valida que la respuesta no este en blanco
while True:
    apellidoMaterno = input('¿Cuál es tu apellido materno? ')
    if not apellidoMaterno.strip():
        print('Este apartado no puede estar en blanco')
    else:
        break

#Bloque 2: Esta variable concatena los tres datos solicitados en el bloque anterior
nombre_completo = nombre, apellidoPaterno, apellidoMaterno

#Bloque 2: Esta variable concatena los tres datos solicitados en el bloque anterior
nombre_completo = nombre, apellidoPaterno, apellidoMaterno


#Bloque 3: En este segundo bloque se solicitan los datos numéricos
#Pide la edad y se asegura de que sea un valor válido
while True:
    try:
        edad = int(input('¿Cuál  es tu edad? '))#Se hace la conversión a entero
        if edad <= 0:
            print('Tu edad debe ser mayor que cero.')
        else:
            break
    except ValueError:
        print('Debes ingresar un número')

#Pide el peso y se asegura de que sea un valor válido
while True:
    try:
        peso = float(input('¿Cuál es tu peso en kg? ')) #Se hace la comversión a float
        if peso <= 0:
            print('Tu peso debe ser mayor que cero.')
        else:
            break
    except ValueError:
        print('Tu peso debe ser expresado en números')

#Pide la estatura y se asegura de que sea un valor válido
while True:
    try:
        estatura = float(input('¿Cuál es tu estatura? ')) #Se hace la conversión a float
        if estatura <= 0:
            print('tu estatura debe ser mayor que cero')
        else:
            break
    except ValueError:
        print('Tu estatura debe estar expresada en números')


#Bloque 4: Se hace el calculo del IMC
imc=peso/estatura**2


#Bloque 5: Se imprime el resultado
print(f"""
+--------------------+
{" ".join(nombre_completo).title()}
Edad: {edad} años
Estatura: {estatura} mts
Peso: {peso} kg
IMC: {imc:.2f}
Gracias por usar esta calculadora.
+--------------------+
""")
