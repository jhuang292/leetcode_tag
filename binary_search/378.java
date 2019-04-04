class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int l = matrix[0][0];
        int r = matrix[matrix.length-1][matrix[0].length-1];
        
        while (l < r) {
            int m = l + (r-l)/2;
            int total = 0;
            
            for (int i = 0; i < matrix.length; i++) {
                for (int j = 0; j < matrix[0].length; j++) {
                    if (matrix[i][j] <= m) 
                        total++;
                }
            }
            if (total >= k)
                r = m;
            else
                l = m+1;
        }
        return l;
    }
}
