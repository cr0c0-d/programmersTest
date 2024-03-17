'''
240317
연습문제 > 나누어 떨어지는 숫자 배열
https://school.programmers.co.kr/learn/courses/30/lessons/12910

문제 설명
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

제한사항
arr은 자연수를 담은 배열입니다.
정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
divisor는 자연수입니다.
array는 길이 1 이상인 배열입니다.

입출력 예
arr	               divisor	 return
[5, 9, 7, 10]	    5	        [5, 10]
[2, 36, 1, 3]	    1	        [1, 2, 3, 36]
[3,2,6]	       10	        [-1]
'''

def solution(arr, divisor) :
    answer = []
    for num in arr :
        if num % divisor == 0 :
            answer.append(num)

    return len(answer) == 0 and [-1] or answer


def solution2(arr, divisor) :
    return sorted([n for n in arr if n % divisor == 0]) or [-1]
    # 리스트 컴프리헨션. n % divisor == 0 조건을 만족하는 n만으로 이루어진 새로운 배열 생성
    # sort([]) or [-1] : or 앞의 배열이 비어있으면 false로 간주하므로...


arr = [2, 36, 1, 3]
divisor = 1
print(solution2(arr, divisor))