a=[1, 2, 3, 4, 1]
b=[3, 4, 1, 2, 1, 3]
n=len(a)
m=len(b)
dp=[[0 for i in range(m+1)] for i in range(n+1)]

for i in range(1,n+1):
	for j in range(1,m+1):
		if a[i-1]==b[j-1]:
			dp[i][j]=1+dp[i-1][j-1]
		else:
			dp[i][j]=max(dp[i-1][j],dp[i][j-1])
i=n
j=m
s=[]
while(i>0 and j>0):
	if a[i-1]==b[j-1]:
		s+=[a[i-1]]
		i-=1
		j-=1
	elif dp[i-1][j]>=dp[i][j-1]:
		i-=1
	else:
		j-=1
print(s[::-1])




