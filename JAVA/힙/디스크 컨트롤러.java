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

        // 요청이 모두 수행될 때까지 반복
        while(count < jobs.length) {

            // 하나의 작업이 완료되는 시점(end)까지 들어온 모든 요청을 큐에 삽입
            while(index < jobs.length && jobs[index][0] <= end) {
                pq.add(jobs[index++]);
            }

            // 큐가 비어있다면 작업 완료(end) 이후에 다시 요청이 들어온다는 의미
            if(pq.isEmpty()) {
                end = jobs[index][0]; // end를 요청의 가장 처음으로 맞춰 줌
            
            // 작업이 끝나기 전(end 이전) 들어온 요청 중 가장 수행시간이 짧은 요청부터 수행
            } else {
                int[] temp = pq.poll(); // 하나씩 뽑아서 처리
                answer += temp[1] + end - temp[0]; // 요청부터 종료까지 걸린 시간
                end += temp[1];
                count++;
            }
        }

        return (int)Math.floor(answer / jobs.length);
    }
}