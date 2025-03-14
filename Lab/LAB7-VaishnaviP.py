def maxProfit(prices):
    total_num = len(prices)
    check = {}

    def using_dynamic(i, stock_present):
        if i >= total_num:
            return 0

        if (i, stock_present) in check:
            return check[(i, stock_present)]

        if stock_present == 1:
            sell_stock = prices[i] + using_dynamic(i + 2, False)
            cooldown_hold = using_dynamic(i + 1, True)
            max_profit = max(sell_stock, cooldown_hold)
        else:
            buy_stock = -prices[i] + using_dynamic(i + 1, True)
            cooldown_donothing = using_dynamic(i + 1, False)
            max_profit = max(buy_stock, cooldown_donothing)

        check[(i, stock_present)] = max_profit
        return max_profit
    
    return using_dynamic(0, False)

