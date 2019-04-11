/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
// version 3: BFS two queries
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        
        if (root == null) {
            return results;
        }
        
        List<TreeNode> Q1 = new ArrayList<TreeNode>();
        List<TreeNode> Q2 = new ArrayList<TreeNode>();
        
        Q1.add(root);
        while (Q1.size() != 0) {
            List<Integer> level = new ArrayList<Integer>();
            Q2.clear();
            for (int i = 0; i < Q1.size(); i++) {
                TreeNode node = Q1.get(i);
                level.add(node.val);
                if (node.left != null) {
                    Q2.add(node.left);
                }
                if (node.right != null) {
                    Q2.add(node.right);
                }
            }
            
            // swap q1 and q2
            List<TreeNode> temp = Q1;
            Q1 = Q2;
            Q2 = temp;
            
            results.add(level);
        }
        return results;
    }
}
