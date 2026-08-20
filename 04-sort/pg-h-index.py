# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42747
# 핵심: h-index = "인용 h회 이상인 논문이 h편 이상"을 만족하는 최대 h.
#       h 후보의 범위는 0~n(논문 수) — 인용수가 아무리 커도 h는 논문 수를 못 넘는다.
#       h를 0부터 올리며 첫 실패에서 break해도 정확함: h가 커질수록 "인용≥h인 논문 수"는
#       줄기만 하므로(단조성) 한 번 실패하면 이후는 전부 실패.
# 리뷰: 3연타로 배운 문제. ①answer 미초기화 → 조건 실패 경로에서 UnboundLocalError(런타임 에러)
#       — "모든 경로에서 반환값이 정의되는가" 점검 습관. ②시작점을 n/2로 가정 → h<n/2인 입력
#       ([0,0,0,0,9]→h=1)을 영영 못 봄. 탐색 시작점은 근거 없이 좁히지 말 것.
#       ③채점 통과 ≠ 정답 — ②상태로 프로그래머스는 통과했음(테스트셋에 해당 분포 부재).
#       반례로 스스로 검증해야 진짜 완성. ④assert는 넣는 게 아니라 "돌리는" 것 —
#       수정→실행→통과 확인까지가 한 세트.
#       (더 우아한 방법: 내림차순 정렬 후 enumerate로 위치 vs 인용수 비교 — 다른 풀이 참고)


def solution(citations):
    sortedCitations = sorted(citations)
    middle = 0  # h 후보는 0부터 — 시작점을 좁힐 근거 없음
    count = 0
    answer = 0  # 어떤 경로로도 반환값 보장 (h=0은 항상 성립)
    while middle <= len(citations):  # 상한은 논문 수 n
        h = middle
        for j in range(len(sortedCitations)):
            if h <= sortedCitations[j]:
                count += 1
        if count >= h:
            answer = h
        else:
            break  # 단조성 덕에 이후 h는 전부 실패 → 조기 종료 OK
        middle += 1
        count = 0

    return answer


if __name__ == "__main__":
    assert solution([3, 0, 6, 1, 5]) == 3  # 공식 예제
    assert solution([0, 0, 0, 0, 9]) == 1  # 시작점 n/2 버그를 잡은 반례
    assert solution([0, 0, 0]) == 0  # 전부 0
    assert solution([5, 5, 5]) == 3  # h = n (전부 우수)
    assert solution([100]) == 1  # 인용 커도 h ≤ 논문 수
    assert solution([10, 8, 5, 4, 3]) == 4
    print("all passed")
