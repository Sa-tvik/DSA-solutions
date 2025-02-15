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
 class BSTIterator {
    private Stack<TreeNode> st = new Stack<>();
    private boolean reverse;
    BSTIterator(TreeNode root, boolean reverse) {
        this.reverse = reverse;
        push(root);
    }
    int next() {
        TreeNode top = st.pop();
        push(!reverse ? top.right : top.left);
        return top.val;
    }
    private void push(TreeNode root) {
        while (root != null) {
            st.push(root);
            root = !reverse ? root.left : root.right;
        }
    }
}

class Solution {
     public boolean findTarget(TreeNode root, int k) {
        BSTIterator leftItr = new BSTIterator(root, false);
        BSTIterator rightItr = new BSTIterator(root, true);

        int left = leftItr.next(), right = rightItr.next();
        while (left < right) {
            if (left + right == k) return true;
            if (left + right < k)
                left = leftItr.next();
            else
                right = rightItr.next();
        }
        return false;
    }
}