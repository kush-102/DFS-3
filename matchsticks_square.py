class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        sum = 0
        maxi = 0
        for num in matchsticks:
            sum += num
            maxi = max(maxi, num)
        if sum % 4 != 0:
            return False
        len_each_side = sum // 4
        if maxi > len_each_side:
            return False

        square = [0, 0, 0, 0]

        matchsticks.sort(reverse=True)
        return self.helper(matchsticks, 0, square, len_each_side)

    def helper(self, matchsticks, idx, square, len_each_side):
        # base case
        if idx == len(matchsticks):
            return True
        # logic
        for i in range(4):
            if square[i] + matchsticks[idx] > len_each_side:
                continue
            # if i > 0 and square[i] == square[i-1]:
            #     continue
            # action
            square[i] += matchsticks[idx]

            # Recurse
            if self.helper(matchsticks, idx + 1, square, len_each_side):
                return True

            # Backtrack
            square[i] -= matchsticks[idx]

        return False


# time complexity is O(4^n)
# space complexity is O(n)
