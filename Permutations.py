class MySolution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        permutations = []
        
        self.dfs(nums, [], permutations)
        return permutations

    def dfs(self, chars, permutation, permutations):
        if len(chars) == len(permutation):
            permutations.append(permutation[:])
            return

        for i in range(len(chars)):
            if chars[i] in permutation:
                continue

            permutation.append(chars[i])
            self.dfs(chars, permutation, permutations)
            permutation.pop()


# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


# Recursion
class Solution1:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        def _permute(result, temp, nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i + 1:])

        if nums is None:
            return []

        if nums is []:
            return [[]]

        result = []
        _permute(result, [], sorted(nums))
        return result


# Non-Recursion
class Solution2:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        if nums is None:
            return []
        if nums == []:
            return [[]]
        nums = sorted(nums)
        permutation = []
        stack = [-1]
        permutations = []
        while len(stack):
            index = stack.pop()
            index += 1
            while index < len(nums):
                if nums[index] not in permutation:
                    break
                index += 1
            else:
                if len(permutation):
                    permutation.pop()
                continue

            stack.append(index)
            stack.append(-1)
            permutation.append(nums[index])
            if len(permutation) == len(nums):
                permutations.append(list(permutation))
        return permutations


class MySolution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        result = []
        visited = [False] * len(nums)
        memo = {}
        self.dfs(nums, 0, visited, [], result)
        return result

    def dfs(self, nums, start, visited, path, result):

        if len(nums) == len(path):
            result.append(path[:])

        for i in range(len(visited)):
            if visited[i]:
                continue
            path.append(nums[i])
            visited[i] = True
            self.dfs(nums, start + 1, visited, path, result)
            path.pop()
            visited[i] = False
        return result