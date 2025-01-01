import java.util.*;

class Solution {
    public int[] solution(int[] prices) {

        int[] answer = new int[prices.length];
        
        Queue<Integer> q = new LinkedList<>();
        for(int i=0; i<prices.length; i++) {
            q.add(prices[i]);
        }
        // 아래와 동일
        // for(int i : prices) {
        //     q.add(i);
        // }

        int index = 0;

        while(!q.isEmpty()) {

            int currentPrice = q.poll();
            int start = prices.length-q.size();
            for(int i=start; i<prices.length; i++) {
                if(q.size() == 0) { // 맨 마지막 요소(하나밖에 안 남았을 때)인 경우
                    answer[index] = 0;
                    break;
                }
                if(currentPrice > prices[i]) { // 가격 떨어짐
                    answer[index]++;
                    break;
                } else { // 가격 유지 or 상승
                    answer[index]++;
                }
            }
            index++;
        }

        return answer;
    }
}