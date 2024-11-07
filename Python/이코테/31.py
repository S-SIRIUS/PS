# 금광
def make_dp():
    for i in range(1, m):
        for j in range(0, n):
            if j==0:
                table[j][i] = max(table[j][i-1], table[j+1][i-1]) + table[j][i]
            elif j==n-1:
                table[j][i] = max(table[j-1][i-1], table[j][i-1]) + table[j][i]
            else:
                table[j][i] = max(table[j-1][i-1], table[j][i-1], table[j+1][i-1]) + table[j][i]
    maxi=-999
    for i in range(n):
        if maxi < table[i][m-1]:
            maxi = table[i][m-1]
    return maxi

T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    table = [[0]*(m) for _ in range(n)]
    temp_list = list(map(int, input().split()))
    for j in range(0, len(temp_list)):
        table[j//4][j%4] = temp_list[j]
    print(make_dp())
