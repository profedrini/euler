import math

def continua(N):
	D=[]
	j=0
	A=int(math.sqrt(N))
	if A*A == N: return 0
	a=A
	d=1
	m=0
	while (m,a,d) not in D:
		D.append((m,a,d))
		m=d*a-m
		d=(N-m*m)//d
		a=int( (A+m)//d)

	return len(D)-1

S=0
for n in range(2,10001):
	if continua(n)%2 ==1:  S=S+1

print(S)