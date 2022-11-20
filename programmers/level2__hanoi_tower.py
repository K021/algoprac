# https://school.programmers.co.kr/learn/courses/30/lessons/12946
# 하노이의 탑, Level 2

def hanoi(n, start=1, target=3):  #default value
    onHand = 6 - start - target #able to change the positions
    if n == 1:
        trace = [[start, target]]
        return trace
    else:
        trace1 = hanoi(n-1, start, onHand)  #trace of the top series
        trace2 = [[start, target]]         #trace of the bottom
        trace3 = hanoi(n-1, onHand, target) #trace of the top series
        trace = trace1 + trace2 + trace3
        return trace

print(hanoi(3))



# version 2
def solution(n):
    def hanoi(n, from_, to):
        another = 6 - from_ - to

        if n == 1:
            return [[from_, to]]

        path = hanoi(n-1, from_, another)
        path += [[from_, to]]
        path += hanoi(n-1, another, to)
        return path
    
    return hanoi(n, 1, 3)