'''
[1903] 01타일 / Silver 3 / 다이나믹 프로그래밍
각각의 타일들은 0 또는 1이 쓰여 있는 낱장의 타일들이다. 현재 1 하나만으로 이루어진 타일 또는 0타일을 두 개 붙인 한 쌍의 00타일들만이 남게 되었다.
예를 들어, N=1일 때 1만 만들 수 있고, N=2일 때는 00, 11을 만들 수 있다.
또한 N=4일 때는 0011, 0000, 1001, 1100, 1111 등 총 5개의 2진 수열을 만들 수 있다.
우리의 목표는 N이 주어졌을 때 지원이가 만들 수 있는 모든 가짓수를 세는 것이다. 단 타일들은 무한히 많은 것으로 가정하자.
'''
"""
N = 1 : 1 (1)
N = 2 : 00, 11 (2)
N = 3 : 001, 100, 111 (3)
N = 4 : 0000, 0011, 1100, 1001, 1111 (5)
N = 5 : 00001, 00100, 10000, 00111, 10011, 11001, 11100, 11111 (8)
N = 6 : 000000, 000011, 001001, 100001, 001100, 100100, 110000, 001111, 100111, 110011, 111001, 111100, 111111 (13)
"""
def Fibo(n) :
    if n == 1 : return 1
    elif n == 2 : return 2
    else :
        n1, n2 = 1, 2
        for i in range(3, n+1) :
            n1, n2 = n2, (n1+n2) % 15746
        return n2

if __name__=="__main__" :
    print(Fibo(int(input())))
    
"""
N = int(input())
dp = [0] * (N+2)
dp[1] = 1
dp[2] = 2

for i in range(3, N+1) :
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N])
"""