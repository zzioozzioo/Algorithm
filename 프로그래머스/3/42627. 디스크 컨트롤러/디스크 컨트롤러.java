import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int end = 0; // 수행되고 난 직후의 시간
        int index = 0; // jobs 배열의 인덱스
        int count = 0; // 수행된 요청 갯수
        
        Arrays.sort(jobs, (o1, o2) -> { // 요청 시간 오름차순 정렬
            return o1[0]-o2[0];
        });

        // 처리 시간 오름차순 정렬
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);

        while(count < jobs.length) {

            while(index < jobs.length && jobs[index][0] <= end) {
                pq.add(jobs[index++]);
            }

            if(pq.isEmpty()) {
                end = jobs[index][0];
            } else {
                int[] temp = pq.poll();
                answer += temp[1] + end - temp[0]; // 요청부터 종료까지 걸린 시간
                end += temp[1];
                count++;
            }
        }

        return (int)Math.floor(answer / jobs.length);
    }
}