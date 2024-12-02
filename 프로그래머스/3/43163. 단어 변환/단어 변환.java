class Solution {

    static int answer = 0;
    static boolean[] visited;

    public int solution(String begin, String target, String[] words) {

        visited = new boolean[words.length];

        

        dfs(begin, target, words, answer);

        return answer;
    }

    public void dfs(String begin, String target, String[] words, int count) {

        if(begin.equals(target)) { // 찾은 경우
            answer = count;
            return;
        }

        for(int i=0; i<words.length; i++) {

            if(visited[i]) { // 이미 방문한 경우: 
                continue;
            }

            // 알파벳 한 개 차이나는 단어 찾기
            int k = 0; 
            for(int j=0; j<begin.length(); j++) {

                if(begin.charAt(j) == words[i].charAt(j)) {
                    k++;
                }

                if(k == begin.length()-1) { // 알파벳 한 개 차이 나는 경우
                    visited[i] = true;
                    dfs(words[i], target, words, count+1);
                    visited[i] = false;
                }

            }
        }
    }
}