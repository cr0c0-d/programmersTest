package me.croco.lv2;


import java.awt.print.Book;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 240309
 * 코딩테스트 연습 > 연습문제 > 호텔 대실
 * https://school.programmers.co.kr/learn/courses/30/lessons/155651
 *
 * 문제 설명
 * 호텔을 운영 중인 코니는 최소한의 객실만을 사용하여 예약 손님들을 받으려고 합니다.
 * 한 번 사용한 객실은 퇴실 시간을 기준으로 10분간 청소를 하고 다음 손님들이 사용할 수 있습니다.
 * 예약 시각이 문자열 형태로 담긴 2차원 배열 book_time이 매개변수로 주어질 때,
 * 코니에게 필요한 최소 객실의 수를 return 하는 solution 함수를 완성해주세요.
 *
 * 제한사항
 * 1 ≤ book_time의 길이 ≤ 1,000
     * book_time[i]는 ["HH:MM", "HH:MM"]의 형태로 이루어진 배열입니다
         * [대실 시작 시각, 대실 종료 시각] 형태입니다.
     * 시각은 HH:MM 형태로 24시간 표기법을 따르며, "00:00" 부터 "23:59" 까지로 주어집니다.
         * 예약 시각이 자정을 넘어가는 경우는 없습니다.
         * 시작 시각은 항상 종료 시각보다 빠릅니다
 *
 * 입출력 예
 * book_time	                                                                                             result
 * [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]	 3
 * [["09:10", "10:10"], ["10:20", "12:20"]]	                                                              1
 * [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]	                                            3
 *
 */
public class Solution2_6 {
    public int solution(String[][] book_time) {
        int answer = 0;

        List<BookInfo> list = new ArrayList<>();


        for(String[] info : book_time) {
            list.add(new BookInfo(info));
        }

        list.sort((b1,b2) -> b1.start == b2.start ? b1.end - b2.end : b1.start - b2.start);

        int now = list.get(0).start;
        int count = 0;
        int occupied = 0;

        while(count != list.size()) {

            for(int i = 0; i < count; i++) {
                if (now == list.get(i).end){
                    occupied--;
                }
            }
            for(int i = count; i < list.size(); i++) {
                if (now == list.get(i).start) {
                    count++;
                    occupied++;
                }
            }
            if(occupied > answer) {
                answer = occupied;
            }
            now++;
        }

        return answer;
    }

    int timeStrToInt(String time) {
        String[] arr = time.split(":");
        return Integer.parseInt(arr[0]) * 60 + Integer.parseInt(arr[1]);
    }

    class BookInfo {
        int start = 0;
        int end = 0;

        BookInfo(String[] info) {
            this.start = timeStrToInt(info[0]);
            this.end = timeStrToInt(info[1]) + 10;
        }

    }

}
