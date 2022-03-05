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
    public TreeNode helper(int[] nums, int lo, int hi){
        if(lo > hi) return null;
        int midpoint = (lo + hi) / 2;
        TreeNode root = new TreeNode(nums[midpoint]);
        root.left = helper(nums, lo, midpoint-1);
        root.right = helper(nums, midpoint+1, hi);
        return root;
    }
    public TreeNode sortedArrayToBST(int[] nums) {
        return helper(nums, 0, nums.length-1);
    }
}