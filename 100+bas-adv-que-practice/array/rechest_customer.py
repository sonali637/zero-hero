def maxWealth(account):
    max_wealth = 0
    for customer in account:
        max_wealth = max(max_wealth, sum(customer))
    return max_wealth
account = [[1,2,3],[5,9,8]]
print(maxWealth(account))    