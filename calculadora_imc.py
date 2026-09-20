#Se espera que estas tres primeras variables sean del tipo string
nombre = input('¿Cuál es tu nombre?')
apellido_paterno = input('¿Cuál es tu apellido paterno?')
apellido_materno = input('¿Cuál es tu apellido materno?')



edad = int(input('¿Cuál es tu edad?')) #Se espera que esta variable sea de tipo entero, por eso se hace la conversión
peso = float(input('¿Cuál es tu peso?')) #Se espera que esta variable sea de tipo float, por eso se hace la conversión
estatura = float(input('¿Cuál es tu estatura?')) #Se espera que esta variable sea de tipo float, por eso se hace la conversión

imc=peso/estatura**2

print(f'{nombre} {apellido_paterno} {apellido_materno}, tu IMC es: {imc}. Gracias por usar esta calculadora.')


