import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {};
        int num = 0;
        int value = 0;

        PriorityQueue<Integer> min = new PriorityQueue<>(); // 최소힙(오름차순)
        PriorityQueue<Integer> max = new PriorityQueue<>(Collections.reverseOrder()); // 최대힙(내림차순)

        for(int i=0; i<operations.length; i++) {
            if(operations[i].startsWith("I")) { // 삽입
                num = Integer.parseInt(operations[i].substring(2)); // 숫자만 남기기
                min.add(num);
                max.add(num);
            } else if(operations[i].startsWith("D")) { // 삭제
                if(min.isEmpty()) { // 빈 큐에서 삭제 연산 -> 무시
                    continue;
                }
                num = Integer.parseInt(operations[i].substring(2)); // 숫자만 남기기
                if(num == 1) { // 최댓값 삭제(max에서 삭제)
                    value = max.remove();
                    min.remove(value);
                } else { // 최솟값 삭제(min에서 삭제)
                    value = min.remove();
                    max.remove(value);
                }
            }
        } // 모든 연산 처리 끝

        if(min.isEmpty()) {
            answer = new int[]{0, 0};
        } else {
            answer = new int[]{max.peek(), min.peek()};
        }

        return answer;
    }
}