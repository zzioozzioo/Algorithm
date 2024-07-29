import java.util.*;

class Solution {
    public int solution(int N, int number) {

        // N: 사용할 숫자
        // number: 만들 숫자

        // countList: HashSet을 포함하고 있는 리스트
        List<Set<Integer>> countList = new ArrayList<>(); 
       
        // HashSet: N을 1~8개 사용해 만들 수 있는 모든 숫자 저장
        for(int i=0; i<9; i++) {
            countList.add(new HashSet<>());
        }

        countList.get(1).add(N); // N을 1개 사용해 만든 숫자는 N밖에 없음

        for(int i=2; i<9; i++) { // 1개 사용한 경우는 이미 처리했으니 2~8개 처리
            // 아까 생성한 HashSet 중 i번째를 가져와서 countSet이라고 함
            Set<Integer> countSet = countList.get(i);

            for(int j=1; j<=i; j++) {
                // preSet: countList에서 N을 j개 사용해 만든 숫자들
                // postSet: countList에서 N을 i-j개 사용해 만든 숫자들
                Set<Integer> preSet = countList.get(j);
                Set<Integer> postSet = countList.get(i-j);

                for(int preNum : preSet) {
                    for(int postNum : postSet) {
                        countSet.add(preNum + postNum); // 덧셈
                        countSet.add(preNum - postNum); // 뺄셈
                        countSet.add(preNum * postNum);  // 곱셈

                        if(preNum!=0 && postNum!=0) {
                            countSet.add(preNum / postNum); // 나눗셈
                        }
                    }
                }

                // N을 연속으로 i번 사용해 만든 숫자 추가
                countSet.add(Integer.parseInt(String.valueOf(N).repeat(i)));
            }

        }
        
        // HashSet을 돌며 number 탐색, 발견 즉시 return(사용한 개수가 가장 적은 것 추출)
        for(Set<Integer> sub : countList) {
            if(sub.contains(number)) {
                return countList.indexOf(sub);
            }
        }

        return -1;
    }
}