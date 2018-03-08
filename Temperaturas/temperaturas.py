from lxml import etree

arbol = etree.parse("http://www.aemet.es/xml/municipios/localidad_41038.xml")

doc = etree.parse("sevilla.xml")

cod_municipios = doc.findall("municipio")

lista = []

lista2 = []

muni = False

municipio = input("Dime un municipio para conocer su temperatura: ")

for cod in cod_municipios:
	cod2 = str(cod.attrib["value"])
	cod3 = cod2.split("-id")
	lista.append(cod3[0])
	lista2.append(cod3[1])

for elem1,elem2 in zip(lista,lista2):
	if municipio == elem1:		
		arbol = etree.parse('http://www.aemet.es/xml/municipios/localidad_'+elem2+'.xml')
		t_maxima = arbol.find("prediccion/dia/temperatura/maxima")
		t_minima = arbol.find("prediccion/dia/temperatura/minima")
		muni = True

if muni == False:
	print( "Se ha producido un error. Municipio equivocado o mal escrito.")
else:			
	print ("Temperatura máxima de {}:".format(municipio),t_maxima.text)
	print ("Temperatura mínima de {}:".format(municipio),t_minima.text)
