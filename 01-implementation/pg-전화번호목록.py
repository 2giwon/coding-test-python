# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 핵심: 사전순 정렬하면 접두사는 (a)항상 앞, (b)자기 확장과 인접 → 인접 쌍만 startswith 검사.
#       zip(a, a[1:]) = 인접 쌍 관용구. O(n log n).
# 리뷰: 첫 시도 이중 반복(모든 쌍 비교)으로 효율성 탈락 — 번호 최대 100만 → O(n²)=1조.
#       교훈: "전수 확인 ≠ 모든 쌍 비교". 정렬로 후보를 인접으로 줄이면 한 번만 훑어도 됨.
#       ※ 정렬은 "번호 리스트를 사전순 재배치"지 자릿수 뒤집기가 아니다(초기 오해).


def solution(phone_book):
    phoneBook = sorted(phone_book)
    for p1, p2 in zip(phoneBook, phoneBook[1:], strict=False):  # 길이 1 차이가 의도
        if p2.startswith(p1):
            return False

    return True


if __name__ == "__main__":
    assert not solution(["119", "97674223", "1195524421"])  # 119가 1195...의 접두사
    assert solution(["123", "456", "789"])  # 접두사 없음
    assert not solution(["12", "123", "1235", "567", "88"])  # 12→123 접두사
    print("all passed")
