package me.croco.lv0;

import java.util.Arrays;

public class Solution0_2 {
    public int[] solution(int[] arr) {
        int[] answer = {};
        String str = "";

        for(int a : arr) {
            for(int i = 0; i < a; i++) {
                str += a + " ";
            }
        }
        answer = Arrays.stream(str.split(" ")).mapToInt(Integer::parseInt).toArray();
        return answer;
    }

    /**
     * 간단
     *
     * return Arrays.stream(arr).boxed().flatMap(num -> Collections.nCopies(num, num).stream()).collect(Collectors.toList());
     */
}
