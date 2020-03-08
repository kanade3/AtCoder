from functools import lru_cache
import sys

sys.getrecursionlimit()
x, y = map(int, input().split())


@lru_cache(maxsize=100000)
def solve(x, y, inx, iny, cnt):
    if x == inx and y == iny:
        cnt += 1
    if x <= inx and y <= iny:
        solve(x + 1, y + 2, inx, iny, cnt)
        solve(x + 2, y + 1, inx, iny, cnt)
    else:
        print(cnt)
    # return cnt


print(solve(0, 0, x, y, 0))
