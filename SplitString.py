class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        result = []
        self.dfs(result, [], s)
        return result

    def dfs(self, result, path, s):
        if s == "":
            result.append(path[:])  # important: use path[:] to clone it
            return
        for i in range(2):
            if i + 1 <= len(s):
                path.append(s[:i + 1])
                self.dfs(result, path, s[i + 1:])
                path.pop()

