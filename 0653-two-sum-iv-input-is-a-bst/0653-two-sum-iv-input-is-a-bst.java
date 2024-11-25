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
    public boolean findTarget(TreeNode root, int k) {
        List<Integer> res = new ArrayList<>();
        // if(res.si)
        inOrder(root, res);
        int j = res.size()-1;
        int i = 0;
        while(i<j){
            int sum = res.get(i) + res.get(j);
            if(sum == k){
                return true;
            }
            if(sum<k){
                i++;
            }else if(sum>k){
                j--;
            }
        }
        return false;
    }
}