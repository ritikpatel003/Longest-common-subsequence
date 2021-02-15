X = 'ABCDGH'
Y = 'AEDFHR'

def sol(n,m):
	if n==0 or m==0:
		return 0
	if X[n-1]==Y[m-1]:
		return 1+sol(n-1,m-1)
	else:
		return max(sol(n-1,m),sol(n,m-1))

print(sol(len(X),len(Y)))

