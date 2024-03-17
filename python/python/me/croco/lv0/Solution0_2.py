'''
240317
코딩테스트 입문 > 배열 뒤집기
https://school.programmers.co.kr/learn/courses/30/lessons/120821?language=python3

문제 설명
정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ num_list의 길이 ≤ 1,000
0 ≤ num_list의 원소 ≤ 1,000

입출력 예
num_list	                result
[1, 2, 3, 4, 5]	        [5, 4, 3, 2, 1]
[1, 1, 1, 1, 1, 2]	    [2, 1, 1, 1, 1, 1]
[1, 0, 1, 1, 1, 3, 5]	[5, 3, 1, 1, 1, 0, 1]
'''
def solution(num_list):
    return num_list[::-1]
    # 슬라이싱을 이용해서 뒤집기
    # [시작 인덱스 : 끝 인덱스 : 스텝] 이므로 시작/끝 인덱스를 생략하면 전체, 대신 스텝을 -1하면 역방향으로 진행되므로 뒤집어짐!!