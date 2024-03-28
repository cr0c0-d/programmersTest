'''
240327
2022 KAKAO BLIND RECRUITMENT > 양과 늑대
https://school.programmers.co.kr/learn/courses/30/lessons/92343

2진 트리 모양 초원의 각 노드에 늑대와 양이 한 마리씩 놓여 있습니다.
이 초원의 루트 노드에서 출발하여 각 노드를 돌아다니며 양을 모으려 합니다.
각 노드를 방문할 때 마다 해당 노드에 있던 양과 늑대가 당신을 따라오게 됩니다.
이때, 늑대는 양을 잡아먹을 기회를 노리고 있으며, 당신이 모은 양의 수보다 늑대의 수가 같거나 더 많아지면 바로 모든 양을 잡아먹어 버립니다.
당신은 중간에 양이 늑대에게 잡아먹히지 않도록 하면서 최대한 많은 수의 양을 모아서 다시 루트 노드로 돌아오려 합니다.

각 노드에 있는 양 또는 늑대에 대한 정보가 담긴 배열 info,
2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열 edges가 매개변수로 주어질 때,
문제에 제시된 조건에 따라 각 노드를 방문하면서 모을 수 있는 양은 최대 몇 마리인지 return 하도록 solution 함수를 완성해주세요.

제한사항
2 ≤ info의 길이 ≤ 17
info의 원소는 0 또는 1 입니다.
info[i]는 i번 노드에 있는 양 또는 늑대를 나타냅니다.
0은 양, 1은 늑대를 의미합니다.
info[0]의 값은 항상 0입니다. 즉, 0번 노드(루트 노드)에는 항상 양이 있습니다.
edges의 세로(행) 길이 = info의 길이 - 1
edges의 가로(열) 길이 = 2
edges의 각 행은 [부모 노드 번호, 자식 노드 번호] 형태로, 서로 연결된 두 노드를 나타냅니다.
동일한 간선에 대한 정보가 중복해서 주어지지 않습니다.
항상 하나의 이진 트리 형태로 입력이 주어지며, 잘못된 데이터가 주어지는 경우는 없습니다.
0번 노드는 항상 루트 노드입니다.

입출력 예
info	edges	result
[0,0,1,1,1,0,1,0,1,0,1,1]	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]	5
[0,1,0,1,1,0,1,0,0,1,0]	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	5
'''
from collections import deque


def solution(info, edges) :
    collect = deque([(0, 1, 0, set())]) # 큐 (현재 동물의 인덱스, 양의 수, 늑대의 수, 접근할 수 있는 동물의 인덱스 배열)

    route_dict = { i : [ ] for i in range(len(info)) }  # { 동물의 인덱스(부모) : [연결된 동물 인덱스 배열](자식) }

    for i in edges :
        route_dict[i[0]].append(i[1])

    max_sheep = 1   # 최대 양의 수를 기록

    while collect :
        curr, sheep, wolf, collectable = collect.popleft()
        max_sheep = max(max_sheep, sheep)   # 최대 양의 수 기록

        collectable.update(route_dict[curr])    # 접근할 수 있는 동물에 현재 노드의 자식 노드들 추가

        for node in collectable :
            if info[node] == 1 :    # 늑대일 경우
                if sheep > wolf + 1 :   # 양의 수보다 적어야 함
                    collect.append((node, sheep, wolf + 1, collectable - {node}))   # 접근할 수 있는 동물 목록에서 현재 동물 빼고 삽입

            else :
                collect.append((node, sheep + 1, wolf, collectable - {node}))

    return max_sheep


info, edges = [0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))