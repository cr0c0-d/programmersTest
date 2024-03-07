package me.croco.lv2;

import java.util.ArrayList;
import java.util.List;

/**
 * 240306
 * 코딩테스트 연습 > 연습문제 > 당구 연습
 * https://school.programmers.co.kr/learn/courses/30/lessons/169198
 *
 * 프로그래머스의 마스코트인 머쓱이는 최근 취미로 당구를 치기 시작했습니다.
 * 머쓱이는 손 대신 날개를 사용해야 해서 당구를 잘 못 칩니다.
 * 하지만 끈기가 강한 머쓱이는 열심히 노력해서 당구를 잘 치려고 당구 학원에 다니고 있습니다.
 * 오늘도 당구 학원에 나온 머쓱이에게 당구 선생님이"원쿠션"(당구에서 공을 쳐서 벽에 맞히는 걸 쿠션이라고 부르고, 벽에 한 번 맞힌 후 공에 맞히면 원쿠션이라고 부릅니다)
 * 연습을 하라면서 당구공의 위치가 담긴 리스트를 건네줬습니다.
 * 리스트에는 머쓱이가 맞춰야 하는 공들의 위치가 담겨있습니다.
 * 머쓱이는 리스트에 담긴 각 위치에 순서대로 공을 놓아가며 "원쿠션" 연습을 하면 됩니다.
 * 이때, 머쓱이는 항상 같은 위치에 공을 놓고 쳐서 리스트에 담긴 위치에 놓인 공을 맞춥니다.
 * 머쓱이와 달리 최근 취미로 알고리즘 문제를 풀기 시작한 당신은, 머쓱이가 친 공이 각각의 목표로한 공에 맞을 때까지 최소 얼마의 거리를 굴러가야 하는지가 궁금해졌습니다.
 * 당구대의 가로 길이 m, 세로 길이 n과 머쓱이가 쳐야 하는 공이 놓인 위치 좌표를 나타내는 두 정수 startX, startY, 그리고 매 회마다 목표로 해야하는 공들의 위치 좌표를 나타내는
 * 정수 쌍들이 들어있는 2차원 정수배열 balls가 주어집니다.
 * "원쿠션" 연습을 위해 머쓱이가 공을 적어도 벽에 한 번은 맞춘 후 목표 공에 맞힌다고 할 때, 각 회마다
 * 머쓱이가 친 공이 굴러간 거리의 최솟값의 제곱을 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
 * 단, 머쓱이가 친 공이 벽에 부딪힐 때 진행 방향은 항상 입사각과 반사각이 동일하며,
 * 만약 꼭짓점에 부딪힐 경우 진입 방향의 반대방향으로 공이 진행됩니다. 공의 크기는 무시하며,
 * 두 공의 좌표가 정확히 일치하는 경우에만 두 공이 서로 맞았다고 판단합니다.
 * 공이 목표 공에 맞기 전에 멈추는 경우는 없으며, 목표 공에 맞으면 바로 멈춘다고 가정합니다.
 */
public class Solution2_4_tmp {
    public static int[] solution(int m, int n, int startX, int startY, int[][] balls) {

        /**
         * * 문제 정리 * *
         *
         * 당구대 가로길이 m, 세로길이 n, 공 좌표 startX, startY, 목표 공 리스트 balls
         *
         * 항상 같은 위치에 공을 놓고, 리스트에 담긴 위치에 놓인 공을 맞춤
         * 시작 공 -> 벽 -> 각각의 공에 맞을 때까지 최소 얼마의 거리를 굴러가야 하는가?
         *
         * 공이 굴러간 거리의 최솟값의 제곱을 배열에 담아 return
         *
         */
        int[] answer = new int[balls.length];

        Points startP = new Points(startX, startY);

        //for(int[] ball : balls) {
        for(int i = 0; i < balls.length; i++) {

            Points tBall = new Points(balls[i][0], balls[i][1]);

            Double shortest = tBall.returnShortest(startP, tBall, startX, startY);

            answer[i] = (int) Math.pow(shortest, 2);
        }

        return answer;
    }
}
class Points {
    int x = 0;
    int y = 0;

    Points(int x, int y) {
        this.x = x;
        this.y = y;
    }

    Double getLength(Points p1, Points p2) {
        return Math.sqrt(Math.pow((p1.x - p2.x), 2) + Math.pow((p1.y - p2.y), 2));
    }
    Double getLengthBy3(Points p1, Points p2, Points wall) {
        return getLength(p1, wall) + getLength(p2, wall);
    }

    Double returnShortest(Points p1, Points p2, int width, int height) {
        int wallX = (p1.x + p2.x) / 2;
        int wallY = (p1.y + p2.y) / 2;


        Double shortest = getLengthBy3(p1, p2, new Points(0, wallY));

        List<Points> pList = new ArrayList<>();
        pList.add(new Points(width, wallY));
        pList.add(new Points(wallX, 0));
        pList.add(new Points(wallX, height));



        for(Points p : pList) {
            Double leng = getLengthBy3(p1, p2, p);
            if(leng < shortest) shortest = leng;
        }
        return shortest;
    }


}
