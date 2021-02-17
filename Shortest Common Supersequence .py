X = "abcd"
Y = "xycd"
m=4
n=4
dp=[[0 for i in range(m+1)] for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if Y[i-1]==X[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(m+n-dp[-1][-1])