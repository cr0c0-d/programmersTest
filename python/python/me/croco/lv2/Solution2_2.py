'''
240316
Summer/Winter Coding(~2018) > 방문 길이
https://school.programmers.co.kr/learn/courses/30/lessons/49994

문제 설명
** 링크로 가서 그림 참조하는게 좋을듯
'''

def solution(dirs) :

    # dirs : UDRL 문자로 이루어짐
    # 게임판은 x y 모두 -5 ~ 5

    dirList = list(dirs)

    bot = [0, 0]

    # 방향과 이동경로를 동시에 저장해야 중복 경로를 거를 수 있음
    history = []

    for direction in dirList :
        dir = [bot[0], bot[1]]
        if direction == "U" and bot[1] < 5: # 위로 = player[1] += 1
            bot[1] += 1

        if direction == "D" and bot[1] > -5: # 아래로 = player[1] -= 1
            bot[1] -= 1

        if direction == "R" and bot[0] < 5 : # 오른쪽으로 = player[0] += 1
            bot[0] += 1

        if direction == "L" and bot[0] > -5: # 왼쪽으로 = player[0] -= 1
            bot[0] -= 1

        if dir[0] == bot[0] and dir[1] == bot[1] :
            continue

        dir[0] += bot[0]
        dir[1] += bot[1]
        history.append(str(dir[0])+str(dir[1]))

    print(history)
    arr = list(set(history))
    return len(arr)


# 결과는 잘 나옴 근데 한참 부족함ㅠㅠㅠㅠㅠㅠ
# 아래는 GPT 코드

def solutionGPT(dirs):
    # dirs: 'UDRL' 문자열로 이루어짐
    # 게임판은 x, y 모두 -5 ~ 5 범위에 있음

    # 현재 위치
    current_pos = [0, 0]

    # 이동 경로를 저장할 집합 (중복 제거)
    visited_paths = set()

    # 방향에 따른 위치 변화 정의
    moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

    for direction in dirs:
        # 현재 위치에서 이동할 방향 계산
        move = moves[direction]
        next_pos = [current_pos[0] + move[0], current_pos[1] + move[1]]

        # 이동 가능한 범위 내인지 확인
        if -5 <= next_pos[0] <= 5 and -5 <= next_pos[1] <= 5:
            # 이동 경로 (시작점, 도착점)을 양방향으로 저장하여 중복 경로를 제거
            visited_paths.add((tuple(current_pos), tuple(next_pos)))
            visited_paths.add((tuple(next_pos), tuple(current_pos)))

            # 현재 위치 업데이트
            current_pos = next_pos

    # 이동한 경로의 수는 양방향으로 저장했으므로 실제 경로 수는 절반임
    return len(visited_paths) // 2
