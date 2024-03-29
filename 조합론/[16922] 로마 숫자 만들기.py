# [16922] 로마 숫자 만들기 | Silver 3 | 조합론
'''
로마 숫자에서는 수를 나타내기 위해서 I, V, X, L을 사용한다. 각 문자는 1, 5, 10, 50을 의미하고, 이 문제에서 다른 문자는 사용하지 않는다.
하나 또는 그 이상의 문자를 이용해서 수를 나타낼 수 있다. 문자열이 나타내는 값은, 각 문자가 의미하는 수를 모두 합한 값이다.
예를 들어, XXXV는 35, IXI는 12를 의미한다.

실제 로마 숫자에서는 문자의 순서가 중요하지만, 이 문제에서는 순서는 신경쓰지 않는다. 예를 들어, 실제 로마 숫자에서 IX는 9를 의미하지만, 이 문제에서는 11을 의미한다.
로마 숫자를 N개 사용해서 만들 수 있는 서로 다른 수의 개수를 구해보자.
'''
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N = int(input())
roma = [1, 5, 10, 50]

answer = set()
for number in combinations_with_replacement(roma, N): # N개의 숫자 조합 생성
    answer.add(sum(number))

print(len(answer))


# def RomaNumber(i, tmp):
#     global answer
#     if i == N: # 숫자 저장
#         answer.add(tmp)
#         return
#     for number in [1, 5, 10, 50]: # i번째 로마 선택
#         RomaNumber(i+1, tmp+number)
#
# if __name__ == "__main__":
#     N = int(input())
#     answer = set()
#     RomaNumber(0, 0)
#     print(len(answer))