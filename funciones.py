def convertir_a_euros(coste):
		euros = int(str(coste/100).split('.')[0])
		centi = int(str(coste/100).split('.')[1])
		return euros, centi

def calcular_coste(segundos, tarifa):
	return segundos * int(tarifa)

def pasar_a_segundos(horas, minutos, segundos):
		if horas > 24 or minutos > 59 or segundos > 59:
				return 0
		else:
				return (horas * 3600) + (minutos * 60) + segundos

						
