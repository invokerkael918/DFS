class Solution:

    def kSumII(self, A, k, target):
        anslist = []
        self.dfs(A, k, target, 0, [], anslist)
        return anslist

    def dfs(self, A, k, target, index, onelist, anslist):
        if target == 0 and k == 0:
            anslist.append(onelist)
            return

        if len(A) == index or target < 0 or k < 0:
            return

        self.dfs(A, k, target, index + 1, onelist, anslist)

        onelist.append(A[index])
        self.dfs(A, k - 1, target - A[index], index + 1, onelist, anslist)
        onelist.pop()