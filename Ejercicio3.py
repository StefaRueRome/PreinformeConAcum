primero=0
for i in range(0,5):
	num=int(input("introduce un número: "))
	if i==0:
		mayor=num
	else:
		if num>mayor:
			mayor=num
print("El número mayor es: ", mayor)


	