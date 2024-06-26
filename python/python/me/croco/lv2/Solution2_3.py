'''
240318
월간 코드 챌린지 시즌2 > 괄호 회전하기
https://school.programmers.co.kr/learn/courses/30/lessons/76502

문제 설명
다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.

(), [], {} 는 모두 올바른 괄호 문자열입니다.
만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다.
예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.

만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다.
예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.

대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다.
이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
s의 길이는 1 이상 1,000 이하입니다.

입출력 예
s	        result
"[](){}"	    3
"}]()[{"	    2
"[)(]"	        0
"}}}"	        0
'''

def solution(s) :


    # 일단 s 길이가 홀수면 0임.
    # 후괄호가 먼저 오면 안됨..
    # 후괄호가 먼저 오면 첫 선괄호 인덱스만큼 땡겨야함

    length = len(s)
    if length % 2 == 1 :
        return 0

    answer = 0

    for i in range(length) :
        stack = []
        for j in range(length) :

            a = s[(i + j) % length]

            if a == '[' or a == '{' or a == '(' :
                stack.append(a)
            else :
                if not stack :
                    break
                else :
                    b = stack[-1]
                    if (b == '[' and a == ']') or (b == '{' and a == '}') or (b == '(' and a == ')'):
                        stack.pop()
                    else :
                        break

        else :      # for-else 구문! for이 끝까지 실행된 경우 else를 실행함. 중간에 break된 경우 실행하지 않음.
            if stack :
                break
            else :
                answer += 1

    return answer

s = "[)(]"
print(solution(s))


