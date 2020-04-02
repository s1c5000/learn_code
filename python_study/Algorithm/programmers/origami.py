'''
직사각형 종이를 n번 접으려고 합니다. 이때, 항상 오른쪽 절반을 왼쪽으로 접어 나갑니다. 다음은 n = 2인 경우의 예시입니다.



먼저 오른쪽 절반을 왼쪽으로 접습니다.



다시 오른쪽 절반을 왼쪽으로 접습니다.



종이를 모두 접은 후에는 종이를 전부 펼칩니다. 종이를 펼칠 때는 종이를 접은 방법의 역순으로 펼쳐서 
처음 놓여있던 때와 같은 상태가 되도록 합니다. 위와 같이 두 번 접은 후 종이를 펼치면 아래 
그림과 같이 종이에 접은 흔적이 생기게 됩니다.



위 그림에서 ∨ 모양이 생긴 부분은 점선(0)으로, ∧ 모양이 생긴 부분은 실선(1)으로 표시했습니다.

종이를 접은 횟수 n이 매개변수로 주어질 때, 종이를 절반씩 n번 접은 후 모두 펼쳤을 때 생기는 
접힌 부분의 모양을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
종이를 접는 횟수 n은 1 이상 20 이하의 자연수입니다.
종이를 접었다 편 후 생긴 굴곡이 ∨ 모양이면 0, ∧ 모양이면 1로 나타냅니다.
가장 왼쪽의 굴곡 모양부터 순서대로 배열에 담아 return 해주세요.
'''
n = 1	#result = [0]
n = 2	#result = [0,0,1]
n = 3	#result = [0,0,1,0,0,1,1]

origami = {
    1:[0],
    2:[0,0,1]
}

def reverse(x):
    if x ==0:
        return 1
    else:
        return 0

def solution(n):
    if n in origami:
        return origami[n]
    else:
        arr = solution(n-1) + [0] + list(map(reverse,reversed(solution(n-1))))
        origami[n] = arr
        return arr
    

#origami[n] = origami[n-1] + [0] + list(map(reverse,origami[n-1]))
print(solution(4))
print(solution(8))