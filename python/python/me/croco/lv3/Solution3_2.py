'''
240321
해시 > 베스트앨범
https://school.programmers.co.kr/learn/courses/30/lessons/42579

문제 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다.
노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.

입출력 예
genres	                                           plays                        return
["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
'''


def solution(genres, plays) :
    # 장르별로 가장 많이 들은 노래 2개, 장르별 > 플레이수 순(내림차) > 고유번호 순(오름차)
    # 1. 장르 순서 구하기 -> 장르별 플레이 수 합산
    # 2. 장르 안에서 플레이 수 구하기 -> (장르별) 플레이 수 sort
    # 3. 고유번호 순 -> 인덱스
    # 그럼 장르 순서, 플레이 top2의 인덱스 필요
    # 장르에 노래가 하나라면 하나만

    genres_total = {}   # 장르별 전체 플레이 수 합산 { 장르명 : 총 플레이 수 }
    songs_dict = {}     # 노래들을 장르별로 분류 { 장르명 : [[노래1의 고유번호, 노래1의 플레이 수], [노래2의 고유번호, 노래2의 플레이 수] ... ] }

    for index, (g, p) in enumerate(zip(genres, plays)) :
        if g in genres_total :
            genres_total[g] = genres_total[g] + p
        else :
            genres_total[g] = p

        # 이렇게 하면 더 깔끔 : genres_total[g] = genres_total.get(g, 0) + p


        if g in songs_dict :
            songs_dict[g].append([index, p])
        else :
            songs_dict[g] = [[index, p]]

        # 이렇게 하면 더 깔끔 : songs_dict.setdefault(g, []).append([index, p])

    genre_list = sorted(genres_total.keys(), key = lambda x : genres_total[x], reverse=True)    # 총 플레이 수 내림차순으로 장르명을 정렬

    answer = []

    for g in genre_list :   # 장르 순서대로
        songs = sorted(songs_dict[g], key = lambda x : (-x[1], x[0]))  # 장르별 노래 목록을 플레이 수 내림차순, 고유번호 오름차순으로 정렬
        answer.extend([song[0] for song in songs[:2]])  # 정렬한 노래 목록 중 상위 2개의 고유번호를 기록

    return answer


'''
gpt가 다듬어준 코드

    def solution(genres, plays):
        genres_total = {}
        songs_dict = {}
    
        # 장르별 총 재생수와 노래 정보를 딕셔너리에 저장
        for index, (genre, play) in enumerate(zip(genres, plays)):
            genres_total[genre] = genres_total.get(genre, 0) + play
            songs_dict.setdefault(genre, []).append([index, play])
    
        # 장르별 총 재생수를 기준으로 내림차순 정렬
        genre_list = sorted(genres_total, key=lambda x: genres_total[x], reverse=True)
    
        answer = []
        for genre in genre_list:
            # 각 장르별 노래를 재생수 기준 내림차순으로 정렬하고, 고유 번호가 낮은 순으로 정렬
            # 노래가 하나만 있는 경우를 고려하여 min 함수를 사용
            songs = sorted(songs_dict[genre], key=lambda x: (-x[1], x[0]))
            answer.extend([song[0] for song in songs[:2]])
        return answer
'''

genres, plays = ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
print(solution(genres, plays))