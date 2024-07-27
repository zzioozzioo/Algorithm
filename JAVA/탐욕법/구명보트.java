import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;

        // 가장 가벼운, 무거운 사람 인덱스
        int lightest = 0; 
        int heaviest = people.length-1;

        // 오름차순 정렬
        Arrays.sort(people);

        while(lightest <= heaviest) {
            if(people[lightest]+people[heaviest] <= limit) { // 두 명 같이 태운 경우
                lightest++; // 가장 가벼운 사람 태우기
            }
            heaviest--; // 가장 무거운 사람 태우기(if 조건과 상관없이 항상 태워짐)
            answer++; // 보트 사용 카운트 증가
        }

        return answer;
    }
}