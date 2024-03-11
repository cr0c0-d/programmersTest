package me.croco.lv0;

public class Solution0_1 {
    /**
     * 문제 설명
     * 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
     *
     * 제한사항
     * 0 ≤ numbers의 원소 ≤ 1,000
     * 1 ≤ numbers의 길이 ≤ 100
     * 정답의 소수 부분이 .0 또는 .5인 경우만 입력으로 주어집니다.
     */
    class Solution0_01 {
        /**
         * 내가 쓴 답변
         */
        public double solution(int[] numbers) {
            double answer = 0;
            for(int i : numbers) {
                answer += i;
            }
            answer /= numbers.length;

            return answer;
        }
        /**
         * 이게 더 간단
         *
         * return Arrays.stream(numbers).average().orElse(0);
         */
    }


    /**
     * 문제 설명
     * 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
     *
     * 제한사항
     * 0 < n ≤ 1000
     */
    class Solution0_02 {
        /**
         * 내가 쓴 답변
         */
        public int solution(int n) {
            int answer = 0;
            for(int i = 0; i <= n; i += 2) {
                answer += i;
            }
            return answer;

            /**
             * 이게 더 간단
             *
             *         return IntStream.rangeClosed(0, n)
             *                 .filter(e -> e % 2 == 0)
             *                 .sum();
             */
        }
    }

    /**
     * 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
     *
     * 제한사항
     * 1 ≤ array의 길이 ≤ 100
     * 0 ≤ array의 원소 ≤ 1,000
     * 0 ≤ n ≤ 1,000
     */
    class Solution0_03 {
        /**
         * 내가 푼 코드
         */
        public int solution(int[] array, int n) {
            int answer = 0;
            for(int i : array) {
                if(i == n) answer += 1;
            }
            return answer;
        }

        /**
         * 이게 더 간단
         *
         * return (int) Arrays.stream(array)
         *                 .filter(e -> e == n)
         *                 .count();
         */
    }

    /**
     * 문제 설명
     * 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
     *
     * 제한사항
     * 1 ≤ my_string의 길이 ≤ 1,000
     */
    class Solution0_04 {
        /**
         * 내가 푼 코드
         */
        public String solution(String my_string) {
            String answer = "";
            for(String s : my_string.split("")) {
                answer = s + answer;
            }
            return answer;
        }

        /**
         * 이게 더 간단
         *
         * return new StringBuilder(myString).reverse().toString();
         */
    }

}
