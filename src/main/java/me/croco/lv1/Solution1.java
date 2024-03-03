package me.croco.lv1;

/**
 * 프로그래머스 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181833
 *
 * 정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.
 *
 * arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.
 */
class Solution {
    public int[][] solution(int n) {

        // 내가 제출한 답
        int[][] answer = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                answer[i][j] = i == j ? 1 : 0;
            }
        }
        return answer;

        /* 더 좋았을 답
        int[][] answer = new int[n][n];

        for (int i = 0; i < n; i++) {
            answer[i][i] = 1;
        }
        return answer;
         */
    }
}