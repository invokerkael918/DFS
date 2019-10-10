class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

    def combinationSum(self, candidates, target):
        # write your code here
        combinations = []
        self.dfs(candidates, target, 0, [], combinations)
        return combinations

    def dfs(self, candidates, target, index, combination, combinations):
        # 小于0说明此combination不成立，直接return
        if target < 0:
            return
        # 每次递归的target都不一样，减到等于0说明等于原始target，加入最后的combinations一定要加[:] 或 list(combination)
        if target == 0:
            combinations.append(combination[:])
        # 因为每个数可以用多次，所以没必要写 i+1
        for i in range(index, len(candidates)):
            combination.append(candidates[i])
            self.dfs(candidates, target - candidates[i], i, combination, combinations)
            combination.pop()


if __name__ == '__main__':
    S = Solution().combinationSum([2, 3, 6, 7], 7)
    print(S)
