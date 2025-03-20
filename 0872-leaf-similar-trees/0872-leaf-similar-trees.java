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
    private void inorder(TreeNode node, List<Integer> res) {
        if (node == null) {
            return;
        }
        if(node.left == null && node.right == null){ res.add(node.val); }
        inorder(node.left, res);
        inorder(node.right, res);
    }  
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> res1 = new ArrayList<>();
        List<Integer> res2 = new ArrayList<>();

        inorder(root1, res1);
        inorder(root2, res2);
        if(res1.size()!=res2.size()){return false;}
        
        return res1.equals(res2);
    }
}