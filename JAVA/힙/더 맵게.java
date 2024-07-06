import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {

        // 최소 힙(루트 노드: K) ?

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i : scoville) {
            pq.add(i); // pq에 scoville 원소 삽입
        }

        int answer = 0;
        while(true) {
            if(pq.peek() >= K) { // 모든 음식의 스코빌 지수가 K 이상
                break;
            }
            if(pq.size() <= 1) {
                return -1;
            }
            int first = pq.poll();
            int second = pq.poll();
            int scv = first + (second*2);
            answer++;
            pq.add(scv);
        }

        // while(pq.size() > 1 && pq.peek() <  K) {
        //     int first = pq.poll();
        //     int second = pq.poll();
        //     int scv = first + (second*2);
        //     answer++;
        //     pq.add(scv);
        // }

        return answer;
    }
}