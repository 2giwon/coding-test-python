# 12-codility — A축 보관소

> 진도표는 `../notes/codility-진도.md`가 SOT.
> 이 폴더는 **Codility 사이트에서 100점 받은 코드를 사후 보관**하는 곳이다.

## 🔴 이 폴더에서 하지 않는 것

| 하지 않는다 | 이유 |
|---|---|
| 테스트 하네스 작성 | 채점은 Codility가 한다. 하네스를 만들면 하루 2문제가 불가능해진다 |
| 로컬에서 먼저 풀고 붙여넣기 | `code pasted from external sources`로 기록된다. **에디터 안에서 직접 쓴다** |
| 통과 전 코드 보관 | 통과한 것만 남긴다. 실패 기록은 진도표의 메모 칸에 한 줄 |

## 파일 형식

`L<레슨번호>-<문제이름>.py`

```python
# L5-PassingCars
# 지문 요건: expected worst-case time complexity is O(N);
#            expected worst-case space complexity is O(1)

def solution(A):
    ...


# ■ 기록
# 점수:        / 100  (정확성     , 성능     )
# 걸린 시간:    분
# 요건이 알려준 것:  O(N) + O(1) 이므로 한 번 훑으면서 카운터만 들고 간다
# 막힌 지점:
```

네 줄 기록이 전부다. 길게 쓰면 양을 못 채운다.

## 영어 지문 읽기 메모

반복해서 나오는 표현만 모아 둔다 (사전 찾을 시간 아끼기).

| 표현 | 뜻 |
|---|---|
| `expected worst-case time complexity` | 요구 시간복잡도. **이게 도구를 알려준다** |
| `expected worst-case space complexity is O(1)` | 추가 배열을 만들지 말라는 뜻 |
| `non-empty array A consisting of N integers` | 길이 N 정수 배열, 빈 배열은 안 들어온다 |
| `each element of array A is an integer within the range [a..b]` | 값 범위 |
| `the function should return -1` | 답이 없을 때 반환값. **놓치면 성능 만점에 정확성 깎인다** |
| `zero-indexed array` | 0부터 시작 |
| `slice of array A` | 연속 구간 (부분수열이 아니다) |
| `permutation` | 1부터 N까지가 정확히 한 번씩 |
| `A[P] + A[Q]` 꼴 조건 | 보통 투포인터 또는 정렬 후 양끝 |
