class Solution {
    
        int answer = 0;

    public int solution(int[] numbers, int target) {
        int sum = 0;
        int depth = 0;

        DFS(numbers, depth, target, sum);

        return answer;
    }

    public void DFS(int[] numbers, int depth, int target, int sum) {
        if(depth == numbers.length) { // 마지막 노드까지 탐색한 경우
            if(target == sum) {
                answer++;
            }
        } else {
            DFS(numbers, depth+1, target, sum+numbers[depth]);
            DFS(numbers, depth+1, target, sum-numbers[depth]);
        }
    }
}