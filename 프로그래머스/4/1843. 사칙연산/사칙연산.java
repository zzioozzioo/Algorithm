import java.util.ArrayList;

class Solution {

    private int numbers[]; // 숫자 기록할 배열
    private String operations[]; // 연산자 기록할 배열
    private int dp[][][]; // [최소 or 최대][범위의 시작][범위의 끝] -> 범위의 최소 혹은 최댓값

    public int solution(String arr[]) {
        // int answer = -1;

        // // 숫자 개수 = Math.ceil((double)arr.length/2)
        // // 연산자 개수 = 괄호 개수 = 숫자 개수-1

        // int numCount = (int)Math.ceil((double)arr.length/2);

        // // 그때그때 정수로 변환해서 사용하는 것 vs 한번에 정수로 변환해서 리스트에 저장해 사용하는 것
        // // 뭐가 좋을까???
        // ArrayList<Integer> numList = new ArrayList<>(); // 숫자 저장할 정수 리스트        
        // for(int i=0; i<arr.length; i=i+2) {
        //     numList.add(Integer.parseInt(arr[i]));
        // }
        

        // return answer;

        int n = arr.length / 2;

        dp = new int[2][200][200]; 
        for (int i = 0; i < n + 1; i++) {
            for (int j = 0; j < n + 1; j++) {

                // dp[0]은 최댓값, dp[1]은 최솟값
                dp[0][i][j] = Integer.MIN_VALUE;
                dp[1][i][j] = Integer.MAX_VALUE;
            }
        }

        numbers = new int[n + 1]; // 숫자 개수 = n+1
        operations = new String[n]; // 연산자 개수 = n

        for (int i = 0; i < arr.length; i++) {
            if (i % 2 == 0) { // 짝수 인덱스: 숫자 기록
                numbers[i / 2] = Integer.parseInt(arr[i]);
                continue;
            } // 홀수 인덱스: 연산자 기록
            operations[i / 2] = arr[i];
        }

        return calculate(0, 0, n);
    }

    // 최대, 최솟값 계산
    private int calculate(int flag, int start, int end) {

        // start == end: 숫자 하나만 선택됨 -> 자기 자신 리턴
        if(start == end) {
            dp[flag][start][end] = numbers[start];
            return dp[flag][start][end];
        }

        // 이미 방문해서 계산했던 경우, 기존에 계산된 값 사용
        if(visited(flag, start, end)) { // visited가 TRUE이면 이미 방문한 것
            return dp[flag][start][end];
        }

        // 방문 체크
        // dp[flag][start][end] = 0;

        int result = flag == 0 ? Integer.MIN_VALUE : Integer.MAX_VALUE;

        // 최댓값을 구해야 할 때: flag = 0
        if(flag == 0) {
            for(int i = start; i < end; i++) {
                if(operations[i].equals("-")) { // a - b

                    // a - b가 최댓값이 되는 조건: a는 최댓값, b는 최솟값 
                    result = Math.max(
                        result, calculate(0, start, i)-calculate(1, i+1, end));
                    continue;
                } // a + b
                // a + b가 최댓값이 되는 조건: a, b 둘 다 최댓값
                result = Math.max(
                    result, calculate(0, start, i)+calculate(0, i+1, end));
            }
        }

        // 최솟값을 구해야 할 때: flag = 1
        if(flag == 1) {
            for(int i = start; i < end; i++) {
                if(operations[i].equals("-")) { // -(a - b)

                    // -(a - b)가 최댓값이 되는 조건: a는 최솟값, b는 최댓값
                    result = Math.min(
                        result, calculate(1, start, i)-calculate(0, i+1, end));
                        continue;
                } // -(a + b)
                // -(a + b)가 최댓값이 되는 조건: a, b 둘 다 최솟값
                result = Math.min(
                        result, calculate(1, start, i)+calculate(1, i+1, end));
            }
            
        }

        dp[flag][start][end] = result;
        return dp[flag][start][end];
    }

    private boolean visited(int flag, int start, int end) {

        // (현재값 != 초기값) 이면 이미 방문한 것
        // flag = 0일 때는 초기값이 Integer.MIN_VALUE;
        // flag = 1일 때는 초기값이 Integer.MAX_VALUE;        
        return dp[flag][start][end] != Integer.MIN_VALUE &&
                dp[flag][start][end] != Integer.MAX_VALUE;
    }

}