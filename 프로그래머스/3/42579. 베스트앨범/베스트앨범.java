import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};

        // genreMap: 각 장르의 총 play 횟수 저장
        HashMap<String, Integer> genreMap = new HashMap<>();

        // 장르별 play 횟수 정리
        for(int i=0; i < genres.length; i++) {
            if(genreMap.containsKey(genres[i])) {
                genreMap.put(genres[i], genreMap.get(genres[i]) + plays[i]);
            } else {
                genreMap.put(genres[i], plays[i]);
            }
        }

        // 장르를 내림차순으로 정렬
        List<String> genresList = new ArrayList<>(genreMap.keySet());
        Collections.sort(genresList, (o1, o2) -> (genreMap.get(o2).compareTo(genreMap.get(o1))));

        // 한 장르 내에서 정렬
        List<Integer> answerList = new ArrayList<>();
        genresList.forEach(li -> {
            // playsMap: 장르별 노래 관리(key: 장르에 해당하는 인덱스, 재생 횟수)
            HashMap<Integer, Integer> playsMap = new HashMap<>();
            for(int i=0; i < genres.length; i++) {
                if(li.equals(genres[i])) {
                    playsMap.put(i, plays[i]);
                }
            }

            // 내림차순으로 정렬
            // playsList: playsMap의 key(장르에 해당하는 인덱스)만 가져와서 저장된 리스트
            List<Integer> playsList = new ArrayList<>(playsMap.keySet());
            // get(key) -> value(재생 횟수)를 기준으로 내림차순 정렬
            Collections.sort(playsList, (o1, o2) -> (playsMap.get(o2).compareTo(playsMap.get(o1))));

            // 베스트 앨범에 추가: 장르별로 가장 많이 play된 음악 2개씩 가져옴
            answerList.add(playsList.get(0));
            if(playsList.size() != 1) {
                answerList.add(playsList.get(1));
            }
        });

        // 결과를 배열로 변환
        answer = new int[answerList.size()];

        for(int index=0; index<answerList.size(); index++) {
            answer[index] = answerList.get(index);
        }

        return answer;
    }
}