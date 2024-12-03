import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;

        // 배열 오름차순 정렬
        Arrays.sort(lost);
        Arrays.sort(reserve);
        
        // Array to List
        List<Integer> lostList = Arrays.stream(lost).boxed().collect(Collectors.toList());
        List<Integer> reserveList = Arrays.stream(reserve).boxed().collect(Collectors.toList());
        List<Integer> newList = new ArrayList<>();

        // 중복 학생(여벌 가져왔지만 도난당한 학생) 제거 로직
        for (Integer i : lostList) {
            if (reserveList.contains(i)) {
                reserveList.remove(i);
            } else {
                newList.add(i);
            }
        }
        lostList = newList; // 중복 처리한 새로운 리스트를 lostList로 교체

        answer = n - lostList.size(); // answer: 체육복을 입을 수 있는 학생 수

        // 여벌 옷 나눠주기 로직
        for (int i=0; i<lostList.size(); i++) { // 도난당한 학생 수만큼 반복
            if (reserveList.isEmpty()) {
                break;
            }
            for (int j=0; j<reserveList.size(); j++) {
                if ((lostList.get(i)+1==reserveList.get(j)) || lostList.get(i)-1==reserveList.get(j)) {
                    answer++;
                    reserveList.remove(j);
                }
            }
            // if (lostList.get(i)-1 == reserveList.get(i)) {
            //     answer++;
            //     reserveList.remove(i);
            // } else if (lostList.get(i)+1 == reserveList.get(i)) {
            //     answer++;
            //     reserveList.remove(i);
            // }

        }
        return answer;
    }
}