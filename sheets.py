"""PyBingo sheets v0.0.2 - Python 3.x - tumtidum.

This script generates BINGO sheets and saves them to a PDF and
a CSV file (in the BINGO_sheets folder).
The PDF can be printed on paper while the CSV will be used for
the BINGO checker script.

This script runs in a terminal.

"""

import csv
import subprocess
import sys
import time
from random import randint, shuffle

import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.font_manager import FontProperties
from matplotlib.patches import Rectangle
from matplotlib.pyplot import clf, gcf, subplot, text


def userSheetsInput():
    """Interact with the user about the amount of sheets."""
    print('Type the amount of sheets you want to make and press ENTER:\n')
    AmountOfSheets = input('--> ')
    valid = AmountOfSheets.isdigit()
    if valid is False:
        print("That's not a valid entry, please try again.")
        return userSheetsInput()
    elif AmountOfSheets == '0':
        print('Made a whole lot of nothing.\n')
        pass
    # Too high amount protection, go back to user sheet input.
    elif int(AmountOfSheets) >= 100000:
        print("OMG! That's just too much! Pick something under " +
              "100,000 please.\nYou can always make several " +
              "sets if you REALLY need THAT many!" +
              "\nJust, give me a break pal! :P\n")
        return userSheetsInput()
    # High amount warning, let user decide to continue or go back.
    elif int(AmountOfSheets) >= 2000:
        sure = input("That's A LOT! Are you SURE you want to go " +
                     "there?! Y/N : ").lower()
        if sure == 'n' or sure == 'no':
            print("Yeah, maybe go for something a bit less " +
                  "ambitious indeed.\n")
            return userSheetsInput()
        if sure == 'y' or sure == 'yes':
            print("\nOk, off we go...")
            bingoStuff(int(AmountOfSheets))
            pass
        else:
            print("Sorry, I don't understand! Let's just start over.\n")
            return userSheetsInput()
    # All is ok, let's go!
    else:
        bingoStuff(int(AmountOfSheets))
        pass


def makeMoreSheets():
    """Ask the user wether to make more sets of sheets or not."""
    answer = input('Do you want to make more sheets? Y/N : ').lower()
    if answer == 'y' or answer == 'yes':
        print("\nOk, let's make more!")
        userSheetsInput()
        return makeMoreSheets()
    if answer == 'n' or answer == 'no':
        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('                      O K ,  B Y E !')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        pass
    else:
        print("Sorry, I don't understand! Please give a YES or NO answer.")
        return makeMoreSheets()


def idCode():
    """Make an hex ID code based on the current date and time."""
    Year = format(time.localtime()[0], '03X')
    Month = format(time.localtime()[1], 'X')
    Day = format(time.localtime()[2], '02X')
    Hours = format(time.localtime()[3], '02X')
    Minutes = format(time.localtime()[4], '02X')
    Seconds = format(time.localtime()[5], '02X')
    Random_num = format(randint(0, 255), '02X')
    code = (Year + Month + Day + Hours + '-' + Minutes + Seconds + Random_num)
    return code


def bingoStuff(user_given):
    """Do all kinda stuff and creates the BINGO sheets.

    Parameters
    ----------
    user_given : integer
        Amount of sheets the user gave as input.

    Returns
    -------
    files
        Both a CSV and a PDF file. The final BINGO sheets products.

    """
    # Get and open the enclosing folder for the sheets file.
    if sys.platform == 'darwin':
        def openFolder(sheet_path):
            subprocess.call(['open', '--', sheet_path])
    elif sys.platform == 'linux':
        def openFolder(sheet_path):
            subprocess.call(['xdg-open', sheet_path])
    elif sys.platform == 'win32':
        def openFolder(sheet_path):
            subprocess.call(['explorer', sheet_path])

    sheet_path = str(sys.path[0]) + '/BINGO_sheets/'
    idcode = idCode()
    naming = str('PyBingo-' + idcode)

    # Open/create a PDF file to write to.
    pp = PdfPages(sheet_path + naming + '.pdf')

    # Open/create a CSV file to write to.
    cvs_pathfile = (sheet_path + naming + '.csv')
    csv_file = open(cvs_pathfile, "w")
    writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)

    # Setting up PDF page (1 row, 2 columns).
    gs = gridspec.GridSpec(1, 2)

    # Will be used to switch columns on the PDF pages.
    l_r_switch = 'L'

    # Font settings.
    # Numbers on the cards.
    font1 = FontProperties(family='sans serif')
    font1.set_size('19')
    font1.set_weight('bold')
    # Free space text (X, Y, Z)
    font2 = FontProperties(family='sans serif')
    font2.set_size('39')
    font2.set_weight('black')
    # ID text under last card.
    font3 = FontProperties(family='monospace')
    font3.set_size('6')
    font3.set_weight('bold')
    # Sheet and number text.
    font5 = FontProperties(family='monospace')
    font5.set_size('10')
    font5.set_weight('bold')
    # Card header text (BINGO).
    font4 = FontProperties(family='sans serif')
    font4.set_size('34')
    font4.set_weight('black')
    # Used to center all numbers on the card grid.
    alignment = {'horizontalalignment': 'center',
                 'verticalalignment': 'center'
                 }
    # Used for sheet info/ID on bottom.
    alignment3 = {'horizontalalignment': 'left',
                  'verticalalignment': 'baseline'
                  }

    # Specifying a layout/grid using rectangles.
    def rectanglesCardHeader(x, y):
        """Draw rectangle for card header."""
        b = Rectangle(
            (x, y),
            width=5,
            height=0.8,
            color='#dddddd',
            fill=True
            )
        ax.add_patch(b)

    def rectanglesGrid(x, y):
        """Draw the rectangles for the number grid/cards."""
        for i in list(range(0, 5)):
            x1 = x
            for i in list(range(0, 5)):
                b = Rectangle(
                    (x1, y),
                    width=1,
                    height=1,
                    color='grey',
                    linewidth=1,
                    fill=False
                    )
                ax.add_patch(b)
                x1 += 1
            y += 1

    def cardHeaderText(x, y):
        """Header text for the cards."""
        for i in 'BINGO':
            text(
                x, y + 0.02,
                i,
                color='white',
                fontproperties=font4,
                **alignment
                )
            x += 1

    def textOnGrid(x, y, z):
        """Drawing the numbers/texts on the grid."""
        # First card on sheet.
        if z == 'X':
            number_list_b = B1
            number_list_i = I1
            number_list_n = N1
            number_list_g = G1
            number_list_o = O1
        # Second card on sheet.
        if z == 'Y':
            number_list_b = B2
            number_list_i = I2
            number_list_n = N2
            number_list_g = G2
            number_list_o = O2
        # Third card on sheet.
        if z == 'Z':
            number_list_b = B3
            number_list_i = I3
            number_list_n = N3
            number_list_g = G3
            number_list_o = O3

        letter = True
        q = 0
        for i in range(0, 5):
            text(
                x, y,
                number_list_b[i],
                fontproperties=font1,
                **alignment
                )
            text(
                x + 1, y,
                number_list_i[i],
                fontproperties=font1,
                **alignment
                )
            # If middle of card (free space).
            if i == 2 and letter is True:
                text(
                    x + 2, y - 0.05,
                    z,
                    color='#d6d6d6',
                    fontproperties=font2,
                    **alignment
                    )
                letter = False
                q -= 1
            else:
                text(
                    x + 2, y,
                    number_list_n[q],
                    fontproperties=font1,
                    **alignment
                    )
            text(
                x + 3, y,
                number_list_g[i],
                fontproperties=font1,
                **alignment
                )
            text(
                x + 4, y,
                number_list_o[i],
                fontproperties=font1,
                **alignment
                )
            q += 1
            y += 1

    def sheetInfo(x, y):
        """Place sheet info under each sheet (1 sheet is 3 cards)."""
        # ID code.
        text(
            x, y + 0.31,
            idcode,
            color='#a0a0a0',
            fontproperties=font3,
            **alignment3
            )
        text(
            x, y + 0.04,
            'Sheet :',
            color='#909090',
            fontproperties=font5,
            **alignment3
            )
        # Sheet number.
        text(
            x + 1.28,
            y + 0.04,
            u + 1,
            color='black',
            fontproperties=font5,
            **alignment3
            )

    # Lists of numbers for each BINGO column.
    B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    Ii = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    N = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
    G = [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
    Oo = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]

    def columnShuffle(x, y):
        """Shuffles all the numbers from a BINGO column.

        Parameters
        ----------
        x : list with integers
            All available numbers (15) for single BINGO column.
        y : integer
            Amount of available rows per column (use 5 or 4).

        Returns
        -------
        list
            Randomized list (with 5 or 4 numbers).

        """
        shuffle(x)
        a = x[:y]
        return a

    # The generating proces will start.
    print('\nGenerating... (this may take a while)')
    # Clear the figure.
    clf()

    # Do this for the given amount of sheets.
    for u in range(user_given):
        print(user_given)
        user_given -= 1

        # Choose page column to draw.
        if l_r_switch == 'L':
            ax = subplot(gs[0, 0])
        if l_r_switch == 'R':
            ax = subplot(gs[0, 1])

        # Get the current figure and set size.
        fig = gcf()
        fig.set_size_inches(8.27, 11.69)
        fig.set_tight_layout(True)
        # Margins of subplots.
        ax.set_axis_off()
        ax.set(xlim=(-0.7, 5.7), ylim=(0.35, 20))

        # Shuffle BINGO columns (for 3 cards on a sheet).
        B1 = columnShuffle(B, 5)
        B2 = columnShuffle(B, 5)
        B3 = columnShuffle(B, 5)
        I1 = columnShuffle(Ii, 5)
        I2 = columnShuffle(Ii, 5)
        I3 = columnShuffle(Ii, 5)
        N1 = columnShuffle(N, 4)
        N2 = columnShuffle(N, 4)
        N3 = columnShuffle(N, 4)
        G1 = columnShuffle(G, 5)
        G2 = columnShuffle(G, 5)
        G3 = columnShuffle(G, 5)
        O1 = columnShuffle(Oo, 5)
        O2 = columnShuffle(Oo, 5)
        O3 = columnShuffle(Oo, 5)

        # Make lists for the CSV file.
        BINGO1 = [int(u + 1), 'X']
        BINGO1 += B1 + I1 + N1 + G1 + O1
        BINGO2 = [int(u + 1), 'Y']
        BINGO2 += B2 + I2 + N2 + G2 + O2
        BINGO3 = [int(u + 1), 'Z']
        BINGO3 += B3 + I3 + N3 + G3 + O3

        # Writing lists as lines to the CSV file.
        for line in [BINGO1]:
            writer.writerow(line)
        for line in [BINGO2]:
            writer.writerow(line)
        for line in [BINGO3]:
            writer.writerow(line)

        # Place the grid and the shuffled numbers into the grids/cards.
        # Upper card -> X.
        rectanglesCardHeader(0, 19)
        cardHeaderText(0.5, 19.31)
        rectanglesGrid(0, 14)
        textOnGrid(0.5, 14.45, 'X')
        # Middle card -> Y.
        rectanglesCardHeader(0, 12.5)
        cardHeaderText(0.5, 12.81)
        rectanglesGrid(0, 7.5)
        textOnGrid(0.5, 7.95, 'Y')
        # Bottom card -> Z.
        rectanglesCardHeader(0, 6)
        cardHeaderText(0.5, 6.31)
        rectanglesGrid(0, 1)
        textOnGrid(0.5, 1.45, 'Z')
        sheetInfo(0, 0.35)

        # Column switcher, save page after second column or at last sheet.
        if user_given == 0:
            pp.savefig()
        elif l_r_switch == 'L':
            l_r_switch = 'R'
        elif l_r_switch == 'R':
            pp.savefig()
            clf()
            l_r_switch = 'L'

    # Close the PDF and CSV files and open the enclosing folder.
    print('.\nD O N E ! !\n')
    print('The file "' + naming + '.pdf" has been SAVED at:\n' +
          sheet_path, '\n')
    pp.close()
    csv_file.close()
    openFolder(sheet_path)
    return


# Now, let's rock!
print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
      '                   PyBingo Sheets v0.0.2\n'
      '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
      'This script generates BINGO playing sheets and saves them\n'
      'to a PDF file.')
userSheetsInput()
makeMoreSheets()
