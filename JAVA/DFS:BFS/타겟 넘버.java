import java.util.ArrayList;

class Solution {
    
    int answer = 0;

    public int solution(int[] numbers, int target) {
        // DFS
        dfs(numbers, 0, target, 0);

        return answer;
    }

    public void dfs(int[] numbers, int depth, int target, int sum) {
        if(depth == numbers.length) { // 마지막 노드까지 탐색한 경우
            if(target == sum) answer++;
        } else {
            dfs(numbers, depth+1, target, sum+numbers[depth]);
            dfs(numbers, depth+1, target, sum-numbers[depth]);
        }
    }
}