class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self.board = [[False]*3, [False]*3, [False]*3]
        self.board = self.create_board(width, height)
        self.new_board = self.create_board(width, height)

    def print_board(self):
        rv = ''
        for row in self.board:
            rv += ' '.join('FT'[c] for c in row)
            rv += '\n'
        return rv

    def create_board(self, width, height):
        tmp = []
        for row in range(height):
            tmp.append([False] * width)
        return tmp

    def place_cell(self, row_num, col_num):
        self.board[row_num][col_num] = True

    def flip_cell(self, width, height):
        print('------------------------------------------')
        for row in range(width):
            for col in range(height):
                n = self.get_number_neighbour(row, col)
                # print(n)
                if n == 3 and self.board[row][col] is False:
                    self.new_board[row][col] = True
                elif 2 <= n <=3 and self.board[row][col] is True:
                    self.new_board[row][col] = True
                else:
                    self.new_board[row][col] = False

        tmp = self.board
        self.board = self.new_board
        self.new_board = tmp



    def get_number_neighbour(self, row_num, col_num):
        accumulator = 0
        for r in (-1, 0, 1):
            for c in (-1, 0, 1):
                if r == c and r == 0:
                    continue
                if self.get_cell(row_num+r, col_num+c):
                    accumulator += 1

        return accumulator

    def get_cell(self, row_num, col_num):
        if 0 <= row_num < self.height:
            if 0 <= col_num < self.width:
                return self.board[row_num][col_num]
        return False


