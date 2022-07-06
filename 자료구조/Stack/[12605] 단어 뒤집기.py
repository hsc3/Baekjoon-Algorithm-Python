'''
[12605] 단어 뒤집기 / Bronze 1 / 자료구조(Stack)
스페이스로 띄어쓰기 된 단어들의 리스트가 주어질때, 단어들을 반대 순서로 뒤집어라.
각 라인은 w개의 영단어로 이루어져 있으며, 총 L개의 알파벳을 가진다.
각 행은 알파벳과 스페이스로만 이루어져 있다. 단어 사이에는 하나의 스페이스만 들어간다.
'''
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T) :
    stk = list(input().split())
    print("Case #{}: ".format(i+1), end = '')
    while stk :
        print(stk.pop(), end = ' ')
