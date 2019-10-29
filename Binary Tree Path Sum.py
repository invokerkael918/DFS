class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        result = []
        path = []
        self.dfs(root,target,result,path)
        return result

    def dfs(self,node,target,result,path):
        if node is None:
            return
        path.append(node.val)
        if node.left is None and node.right is None and target == node.val:
            result.append(path[:])
        self.dfs(node.left,target-node.val,result,path)
        self.dfs(node.right,target-node.val,result,path)
        path.pop()