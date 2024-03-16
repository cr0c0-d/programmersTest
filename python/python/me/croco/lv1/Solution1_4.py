'''
240316
2019 KAKAO BLIND RECRUITMENT > 실패율
https://school.programmers.co.kr/learn/courses/30/lessons/42889

슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다.
그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감한 것이다.
원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.

이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다.
역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다. 오
렐리를 위해 실패율을 구하는 코드를 완성하라.

실패율은 다음과 같이 정의한다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때,
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.

제한사항
스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
stages의 길이는 1 이상 200,000 이하이다.
stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

입출력 예
N	stages	                      result
5	[2, 1, 2, 6, 2, 4, 3, 3]	    [3,4,2,1,5]
4	[4,4,4,4,4]	               [4,1,2,3]

'''

# 리턴값 : 실패율이 높은 스태이지 -> 낮은 스테이지 순 번호 배열
# (실패율) : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 매개변수 : 전체 스테이지 개수 N, 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
# 1 <= N <= 500
# 1 <= len(stages) <= 200,000
# N + 1 = 모두 클리어한 사용자
# 실패율이 같은 스테이지 -> 작은 번호부터
# 스테이지에 도달한 유저가 없음 -> 실패율 0


def solution(n, stages):
    # 리턴값 : 길이 N인 배열 -> 선언
    # 실패율을 어디다 기록할까 ? 분모와 분자를 각각 기록해야 함. -> 리스트를 두개?
    list1 = [0] * n     # 도달했으나 클리어하지 못한 플레이어 수
    list2 = [0] * n     # 스테이지에 도달한 플레이어 수

    # stages에서 반복 (i)
    for stage in stages :

    # > 현재 stage 번호보다 작은 stage들은 전부 스테이지에 도달한 플레이어 수 + 1
        #for i in range(stage == n+1 and n or stage) :  => 아래처럼 수정함
        for i in range(min(stage, n)):
            list2[i] += 1

    # > 현재 stage 번호와 같은 stage는 도달했으나 클리어하지 못한 플레이어 수 + 1
        if stage <= n :
            list1[stage-1] += 1

    list = [ a / b if b > 0 else 0 for a, b in zip(list1, list2)]    # 실패율 리스트

    # 여기까지 풀고 gpt 도움 받음 => 값으로 정렬하되 값 대신 인덱스를 결과로 추출하는 방법

    sorted_pairs = sorted(enumerate(list), key=lambda x: x[1], reverse=True)
    # 정렬된 쌍에서 인덱스만 추출
    sorted_indices = [index + 1 for index, _ in sorted_pairs]

    return sorted_indices


# GPT가 작성한 코드
def solutionGPT(N, stages):
    # 스테이지별 도달했으나 클리어하지 못한 플레이어 수와 도달한 플레이어 수를 저장할 딕셔너리
    stage_failure = {stage: [0, 0] for stage in range(1, N + 1)}  # [클리어하지 못한 플레이어 수, 도달한 플레이어 수]

    for stage in stages:
        for i in range(1, min(stage, N + 1)):
            stage_failure[i][1] += 1  # 도달한 플레이어 수 증가
        if stage <= N:
            stage_failure[stage][0] += 1  # 클리어하지 못한 플레이어 수 증가

    # 실패율 계산
    for stage in stage_failure:
        if stage_failure[stage][1] > 0:  # 도달한 플레이어가 있을 경우 실패율 계산
            stage_failure[stage] = stage_failure[stage][0] / stage_failure[stage][1]
        else:  # 도달한 플레이어가 없을 경우 실패율을 0으로 설정
            stage_failure[stage] = 0

    # 실패율을 기준으로 스테이지 정렬
    sorted_stages = sorted(stage_failure, key=lambda x: (stage_failure[x], -x), reverse=True)   # lambda x: (stage_failure[x], -x) => stage_failure[x] 값으로 내림차순 정렬을 하되, -x : 같은 값일 경우 인덱스 오름차순으로 정렬하라

    return sorted_stages


N = 5
arr = [2, 1, 2, 6, 2, 4, 3, 3]
# 예상결과 : [3,4,2,1,5]
print(solutionGPT(N, arr))