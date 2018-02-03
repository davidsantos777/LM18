def convertir_a_euros(coste):
		euros = int(str(coste/100).split('.')[0])
		centi = int(str(coste/100).split('.')[1])

def calcular_coste(s, tarifa):

		return s * int(tarifa)

def pasar_a_segundos(h, m, s):
		if h > 24 or m > 59 or s > 59:
				return 0
		else:
				return (h * 3600) + (m * 60) + s						