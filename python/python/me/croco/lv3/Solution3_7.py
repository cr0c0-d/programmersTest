'''
240402
2023 KAKAO BLIND RECRUITMENT > 표현 가능한 이진트리
https://school.programmers.co.kr/learn/courses/30/lessons/150367

'''
from collections import deque


def solution(numbers) :
    bin_numbers = [bin(i)[2:] for i in numbers]     # 각 숫자들을 이진수로 변환하고 앞 두 글자(0b)를 잘라서 배열로 저장

    answer = [-1] * len(numbers)    # 리턴할 answer 배열을 초기화

    for index, num in enumerate(bin_numbers) :
        num = str(num)

        # 포화 이진트리를 구성할 수 있는 길이로 만드는 과정
        # 포화 이진트리의 노드의 수는 2^n - 1 이므로 이 길이가 될 때까지 문자열의 앞에 '0'을 붙이는 과정
        # 문자열 길이+1이 2의 거듭제곱인지 확인한다.
        # 확인은 비트연산자 &를 활용함
        # 2의 거듭제곱 수를 이진법으로 표현하면 1 뒤에 모두 0이 오는 구조임 (ex. 2 : 10, 4 : 100, 8 : 1000)
        # 여기서 1을 빼면 1과 0이 뒤바뀐 구조가 되므로 (ex. 1 : 01, 3 : 011, 7 : 0111)
        # & 연산자를 사용하면 각 비트에 동일한 비트가 없으므로 0임
        # 0이 아닌 경우 맨 앞에 '0'을 붙여가며 다시 확인
        while True :
            length = len(num)
            if (length+1) & length == 0 :
                break
            else :
                num = '0' + num

        tree = deque()
        tree.append(num)

        # 포화 이진트리를 만들 수 있는지 확인
        while answer[index] == -1 :

            t = tree.popleft()
            if len(t) == 1 :
                answer[index] = 1
                break

            center = int((len(t) - 1) / 2)   # 루트의 위치 찾음(포화 이진트리이므로 전체 길이의 중앙)

            # 트리의 루트가 0인데 하위 노드에 1이 있는 경우
            # 더미노드의 하위 트리는 모두 0이어야 하므로 answer 0
            if t[center] == "0" and "1" in t:
                answer[index] = 0
                break

            tree.append(t[:center])     # 루트를 기준으로 좌/우 서브트리를 나눠서 큐에 삽입
            tree.append(t[center+1:len(t)])

    return answer

numbers = [63, 111, 95]
print(solution(numbers))