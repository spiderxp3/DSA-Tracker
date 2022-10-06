arr = [1,5,5,11]
total = sum(arr)
n = len(arr)
def solve(arr,n,total):
    t = [[False for x in range(total+1)]for x in range(n+1)]
    for i in range(n+1):
        for j in range(total+1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True
            elif arr[i-1]<=total:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    return t[n][total]
if total%2!=0:
    print(False)
else:
    print(solve(arr,n,total//2))