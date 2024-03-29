# [2670] 연속부분최대곱 | Silver 4 | 다이나믹 프로그래밍
'''
N개의 실수가 있을 때, 한 개 이상의 연속된 수들의 곱이 최대가 되는 부분을 찾아, 그 곱을 출력하는 프로그램을 작성하시오.
[입력]
실수는 소수점 첫째자리까지 주어지며, 0.0보다 크거나 같고, 9.9보다 작거나 같다.
[출력]
계산된 최댓값을 소수점 이하 넷째 자리에서 반올림하여 소수점 이하 셋째 자리까지 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [float(input()) for _ in range(N)]

# 기존 숫자와 (이전 연속 수들의 곱 * 기존 숫자) 중 큰 값을 선택
# 연속적으로 수를 곱하는 것이 기존 숫자보다 크면 선택
for i in range(1, len(dp)):
    dp[i] = max(dp[i], (dp[i]*dp[i-1]))

print("{:.3f}".format(max(dp))) # 소수점 셋째자리까지 출력
