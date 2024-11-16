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
    public int num = 0;
    public int ans = 0;
    private void inOrder(TreeNode node, int k) {
        if (node == null) {
            return;
        }
        inOrder(node.left, k);
        num++;
        if(k == num){
            ans = node.val;
            return;
        }
        inOrder(node.right, k);
    }  
    public int kthSmallest(TreeNode root, int k) {
        inOrder(root, k);
        return ans;
    }
}