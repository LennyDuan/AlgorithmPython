def change(amount: int, coins: list()) -> int:
    result = list()

    def getChange(amount, coins, index, current):
        if amount == 0:
            result.append(current)
            return
        else:
            for i in range(index, len(coins)):
                if amount < 0:
                    break
                getChange(amount - coins[i], coins, i, current + [coins[i]])

    getChange(amount, coins, 0 ,[])
    print(result)

    return len(result)


# change(3, [2])
# change(10, [10])
change(5, [1, 2, 5])
