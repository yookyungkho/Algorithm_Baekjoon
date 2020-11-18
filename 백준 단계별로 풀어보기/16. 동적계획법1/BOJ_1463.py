n = int(input())
if n == 1:
    print(0)
elif n<=3:
    print(1)

#예를들어 30은 3으로 나눈 후 10의 연산횟수를 더하기만 하면 된다
#마찬가지로 10은 1을 뺀 후 9의 최소 연산횟수를 더하기만 하면 된다
#이 규칙을 생각해보면 1을 빼거나(2or3으로 나누어 떨어지지 않을때)
#2 or 3으로 나눴을때의 dp가 가장 작은 연산을 택하면 된다

else:
    dp = [0]*(n+1) #1부터 최소 연산횟수 저장
    dp[2] = 1
    dp[3] = 1
    for i in range(4,n+1):
        dp[i] = dp[i-1] + 1
        if i%3 == 0: #3으로 나누어 떨어지는 경우는 더 작은 경우의 수를 고려해야한다
            dp[i] = min(dp[i], dp[i//3]+1)
        if i%2 == 0: #2로 나누어 떨어질때도 마찬가지(2와 3 동시에 나누어 떨어지는 경우도 고려)
            dp[i] = min(dp[i], dp[i//2]+1)

    print(dp[n])