arr = [2,3,5,9,10]
n = len(arr)
ans = 6
t = [[False for x in range(ans+1)] for x in range(n+1)]
for i in range(n+1):
    for j in range(ans+1):
        if i == 0:
            t[i][j] = False
        if j == 0:
            t[i][j] = True
        elif arr[i-1]<= ans:
            t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
        else:
            t[i][j] = t[i-1][j]
print(t[n][ans])