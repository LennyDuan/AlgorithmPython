def change(amount: int, coins: list()) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for index in range(1, amount + 1):
            if index >= coin:
                dp[index] += dp[index - coin]

    print(dp)
    return dp[amount]

#
# #change(3, [2])
# change(10, [10])
change(5, [1, 2, 5])
