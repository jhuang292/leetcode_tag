class Solution {
    public int findCircleNum(int[][] M) {
        int n = M.length;
        if (n == 0) return 0;
        
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (M[i][i] == 0) continue;
            ans++;
            dfs(M, i, n);
        }
        return ans;
    }
    private void dfs(int[][] M, int cur, int n) {
        for (int i = 0; i < n; i++) {
            if (M[cur][i] == 0) continue;
            M[cur][i] = M[i][cur] = 0;
            dfs(M, i, n);
        }
    }
}
