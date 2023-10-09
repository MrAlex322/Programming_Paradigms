class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def display_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * 9)

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def make_move(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2 or self.board[row][col] != ' ':
            return False  # Некорректный ход
        self.board[row][col] = self.current_player
        return True

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.display_board()
            print(f'Ход игрока {self.current_player}')
            
            # Ввод координат от игрока
            row = int(input('Введите номер строки (0, 1, 2): '))
            col = int(input('Введите номер столбца (0, 1, 2): '))
            
            if self.make_move(row, col):
                if self.check_winner(self.current_player):
                    self.display_board()
                    print(f'Игрок {self.current_player} победил!')
                    break
                elif self.check_draw():
                    self.display_board()
                    print('Ничья!')
                    break
                self.switch_player()
            else:
                print('Некорректный ход. Попробуйте снова.')


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
