import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {

        Queue<Integer> q = new LinkedList<>();

        int answer = 0;
        int sum = 0;
        
        for(int truck : truck_weights) {
            while(true) {
                if(q.isEmpty()) { // 다리가 비었을 경우

                    q.add(truck);
                    answer++;
                    sum += truck;
                    break;
                } else if(q.size() < bridge_length) { // 다리에 가득 차지 않은 경우
                    
                    if(sum+truck <= weight) { // 더 실을 수 있음
                        q.add(truck);
                        sum += truck;
                        answer++;
                        break;
                    } else { // 더 실을 수 없음
                        q.add(0);
                        answer++;
                    }
                } else if(q.size() == bridge_length) { // 다리가 가득 찬 경우
                    
                    sum -= q.poll();
                }
            }
        }

        answer += bridge_length;

        return answer;
    }
}