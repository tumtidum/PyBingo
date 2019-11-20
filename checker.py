"""PyBingo full-card-checker with GUI v0.0.2  - Python 3.x - tumtidum.

With this script you can check during a game wether a full-card-BINGO
is true or false on any of the cards from the loaded set of sheets.

"""

# import sys
from mod.check_bingo import (CsvToList, Bingo)
from tkinter import (ttk, Tk, filedialog, Frame, N, W, E, S, IntVar,
                     StringVar, END, Scrollbar, Listbox)


class App(Frame):
    """Main GUI application (tkinter)."""

    def askOpenFileName(self):
        """Summary here.

        This time the dialog just returns a filename and the
        file is opened by your own code.
        NOT working yet!

        """
        # Define options for opening or saving a file.
        self.file_opt = options = {}
        options['defaultextension'] = '.csv'
        options['filetypes'] = [('all files', '.*'), ('csv files', '.csv')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'myfile.csv'
        options['parent'] = root
        options['title'] = 'Open a sheet file (.csv)'
        # Get filename.
        filename = filedialog.askopenfilename(**self.file_opt)
        # Open file on your own.
        if filename:
            sheets = CsvToList(filename).getSheets()
            return(sheets)

    def __init__(self, root):
        """Summary here."""
        Frame.__init__(self, root)

        # Frames.
        rootframe = ttk.Frame(
            root,
            padding='16 12 16 12'
            )
        rootframe.grid(
            column=0,
            row=0,
            sticky=(N, W, E, S)
            )
        frame_one = ttk.Frame(
            rootframe,
            padding='4 16 4 4'
            )
        frame_one.grid(
            column=0,
            row=0,
            sticky=(N, W, E, S)
            )
        frame_two = ttk.Frame(
            rootframe,
            padding='4 16 4 4'
            )
        frame_two.grid(
            column=1,
            row=0,
            sticky=(N, W, E, S)
            )
        callingframe = ttk.LabelFrame(
            frame_one,
            text='Number calls',
            padding='8 8 8 8'
            )
        callingframe.grid(
            column=0,
            row=0,
            sticky=(N, W, E, S)
            )
        roundsframe = ttk.LabelFrame(
            frame_one,
            text='Round',
            padding='8 8 8 8'
            )
        roundsframe.grid(
            column=1,
            row=0,
            sticky=(N, W, E, S)
            )
        bingocardframe = ttk.LabelFrame(
            frame_two,
            text='Winning cards',
            padding='8 8 8 8'
            )
        bingocardframe.grid(
            column=0,
            row=0,
            sticky=(N, W, E, S)
            )
        cardframe = ttk.LabelFrame(
            frame_two,
            text='Sheet & card',
            padding='8 8 8 8'
            )
        cardframe.grid(
            column=0,
            row=1,
            rowspan=2,
            sticky=(N, W, E, S)
            )
        cardgridframe = ttk.Frame(
            cardframe,
            padding='20 0 0 0'
            )
        cardgridframe.grid(
            column=1,
            row=0,
            rowspan=5,
            sticky=(N, W, E, S)
            )
        fileframe = ttk.LabelFrame(
            frame_two,
            text='File',
            padding='8 8 8 8'
            )
        fileframe.grid(
            column=0,
            row=3,
            sticky=W
            )

        # This is the variable bounded to checkbutton to get the
        # checkbutton state value.
        self.var = []
        for i in range(75):
            self.var.append(IntVar())

        # Variables bindings.
        ball_list_var = StringVar()
        cards_list_var = StringVar()
        round_var = StringVar()
        round_var.set('0')
        amount_cards_var = StringVar()
        amount_cards_var.set('0')
        called_card_var = StringVar()
        called_card_int_var = IntVar()
        called_card_int_var.set(1)
        called_card_str_var = StringVar()
        called_card_str_var.set('X')

        called_card_list_var = []
        for i in range(24):
            called_card_list_var.append(StringVar())

        card_num_colors = []
        for i in range(24):
            card_num_colors.append('yellow')

        # Open file.
        sheets1 = self.askOpenFileName()
        balls_in_play = []
        game1 = Bingo(balls_in_play, sheets1)

        def checkgame():
            """Check for matches.

            update ball/rounds listbox and matching
            sheets/cards listbox.

            """
            game1.bingoCheck()
            ball_list_var.set(game1.returnBallsInGame())
            round_var.set(len(game1.returnBallsInGame()))
            cards_list_var.set(game1.returnWinningCards())
            amount_cards_var.set(game1.bingoCheck())

            listbox1.delete(0, END)
            for i in game1.returnBallsInGame():
                listbox1.insert(0, i)
            listbox1.activate(0)
            listbox1.selection_set(0)

            listbox2.delete(0, END)
            for i in game1.returnWinningCards():
                listbox2.insert(0, i[:2])
            callingCard()

        def sel():
            """Update card display when changing X Y or Z."""
            callingCard()

        def callback(eventObject):
            """Update card display when changing sheet in combobox."""
            callingCard()

        def callingCard():
            """Check for matches on a card.

            Display green colors for the matches and
            red for the non-matches.

            """
            y = game1.checkCard(
                called_card_int_var.get(),
                called_card_str_var.get()
                )
            b = 0
            for x in y[0:24]:
                called_card_list_var[b].set(x[0])
                if x[1] is False:
                    card_num_colors[b] = '#e11'
                if x[1] is True:
                    card_num_colors[b] = '#292'
                b += 1
            G0.configure(foreground=card_num_colors[0])
            G1.configure(foreground=card_num_colors[1])
            G2.configure(foreground=card_num_colors[2])
            G3.configure(foreground=card_num_colors[3])
            G4.configure(foreground=card_num_colors[4])
            G5.configure(foreground=card_num_colors[5])
            G6.configure(foreground=card_num_colors[6])
            G7.configure(foreground=card_num_colors[7])
            G8.configure(foreground=card_num_colors[8])
            G9.configure(foreground=card_num_colors[9])
            G10.configure(foreground=card_num_colors[10])
            G11.configure(foreground=card_num_colors[11])
            G12.configure(foreground=card_num_colors[12])
            G13.configure(foreground=card_num_colors[13])
            G14.configure(foreground=card_num_colors[14])
            G15.configure(foreground=card_num_colors[15])
            G16.configure(foreground=card_num_colors[16])
            G17.configure(foreground=card_num_colors[17])
            G18.configure(foreground=card_num_colors[18])
            G19.configure(foreground=card_num_colors[19])
            G20.configure(foreground=card_num_colors[20])
            G21.configure(foreground=card_num_colors[21])
            G22.configure(foreground=card_num_colors[22])
            G23.configure(foreground=card_num_colors[23])
            called_card_var.set(y)

        # Change variables via checkboxes and check the game.
        def adding_removing_ball_1():
            game1.callBall(self.var[0].get())
            checkgame()

        def adding_removing_ball_2():
            game1.callBall(self.var[1].get())
            checkgame()

        def adding_removing_ball_3():
            game1.callBall(self.var[2].get())
            checkgame()

        def adding_removing_ball_4():
            game1.callBall(self.var[3].get())
            checkgame()

        def adding_removing_ball_5():
            game1.callBall(self.var[4].get())
            checkgame()

        def adding_removing_ball_6():
            game1.callBall(self.var[5].get())
            checkgame()

        def adding_removing_ball_7():
            game1.callBall(self.var[6].get())
            checkgame()

        def adding_removing_ball_8():
            game1.callBall(self.var[7].get())
            checkgame()

        def adding_removing_ball_9():
            game1.callBall(self.var[8].get())
            checkgame()

        def adding_removing_ball_10():
            game1.callBall(self.var[9].get())
            checkgame()

        def adding_removing_ball_11():
            game1.callBall(self.var[10].get())
            checkgame()

        def adding_removing_ball_12():
            game1.callBall(self.var[11].get())
            checkgame()

        def adding_removing_ball_13():
            game1.callBall(self.var[12].get())
            checkgame()

        def adding_removing_ball_14():
            game1.callBall(self.var[13].get())
            checkgame()

        def adding_removing_ball_15():
            game1.callBall(self.var[14].get())
            checkgame()

        def adding_removing_ball_16():
            game1.callBall(self.var[15].get())
            checkgame()

        def adding_removing_ball_17():
            game1.callBall(self.var[16].get())
            checkgame()

        def adding_removing_ball_18():
            game1.callBall(self.var[17].get())
            checkgame()

        def adding_removing_ball_19():
            game1.callBall(self.var[18].get())
            checkgame()

        def adding_removing_ball_20():
            game1.callBall(self.var[19].get())
            checkgame()

        def adding_removing_ball_21():
            game1.callBall(self.var[20].get())
            checkgame()

        def adding_removing_ball_22():
            game1.callBall(self.var[21].get())
            checkgame()

        def adding_removing_ball_23():
            game1.callBall(self.var[22].get())
            checkgame()

        def adding_removing_ball_24():
            game1.callBall(self.var[23].get())
            checkgame()

        def adding_removing_ball_25():
            game1.callBall(self.var[24].get())
            checkgame()

        def adding_removing_ball_26():
            game1.callBall(self.var[25].get())
            checkgame()

        def adding_removing_ball_27():
            game1.callBall(self.var[26].get())
            checkgame()

        def adding_removing_ball_28():
            game1.callBall(self.var[27].get())
            checkgame()

        def adding_removing_ball_29():
            game1.callBall(self.var[28].get())
            checkgame()

        def adding_removing_ball_30():
            game1.callBall(self.var[29].get())
            checkgame()

        def adding_removing_ball_31():
            game1.callBall(self.var[30].get())
            checkgame()

        def adding_removing_ball_32():
            game1.callBall(self.var[31].get())
            checkgame()

        def adding_removing_ball_33():
            game1.callBall(self.var[32].get())
            checkgame()

        def adding_removing_ball_34():
            game1.callBall(self.var[33].get())
            checkgame()

        def adding_removing_ball_35():
            game1.callBall(self.var[34].get())
            checkgame()

        def adding_removing_ball_36():
            game1.callBall(self.var[35].get())
            checkgame()

        def adding_removing_ball_37():
            game1.callBall(self.var[36].get())
            checkgame()

        def adding_removing_ball_38():
            game1.callBall(self.var[37].get())
            checkgame()

        def adding_removing_ball_39():
            game1.callBall(self.var[38].get())
            checkgame()

        def adding_removing_ball_40():
            game1.callBall(self.var[39].get())
            checkgame()

        def adding_removing_ball_41():
            game1.callBall(self.var[40].get())
            checkgame()

        def adding_removing_ball_42():
            game1.callBall(self.var[41].get())
            checkgame()

        def adding_removing_ball_43():
            game1.callBall(self.var[42].get())
            checkgame()

        def adding_removing_ball_44():
            game1.callBall(self.var[43].get())
            checkgame()

        def adding_removing_ball_45():
            game1.callBall(self.var[44].get())
            checkgame()

        def adding_removing_ball_46():
            game1.callBall(self.var[45].get())
            checkgame()

        def adding_removing_ball_47():
            game1.callBall(self.var[46].get())
            checkgame()

        def adding_removing_ball_48():
            game1.callBall(self.var[47].get())
            checkgame()

        def adding_removing_ball_49():
            game1.callBall(self.var[48].get())
            checkgame()

        def adding_removing_ball_50():
            game1.callBall(self.var[49].get())
            checkgame()

        def adding_removing_ball_51():
            game1.callBall(self.var[50].get())
            checkgame()

        def adding_removing_ball_52():
            game1.callBall(self.var[51].get())
            checkgame()

        def adding_removing_ball_53():
            game1.callBall(self.var[52].get())
            checkgame()

        def adding_removing_ball_54():
            game1.callBall(self.var[53].get())
            checkgame()

        def adding_removing_ball_55():
            game1.callBall(self.var[54].get())
            checkgame()

        def adding_removing_ball_56():
            game1.callBall(self.var[55].get())
            checkgame()

        def adding_removing_ball_57():
            game1.callBall(self.var[56].get())
            checkgame()

        def adding_removing_ball_58():
            game1.callBall(self.var[57].get())
            checkgame()

        def adding_removing_ball_59():
            game1.callBall(self.var[58].get())
            checkgame()

        def adding_removing_ball_60():
            game1.callBall(self.var[59].get())
            checkgame()

        def adding_removing_ball_61():
            game1.callBall(self.var[60].get())
            checkgame()

        def adding_removing_ball_62():
            game1.callBall(self.var[61].get())
            checkgame()

        def adding_removing_ball_63():
            game1.callBall(self.var[62].get())
            checkgame()

        def adding_removing_ball_64():
            game1.callBall(self.var[63].get())
            checkgame()

        def adding_removing_ball_65():
            game1.callBall(self.var[64].get())
            checkgame()

        def adding_removing_ball_66():
            game1.callBall(self.var[65].get())
            checkgame()

        def adding_removing_ball_67():
            game1.callBall(self.var[66].get())
            checkgame()

        def adding_removing_ball_68():
            game1.callBall(self.var[67].get())
            checkgame()

        def adding_removing_ball_69():
            game1.callBall(self.var[68].get())
            checkgame()

        def adding_removing_ball_70():
            game1.callBall(self.var[69].get())
            checkgame()

        def adding_removing_ball_71():
            game1.callBall(self.var[70].get())
            checkgame()

        def adding_removing_ball_72():
            game1.callBall(self.var[71].get())
            checkgame()

        def adding_removing_ball_73():
            game1.callBall(self.var[72].get())
            checkgame()

        def adding_removing_ball_74():
            game1.callBall(self.var[73].get())
            checkgame()

        def adding_removing_ball_75():
            game1.callBall(self.var[74].get())
            checkgame()

        # Listbox 1, displays the current round and called balls.
        scrollbar1 = Scrollbar(roundsframe)
        listbox1 = Listbox(
            roundsframe,
            width=3,
            height=31,
            yscrollcommand=scrollbar1.set
            )
        listbox1.grid(
            column=0,
            row=1,
            padx=8,
            pady=8,
            sticky=(N, S, E, W)
            )
        roundlabel = ttk.Label(
            roundsframe,
            textvariable=round_var,
            foreground='#666'
            )
        roundlabel.grid(
            column=0,
            row=0,
            padx=8,
            pady=0,
            sticky=W
            )
        scrollbar1.grid(
            column=1,
            row=1,
            padx=0,
            pady=8,
            sticky=(N, S, E, W)
            )
        scrollbar1.config(command=listbox1.yview)

        # Listbox 2, displays the winning sheets/cards.
        cardswinlabel = ttk.Label(
            bingocardframe,
            textvariable=amount_cards_var,
            foreground='#666'
            )
        cardswinlabel.grid(
            column=1,
            row=0,
            padx=8,
            pady=0,
            sticky=W
            )
        scrollbar2 = Scrollbar(bingocardframe)
        scrollbar2.grid(
            column=2,
            row=1,
            padx=0,
            pady=8,
            sticky=(N, S, E, W)
            )
        listbox2 = Listbox(
            bingocardframe,
            width=24,
            height=6,
            yscrollcommand=scrollbar2.set
            )
        listbox2.grid(
            column=1,
            row=1,
            padx=8,
            pady=8,
            sticky=(N, S, E, W)
            )
        scrollbar2.config(command=listbox2.yview)

        # Calling cards.
        L1 = int(len(sheets1) / 3 + 1)
        L2 = list(range(1, L1))

        called_card_int_entry = ttk.Combobox(
            cardframe,
            width=5,
            value=L2,
            textvariable=called_card_int_var,
            state='readonly'
            )
        called_card_int_entry.grid(
            column=0,
            row=0,
            padx=1,
            sticky=W
            )
        called_card_int_entry.config(validate='all')
        called_card_int_entry.current(0)
        called_card_int_entry.bind("<<ComboboxSelected>>", callback)

        R1 = ttk.Radiobutton(
            cardframe,
            text='X',
            variable=called_card_str_var,
            value='X',
            command=sel
            )
        R1.grid(
            column=0,
            row=1,
            sticky=W,
            padx=1
            )
        R2 = ttk.Radiobutton(
            cardframe,
            text='Y',
            variable=called_card_str_var,
            value='Y',
            command=sel
            )
        R2.grid(
            column=0,
            row=2,
            sticky=W,
            padx=1
            )
        R3 = ttk.Radiobutton(
            cardframe,
            text='Z',
            variable=called_card_str_var,
            value='Z',
            command=sel
            )
        R3.grid(
            column=0,
            row=3,
            sticky=W,
            padx=1
            )

        load_button = ttk.Button(
            fileframe,
            text='Load set',
            command=self.askOpenFileName
            )
        load_button.grid(
            column=0,
            row=0,
            columnspan=1,
            padx=8,
            pady=8,
            sticky=W
            )
        file_label = ttk.Label(
            fileframe,
            text='Current set in use: filename here'
            )
        file_label.grid(
            column=0,
            row=1,
            columnspan=1,
            padx=8,
            pady=8,
            sticky=W
            )

        # Grid for the active card to be displayed.
        gridpadding = 4
        gridsticky = (N, E, S, W)

        G0 = ttk.Label(cardgridframe, textvariable=called_card_list_var[0])
        G0.grid(
            column=0,
            row=4,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G1 = ttk.Label(cardgridframe, textvariable=called_card_list_var[1])
        G1.grid(
            column=0,
            row=3,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G2 = ttk.Label(cardgridframe, textvariable=called_card_list_var[2])
        G2.grid(
            column=0,
            row=2,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G3 = ttk.Label(cardgridframe, textvariable=called_card_list_var[3])
        G3.grid(
            column=0,
            row=1,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G4 = ttk.Label(cardgridframe, textvariable=called_card_list_var[4])
        G4.grid(
            column=0,
            row=0,
            padx=gridpadding,
            pady=4,
            sticky=gridsticky
            )
        G5 = ttk.Label(cardgridframe, textvariable=called_card_list_var[5])
        G5.grid(
            column=1,
            row=4,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G6 = ttk.Label(cardgridframe, textvariable=called_card_list_var[6])
        G6.grid(
            column=1,
            row=3,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G7 = ttk.Label(cardgridframe, textvariable=called_card_list_var[7])
        G7.grid(
            column=1,
            row=2,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G8 = ttk.Label(cardgridframe, textvariable=called_card_list_var[8])
        G8.grid(
            column=1,
            row=1,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G9 = ttk.Label(cardgridframe, textvariable=called_card_list_var[9])
        G9.grid(
            column=1,
            row=0,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G10 = ttk.Label(cardgridframe, textvariable=called_card_list_var[10])
        G10.grid(
            column=2,
            row=4,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G11 = ttk.Label(cardgridframe, textvariable=called_card_list_var[11])
        G11.grid(
            column=2,
            row=3,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G12 = ttk.Label(cardgridframe, textvariable=called_card_list_var[12])
        G12.grid(
            column=2,
            row=1,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G13 = ttk.Label(cardgridframe, textvariable=called_card_list_var[13])
        G13.grid(
            column=2,
            row=0,
            padx=gridpadding,
            pady=gridpadding,
            sticky=(W, E, N, S)
            )
        G14 = ttk.Label(cardgridframe, textvariable=called_card_list_var[14])
        G14.grid(
            column=3,
            row=4,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G15 = ttk.Label(cardgridframe, textvariable=called_card_list_var[15])
        G15.grid(
            column=3,
            row=3,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G16 = ttk.Label(cardgridframe, textvariable=called_card_list_var[16])
        G16.grid(
            column=3,
            row=2,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G17 = ttk.Label(cardgridframe, textvariable=called_card_list_var[17])
        G17.grid(
            column=3,
            row=1,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G18 = ttk.Label(cardgridframe, textvariable=called_card_list_var[18])
        G18.grid(
            column=3,
            row=0,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G19 = ttk.Label(cardgridframe, textvariable=called_card_list_var[19])
        G19.grid(
            column=4,
            row=4,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G20 = ttk.Label(cardgridframe, textvariable=called_card_list_var[20])
        G20.grid(
            column=4,
            row=3,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G21 = ttk.Label(cardgridframe, textvariable=called_card_list_var[21])
        G21.grid(
            column=4,
            row=2,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G22 = ttk.Label(cardgridframe, textvariable=called_card_list_var[22])
        G22.grid(
            column=4,
            row=1,
            padx=gridpadding,
            pady=gridpadding,
            sticky=gridsticky
            )
        G23 = ttk.Label(cardgridframe, textvariable=called_card_list_var[23])
        G23.grid(
            column=4,
            row=0,
            padx=gridpadding,
            pady=gridpadding,
            sticky=(W, E, N, S)
            )

        # Check buttons for active balls/numbers.
        checkpadding = 8
        checksticky = W

        self.checkbutton1 = ttk.Checkbutton(
            callingframe,
            text='1',
            command=adding_removing_ball_1,
            variable=self.var[0],
            onvalue=1,
            offvalue=-1
            )
        self.checkbutton1.grid(
            column=0,
            row=0,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton2 = ttk.Checkbutton(
            callingframe,
            text='2',
            command=adding_removing_ball_2,
            variable=self.var[1],
            onvalue=2,
            offvalue=-2
            )
        self.checkbutton2.grid(
            column=0,
            row=1,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton3 = ttk.Checkbutton(
            callingframe,
            text='3',
            command=adding_removing_ball_3,
            variable=self.var[2],
            onvalue=3,
            offvalue=-3
            )
        self.checkbutton3.grid(
            column=0,
            row=2,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton4 = ttk.Checkbutton(
            callingframe,
            text='4',
            command=adding_removing_ball_4,
            variable=self.var[3],
            onvalue=4,
            offvalue=-4
            )
        self.checkbutton4.grid(
            column=0,
            row=3,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton5 = ttk.Checkbutton(
            callingframe,
            text='5',
            command=adding_removing_ball_5,
            variable=self.var[4],
            onvalue=5,
            offvalue=-5
            )
        self.checkbutton5.grid(
            column=0,
            row=4,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton6 = ttk.Checkbutton(
            callingframe,
            text='6',
            command=adding_removing_ball_6,
            variable=self.var[5],
            onvalue=6,
            offvalue=-6
            )
        self.checkbutton6.grid(
            column=0,
            row=5,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton7 = ttk.Checkbutton(
            callingframe,
            text='7',
            command=adding_removing_ball_7,
            variable=self.var[6],
            onvalue=7,
            offvalue=-7
            )
        self.checkbutton7.grid(
            column=0,
            row=6,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton8 = ttk.Checkbutton(
            callingframe,
            text='8',
            command=adding_removing_ball_8,
            variable=self.var[7],
            onvalue=8,
            offvalue=-8
            )
        self.checkbutton8.grid(
            column=0,
            row=7,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton9 = ttk.Checkbutton(
            callingframe,
            text='9',
            command=adding_removing_ball_9,
            variable=self.var[8],
            onvalue=9,
            offvalue=-9
            )
        self.checkbutton9.grid(
            column=0,
            row=8,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton10 = ttk.Checkbutton(
            callingframe,
            text='10',
            command=adding_removing_ball_10,
            variable=self.var[9],
            onvalue=10,
            offvalue=-10
            )
        self.checkbutton10.grid(
            column=0,
            row=9,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton11 = ttk.Checkbutton(
            callingframe,
            text='11',
            command=adding_removing_ball_11,
            variable=self.var[10],
            onvalue=11,
            offvalue=-11
            )
        self.checkbutton11.grid(
            column=0,
            row=10,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton12 = ttk.Checkbutton(
            callingframe,
            text='12',
            command=adding_removing_ball_12,
            variable=self.var[11],
            onvalue=12,
            offvalue=-12
            )
        self.checkbutton12.grid(
            column=0,
            row=11,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton13 = ttk.Checkbutton(
            callingframe,
            text='13',
            command=adding_removing_ball_13,
            variable=self.var[12],
            onvalue=13,
            offvalue=-13
            )
        self.checkbutton13.grid(
            column=0,
            row=12,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton14 = ttk.Checkbutton(
            callingframe,
            text='14',
            command=adding_removing_ball_14,
            variable=self.var[13],
            onvalue=14,
            offvalue=-14
            )
        self.checkbutton14.grid(
            column=0,
            row=13,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton15 = ttk.Checkbutton(
            callingframe,
            text='15',
            command=adding_removing_ball_15,
            variable=self.var[14],
            onvalue=15,
            offvalue=-15
            )
        self.checkbutton15.grid(
            column=0,
            row=14,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton16 = ttk.Checkbutton(
            callingframe,
            text='16',
            command=adding_removing_ball_16,
            variable=self.var[15],
            onvalue=16,
            offvalue=-16
            )
        self.checkbutton16.grid(
            column=1,
            row=0,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton17 = ttk.Checkbutton(
            callingframe,
            text='17',
            command=adding_removing_ball_17,
            variable=self.var[16],
            onvalue=17,
            offvalue=-17
            )
        self.checkbutton17.grid(
            column=1,
            row=1,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton18 = ttk.Checkbutton(
            callingframe,
            text='18',
            command=adding_removing_ball_18,
            variable=self.var[17],
            onvalue=18,
            offvalue=-18
            )
        self.checkbutton18.grid(
            column=1,
            row=2,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton19 = ttk.Checkbutton(
            callingframe,
            text='19',
            command=adding_removing_ball_19,
            variable=self.var[18],
            onvalue=19,
            offvalue=-19
            )
        self.checkbutton19.grid(
            column=1,
            row=3,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton20 = ttk.Checkbutton(
            callingframe,
            text='20',
            command=adding_removing_ball_20,
            variable=self.var[19],
            onvalue=20,
            offvalue=-20
            )
        self.checkbutton20.grid(
            column=1,
            row=4,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton21 = ttk.Checkbutton(
            callingframe,
            text='21',
            command=adding_removing_ball_21,
            variable=self.var[20],
            onvalue=21,
            offvalue=-21
            )
        self.checkbutton21.grid(
            column=1,
            row=5,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton22 = ttk.Checkbutton(
            callingframe,
            text='22',
            command=adding_removing_ball_22,
            variable=self.var[21],
            onvalue=22,
            offvalue=-22
            )
        self.checkbutton22.grid(
            column=1,
            row=6,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton23 = ttk.Checkbutton(
            callingframe,
            text='23',
            command=adding_removing_ball_23,
            variable=self.var[22],
            onvalue=23,
            offvalue=-23
            )
        self.checkbutton23.grid(
            column=1,
            row=7,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton24 = ttk.Checkbutton(
            callingframe,
            text='24',
            command=adding_removing_ball_24,
            variable=self.var[23],
            onvalue=24,
            offvalue=-24
            )
        self.checkbutton24.grid(
            column=1,
            row=8,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton25 = ttk.Checkbutton(
            callingframe,
            text='25',
            command=adding_removing_ball_25,
            variable=self.var[24],
            onvalue=25,
            offvalue=-25
            )
        self.checkbutton25.grid(
            column=1,
            row=9,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton26 = ttk.Checkbutton(
            callingframe,
            text='26',
            command=adding_removing_ball_26,
            variable=self.var[25],
            onvalue=26,
            offvalue=-26
            )
        self.checkbutton26.grid(
            column=1,
            row=10,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton27 = ttk.Checkbutton(
            callingframe,
            text='27',
            command=adding_removing_ball_27,
            variable=self.var[26],
            onvalue=27,
            offvalue=-27
            )
        self.checkbutton27.grid(
            column=1,
            row=11,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton28 = ttk.Checkbutton(
            callingframe,
            text='28',
            command=adding_removing_ball_28,
            variable=self.var[27],
            onvalue=28,
            offvalue=-28
            )
        self.checkbutton28.grid(
            column=1,
            row=12,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton29 = ttk.Checkbutton(
            callingframe,
            text='29',
            command=adding_removing_ball_29,
            variable=self.var[28],
            onvalue=29,
            offvalue=-29
            )
        self.checkbutton29.grid(
            column=1,
            row=13,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton30 = ttk.Checkbutton(
            callingframe,
            text='30',
            command=adding_removing_ball_30,
            variable=self.var[29],
            onvalue=30,
            offvalue=-30
            )
        self.checkbutton30.grid(
            column=1,
            row=14,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton31 = ttk.Checkbutton(
            callingframe,
            text='31',
            command=adding_removing_ball_31,
            variable=self.var[30],
            onvalue=31,
            offvalue=-31
            )
        self.checkbutton31.grid(
            column=2,
            row=0,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton32 = ttk.Checkbutton(
            callingframe,
            text='32',
            command=adding_removing_ball_32,
            variable=self.var[31],
            onvalue=32,
            offvalue=-32
            )
        self.checkbutton32.grid(
            column=2,
            row=1,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton33 = ttk.Checkbutton(
            callingframe,
            text='33',
            command=adding_removing_ball_33,
            variable=self.var[32],
            onvalue=33,
            offvalue=-33
            )
        self.checkbutton33.grid(
            column=2,
            row=2,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton34 = ttk.Checkbutton(
            callingframe,
            text='34',
            command=adding_removing_ball_34,
            variable=self.var[33],
            onvalue=34,
            offvalue=-34
            )
        self.checkbutton34.grid(
            column=2,
            row=3,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton35 = ttk.Checkbutton(
            callingframe,
            text='35',
            command=adding_removing_ball_35,
            variable=self.var[34],
            onvalue=35,
            offvalue=-35
            )
        self.checkbutton35.grid(
            column=2,
            row=4,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton36 = ttk.Checkbutton(
            callingframe,
            text='36',
            command=adding_removing_ball_36,
            variable=self.var[35],
            onvalue=36,
            offvalue=-36
            )
        self.checkbutton36.grid(
            column=2,
            row=5,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton37 = ttk.Checkbutton(
            callingframe,
            text='37',
            command=adding_removing_ball_37,
            variable=self.var[36],
            onvalue=37,
            offvalue=-37
            )
        self.checkbutton37.grid(
            column=2,
            row=6,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton38 = ttk.Checkbutton(
            callingframe,
            text='38',
            command=adding_removing_ball_38,
            variable=self.var[37],
            onvalue=38,
            offvalue=-38
            )
        self.checkbutton38.grid(
            column=2,
            row=7,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton39 = ttk.Checkbutton(
            callingframe,
            text='39',
            command=adding_removing_ball_39,
            variable=self.var[38],
            onvalue=39,
            offvalue=-39
            )
        self.checkbutton39.grid(
            column=2,
            row=8,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton40 = ttk.Checkbutton(
            callingframe,
            text='40',
            command=adding_removing_ball_40,
            variable=self.var[39],
            onvalue=40,
            offvalue=-40
            )
        self.checkbutton40.grid(
            column=2,
            row=9,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton41 = ttk.Checkbutton(
            callingframe,
            text='41',
            command=adding_removing_ball_41,
            variable=self.var[40],
            onvalue=41,
            offvalue=-41
            )
        self.checkbutton41.grid(
            column=2,
            row=10,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton42 = ttk.Checkbutton(
            callingframe,
            text='42',
            command=adding_removing_ball_42,
            variable=self.var[41],
            onvalue=42,
            offvalue=-42
            )
        self.checkbutton42.grid(
            column=2,
            row=11,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton43 = ttk.Checkbutton(
            callingframe,
            text='43',
            command=adding_removing_ball_43,
            variable=self.var[42],
            onvalue=43,
            offvalue=-43
            )
        self.checkbutton43.grid(
            column=2,
            row=12,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton44 = ttk.Checkbutton(
            callingframe,
            text='44',
            command=adding_removing_ball_44,
            variable=self.var[43],
            onvalue=44,
            offvalue=-44
            )
        self.checkbutton44.grid(
            column=2,
            row=13,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton45 = ttk.Checkbutton(
            callingframe,
            text='45',
            command=adding_removing_ball_45,
            variable=self.var[44],
            onvalue=45,
            offvalue=-45
            )
        self.checkbutton45.grid(
            column=2,
            row=14,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton46 = ttk.Checkbutton(
            callingframe,
            text='46',
            command=adding_removing_ball_46,
            variable=self.var[45],
            onvalue=46,
            offvalue=-46
            )
        self.checkbutton46.grid(
            column=3,
            row=0,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton47 = ttk.Checkbutton(
            callingframe,
            text='47',
            command=adding_removing_ball_47,
            variable=self.var[46],
            onvalue=47,
            offvalue=-47
            )
        self.checkbutton47.grid(
            column=3,
            row=1,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton48 = ttk.Checkbutton(
            callingframe,
            text='48',
            command=adding_removing_ball_48,
            variable=self.var[47],
            onvalue=48,
            offvalue=-48
            )
        self.checkbutton48.grid(
            column=3,
            row=2,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton49 = ttk.Checkbutton(
            callingframe,
            text='49',
            command=adding_removing_ball_49,
            variable=self.var[48],
            onvalue=49,
            offvalue=-49
            )
        self.checkbutton49.grid(
            column=3,
            row=3,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton50 = ttk.Checkbutton(
            callingframe,
            text='50',
            command=adding_removing_ball_50,
            variable=self.var[49],
            onvalue=50,
            offvalue=-50
            )
        self.checkbutton50.grid(
            column=3,
            row=4,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton51 = ttk.Checkbutton(
            callingframe,
            text='51',
            command=adding_removing_ball_51,
            variable=self.var[50],
            onvalue=51,
            offvalue=-51
            )
        self.checkbutton51.grid(
            column=3,
            row=5,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton52 = ttk.Checkbutton(
            callingframe,
            text='52',
            command=adding_removing_ball_52,
            variable=self.var[51],
            onvalue=52,
            offvalue=-52
            )
        self.checkbutton52.grid(
            column=3,
            row=6,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton53 = ttk.Checkbutton(
            callingframe,
            text='53',
            command=adding_removing_ball_53,
            variable=self.var[52],
            onvalue=53,
            offvalue=-53
            )
        self.checkbutton53.grid(
            column=3,
            row=7,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton54 = ttk.Checkbutton(
            callingframe,
            text='54',
            command=adding_removing_ball_54,
            variable=self.var[53],
            onvalue=54,
            offvalue=-54
            )
        self.checkbutton54.grid(
            column=3,
            row=8,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton55 = ttk.Checkbutton(
            callingframe,
            text='55',
            command=adding_removing_ball_55,
            variable=self.var[54],
            onvalue=55,
            offvalue=-55
            )
        self.checkbutton55.grid(
            column=3,
            row=9,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton56 = ttk.Checkbutton(
            callingframe,
            text='56',
            command=adding_removing_ball_56,
            variable=self.var[55],
            onvalue=56,
            offvalue=-56
            )
        self.checkbutton56.grid(
            column=3,
            row=10,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton57 = ttk.Checkbutton(
            callingframe,
            text='57',
            command=adding_removing_ball_57,
            variable=self.var[56],
            onvalue=57,
            offvalue=-57
            )
        self.checkbutton57.grid(
            column=3,
            row=11,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton58 = ttk.Checkbutton(
            callingframe,
            text='58',
            command=adding_removing_ball_58,
            variable=self.var[57],
            onvalue=58,
            offvalue=-58
            )
        self.checkbutton58.grid(
            column=3,
            row=12,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton59 = ttk.Checkbutton(
            callingframe,
            text='59',
            command=adding_removing_ball_59,
            variable=self.var[58],
            onvalue=59,
            offvalue=-59
            )
        self.checkbutton59.grid(
            column=3,
            row=13,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton60 = ttk.Checkbutton(
            callingframe,
            text='60',
            command=adding_removing_ball_60,
            variable=self.var[59],
            onvalue=60,
            offvalue=-60
            )
        self.checkbutton60.grid(
            column=3,
            row=14,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton61 = ttk.Checkbutton(
            callingframe,
            text='61',
            command=adding_removing_ball_61,
            variable=self.var[60],
            onvalue=61,
            offvalue=-61
            )
        self.checkbutton61.grid(
            column=4,
            row=0,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton62 = ttk.Checkbutton(
            callingframe,
            text='62',
            command=adding_removing_ball_62,
            variable=self.var[61],
            onvalue=62,
            offvalue=-62
            )
        self.checkbutton62.grid(
            column=4,
            row=1,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton63 = ttk.Checkbutton(
            callingframe,
            text='63',
            command=adding_removing_ball_63,
            variable=self.var[62],
            onvalue=63,
            offvalue=-63
            )
        self.checkbutton63.grid(
            column=4,
            row=2,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton64 = ttk.Checkbutton(
            callingframe,
            text='64',
            command=adding_removing_ball_64,
            variable=self.var[63],
            onvalue=64,
            offvalue=-64
            )
        self.checkbutton64.grid(
            column=4,
            row=3,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton65 = ttk.Checkbutton(
            callingframe,
            text='65',
            command=adding_removing_ball_65,
            variable=self.var[64],
            onvalue=65,
            offvalue=-65
            )
        self.checkbutton65.grid(
            column=4,
            row=4,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton66 = ttk.Checkbutton(
            callingframe,
            text='66',
            command=adding_removing_ball_66,
            variable=self.var[65],
            onvalue=66,
            offvalue=-66
            )
        self.checkbutton66.grid(
            column=4,
            row=5,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton67 = ttk.Checkbutton(
            callingframe,
            text='67',
            command=adding_removing_ball_67,
            variable=self.var[66],
            onvalue=67,
            offvalue=-67
            )
        self.checkbutton67.grid(
            column=4,
            row=6,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton68 = ttk.Checkbutton(
            callingframe,
            text='68',
            command=adding_removing_ball_68,
            variable=self.var[67],
            onvalue=68,
            offvalue=-68
            )
        self.checkbutton68.grid(
            column=4,
            row=7,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton69 = ttk.Checkbutton(
            callingframe,
            text='69',
            command=adding_removing_ball_69,
            variable=self.var[68],
            onvalue=69,
            offvalue=-69
            )
        self.checkbutton69.grid(
            column=4,
            row=8,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton70 = ttk.Checkbutton(
            callingframe,
            text='70',
            command=adding_removing_ball_70,
            variable=self.var[69],
            onvalue=70,
            offvalue=-70
            )
        self.checkbutton70.grid(
            column=4,
            row=9,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton71 = ttk.Checkbutton(
            callingframe,
            text='71',
            command=adding_removing_ball_71,
            variable=self.var[70],
            onvalue=71,
            offvalue=-71
            )
        self.checkbutton71.grid(
            column=4,
            row=10,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton72 = ttk.Checkbutton(
            callingframe,
            text='72',
            command=adding_removing_ball_72,
            variable=self.var[71],
            onvalue=72,
            offvalue=-72
            )
        self.checkbutton72.grid(
            column=4,
            row=11,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton73 = ttk.Checkbutton(
            callingframe,
            text='73',
            command=adding_removing_ball_73,
            variable=self.var[72],
            onvalue=73,
            offvalue=-73
            )
        self.checkbutton73.grid(
            column=4,
            row=12,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton74 = ttk.Checkbutton(
            callingframe,
            text='74',
            command=adding_removing_ball_74,
            variable=self.var[73],
            onvalue=74,
            offvalue=-74
            )
        self.checkbutton74.grid(
            column=4,
            row=13,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )
        self.checkbutton75 = ttk.Checkbutton(
            callingframe,
            text='75',
            command=adding_removing_ball_75,
            variable=self.var[74],
            onvalue=75,
            offvalue=-75
            )
        self.checkbutton75.grid(
            column=4,
            row=14,
            padx=checkpadding,
            pady=checkpadding,
            sticky=checksticky
            )


if __name__ == '__main__':
    root = Tk()
    root.title('PyBingo checker v0.0.2')
    app = App(root)
    root.mainloop()
