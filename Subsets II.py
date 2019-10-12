class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        nums.sort()
        subsets = []
        index = 0
        self.dfs(nums, index, [], subsets)
        return subsets

    def dfs(self, nums, index, subset, subsets):

        subsets.append(list(subset))

        for i in range(index, len(nums)):
            # index为外层 , i 是内层，所以当 i > index时不再回溯，继续走外层
            if i > index and nums[i] == nums[i - 1]:
                continue

            subset.append(nums[i])
            self.dfs(nums, i + 1, subset, subsets)
            subset.pop()


if __name__ == '__main__':
    S = Solution().subsets([1, 2, 2])
    print(S)
