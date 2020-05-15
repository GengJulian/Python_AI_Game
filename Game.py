class Blue_red_game:
    def __init__(self):
        self.current_state = [['.', '.', '.', '.', '.'],
                              ['.', '.', '.', '.', '.'],
                              ['.', '.', '.', '.', '.'],
                              ['.', '.', '.', '.', '.'],
                              ['.', '.', '.', '.', '.']]
        self.result = None
        self.player_turn = 'B'

    def draw_board(self):
        for i in range(0, 5):
            print(" | ", self.current_state[i][0], " | ", self.current_state[i][1], " | ", self.current_state[i][2],
                  " | ", self.current_state[i][3], " | ", self.current_state[i][4], " |\n ")
        print()
    def play(self):
        self.game_loop()

    def game_loop(self):
        while True:
            self.draw_board()
            self.result = self.is_end_state()
            if self.result is not None:
                if self.result == 'B':
                    print("The winner is Blue!")
                elif self.result == 'R':
                    print("The winner is Red!")
                elif self.result == '.':
                    print("It's a tie!")
                return

            if self.player_turn == 'B':
                while True:

                    px = int(input("Insert the X coordinate: "))
                    py = int(input("Insert the Y coordinate: "))

                    if self.is_valid_position(px, py):
                        self.current_state[px][py] = 'B'
                        self.player_turn = 'R'
                        break
                    else:
                        print("The move is not valid! Try again.")

            else:
                """""
                while True:

                    px = int(input("Insert the X coordinate: "))
                    py = int(input("Insert the Y coordinate: "))

                    if self.is_valid_position(px, py):
                        self.current_state[px][py] = 'R'
                        self.player_turn = 'B'
                        break
                    else:
                        print("The move is not valid! Try again.")
                """""


                (m, px, py) = self.max(0,7,-2,2)
                self.current_state[px][py] = 'R'
                self.player_turn = 'B'

    def is_valid_position(self, x, y):
        if x < 0 or x > 4 or y < 0 or y > 4:
            return False
        elif self.current_state[x][y] != '.':
            return False
        else:
            return True

    def is_end_state(self):
        numberOfBlue = 0
        numberOfRed = 0

        # Vertical win
        for i in range(5):
            for j in range(5):
                if self.current_state[j][i] == 'B':
                    numberOfBlue += 1
                    if numberOfBlue == 3:
                        return 'R'
                elif self.current_state[j][i] == 'R':
                    numberOfRed += 1
                    if numberOfRed == 3:
                        return 'B'
            numberOfBlue = 0
            numberOfRed = 0

        # Horizontal win
        for i in range(5):
            for j in range(5):
                if self.current_state[i][j] == 'B':
                    numberOfBlue += 1
                    if numberOfBlue == 3:
                        return 'R'
                elif self.current_state[i][j] == 'R':
                    numberOfRed += 1
                    if numberOfRed == 3:
                        return 'B'
            numberOfBlue = 0
            numberOfRed = 0

        # főátlók vizsgálata
        for k in range(2, 5):
            i = k
            j = 0
            while i >= 0:
                if self.current_state[i][j] == 'B':
                    numberOfBlue += 1
                    # print("kékek száma felső főátlókban")
                    # print(numberOfBlue)
                    if numberOfBlue == 3:
                        return 'R'
                elif self.current_state[i][j] == 'R':
                    numberOfRed += 1
                    if numberOfRed == 3:
                        return 'B'

                i = i - 1
                j = j + 1

            numberOfBlue = 0
            numberOfRed = 0

        for k in range(1, 3):
            i = 4
            j = k
            while j <= 4:
                if self.current_state[i][j] == 'B':
                    numberOfBlue += 1
                    # print("kékek száma alső főtálókban")
                    # print(numberOfBlue)
                    if numberOfBlue == 3:
                        return 'R'
                elif self.current_state[i][j] == 'R':
                    numberOfRed += 1
                    if numberOfRed == 3:
                        return 'B'

                i = i - 1
                j = j + 1

            numberOfBlue = 0
            numberOfRed = 0

        # másod átlók
        for k in range(2, 5):
            i = k
            j = 4
            while i >= 0:
                if self.current_state[j][i] == 'B':
                    numberOfBlue += 1
                    # print("kékek száma az alsó mellékátlókban")
                    # print(numberOfBlue)
                    if numberOfBlue == 3:
                        return 'R'
                elif self.current_state[j][i] == 'R':
                    numberOfRed += 1
                    if numberOfRed == 3:
                        return 'B'

                i = i - 1
                j = j - 1

            numberOfBlue = 0
            numberOfRed = 0

        for k in range(3, 1, -1):
            j = k
            i = 4

            while j >= 0:
                if self.current_state[j][i] == 'B':
                    numberOfBlue += 1
                    # print("kékek száma a felső mellékátlókban")
                    # print(numberOfBlue)
                    if numberOfBlue == 3:
                        return 'R'
                elif self.current_state[j][i] == 'R':
                    numberOfRed += 1
                    if numberOfRed == 3:
                        return 'B'

                i = i - 1
                j = j - 1

            numberOfBlue = 0
            numberOfRed = 0

        # BOARD FULL
        for i in range(5):
            for j in range(5):
                if self.current_state[i][j] == '.':
                    return None
        return '.'

    def max(self,depth,depth_limit,alpha,beta):
        maxvalue = -2
        px = None
        py = None

        if depth == depth_limit:
            return maxvalue, px, py
        result = self.is_end_state()

        if result == 'B':
            return -1, 0, 0
        elif result == 'R':

            return 1, 0, 0
        elif result == '.':
            return 0, 0, 0

        for i in range(5):
            for j in range(5):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'R'
                    #self.draw_board()
                    (m, min_i, min_j) = self.min(depth + 1, depth_limit,alpha,beta)
                    if m > maxvalue:
                        maxvalue = m
                        px = i
                        py = j

                    self.current_state[i][j] = '.'

                    if maxvalue >= beta:
                        return maxvalue, px, py

                    if maxvalue > alpha:
                        alpha = maxvalue

        return maxvalue, px, py

    def min(self,depth,depth_limit,alpha,beta):
        minvalue = 2
        qx = None
        qy = None

        if depth == depth_limit:
            return minvalue, qx, qy

        result = self.is_end_state()

        if result == 'B':
            return -1, 0, 0
        elif result == 'R':
            return 1, 0, 0
        elif result == '.':
            return 0, 0, 0

        for i in range(5):
            for j in range(5):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'B'
                    #self.draw_board()
                    (m, max_i, max_j) = self.max(depth+1,depth_limit,alpha,beta)
                    if m < minvalue:
                        minvalue = m
                        qx = i
                        qy = j

                    self.current_state[i][j] = '.'

                    if minvalue <= alpha:
                        return minvalue, qx ,qy

                    if minvalue< beta:
                        beta = minvalue

        return minvalue, qx, qy
