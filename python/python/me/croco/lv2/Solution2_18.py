'''
240407
깊이/너비 우선 탐색(DFS/BFS) > 게임 맵 최단거리
https://school.programmers.co.kr/learn/courses/30/lessons/1844

문제설명
링크 참고
게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요.
단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.

제한사항
maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.

입출력 예
maps	                                                         answer
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	11
[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	-1
'''
from collections import deque
def solution(maps) :
    n = len(maps[0])    # 게임맵 가로길이
    m = len(maps)       # 게임맵 세로길이

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)]) # 좌표, 길이, 방문한 좌표
    visited = [[-1 for _ in range(n)] for _ in range(m)]
    visited[0][0] = 1

    while queue :
        x, y = queue.popleft()
        distance = visited[y][x]
        if x == n-1 and y == m-1 :  # 도착지점
            return distance

        for i, k in direction :
            nx = x+i
            ny = y+k

            if 0 <= nx < n and 0 <= ny < m and maps[ny][nx] == 1 and visited[ny][nx] == -1 :
                visited[ny][nx] = distance + 1
                queue.append((nx, ny))

    return -1


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))