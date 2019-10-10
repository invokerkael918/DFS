class Solution:
    """
    @param str: A string
    @return: all permutations
    """

    def stringPermutation2(self, str):
        chars = sorted(list(str))
        visited = [False] * len(chars)
        permutations = []
        self.dfs(chars, visited, [], permutations)
        return permutations

    def dfs(self, chars, visited, permutation, permutations):



        if len(chars) == len(permutation):
            permutations.append(''.join(permutation))
            return

        for i in range(len(chars)):
            if visited[i]:
                continue

            # a' a" b
            # => a' a" b => √
            # => a" a' b => x
            # 不能跳过一个a选下一个a
            if i > 0 and chars[i] == chars[i - 1] and not visited[i - 1]:
                continue

            # make changes
            visited[i] = True
            permutation.append(chars[i])

            # 找到所有 permutation 开头的排列
            # 找到所有 "a" 开头的
            self.dfs(chars, visited, permutation, permutations)

            # backtracking
            permutation.pop()
            visited[i] = False
if __name__ == '__main__':
    S = Solution().stringPermutation2('abb')
    print(S)