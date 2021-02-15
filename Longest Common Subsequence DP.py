X = 'ABCDGH'
Y = 'AEDFHR'
n=len(X)
m=len(Y)

dp=[[0 for i in range(m+1)] for i in range(n+1)]

for i in range(1,n+1):
	for j in range(1,m+1):
		if X[i-1]==Y[j-1]:
			dp[i][j]=1+dp[i-1][j-1]
		else:
			dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])
