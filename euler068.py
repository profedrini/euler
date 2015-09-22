import itertools as it 

M=5
L=range(1,2*M+1)

print(list(L))
def Check(p):
	D=[p[-1]+p[0]]
	for k in range(M-1):
		D.append(p[k]+p[k+1])
	if len(set(D))==M and max(D)-min(D)==M-1:
		suma=max(p)+1 + max(D)
		cola=[suma-m for m in D]
		T=list(p)+cola
		if set(T)==set(L) and cola[0]==min(cola):
			chain=""
			for k in range(len(cola)):
				chain =chain+"".join(map(str, [cola[k],p[k-1],p[k]]))
		
			print(p,"\t", "suma:", suma , "\t", cola, "\t", min(cola), T, D,chain)
			return int(chain)
	return 0

X=[]
for p in it.permutations(L,M):
	g=Check(p)
	if g>0: X.append(g)

print(X)
for x in X: print(x)
print("--------")
print(max(X))
	