class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """

    def combine(self, n, k):
        # write your code here
        result = []
        self.dfs(n, k, 1, [], result)
        return result

    def dfs(self, n, k, start, path, result):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            if i in path:
                continue
            path.append(i)
            self.dfs(n, k, i, path, result)
            path.pop()
