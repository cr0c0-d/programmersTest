'''
240315
완전탐색 > 모의고사
https://school.programmers.co.kr/learn/courses/30/lessons/42840

문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]

'''

def solution(arr) :
    answers = list(arr)
    length = len(answers)

    num_list = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer_list = [0, 0, 0]


    for i in range(length) :
        for j in range(3) :
            if answers[i] == num_list[j][i % len(num_list[j])] :
                answer_list[j] = answer_list[j] + 1

    max_value = max(answer_list)

    answer = []
    for i in range(3) :
        if max_value == answer_list[i] :
            answer.append(i+1)

    return  answer

'''
나름 잘 풀었지만 enumerate()라는 걸 배움!
enumerate(iterable, start=0)
반복 가능한 객체(리스트, 튜플, 문자열 등), 

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)
    
    0 apple
    1 banana
    2 cherry
    

'''

# enumerate() 사용해서 아래처럼 수정함

def solution2(answers):
    length = len(answers)

    num_list = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer_list = [0, 0, 0]


    for i, answer in enumerate(answers) :
        for j, point in enumerate(answer_list) :
            if answer == num_list[j][i % len(num_list[j])] :
                answer_list[j] = point + 1

    max_value = max(answer_list)

    answer = []
    for i, point in enumerate(answer_list) :
        if max_value == point :
            answer.append(i+1)

    return  answer
