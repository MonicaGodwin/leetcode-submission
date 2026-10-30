class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            total = 0
            for num in account:
                total += num
            if total > max_wealth:
                max_wealth = total
        return max_wealth

