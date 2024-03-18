'''
240318
2019 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임
https://school.programmers.co.kr/learn/courses/30/lessons/64061

문제설명은 링크로
'''
def solution(board, moves):
    # board[?][move]에서 ?의 최솟값이 스택으로 쌓일것임. 해당 자리는 0
    # 스택에서 같은 정수는 제거하고 리턴값에 +2씩 해줌

    stack = []
    answer = 0

    for move in moves :
        for index, line in enumerate(board) :
            if line[move-1] != 0 :
                puppet = line[move-1]
                board[index][move-1] = 0
                if stack and stack[-1] == puppet :
                    stack.pop()
                    answer += 2
                else :
                    stack.append(puppet)
                break

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))