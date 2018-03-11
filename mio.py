import math
class atributo():
	nombre=""
	filas=[]
	tiposv=[]
	iden=[]
	
def log2(numero):
	return math.log(numero,2)

def esta_en_lista(elemento, lista):
	for i in lista:
		if i==elemento:
			return 1
	else: 
		return 0

def entropia(pos, neg):
	if pos==0 or neg==0:
		return 0;
	elif pos==neg:
		return 1
	else:
		total=float(pos)+float(neg)
		return -(pos/total)*log2(float(pos/total))-(neg/total)*log2(float(neg/total))

def obt_tiposv_atributos(atributo):
	tiposv_atributo=[]
	for valor in atributo[1:len(atributo)]:
		if esta_en_lista(valor, tiposv_atributo)==0:
			tiposv_atributo.append(valor)
	return tiposv_atributo
	
def cuenta_apariciones (elemento, lista):
	cuenta=0
	for i in lista:
		if i==elemento:
			cuenta=cuenta+1
	return cuenta
	
def match_val_atr_sino(valor, filas, si_no):
	contar=0
	for i in range(0,len (filas)):
		if filas[i]==valor and atributo4.filas[i]==si_no:
			contar+=1
	return contar
	
def match_val_atr_atr_sino(valor1, filas1, valor2, filas2, si_no):
	contar=0
	for i in range(0,len (filas1)):
		if filas1[i]==valor1 and filas2[i]==valor2 and atributo4.filas[i]==si_no:
			contar+=1
	return contar

def ganancia_D(D,atributo):
	ganancia=ent_inicial
	for i in atributo.tiposv:
		pos=match_val_atr_sino(i, atributo.filas, "si")
		neg=match_val_atr_sino(i, atributo.filas, "no")
		ganancia=ganancia-( float(cuenta_apariciones(i, atributo.filas) )/float (D) )* entropia(pos,neg)
	return ganancia
	
def gananciaD_at(D,atributoa, v_atributoa, atributob, ent_ini):
	ganancia=ent_ini
	for i in atributob.tiposv:
		pos= match_val_atr_atr_sino(v_atributoa, atributoa.filas, i, atributob.filas, "si")
		neg= match_val_atr_atr_sino(v_atributoa, atributoa.filas, i, atributob.filas, "no")
		ganancia=ganancia-( float(pos+neg) /float (D) ) * entropia(pos, neg)
	return ganancia

def obt_nombre_atributo(num):
	if num==0:
		return atributo1.nombre
	elif num==1:
		return atributo2.nombre
	elif num==2:
		return atributo3.nombre
		
def lis_at_res(actual):
	at_res=[]
	for z in la:
		if esta_en_lista(z.nombre, at_res)==0 and z.nombre!=actual:
			at_res.append(z.nombre)
	return at_res
			
def atr_num(atributo):
	if atributo==atributo1.nombre:
		return 0
	elif atributo==atributo2.nombre:
		return 1
	elif atributo==atributo3.nombre:
		return 2
"""
Se tienen como arreglos cada atributo
at_prin: Atributo principal que determina si/no, +,-, etc.
atributos: lista de atributos
nodo elegido: tiposv
Si se elige un atributo, entonces todos los atributos tendran el mismo tipo del nodo elegido (mismas filas)
"""
def id3(at_prin, atributos,nodo_elegido): 

	#Si ninguna da "si" regresar -
	if cuenta_apariciones("si", at_prin.filas)==0:
		print "en "+nodo_elegido.nombre+" "+nodo_elegido.filas[1]+" Se selecciono 'no'"
		return "-"
	elif cuenta_apariciones("no", at_prin.filas)==0:
		print "en "+nodo_elegido.nombre+" "+nodo_elegido.filas[1]+" Se selecciono 'si'"
		return "+"
	elif len(atributos)<=2:
		print "en "+nodo_elegido.nombre+" "+nodo_elegido.filas[1]+" Se selecciono '?'"
		return "?"
	#elif len(atributos)==2:

	else:
		ent_inicial=entropia(cuenta_apariciones("si", at_prin.filas),cuenta_apariciones("no", at_prin.filas))
		#total de filas con datos en la tabla
		D=len(at_prin.filas)-1	

		ganancias_D=[]
		for i in range(len(atributos)-1):
			ganancias_D.append(ganancia_D(D,atributos[i]))
		for i in range(len(atributos)-1):
			if nodo_elegido==[]:
				print "Ganancia (D,"+atributos[i].nombre+") = " + str(ganancias_D[i])+"\n"
			else:		
				print "Ganancia (D"+nodo_elegido.filas[1]+","+atributos[i].nombre+") = " + str(ganancias_D[i])+"\n"
		#Obteniendo nodo raiz (atributo ganador)
		indice_raiz=ganancias_D.index(max(ganancias_D))
		nodo_raiz=atributos[indice_raiz]
		#Quitamos de los atributos, al atributo ganador
		atributos.pop(indice_raiz)	
		atrib_restantes=atributos
		####################################################Esto ya no va
		#for i in range(len(atributos)):
		#	if i!=indice_raiz:
		#		atrib_restantes.append(atributos[i])
		################################################################
		""" Esto ya dudo que funcione
		for i in range(len(atributos)):
			if i!=indice_raiz:
				atrib_restantes.append(atributos[i])
		"""

		#Salvo atributos restantes para ciclar cada tipo de atributo
		lista_at_aux=atrib_restantes 
		##Implementar crear arbol bifurcacion de tipos
		#Para cada tipo del atributo (ej. Rojo, Azul, Verde...)
		for i in range(len(nodo_raiz.tiposv)):
			atrib_restantes=lista_at_aux
			listaids=[] #Lista identificadores que hay que borrar 
			#El identificador 0 no pertenece a ningun tipo
			for j in range(1,len(nodo_raiz.iden)): 
				if i!=nodo_raiz.iden[j]:
					listaids.append(i) #Los que hay que borrar

			#aqui borramos 
			for k in range(len(atrib_restantes)):
				for j in reversed(range(len(atrib_restantes))):
					atrib_restantes[k].iden.pop(j)
			id3(at_prin,atrib_restantes,nodo_raiz)	
				
		#id3(at_prin,atrib_restantes,nodo_raiz)
			

#####SE CREA Y RELLENA LA TABLA
atributo1=atributo()
atributo1.filas=["ejemplares","<=4",">4",">4","<=4",">4",">4","<=4","<=4",">4"
	,"<=4","<=4",">4","<=4",">4",">4"]

atributo2=atributo()
atributo2.filas=["ventas","buenas","buenas","buenas","buenas","buenas","bajas","bajas","bajas","bajas"
	,"bajas","promedio","promedio","promedio","promedio","promedio"]

atributo3=atributo()
atributo3.filas=["precio","<=150",">150","<=150",">150",">150",">150",">150",">150","<=150"
	,"<=150","<=150","<=150",">150",">150","<=150"]
	
atributo4=atributo()
atributo4.filas=["descuento","si","si","si","si","si","si","no","si","si"
	,"no","no","no","si","si","no"]

#Se les pone un numero de identificador, el 0 pertenece al nombre
for i in range(len(atributo1.filas)):
	atributo1.iden.append(i)
	atributo2.iden.append(i)
	atributo3.iden.append(i)
	atributo4.iden.append(i)	
#########EL AGENTE RECONOCE A LOS TIPOS DE VALORES DE CADA ATRIBUTO	
#Obtener los tipos de valores de cada atributo
atributo1.tiposv=obt_tiposv_atributos(atributo1.filas)
atributo2.tiposv=obt_tiposv_atributos(atributo2.filas)
atributo3.tiposv=obt_tiposv_atributos(atributo3.filas)
#Obteniendo nombres
atributo1.nombre=atributo1.filas[0]
atributo2.nombre=atributo2.filas[0]
atributo3.nombre=atributo3.filas[0]
#Lista atributos??
atrib=[atributo1,atributo2,atributo3,atributo4]
ent_inicial=entropia(cuenta_apariciones("si", atributo4.filas),cuenta_apariciones("no", atributo4.filas))
path=""

id3(atrib[3],atrib,[])



