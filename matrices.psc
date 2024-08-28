Funcion num <- NumeroRandom(n)
	Definir num Como Entero;
	
	// Generar un número aleatorio entre 0 y 2n
	num = Azar(2 * n + 1) - 1
	
	// Ajustar para que esté en el rango [-n, n]
	num = num - n
	
Fin Funcion



Algoritmo matrices
	
	Definir i Como Entero;
	Definir j Como Entero;
	Definir n Como Entero;
	Definir m Como Entero;
	Definir a Como Caracter;
	Definir x como Entero;
	
	m = 5;
	n = 5;
	a = "";
	
	Escribir "Ingrese cantidad de columnas";
	Leer m;
	Escribir "Ingrese cantidad de filas";
	Leer n;
	
	Para i = 1 Hasta m Hacer
		Para j = 1 Hasta n Hacer
			a = a + "a" + ConvertirATexto(i) + ConvertirATexto(j) + " ";
		Fin Para
		Escribir a;
		a = "";
	Fin Para
	
	Escribir "----------"
	Escribir "Matriz con valores random";
	// Crear la matriz con valores aleatorios entre -10 y 10
	Para i = 1 Hasta m Hacer
		Para j = 1 Hasta n Hacer
			x=NumeroRandom(10);
			Si x<0 Entonces
				a = a+ConvertirATexto(x)+" ";
			SiNo
				a = a+" "+ConvertirATexto(x)+" ";
			Fin Si
		Fin Para
		Escribir a;
		a = "";
	Fin Para
	
FinAlgoritmo
