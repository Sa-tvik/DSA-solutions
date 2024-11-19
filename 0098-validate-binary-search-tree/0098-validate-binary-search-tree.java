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
    public Long temp = Long.MIN_VALUE;
    public boolean flag = true;
    private void inOrder(TreeNode node) {
        if (node == null) {
            return;
        }
        if(flag == false){return;}
        inOrder(node.left);
        if(temp>=(long)node.val){ 
            flag = false;
            return;
        }else{
            temp = (long)node.val;
        }
        inOrder(node.right);
    }  
    public boolean isValidBST(TreeNode root) {
        inOrder(root);
        return flag; 
    }
}