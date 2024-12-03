class Solution {
    public String solution(String number, int k) {
        String answer = "";

        int startIndex = 0;
        StringBuilder sb = new StringBuilder();

        // 각 구간별 max 탐색 로직
        for(int i=0; i<number.length()-k; i++) { // 만들어야 할 문자의 길이(k개가 제거될 때까지)만큼 반복
            char max = 0; // 최댓값 저장할 변수

            for(int j=startIndex; j<=k+i; j++) {
                if(max < number.charAt(j)) {
                    max = number.charAt(j);
                    startIndex = j+1; // max 다음 인덱스부터 다시 max 찾을 수 있도록 설정
                }
            }
            sb.append(max);
        }
        
        // StringBuilder -> String
        answer = sb.toString();

        return answer;
    }
}