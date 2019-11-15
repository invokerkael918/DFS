import math


class MySolution:
    """
    @param n: An integer
    @return: a list of combination
    Input: 8
    Output: [[2,2,2],[2,4]]
    """

    def getFactors(self, n):
        # write your code here
        result = []
        self.dfs(n, 2, [], result)
        return result

    def dfs(self, n, start, path, result):

        if len(path) != 0:
            result.append(path[:] + [n])

        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                path.append(i)
                self.dfs(int(n / i), i, path, result)
                path.pop()


class Solution2:
    """
    @param n: An integer
    @return: a list of combination
    Input: 8
    Output: [[2,2,2],[2,4]]
    """

    def getFactors(self, n):
        # write your code here
        result = []
        self.dfs(n, 2, 0, [], result)
        return result

    def dfs(self, n, start, reminder, path, result):
        if path:
            path.append(int(reminder))
            result.append(path[:])
            path.pop()
        for i in range(start, int(math.sqrt(n)) + 1):
            if n % i == 0:
                reminder = n / i
                path.append(i)
                self.dfs(int(n / i), i, reminder, path, result)
                path.pop()
