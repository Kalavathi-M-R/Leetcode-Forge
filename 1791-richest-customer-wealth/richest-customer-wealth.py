class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealth = []
        sum = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                sum += accounts[i] [j]
            wealth.append(sum)
            sum = 0
        return max(wealth)