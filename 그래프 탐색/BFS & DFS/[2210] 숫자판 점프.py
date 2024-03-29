'''
[2210] 숫자판 점프 / Silver 2 / 그래프 탐색(BFS), 브루트포스
5×5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 
이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 
이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.
숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline

res = set()
matrix = [list(map(str, input().split())) for _ in range(5)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y, number) :
    global res

    if len(number) == 6 :
        res.add(number)
        return
    
    for k in range(4) :
        xx, yy = x + dx[k], y + dy[k]
        if 0 <= xx < 5 and 0 <= yy < 5 :
            DFS(xx, yy, number + matrix[xx][yy])
      

for i in range(5) :
    for j in range(5) :
        res.add(DFS(i, j, matrix[i][j]))

print(len(res)-1)
