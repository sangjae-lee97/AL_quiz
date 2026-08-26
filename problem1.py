import random
# 2 <= N <= 64
# N은 항상 2의 거듭제공
# 각 픽셀은 0 또는 1

N = int(input("행령의 숫자를 입력하세요(2<=N<=64, N은 2의 거듭제곱): "))
matrix_64x64_random = [
    "".join(str(random.randint(0, 1)) for _ in range(N))
    for _ in range(N)
]

def compress(r, c, size):
    half = size // 2
    split_sections = [(r, c, half), (r, c + half, half), (r + half, c, half), (r + half, c + half, half)]
    first_color = matrix_64x64_random[r][c]
    is_same = True

    for i in range(r, r + size):
        for j in range(c, c + size):
            if matrix_64x64_random[i][j] != first_color:
                is_same = False
                break
        if is_same == False:
            break

    if is_same == False:
        print("(", end="")
        compress(r, c, half)
        compress(r, c + half, half)
        compress(r + half, c, half)
        compress(r + half, c + half, half)
        print(")", end="")
    else:
        print(first_color, end="")

compress(0,0,N)
