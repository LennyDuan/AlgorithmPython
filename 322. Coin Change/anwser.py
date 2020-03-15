def coinChange(coins: list(), amount: int) -> int:
    max = float('inf')
    results = [max] * (amount + 1)
    results[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            results[i] = min(results[i], results[i - coin] + 1)

    numbs = results[amount] if results[amount] != max else -1
    return numbs


# Output: 3
# Explanation: 11 = 5 + 5 + 1
coinChange([1, 2, 5], 11)

# Output: -1
coinChange([2], 3)
