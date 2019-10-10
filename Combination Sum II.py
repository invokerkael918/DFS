class MySolution2:
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """

    def combinationSum2(self, candidates, target):
        # write your code here
        candidates.sort()
        result = []
        visited = [0] * len(candidates)
        self.dfs(candidates, target, 0, [], visited, result)
        return result

    def dfs(self, candidates, target, index, combination, visited, result):

        if target == 0:
            result.append(combination[:])
            return
        for i in range(index, len(candidates)):
            if target > 0 and (i == 0 or candidates[i] != candidates[i - 1] or visited[i - 1] == 1):
                combination.append(candidates[i])
                visited[i] = 1
                self.dfs(candidates, target - candidates[i], i + 1, combination, visited, result)
                combination.pop()
                visited[i] = 0


class MySolution1:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum2(self, candidates, target):
        # write your code here
        candidates.sort()
        combinations = []
        self.dfs(candidates, target, 0, [], combinations)
        return combinations

    def dfs(self, candidates, target, index, combination, combinations):
        # 小于0说明此combination不成立，直接return
        if target < 0:
            return
        # 每次递归的target都不一样，减到等于0说明等于原始target，加入最后的combinations一定要加[:] 或 list(combination)
        # 并且需要检查combinations里面是否有重复的
        if target == 0 and combination not in combinations:
            combinations.append(combination[:])
        # 跟之前相反，因为每个数只能用一次，所以需要 i+1
        for i in range(index, len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i + 1, combination, combinations)
            combination.pop()


if __name__ == '__main__':
    S = MySolution2().combinationSum2([7, 1, 2, 5, 1, 6, 10], 8)
    print(S)
