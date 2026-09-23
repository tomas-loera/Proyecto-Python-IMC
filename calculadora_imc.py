#En este primer bloque se solicita el nombre completo del usuario.
#Se espera que todos sean del tipo string
nombre = input('¿Cuál es tu nombre(s)? ')
apellido_paterno = input('¿Cuál es tu apellido paterno? ')
apellido_materno = input('¿Cuál es tu apellido materno? ')

#Esta variable concatena los tres datos solicitados en el bloque anterior
nombre_completo = nombre, apellido_paterno, apellido_materno

#En este segundo bloque se solicitan los datos numéricos
edad = int(input('¿Cuál  es tu edad? '))#Se hace la conversión a entero
peso = int(input('¿Cuál es tu peso? '))#Se hace la conversión a entero
estatura = float(input('¿Cuál es tu estatura? '))#Se hace la conversión a float

#Se hace el calculo del IMC
imc=peso/estatura**2

#Se imprime el resultado
print(f"""
+--------------------+
{" ".join(nombre_completo).title()}
Edad: {edad}
Estatura: {estatura}
Peso: {peso}\nIMC: {imc:.2f}
Gracias por usar esta calculadora.
+--------------------+
""")
