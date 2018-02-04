from funciones import convertir_a_euros, pasar_a_segundos, calcular_coste

with open("comunicaciones.txt", "r") as fichero:

	lines = fichero.readlines()

acumulador = 0

lista = []

costes_de_tarifa = []