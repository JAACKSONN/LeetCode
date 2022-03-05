public boolean hasPathSum(TreeNode root, int targetSum) {
    if(root==null) return false;

    targetSum = targetSum - root.val;

    if(root.left==null && root.right==null && targetSum==0) return true;

    if(root.left==null && root.right==null) return false;
    
    
    return hasPathSum(root.right,targetSum) || hasPathSum(root.left,targetSum);
    
}