class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        if len(nums) == 0:
            return [[]]
        nums.sort()
        result = []
        visit = [False] * len(nums)
        self.dfs(nums, visit, [], result)
        return result

    def dfs(self, nums, visit, path, result):

        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if visit[i] == True:
                continue
            if i - 1 >= 0 and visit[i - 1] == True and nums[i] == nums[i - 1]:
                continue
            visit[i] = True
            path.append(nums[i])
            self.dfs(nums, visit, path, result)
            path.pop()
            visit[i] = False
