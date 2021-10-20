def lrs(s1,s2,m,n):
    dp=[[-1 for x in range(n+1) ]for y in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j]=0
            elif s1[i-1] == s2[j-1] and i!=j:
                dp[i][n-j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    return  dp[m][n]
s='agbbagc'
print(lrs(s,s,len(s),len(s)))