package me.croco.lv2;

/**
 * 240306
 * 코딩테스트 연습 > 스택/큐 > 올바른 괄호
 * https://school.programmers.co.kr/learn/courses/30/lessons/12909
 *
 * 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어
 *
 * "()()" 또는 "(())()" 는 올바른 괄호입니다.
 * ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
 * '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
 *
 * 제한사항
 * 문자열 s의 길이 : 100,000 이하의 자연수
 * 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.
 */
public class Solution2_3 {
    public static boolean solution(String s) {
        String[] arr = s.split("");
        int left = 0;

        for(String st : arr) {
            if(st.equals("(")) {
                left++;
            } else {
                left--;
            }
            if (left < 0) {
                return false;
            }
        }

        if(left != 0) return false;

        return true;
    }
}
