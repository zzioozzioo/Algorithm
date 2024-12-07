import java.util.ArrayList;

class Solution {

    static ArrayList<Integer> arr = new ArrayList<>(); // arr: 만들 수 있는 모든 숫자 조합 저장
    static boolean[] check = new boolean[7]; // numbers의 최대 길이=7

    public int solution(String numbers) {
        int answer = 0;

        // numbers 문자열에서 만들 수 있는 모든 조합 찾기
        for(int i=0; i<numbers.length(); i++) {
            dfs(numbers, "", i+1);
        }

        for(int i=0; i<arr.size(); i++) {
            if(isPrime(arr.get(i))) { // 리스트 i번째 요소가 소수이면
                answer++;
            }
        }

        return answer;
    }


    // 백트래킹
    static void dfs(String str, String temp, int m) {
        // str: 주어진 문자열 numbers
        // temp: 현재까지 선택된 문자들로 구성된 임시 문자열
        // m: 목표하는 숫자 조합의 길이

        // 조건 확인 후 숫자 조합 리스트에 추가
        if(temp.length() == m) { // 목표 길이에 도달?
            int num = Integer.parseInt(temp); // temp 문자열 -> 정수
            if(!arr.contains(num)) { // 중복 검사
                arr.add(num);
            }
        }

        // 모든 조합 탐색
        for(int i=0; i<str.length(); i++) {
            if(!check[i]) {
                check[i] = true; // '사용 중'으로 변경
                temp += str.charAt(i); // 해당 문자 temp에 추가
                dfs(str, temp, m); // 재귀 호출
                check[i] = false; // 다시 '사용 안 함'으로 초기화
                temp = temp.substring(0, temp.length()-1); 
                // 마지막 문자 제거 -> temp를 원래 상태로 복귀
            }
        }
    }


    // 소수 판별
    static boolean isPrime(int n) {
        if(n<2) {
            return false;
        }
        for(int i=2; i<=(int)Math.sqrt(n); i++) {
            if(n%i == 0) {
                return false;
            }
        }
        return true;
    }
}