from collections import deque


class Solution:
    def confusingNumberII(self, n: int) -> int:

        hashmap = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}  # Fixed mapping values

        q = deque()
        q.append(0)
        count = 0

        while q:
            curr_num = q.popleft()

            if curr_num != 0 and self.isconfusing(curr_num, hashmap):
                count += 1

            for key in hashmap.keys():
                new_num = curr_num * 10 + key
                if new_num != 0 and new_num <= n:
                    q.append(new_num)

        return count

    def isconfusing(self, num, hashmap):
        temp = num
        result = 0

        while num > 0:
            last_digit = num % 10
            result = result * 10 + hashmap[last_digit]
            num = num // 10

        return result != temp


# time complexity is O(5^d) where d is the number of digits
# space complexity is O(5^d)
