import java.util.Arrays;

class Solution {

    // Union 연산(집합 합치기)
    public static void union(int []parent, int a, int b) {

        int parentA = find(parent, a);
        int parentB = find(parent, b);

        if(parentA < parentB) {
            parent[parentB] = parentA;
        } else {
            parent[parentA] = parentB;
        }
    } 

    // Find 연산(부모 조회)
    public static int find(int []parent, int i) {

        if(parent[i] == i) { // 자기 자신이 부모
            return i;
        }
        return find(parent, parent[i]);
        
    }

    public int solution(int n, int[][] costs) {

        // n: 섬의 개수
        // costs: 다리가 연결되는 두 섬의 번호, 다리 건설 비용

        int answer = 0;
        
        // 크루스칼 알고리즘 사용하기 위해 가중치 기준 오름차순 정렬
        Arrays.sort(costs, (int[] c1, int[] c2) -> c1[2]-c2[2]);

        int []parent = new int[n]; // 초기: 섬 개수만큼 부모 존재(자기자신)
        for(int i=0; i<n; i++) {
            parent[i] = i;
        }

        // 모든 간선을 지나며 사이클이 형성되는지 파악
        for(int i=0; i<costs.length; i++) {
            if(find(parent, costs[i][0]) != find(parent, costs[i][1])) { // 사이클 판단
                answer += costs[i][2];
                union(parent, costs[i][0], costs[i][1]);
            }
        }
        
        return answer;
    }
}