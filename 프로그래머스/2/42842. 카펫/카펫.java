class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];

        int area = brown + yellow; // 카펫의 넓이
        
        // 최소 3*3(width*height)
        for(int i=3; i<area; i++) {
            int j = area/i;

            if(area % i == 0 && j >= 3) {
                int width = Math.max(i, j); // 가로 >= 세로
                int height = Math.min(i, j);
                
                int center = (width-2) * (height-2);

                if(center == yellow) {
                    answer[0] = width;
                    answer[1] = height;

                    return answer;
                }
            }
        }
        return answer;
    }
}