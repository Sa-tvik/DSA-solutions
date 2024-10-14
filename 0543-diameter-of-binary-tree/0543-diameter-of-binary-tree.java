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
            return new int[] {0,0};
        }
        int[] left = new int[2];
        int[] right = new int[2];
        left = maxDepth(root.left);
        int max2 = left[1];
        right = maxDepth(root.right);
        max2 = Math.max(max2, right[1]);
        
        return new int[] { 1 + Math.max(left[0], right[0]), 1 + Math.min(left[1],right[1]) };
    }
    public int diameterOfBinaryTree(TreeNode root) {
        int[] res = new int[2];
        res = maxDepth(root);
        return res[0]+res[1]-2;
    }
}