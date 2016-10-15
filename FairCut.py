__Author__ = 'Anupam Panwar'

__Created_On__ = 9 / 25 / 2016

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
S = map(int,raw_input().strip().split(' '))
S = sorted(S)


def fairCut(n,k,S):
    mat = [[float('inf') for i in range(k)] for j in range(n)]
