# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 핵심: 딕셔너리 2개 — genre_total{장르:총재생수}로 장르 순서, genre_songs{장르:[(재생,인덱스)]}로
#       장르 내 정렬. 장르는 총재생수 내림차순, 노래는 (재생수 내림, 인덱스 오름) 후 장르당 2곡.
# 리뷰: 딕셔너리 구성/정렬 mechanics에서 막혀 시간초과(발상은 정답이었음).
#       배운 것: ①defaultdict(list)+append로 그룹핑 ②정렬 기본=오름차순, 내림은 -키 or reverse=True
#       ③다중키 key=lambda x:(-x[0], x[1]) ④min(len,2)로 1곡 장르 IndexError 방어
from collections import defaultdict


def solution(genres, plays):
    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)

    for i, (g, p) in enumerate(zip(genres, plays, strict=True)):  # 두 배열 길이 동일 보장
        genre_total[g] += p
        genre_songs[g].append((p, i))

    answer = []

    for g in sorted(genre_total, key=lambda x: -genre_total[x]):
        songs = sorted(genre_songs[g], key=lambda x: (-x[0], x[1]))
        for i in range(min(len(songs), 2)):
            answer.append(songs[i][1])

    return answer


if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    assert solution(genres, plays) == [4, 1, 3, 0]
    # 1곡뿐인 장르 방어
    assert solution(["rock", "pop"], [10, 20]) == [1, 0]
    print("all passed")
