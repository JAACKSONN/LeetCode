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
    public boolean isSymmetricHelper(TreeNode left, TreeNode right){
        if(left == null && right == null) return true;
        else if (left == null || right == null) return false;
        return isSymmetricHelper(left.left, right.right) && isSymmetricHelper(left.right, right.left) && (left.val == right.val);
    }
    public boolean isSymmetric(TreeNode root) 
    {
       return isSymmetricHelper(root.left, root.right); 
    }
}