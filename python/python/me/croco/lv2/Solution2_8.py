'''
240321
연습문제 > 할인행사
https://school.programmers.co.kr/learn/courses/30/lessons/131127

문제 설명
XYZ 마트는 일정한 금액을 지불하면 10일 동안 회원 자격을 부여합니다.
XYZ 마트에서는 회원을 대상으로 매일 한 가지 제품을 할인하는 행사를 합니다.
할인하는 제품은 하루에 하나씩만 구매할 수 있습니다.
알뜰한 정현이는 자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속으로 일치할 경우에 맞춰서 회원가입을 하려 합니다.

예를 들어, 정현이가 원하는 제품이 바나나 3개, 사과 2개, 쌀 2개, 돼지고기 2개, 냄비 1개이며,
XYZ 마트에서 14일간 회원을 대상으로 할인하는 제품이 날짜 순서대로

치킨, 사과, 사과, 바나나, 쌀, 사과, 돼지고기, 바나나, 돼지고기, 쌀, 냄비, 바나나, 사과, 바나나

인 경우에 대해 알아봅시다.

첫째 날부터 열흘 간에는 냄비가 할인하지 않기 때문에 첫째 날에는 회원가입을 하지 않습니다.
둘째 날부터 열흘 간에는 바나나를 원하는 만큼 할인구매할 수 없기 때문에 둘째 날에도 회원가입을 하지 않습니다.
셋째 날, 넷째 날, 다섯째 날부터 각각 열흘은 원하는 제품과 수량이 일치하기 때문에 셋 중 하루에 회원가입을 하려 합니다.

정현이가 원하는 제품을 나타내는 문자열 배열 want와 정현이가 원하는 제품의 수량을 나타내는 정수 배열 number,
XYZ 마트에서 할인하는 제품을 나타내는 문자열 배열 discount가 주어졌을 때,
회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return 하는 solution 함수를 완성하시오.
가능한 날이 없으면 0을 return 합니다.

제한사항
1 ≤ want의 길이 = number의 길이 ≤ 10
1 ≤ number의 원소 ≤ 10
number[i]는 want[i]의 수량을 의미하며, number의 원소의 합은 10입니다.
10 ≤ discount의 길이 ≤ 100,000
want와 discount의 원소들은 알파벳 소문자로 이루어진 문자열입니다.
1 ≤ want의 원소의 길이, discount의 원소의 길이 ≤ 12

입출력 예
want	                                        number	            discount	                                                                                                                        result
["banana", "apple", "rice", "pork", "pot"]	    [3, 2, 2, 2, 1]	    ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]	    3
["apple"]	                                    [10]	            ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]	                                0
'''

from collections import deque
def solution(want, number, discount) :
    # discount의 길이가 10만이므로 O(NlogN) 이하로 계산해야 함
    # discount의 인덱스가 10개일 때부터 계산하면 됨(10개 원소의 수량을 분류하는게 목적이니까)
    # want에 없는 원소를 기준으로 10개씩 나누면 어떨까??
    want_dict = dict(zip(want, number))

    arr = deque(discount[:10])
    arr_dict = dict_count(arr)
    answer = want_dict == arr_dict and 1 or 0

    for i in range(10, len(discount)) :
        arr.popleft()
        arr.append(discount[i])
        arr_dict = dict_count(arr)

        if want_dict == arr_dict :
            answer += 1

    return answer


def dict_count(arr) :
    dict1 = {}

    for i in arr :
        if i in dict1 :
            dict1[i] = dict1[i] + 1
        else :
            dict1[i] = 1

    return dict1










want, number, discount = ["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))