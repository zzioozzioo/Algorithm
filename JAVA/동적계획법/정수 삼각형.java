// 아래 -> 위
class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;

        for(int i=triangle.length-2; i>=0; i--) { // 아래층->위층, 밑에서 두 번째 층에서 시작
            for(int j=0; j<=i; j++) { // 각 층의 모든 요소에 대해 반복

                // triangle[i][j] = 
                // (triangle[i+1][j] < triangle[i+1][j+1]) ? 
                // triangle[i+1][j+1] : triangle[i+1][j];

                triangle[i][j] += Math.max(triangle[i+1][j], triangle[i+1][j+1]);
            }
        }
    
        answer = triangle[0][0];

        return answer;
    }
}

// 위 -> 아래
// class Solution {
//     public int solution(int[][] triangle) {
//         int answer = 0;
//         int height = triangle.length;
//         int[][] dp = new int[height][height];

//         // 0번째 인덱스 초기 세팅
//         dp[0][0] = triangle[0][0];
//         for(int i=1; i<height; i++) {
//             dp[i][0] = dp[i-1][0] + triangle[i][0];
//         }

//         for(int i=1; i<height; i++) {
//             for(int j=1; j<triangle[i].length; j++) {
//                 dp[i][j] = Math.max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j]);
//             }
//         }

//         for(int i=0; i<height; i++) {
//             answer = Math.max(dp[height-1][i], answer);
//         }
        
//         return answer;
//     }
// }