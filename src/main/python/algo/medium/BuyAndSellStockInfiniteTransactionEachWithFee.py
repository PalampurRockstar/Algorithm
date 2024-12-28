# Best Time to Buy and Sell Stock with Transaction Fee
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

def solve(arr, fee):
    sellingAgentProfit = 0
    if len(arr) == 0: return 0
    buyingAgentProfit = -arr[0]
    for element in arr[1:]:
        newBuyingAgentProfit = max(buyingAgentProfit, sellingAgentProfit - element)
        newSellingAgentProfit = max(sellingAgentProfit, buyingAgentProfit + element - fee)
        buyingAgentProfit = newBuyingAgentProfit
        sellingAgentProfit = newSellingAgentProfit
    return sellingAgentProfit


# buying : -e
# selling :+e
# buying agent  : I am buying better or selling agent should also buy
# selling agent : I am selling better or buying agent should also sell & pay fee


# leet code test
assert solve([0, 5, 7, 10, 6, 8, 12, 10, 12, 10, 13, 15], 3) == 13
assert solve([1, 3, 7, 5, 10, 3], 3) == 6
assert solve([1, 3, 2, 8, 4, 9], 2) == 8
assert solve([9, 8, 7, 1, 2], 3) == 0
assert solve([1], 0) == 0

