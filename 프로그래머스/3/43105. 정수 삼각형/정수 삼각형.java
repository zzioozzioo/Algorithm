class Solution {
    public int solution(int[][] triangle) {
        int n = triangle.length;

        // 아래에서부터 거꾸로 올라가면서 값을 갱신
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j <= i; j++) {
                // 아래 층의 좌측과 우측 값 중 더 큰 값을 더함
                triangle[i][j] += Math.max(triangle[i + 1][j], triangle[i + 1][j + 1]);
            }
        }

        // 가장 꼭대기의 값이 최대값
        return triangle[0][0];
    }
}