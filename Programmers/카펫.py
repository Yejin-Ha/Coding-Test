def solution(brown, yellow):
    for row in range(1, int(yellow**0.5)+1):
        # row가 yellow의 약수라면
        if yellow % row == 0:
            col = yellow // row

            # 카펫의 둘레와 일치하는지 확인
            if 2 * row + 2 * col + 4 == brown:
                # row가 yellow의 제곱근이므로 값이 작을 수 밖에 없다.
                # 문제의 조건이 가로 길이(col+2)는 세로 길이(row+2)와 같거나 커야 한다.
                return [col+2, row+2]
