class Solution {
    public int solution(int a, int b) {
        int answer = 0;

        String aa = String.valueOf(a);
        String bb = String.valueOf(b);

        int aabb = Integer.valueOf(aa + bb);
        int aabb2 = 2 * a * b;

        if (aabb > aabb2 || aabb == aabb2)
            answer = aabb;

        if (aabb < aabb2)
            answer = aabb2;

        return answer;
    }
}