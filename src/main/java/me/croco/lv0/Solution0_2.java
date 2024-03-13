package me.croco.lv0;

import java.util.Arrays;
import java.util.stream.IntStream;

public class Solution0_2 {
    public int[] solution0_01(int[] arr) {
        int[] answer = {};
        String str = "";

        for(int a : arr) {
            for(int i = 0; i < a; i++) {
                str += a + " ";
            }
        }
        answer = Arrays.stream(str.split(" ")).mapToInt(Integer::parseInt).toArray();
        return answer;

        /**
         * 간단
         *
         * return Arrays.stream(arr).boxed().flatMap(num -> Collections.nCopies(num, num).stream()).collect(Collectors.toList());
         */
    }



    /**
     * 어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.
     *
     * 제한사항
     * 1 ≤ n ≤ 10
     * 1 ≤ t ≤ 15
     */
    public int solution0_02(int n, int t) {

        return (int) (n * Math.pow(2, t));

        /**
         * public int solution(int n, int t) {
         * int answer = 0;
         *
         * answer = n << t;
         *
         * return answer;
         * }
         */
    }

}
