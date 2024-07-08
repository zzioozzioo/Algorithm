import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        StringBuffer answer = new StringBuffer();
        String[] arr = new String[numbers.length];

        // numbers 정수 배열 -> String 배열로 변환
        for(int i=0; i<numbers.length; i++) {
            arr[i] = String.valueOf(numbers[i]);
        }
        
        Arrays.sort(arr, (o1, o2) -> (o2+o1).compareTo(o1+o2));

        if(arr[0].equals("0")) {
            return "0";
        }

        for(String num : arr) {
            answer.append(num);
        }

        return answer.toString();
    }
}