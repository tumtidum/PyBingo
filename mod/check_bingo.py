"""PyBingo Check v0.0.2 - Python 3.x - tumtidum.

Here are some classes and definitions which will be used by the GUI
checker file. This file should NOT be executed by the user, to run the
BINGO checker, use the check_gui.py file.

"""

import csv
from random import shuffle


class CsvToList:
    """Import a csv file to a list in memory."""

    def __init__(self, csv_file):
        """Summary here."""
        self.a = csv_file
        self.bingo_sheet_list = []

        with open(self.a, newline='') as f:
            reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                self.bingo_sheet_list.append(row)
        f.close()
        # Convert all floats in list to integers, leave strings as they are.
        row_counter = -1
        while row_counter <= (len(self.bingo_sheet_list) - 2):
            row_counter += 1
            self.bingo_sheet_list[row_counter][0:1] = list(
                map(int, self.bingo_sheet_list[row_counter][0:1])
            )
            self.bingo_sheet_list[row_counter][2:] = list(
                map(int, self.bingo_sheet_list[row_counter][2:])
            )

    def getSheets(self):
        """Summary here."""
        return self.bingo_sheet_list


class Bingo:
    """Main BINGO class."""

    def __init__(self, initBalls, initSheets):
        """Summary here."""
        self.balls_in_game = initBalls
        self.bingo_sheet_list = initSheets
        self.winning_cards_list = []

    def shuffleBalls(value):
        """Shuffling balls.

        Generate a random number-sequence (of max. 75)
        for BINGO game testing.

        """
        drawn = []
        balls = list(range(1, 76))
        shuffle(balls)
        drawn = balls[:value]
        drawn.sort()
        return drawn

    def callBall(self, value):
        """Add or remove a ball/number."""
        # Add a ball.
        if int(value) > 0 and int(value) < 76:
            if int(value) not in self.balls_in_game:
                self.balls_in_game.append(int(value))
            else:
                print('That number is already in the list!')
                pass
        # Remove a ball.
        elif int(value) < 0 and int(value) > -76:
            if int(value * -1) not in self.balls_in_game:
                print('That number is not in the list!')
                pass
            else:
                self.balls_in_game.remove(int(value * -1))
        else:
            print("That's not a valid entry!")
            pass

    def bingoCheck(self):
        """Compare two lists to check if BINGO is true."""
        for x in self.bingo_sheet_list:
            y = set(x[2:]).intersection(self.balls_in_game)
            if len(y) >= 24 and x[0:2] not in self.winning_cards_list:
                self.winning_cards_list.append(x[0:2])
                # bingo = True
            if len(y) < 24 and x[0:2] in self.winning_cards_list:
                self.winning_cards_list.remove(x[0:2])
        # Calculate percentage of cards with BINGO in this set.
        if len(self.winning_cards_list) > 0:
            kans = round((100 / (int(len(self.bingo_sheet_list)/3)))
                         * len(self.winning_cards_list), 2)

        else:
            kans = 0

        kans_output = str(len(self.winning_cards_list)) + ' out of ' + str(
                      int(len(self.bingo_sheet_list)/3)) + '  (' + str(
                      kans) + '%)'
        return(kans_output)

    def returnBallsInGame(self):
        """Summary here."""
        return(self.balls_in_game)

    def returnWinningCards(self):
        """Summary here."""
        return(self.winning_cards_list)

    def checkCard(self, int_obj, str_obj):
        """Check a particular sheet/card."""
        # Get location of card.
        if str_obj == 'X':
            sheet_and_card = (int_obj - 1) * 3
        if str_obj == 'Y':
            sheet_and_card = ((int_obj - 1) * 3) + 1
        if str_obj == 'Z':
            sheet_and_card = ((int_obj - 1) * 3) + 2
        card = (self.bingo_sheet_list[sheet_and_card])
        # Get the missing numbers.
        missing = [x for x in card[2:] if x not in self.balls_in_game]
        y = []
        for z in card[2:]:
            if z in missing:
                y.append([z, False])
            else:
                y.append([z, True])
        return(y)
