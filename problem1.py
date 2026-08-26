import random

matrix_64x64_random = [
    "".join(str(random.randint(0, 1)) for _ in range(64))
    for _ in range(64)
]

def compress(r, c, size):
    half = size // 2
    split_sections = [(r, c, half), (r, c + half, half), (r + half, c, half), (r + half, c + half, half)]
    first_color = data[r][c]
    is_same = True

    for i in range(r, r + size):
        for j in range(c, c + size):
            if data[i][j] != first_color:
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


    


