# [1259] 팰린드롬수 / Bronze 1 / 문자열
'''
어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어를 팰린드롬이라고 한다. 'radar', 'sees'는 팰린드롬이다.
수도 팰린드롬으로 취급할 수 있다. 수의 숫자들을 뒤에서부터 읽어도 같다면 그 수는 팰린드롬수다. 121, 12421 등은 팰린드롬수다. 123, 1231은 뒤에서부터 읽으면 다르므로 팰린드롬수가 아니다.
또한 10도 팰린드롬수가 아닌데, 앞에 무의미한 0이 올 수 있다면 010이 되어 팰린드롬수로 취급할 수도 있지만, 특별히 이번 문제에서는 무의미한 0이 앞에 올 수 없다고 하자.
'''

import sys
input = sys.stdin.readline

def IsFelindrom(number) :
    start = 0
    end = len(number)-1
    while start < end : 
        if number[start] != number[end] :
            return False
        else :
            start += 1
            end -= 1
    return True

def Solution() :
    ans = []
    while True :
        data = int(input())
        if data == 0 : 
            break
        
        if IsFelindrom(str(data)) :
            ans.append("yes")
        else : 
            ans.append("no")

    print(*ans, sep='\n')

if __name__=="__main__" :
    Solution()

'''
- 다른 풀이법 -

(1) if n == n[::-1]

(2) if string_n == ''.join(reversed(string_n)):

'''

