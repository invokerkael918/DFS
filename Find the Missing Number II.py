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
        if len(result) != 0:
            # result 为所有可行方案，只需要其中一个
            return
        if start == len(s):
            # 当start到了最后的位置就证明此方案可行，所以加入result
            result.append(path[:])
        for i in range(1, 3):
            # 一次最多取两位
            if i + start > len(s):
                # 保证不越界
                break
            subString = s[start:start + i]
            # 取subString， 从start到+1 或者 +2
            if i == 2 and subString[0] == "0":
                # 如果在取两位数， 第一位不能为0，如果是就跳过
                continue
            intSubString = int(subString)
            if intSubString > n or intSubString == 0:
                # 如果取的数比n大，或者是0，直接跳过
                continue
            if intSubString in visited:
                # 如果取的数已经被取过，证明此方案有重复数字出现，直接跳过
                continue
            path.append(intSubString)
            visited.add(intSubString)

            self.dfs(n, s, start + i, path, result, visited)
            path.pop()
            visited.remove(intSubString)
