s="abab"
r=s
n=len(s)
dp=[[0 for i in range(n+1)] for i in range(n+1)] 
for i in range(1,n+1):
	for j in range(1,n+1):
		if s[i-1]==r[j-1] and i!=j:
			dp[i][j]=1+dp[i-1][j-1]
		else:
			dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])