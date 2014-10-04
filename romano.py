def romano (n):
	if n>=100 : 
		print 'solo menores que 100 ;)';
	else:
		cadena = "";
		i = 1
		num = 0
		while n != 0:
			num = n % 10 
			cadena = romanaux(num,i) + cadena			
			n = n / 10
			i = i + 1
			
		print cadena; 
	
def romanaux(num,t) :
	cadena = ""
	i =1	
	if t == 1:
		uno = "I"
		cinco ="V"
		diez = "X"
	else : 
	 	uno = "X"
		cinco ="L"
		diez = "C"
	if num < 4 : 
		
		while i <= num: 
			cadena = cadena + uno 		
			i=i+1
		
	elif num == 4 : 
		cadena = uno + cinco

	elif num == 5 : 
		return cinco
	elif num > 5 and num < 9 : 
		cadena = cinco		
		while i <= (num-5) : 
			cadena = cadena + uno
			i = i+1
	else : 
		cadena = uno + diez
	return cadena 
			

		
romano(87)
