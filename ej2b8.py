from funciones import convertir_a_euros, pasar_a_segundos, calcular_coste

with open("comunicaciones.txt", "r") as fichero:

	lines = fichero.readlines()

acumulador = 0

lista = []

costes_de_tarifa = []

for i in lines:

	lista.append(i.strip('\n'))

tarifa = lista[0].lstrip("Tarifa ")

lista.pop(0)

for i in lista:

	horas = int(i.split(':')[0])

	minutos = int(i.split(':')[1])

	segundos = int(i.split(':')[2])

	coste = calcular_coste(pasar_a_segundos(horas,minutos,segundos),tarifa)

	acumulador += coste

	euros, centi = convertir_a_euros(coste)

	done = (euros,centi)

	costes_de_tarifa.append(done)