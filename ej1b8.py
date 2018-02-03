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

	coste = calcular_coste(pasar_a_segundos(horas, minutos, segundos), tarifa)

	acumulador += coste

	euros, centi = convertir_a_euros(coste)

	tupla = (euros, centi)

	costes_de_tarifa.append(tupla)

	print("La comunicación tiene un coste de {}".format(i + 1), end = ' ')