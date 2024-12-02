class Solution {

    public int solution(int n, int[][] computers) {
        
        int answer = 0;
        boolean[] visited = new boolean[n]; // 방문한 컴퓨터 체크할 배열

        for(int i=0; i<n; i++) {
            if(!visited[i]) { // 아직 방문하지 않은 컴퓨터인 경우
                dfs(computers, visited, i); // 탐색
                answer++;
            }
        }

        return answer;
    }

    public void dfs(int[][] computers, boolean[] visited, int index) {
        visited[index] = true; // 현재 컴퓨터 방문 처리

        for(int j=0; j<computers.length; j++) {
            if(computers[index][j] == 1 && !visited[j]) { 
                // j번째 인덱스 컴퓨터가 현재 컴퓨터와 연결되어 있고, 아직 방문하지 않았다면
                dfs(computers, visited, j); // 그 컴퓨터(j번째 인덱스)로 이동하여 다시 탐색
            }
        }
    }
}