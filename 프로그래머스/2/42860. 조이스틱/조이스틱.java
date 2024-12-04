import java.util.*;

class Solution {
    public int solution(String name) {
        int answer = 0;
        int index; // 다음 값들을 확인할 때 사용
        int move = name.length()-1; // 좌우 움직임 수 체크

        for(int i=0; i<name.length(); i++) {
            // [상하 이동]
            // 'A'와'Z' 중에 어디에서 움직이는 게 가까운지 판별
            answer += Math.min(name.charAt(i)-'A', 'Z'-name.charAt(i)+1);

            index = i+1;

            // 연속되는 A 갯수 체크
            while(index < name.length() && name.charAt(index) == 'A') {
                index++;
            }

            // [좌우 이동]
            // 순서대로 가는 것, 뒤로 돌아가는 것 중 이동수가 적은 것을 선택
            move = Math.min(move, i*2 + name.length()-index);
            // 뒷부분을 먼저 입력하는 것이 더 빠른 경우도 고려(예: BBBBAAAAAAAB)
            move = Math.min(move, (name.length()-index)*2 + i);
            
        }

        return answer + move;
    }
}