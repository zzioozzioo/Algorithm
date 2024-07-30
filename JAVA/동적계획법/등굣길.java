class Solution {
    public int solution(int m, int n, int[][] puddles) {

        int mod = 1_000_000_007;
        int[][] dp = new int[n+1][m+1]; // 시작점이 (1,1)이기 때문에 각 인덱스에 +1

        for(int[] i : puddles) {
            dp[i[1]][i[0]] = -1; // 웅덩이는 -1으로 설정(행, 열 순서 잘 고려)
        }
        dp[1][1] = 1;
        for(int i=1; i<n+1; i++) {
            for(int j=1; j<m+1; j++) {
                if(dp[i][j] == -1) { // 웅덩이인 경우
                    continue; // 패스
                }
                if(dp[i-1][j] > 0) { // 위쪽 값이 유효하면
                    dp[i][j] = (dp[i][j] + dp[i-1][j]) % mod; // 위쪽 값 더해주기
                }
                if(dp[i][j-1] > 0) {
                    dp[i][j] = (dp[i][j] + dp[i][j-1]) % mod; // 왼쪽 값 더해주기
                }
            }
        }

        return dp[n][m]; // 최종값 리턴
    }
}