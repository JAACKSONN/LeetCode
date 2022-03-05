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
    public void helper(TreeNode root, List<Integer> output){
        if(root == null) return;
        helper(root.left, output);
        output.add(root.val);
        helper(root.right, output);
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> output = new ArrayList<Integer>();
        helper(root, output);
        return output;
    }
}

