def find_coins_greedy(amount: int) -> dict:
    """
    Find the minimum number of coins needed to make change for a given amount
    Uses a greedy algorithm

    Returns a dictionary with the coin value as key and the number of coins as value
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount <= 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
        amount -= count * coin
    return result


def find_min_coins(amount: int) -> dict:
    """
    Find the minimum number of coins needed to make change for a given amount
    Uses dynamic programming

    Returns a dictionary with the coin value as key and the number of coins as value
    """
    coins = [1, 2, 5, 10, 25, 50]
    min_coins = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    # Reconstruct the result
    result = {}
    i = amount
    while i > 0:
        coin = coin_used[i]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        i -= coin

    return result


if __name__ == '__main__':
    amount = 123
    print(f'Amount: {amount}')
    print(f'Greedy algorithm: {find_coins_greedy(amount)}')
    print(f'Dynamic programming: {find_min_coins(amount)}')

    amount = 123123123
    print(f'Amount: {amount}')
    print(f'Greedy algorithm: {find_coins_greedy(amount)}')
    print(f'Dynamic programming: {find_min_coins(amount)}')