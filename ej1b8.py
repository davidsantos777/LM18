from funciones import convertir_a_euros, pasar_a_segundos, calcular_coste

acumulador = 0

costes_de_tarifa = []

tarifa = input("Escribe la tarifa por segundos en céntimos: ")

comunicaciones = int(input("Escribe el número de comunicaciones realizadas: "))

for i in range(comunicaciones):

	tiempo = input("¿Cuánto tiempo duró la comunicación {}? (HH:MM:SS): ".format(i + 1))

	horas = int(tiempo.split(':')[0])

	minutos = int(tiempo.split(':')[1])

	segundos = int(tiempo.split(':')[2])