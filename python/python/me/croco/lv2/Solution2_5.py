'''
240318
스택/큐 > 주식가격
https://school.programmers.co.kr/learn/courses/30/lessons/42584

문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

입출력 예
prices                return
[1, 2, 3, 2, 3]	    [4, 3, 1, 1, 0]
'''

def solution(prices) :
    # 현재 가격이 top보다 낮으면? pop하고 시간 기록(인덱스의 차).
    # 높으면? 그냥 쌓기.

    stack = []

    answer = [0] * len(prices)

    for index, price in enumerate(prices) :
        while stack and prices[stack[-1]] > price:          # 같은 price가 연속으로 쌓여있는 경우를 고려하지 못해서 처음엔 실패함. while로 계속 제거해줘야했음.
            top = stack.pop()
            answer[top] = index - top

        stack.append(index)

    if stack :
        for num in stack :
            answer[num] = len(prices) - num - 1

    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))