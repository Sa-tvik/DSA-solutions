/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = maxDepth(root.left);
        if(left == -1){ return -1; }
        
        int right = maxDepth(root.right);
        if(right == -1){ return -1; }

        if (left == right || Math.abs(left - right) == 1) {
            return 1 + Math.max(left, right);
        }
        return -1;
    }

    public boolean isBalanced(TreeNode root) {
        int res = maxDepth(root);
        return (res != -1)?true:false;
    }
}