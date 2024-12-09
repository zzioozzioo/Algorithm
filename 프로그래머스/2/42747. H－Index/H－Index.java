import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations); // 오름차순 정렬

        for(int i=0; i<citations.length; i++) {
            int h = citations.length - i; // h: 해당 논문(i)보다 인용 횟수가 크거나 같은 논문 편수

            if(citations[i] >= h) {
                answer = h;
                break;
            }
        }

        return answer;
    }
}