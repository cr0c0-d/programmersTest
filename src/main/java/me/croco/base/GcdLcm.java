package me.croco.base;


/**
 * 최대공약수(GCD, Greatest Common Divisor)
 * 최소공배수(LCM, Least common multiple)
 */
public class GcdLcm {

    /**
     * 최대공약수 - 재귀방식
     */

    public static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    /**
     * 최대공약수 - 반복문
     */
    public static int gcdIterative(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    /**
     * 최소공배수
     */
    public static int lcm(int a, int b) {
        int gcd = gcd(a, b);
        return a * b / gcd;
    }

}
