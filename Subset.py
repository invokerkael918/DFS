class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        nums.sort()
        subsets = []
        index = 0
        self.dfs(nums,index,[],subsets)
        return subsets

    def dfs(self,nums,index,subset,subsets):
        print(subset)
        subsets.append(list(subset))

        for i in range(index,len(nums)):
            subset.append(nums[i])
            self.dfs(nums,i+1,subset,subsets)
            subset.pop()
if __name__ == '__main__':
    S = Solution().subsets([1,2,3])
    print(S)