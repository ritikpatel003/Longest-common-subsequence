S1 = "ABCD"
S2 = "ABC"
n = len(S1)
m = len(S2)

dp=[[0 for i in range(m+1)] for i in range(n+1)]

for i in range(1,n+1):
	for j in range(1,m+1):
		if S1[i-1]==S2[j-1]:
			dp[i][j]=1+dp[i-1][j-1]
		else:
			dp[i][j]=0
mx=-2**32
for i in dp:
    a=max(i)
    if a>mx:
        mx=a
print(mx)