x = int(input())

center_row = x // 2

for i in range(x):

    spaces = " " * (x - i - 1)
    
    if i == center_row:
        side_hashes = "#" * i
        diamond_shape = "♦"
        content = side_hashes + diamond_shape + side_hashes
    else:
        content = "#" * (2 * i + 1)       
    print(spaces + content)