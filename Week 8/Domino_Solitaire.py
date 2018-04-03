n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dp = []
dp.append(abs(a[0]-b[0]))
#print(a,b)
if n > 1:
  dp.append(max(abs(a[0]-a[1]) + abs(b[0]-b[1]), abs(a[0]-b[0])+abs(a[1]-b[1])))
  while len(dp) != n:
    i = len(dp)
    dp.append(max(dp[i-1] + abs(a[i]-b[i]),dp[i-2] + abs(a[i-1]-a[i]) + abs(b[i-1]-b[i])))
    #print(dp[i])
  print(dp[n-1])
else:
  print(abs(a[0]-b[0]))  
