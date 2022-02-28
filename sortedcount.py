m, s, e = map(int, input().split())
dp = [[0 for i in range(e-s+1)] for i in range(m)]

for i in range(m):
    dp[i][0] = 1

for j in range(1, len(dp[0])):
    dp[0][j] = dp[0][j-1] + 1

ans = dp[0][e-s]
for p in range(1, m):
    for q in range(1, e-s+1):
        dp[p][q] = dp[p-1][q] + dp[p][q-1]
    ans += dp[p][e-s]

print(ans)
