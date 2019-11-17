class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """

    def findMissing2(self, n, string):
        path, result = [], []
        visited = set()
        self.dfs(n, string, 0, path, result, visited)
        total = (n * (n + 1)) // 2
        return total - sum(result[0])

    def dfs(self, n, s, start, path, result, visited):
        if start == len(s):
            result.append(path[:])
        for i in range(1, 3):
            if i + start > len(s):
                break
            subString = s[start:start + i]
            if i == 2 and subString[0] == "0":
                continue
            intSubString = int(subString)
            if intSubString > n or intSubString == 0:
                continue
            if intSubString in visited:
                continue
            path.append(intSubString)
            visited.add(intSubString)

            self.dfs(n, s, start + i, path, result, visited)
            path.pop()
            visited.remove(intSubString)
