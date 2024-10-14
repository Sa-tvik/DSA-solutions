/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
   public int[] maxDepth(TreeNode root) {
        if (root == null) {
            return new int[] {0, 0};
        }
        
        int[] left = maxDepth(root.left);
        int[] right = maxDepth(root.right);
        
        int height = 1 + Math.max(left[0], right[0]);
        int diameter = Math.max(left[1], Math.max(right[1], left[0] + right[0]));
        
        return new int[] {height, diameter};
    }

    public int diameterOfBinaryTree(TreeNode root) {
        return maxDepth(root)[1];
    }
}