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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if(root == null){ return res; }
        ArrayDeque<TreeNode> q = new ArrayDeque();
        q.addLast(root);
        while(!q.isEmpty()){
            int n = q.size();          
            List<Integer> temp = new ArrayList<>();
            
            for (int i = 0; i < n; i++) {
                TreeNode current = q.pollFirst();
                temp.add(current.val);
                
                if (current.left != null) {
                    q.addLast(current.left);
                }
                if (current.right != null) {
                    q.addLast(current.right);
                }
            }
            res.add(temp);
        }
        return res; 
    }
}