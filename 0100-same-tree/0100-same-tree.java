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
    private void inOrder(TreeNode node, List<Integer> res) {
        if (node == null) {
            return;
        }

        inOrder(node.left, res);
        res.add(node.val);
        inOrder(node.right, res);
    } 
    public boolean isSameTree(TreeNode p, TreeNode q) {
        List<Integer> res = new ArrayList<>();
        List<Integer> res1 = new ArrayList<>();

        inOrder(p, res);
        inOrder(q, res1);

        if(res.size()!=res1.size()){ return false; }

        for(int i = 0;i<res.size();i++){
            if(res1.get(i)!=res.get(i)){
                return false;
            }
        }
        return true;
    }
}