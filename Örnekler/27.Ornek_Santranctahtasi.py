# Tahta boyutları
board_size = 8
square_size = 4

# Tahta renkleri
light_color = "\033[47m"
dark_color = "\033[40m"

# Tahta durumunu temsil eden liste
board = [[(i+j)%2 for i in range(board_size)] for j in range(board_size)]

# Tahtayı çizdirme
for i in range(board_size * square_size):
    for j in range(board_size * square_size):
        x = j // square_size
        y = i // square_size
        if board[y][x] == 0:
            color = light_color
        else:
            color = dark_color
        print(color + "  ", end="")
    print("\033[0m")
