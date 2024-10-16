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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if(root == null){ return res; }
        ArrayDeque<TreeNode> q = new ArrayDeque();
        q.addLast(root);
        int j = 0;
        while(!q.isEmpty()){
            int n = q.size();          
            List<Integer> temp = new ArrayList<>();
            if(j%2!=0){
                for (int i = 0; i < n; i++) {
                    TreeNode current = q.pollLast();
                    temp.add(current.val);

                    if (current.right != null) {
                        q.addFirst(current.right);
                    }
                    if (current.left != null) {
                        q.addFirst(current.left);
                    }
                }
            }else{
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
            }
            j++;
            res.add(temp);
        }
        return res; 
    }
}