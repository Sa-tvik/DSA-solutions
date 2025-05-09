/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    private TreeNode helper(TreeNode node, TreeNode p, TreeNode q){
        if(node == null || node == p || node == q){ return node; }


        TreeNode left = helper(node.left,p,q);
        TreeNode right = helper(node.right,p,q);
        
        if(left!=null && right !=null){
            return node;
        }
        
        return (left!=null) ? left : right; 
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return helper(root, p, q);
    }
}