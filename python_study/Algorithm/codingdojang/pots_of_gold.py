'''
A, B 두명의 플레이어가 있다.
한개의 선 위에 여러개의 금 항아리가 놓여져 있다. 각 항아리는 금화를 담고 있다.
(플레이어는 각 항아리에 얼마의 금화가 들어있는지 알 수 있다.) 
각 플레이어는 교대로 선에 놓여있는 양쪽 가장자리 항아리 중에서 한 개씩 선택 할 수 있다. 
(가장 우측 항아리 또는 가장 좌측 항아리 중 하나를 선택해야 한다.)
모든 항아리 선택이 끝난 후 가장 많은 금화를 차지한 플레이어가 승리하게 된다.
이 게임의 목표는 A가 먼저 게임을 시작할 때 A가 가장 많은(Maximize) 금화를 가질 수 있도록 하는 것이다.
B 역시 최적의 알고리즘으로 항아리를 선택한다고 가정한다.
A가 이길 수 있는 최선의 전략을 찾아 보시오. 그리고 이것을 프로그래밍 코드로 작성 해 보시오.
'''
#내 풀이 아님, 재귀공부

def maximize(pots):
    if not pots: return 0

    # A가 먼저 좌측을 선택할 경우
    choose_leftmost = pots[0]

    # B는 최적의 선택을 하므로 그 다음 A가 B이후에 가질 수 있는 값은
    # -> B가 좌측을 선택하고 남은 항아리들의 maximize값
    # -> B가 우측을 선택하고 남은 항아리들의 maximize값
    # 위 둘 중 작은 값을 가져야만 한다.
    # 왜냐하면 B가 최선의 선택을 하기 때문에 A는 둘 중에 작은 값을 가질 수 밖에 없다.
    next_choose_left = maximize(pots[2:])       # a가 좌측, b가 좌측선택
    next_choose_right = maximize(pots[1:-1])    # a가 좌측, b가 우측선택
    next_value = min(next_choose_left, next_choose_right)

    # 두 값을 더한다.
    left_case = choose_leftmost + next_value

    # 이번에는 A가 우측을 선택할 경우
    choose_rightmost = pots[-1]

    # 위와 마찬가지 경우이므로 설명 생략
    next_choose_left = maximize(pots[1:-1])     # a가 우측, b가 좌측
    next_choose_right = maximize(pots[0:-2])    # a가 우측, b가 우측
    next_value = min(next_choose_left, next_choose_right)

    # 두 값을 더한다.
    right_case = choose_rightmost + next_value

    
    # 최종적으로 둘중에 큰값을 리턴한다.
    return max(left_case, right_case)


print(maximize([9,8,7,5,4,6,3,1,2,7]))

