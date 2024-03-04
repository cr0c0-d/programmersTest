package me.croco.lv2;

import java.util.Arrays;
import java.util.List;

/* Lv2. 최댓값과 최솟값
 * 240304
 * https://school.programmers.co.kr/learn/courses/30/lessons/12939
 *
 * 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
 * 예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
 *
 * 제한 조건
 * s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.
 */
public class Solution2_2 {
    public static String solution(String s) {
        String answer = "";
        /*
        처음엔 이렇게 했는데 자바 버전때문에 제출 안 됨.

        List<Integer> list = Arrays.stream(s.split(" ")).map((string) -> Integer.parseInt(string)).collect(Collectors.toList());
        answer += list.stream().max(Integer::compare).orElse(0) + " " + list.stream().min(Integer::compare).orElse(0);
        */

        /** chatGPT가 수정해준 위 코드
         * List<Integer> list = Arrays.stream(s.split(" "))
         *                            .map(Integer::parseInt)
         *                            .collect(Collectors.toList());
         *
         * int max = list.stream().mapToInt(Integer::intValue).max().orElse(0);
         * int min = list.stream().mapToInt(Integer::intValue).min().orElse(0);
         *
         * String answer = max + " " + min;
         */

        // 새로 작성한 코드
        List<String> list = Arrays.asList(s.split(" "));

        answer += list.stream().mapToInt(Integer::parseInt).max().orElse(0)
                + " "
                + list.stream().mapToInt(Integer::parseInt).min().orElse(0);


        return answer;
    }
}
