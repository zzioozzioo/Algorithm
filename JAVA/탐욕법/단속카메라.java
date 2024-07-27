import java.util.Arrays;

class Solution {
    public int solution(int[][] routes) {

        // 진출 지점 기준으로 오름차순 정렬
        Arrays.sort(routes, (int[] r1, int[] r2) -> r1[1] - r2[1]);

        int answer = 1;
        int end = routes[0][1]; // 첫 번째 차량의 진출 지점으로 설정

        for(int i=1; i<routes.length; i++) {
            if(routes[i][0] > end) { // 진입 지점이 end를 벗어난 경우
                answer++;
                end = routes[i][1];
            }
        }

        return answer;
    }
}