Algoritmo GafasYBarba
	gafas = "n"
	barba = "n"
	
	Escribir "Programa para comprobar tu nivel de inform�tico"
	Escribir "-----------------------------------------------"
	
	Escribir "�Tienes gafas (s/n)?"
	Leer gafas
	Escribir "�Tienes barbas (s/n)?"
	Leer barba
	
	Si barba == "s" y gafas ="s" Entonces
		Escribir "Eres inform�tico 100%"
	Sino 
		Si barba == "s" o gafas == "s" Entonces 
			Escribir "Eres inform�tico al 50%"
		Sino
			Escribir "Impostor! T� no eres inform�tico"
		FinSi
	FinSi
FinAlgoritmo
