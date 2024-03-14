package me.croco.lv0;

/**
 * 240314
 * 코딩테스트 입문 > 분수의 덧셈
 * https://school.programmers.co.kr/learn/courses/30/lessons/120808
 *
 * 문제 설명
 * 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
 * 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
 *
 * 제한사항
 * 0 <numer1, denom1, numer2, denom2 < 1,000
 */
public class Solution0_4 {

    // 최대공약수, 최소공배수 이용해서 풀었음
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int gcd = gcd(denom1, denom2);

        int numer3 = (numer1 * denom2 + numer2 * denom1) / gcd;
        int denom3 = denom1 * denom2 / gcd;

        int gcd2 = gcd(numer3, denom3);

        int[] answer = {numer3 / gcd2, denom3 / gcd2};
        return answer;
    }

    public int gcd(int a, int b) {
        if(b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }


    /**
     * 참고할만한 풀이
     *
     * public int[] solution(int denum1, int num1, int denum2, int num2) {
     *         int mother = num1 * num2;
     *         int son1 = num1 * denum2;
     *         int son2 = num2 * denum1;
     *         int totalSon = son1 + son2;
     *         for(int i = mother; i >= 1; i--){
     *             if(totalSon % i == 0 && mother % i == 0){
     *                 totalSon /= i;
     *                 mother /= i;
     *             }
     *         }
     *         int[] answer = {totalSon, mother};
     *         return answer;
     *     }
     */
}
