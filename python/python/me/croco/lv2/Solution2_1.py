'''
240316
연습문제 > 행렬의 곱셈
https://school.programmers.co.kr/learn/courses/30/lessons/12949

문제 설명
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.

입출력 예
arr1	                              arr2	                                return
[[1, 4], [3, 2], [4, 1]]	            [[3, 3], [3, 3]]	                [[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	 [[5, 4, 3], [2, 4, 1], [3, 1, 1]]	  [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
'''

def solution(arr1, arr2) :
    n1, m1 = len(arr1), len(arr1[0])
    n2, m2 = len(arr2), len(arr2[0])

    result = [[0] * m2 for _ in range(n1)]

    for i in range(n1) :
        for j in range(m2) :

            for k in range(m1) :
                result[i][j] += arr1[i][k] * arr2[k][j]

    return result


'''
zip() 이라는 함수를 알게 됨!
zip(iterable1, iterable2, ...)

list = [1, 2]
list2 = ['a', 'b']
print(zip(list, list2))     # [(1, 'a'), (2, 'b')]
'''

# zip을 이용해 구현하기

def solution2(arr1, arr2):
    # arr2의 전치 행렬을 구함   * 전치행렬 : 기존 행렬의 행과 열을 바꾼 행렬
    arr2_transposed = list(zip(*arr2))

    result = [
        [
            sum(
                a*b for a, b in zip(row_a, col_b)
            ) for col_b in arr2_transposed
        ] for row_a in arr1
    ]

    return result






arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
res = solution2(arr1, arr2)
print(res)
