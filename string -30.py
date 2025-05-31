def max_alternating_string(binary_string, worth):
    n = len(binary_string)
    keep = [0] * n

    for i in range(n):
        keep[i] = int(binary_string[i]) + worth[i]

    dp = [[0] * 2 for _ in range(n)]

    dp[0][int(binary_string[0])] = worth[0]

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1] + (binary_string[i] == '0') * worth[i], dp[i-1][0])
        dp[i][1] = max(dp[i-1][0] + (binary_string[i] == '1') * worth[i], dp[i-1][1])

    max_worth = max(dp[-1][0], dp[-1][1])
    total_worth = sum(worth)
    return total_worth - max_worth

# Input binary string
binary_string = input().strip()

# Input worth of each character
worth = list(map(int, input().strip().split()))

result = max_alternating_string(binary_string, worth)
print(result)
