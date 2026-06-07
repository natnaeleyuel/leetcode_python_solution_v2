# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        root = None
        non_root = set(descriptions[i][1] for i in range(len(descriptions)))
        tree = defaultdict(TreeNode)

        for (p, c, il) in descriptions:
            if tree[p].val == 0:
                tree[p] = TreeNode(p)

            if tree[c].val == 0:
                tree[c] = TreeNode(c)

            if il == 1:
                tree[p].left = tree[c]
            else:
                tree[p].right = tree[c]

            if p not in non_root:
                root = tree[p]
        
        return root

