import java.util.Arrays;
import java.util.List;
import java.util.Collections;
import java.util.stream.Collectors;
class Solution {
    public int solution(int[] numbers) {
        
        List<Integer> intNumbers = Arrays.stream(numbers)
                           .boxed()
                           .collect(Collectors.toList());
        
        Collections.sort(intNumbers, Collections.reverseOrder());
        return intNumbers.get(0) * intNumbers.get(1);
    }
}