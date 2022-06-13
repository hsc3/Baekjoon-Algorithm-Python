'''
- Algorithm : 구현, 문자열 
[1100] 하얀 칸 | https://www.acmicpc.net/problem/1100
체스판은 8×8크기이고, 검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다. 
체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하는 프로그램을 작성하시오.
'''
chess = []
for _ in range(8) :
    chess.append(input().rstrip())

answer = 0

for i in range(0,8) :
    for j in range(0, 8) :
        if i % 2 == j % 2 and chess[i][j] == 'F' :
            answer += 1

print(answer)