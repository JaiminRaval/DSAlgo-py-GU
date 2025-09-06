# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def findNums(m, n):
            # finding mid point
            mid = (n + m) // 2
            # conditions as mentioned in comments
            if guess(mid) == 0:
                return mid
            if guess(mid) == -1:
                return findNums(m, mid - 1)
            else:
                return findNums(mid + 1, n)
        # recursion used
        return findNums(1, n)
