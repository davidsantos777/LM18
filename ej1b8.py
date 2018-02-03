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

	if costes_de_tarifa[i][0] == "0":
		if costes_de_tarifa[i][1] == "1":
			print("{} céntimo".format(costes_de_tarifa[i][1]))
		else:
			print("{} céntimos".format(costes_de_tarifa[i][1]))

	elif costes_de_tarifa[i][1] == "0":
		print("{} euro/s".format(costes_de_tarifa[i][0]))

	else:
		if costes_de_tarifa[i][1] == "1":
			print("{} euro/s y {} céntimo".format(costes_de_tarifa[i][0], costes_de_tarifa[i][1]))
		else:
			print("{} euro/s y {} céntimos".format(costes_de_tarifa[i][0], costes_de_tarifa[i][1]))

total_euros, total_centi = convertir_a_euros(acumulador)

print("El coste total de las comunicaciones es de: {} euro/s y {} céntimos".format(total_euros, total_centi))