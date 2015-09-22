d=2
counter=0
for y in range(1901,2001):
	bis= ((y%4==0) - (y%100 ==0) + (y%400==0)) %7
	M=[31, (28+bis), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	
	Inicios=[(d+sum(M[0:k])) %7 for k  in range(12)]
	IniciosZ=[k for k in Inicios if k==0]
	counter=counter+len(IniciosZ)
	d=(d+sum(M))%7

print (counter)