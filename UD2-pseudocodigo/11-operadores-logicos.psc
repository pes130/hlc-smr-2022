Algoritmo GafasYBarba
	gafas = "n"
	barba = "n"
	
	Escribir "Programa para comprobar tu nivel de informático"
	Escribir "-----------------------------------------------"
	
	Escribir "¿Tienes gafas (s/n)?"
	Leer gafas
	Escribir "¿Tienes barbas (s/n)?"
	Leer barba
	
	Si barba == "s" y gafas ="s" Entonces
		Escribir "Eres informático 100%"
	Sino 
		Si barba == "s" o gafas == "s" Entonces 
			Escribir "Eres informático al 50%"
		Sino
			Escribir "Impostor! Tú no eres informático"
		FinSi
	FinSi
FinAlgoritmo
