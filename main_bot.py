import random
from tkinter import *
from tkinter import messagebox
import tkinter as tk

two_players = None
bot_first = True
moves_logger = []  # logs moves made by the players
button_names = {}

def multiplayer():
    global two_players
    two_players = True
    open_second_window()
def human_vs_bot():
    global two_players
    two_players = False
    open_second_window()

# ---------------------------------------------------------- #
start_center2nd = None
bot_corner1 = None
bot_strt_center_edg = None
bot_strt_center_crn = None
bot_strt_center_edge_fnl = None
bot_strt_mid_final = None
bot_strt_mid_2ndcorner = None
bot_strt_mid_corner_final = None
bot_corner_human_not_cntr = None
bot_corner_human_mid = None
bot_corner_human_notmid_final = None
bot_corner_human_mid1 = None
bot_corner_human_mid2 = None
human_1st = None
human_go_center = None
human_1st_is_center = None
human_1st_cntr3 = None
human_1st_cntr4 = None
human_go_corner = None
human_1st_diagonal = None
human_1st_diagonal2 = None
human_1st_no_diag = None
human_1st_no_diag2 = None
human_first_edge = None
human_first_edge2 = None
human_first_edge3 = None
human_first_edge_end = None
# ---------------------------------------------------------- #

# Create the main (welcome) window
root = tk.Tk()
root.title("Welcome to TicTacToe")
root.resizable(0, 0)

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the center position
window_width = 330
window_height = 150
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# Set the position and size of the root window
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

welcome_label = tk.Label(root, text="Welcome", font=("Arial", 15), width= 30)
welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

human_players = tk.Button(root, text="Two players", command=multiplayer)
human_players.grid(row=1, column=0, pady=10)

vs_bot = tk.Button(root, text="VS Bot", command=human_vs_bot)
vs_bot.grid(row=1, column=1, pady=10)

player_x = 0
player_o = 0

def open_second_window():
    root.withdraw()
    second_window = tk.Toplevel(root)
    second_window.title("TicTacToe")
    second_window.config(padx=30, pady=30, bg='#505251')
    second_window.resizable(0, 0)  # Disable resizing
    button_frame = Frame(second_window, bg='#505251')
    button_frame.grid(row=0, column=0)
    global player_x, player_o
    score = Label(second_window, text=f"X: {player_x} pts | O: {player_o} pts")
    score.grid(row=1, column=0, pady=5)


    # -------------------------- UI -------------------------------- #

    button1 = Button(second_window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e',
                     activebackground='#edbc2e',
                     command=lambda: on_button_click(button1))
    button_names[button1] = 'button1'

    button2 = Button(second_window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e',
                     activebackground='#edbc2e',
                     command=lambda: on_button_click(button2))
    button_names[button2] = 'button2'

    button3 = Button(second_window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e',
                     activebackground='#edbc2e',
                     command=lambda: on_button_click(button3))
    button_names[button3] = 'button3'

    button4 = Button(second_window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e',
                     activebackground='#edbc2e',
                     command=lambda: on_button_click(button4))
    button_names[button4] = 'button4'

    button5 = Button(second_window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e',
                     activebackground='#edbc2e',
                     command=lambda: on_button_click(button5))
    button_names[button5] = 'button5'

    button6 = Button(second_window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e',
                     activebackground='#edbc2e',
                     command=lambda: on_button_click(button6))
    button_names[button6] = 'button6'

    button7 = Button(second_window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e',
                     activebackground='#edbc2e',
                     command=lambda: on_button_click(button7))
    button_names[button7] = 'button7'

    button8 = Button(second_window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e',
                     activebackground='#edbc2e',
                     command=lambda: on_button_click(button8))
    button_names[button8] = 'button8'
    
    button9 = Button(second_window, text="", width=6, height=4, padx=5, pady=5, bd=2, bg='#edbc2e',
                     activebackground='#edbc2e',
                     command=lambda: on_button_click(button9))
    button_names[button9] = 'button9'

    button1.grid(row=0, column=0, in_=button_frame)
    button2.grid(row=0, column=1, in_=button_frame)
    button3.grid(row=0, column=2, in_=button_frame)
    button4.grid(row=1, column=0, in_=button_frame)
    button5.grid(row=1, column=1, in_=button_frame)
    button6.grid(row=1, column=2, in_=button_frame)
    button7.grid(row=2, column=0, in_=button_frame)
    button8.grid(row=2, column=1, in_=button_frame)
    button9.grid(row=2, column=2, in_=button_frame)

    buttons = {
        'button1': button1,
        'button2': button2,
        'button3': button3,
        'button4': button4,
        'button5': button5,
        'button6': button6,
        'button7': button7,
        'button8': button8,
        'button9': button9,
    }

    def second_window_close():
        second_window.destroy()

    exit_button = Button(second_window, text="Exit", command=second_window_close)
    exit_button.grid(row=2, column=0, pady=5)

    second_window.geometry(
        "+%d+%d" % (second_window.winfo_screenwidth() // 2.05 - 100, second_window.winfo_screenheight() // 2.3 - 100))
    messagebox.showinfo(title="Welcome", message="First player is X, next game O plays first",
                        parent=second_window)

    # -------------------------- UI -------------------------------- #

    def is_winner():
        global player_x, player_o
        # horizontal lines
        if button1.cget("text") == button2.cget("text") == button3.cget("text"):
            if button1.cget("text") == 'X':
                player_x += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player X won", parent=second_window)
                reset_game()
            elif button1.cget("text") == 'O':
                player_o += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player O won", parent=second_window)
                reset_game()

        elif button4.cget("text") == button5.cget("text") == button6.cget("text"):
            if button4.cget("text") == 'X':
                player_x += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player X won", parent=second_window)
                reset_game()
            elif button4.cget("text") == 'O':
                player_o += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player O won", parent=second_window)
                reset_game()

        elif button7.cget("text") == button8.cget("text") == button9.cget("text"):
            if button7.cget("text") == 'X':
                player_x += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player X won", parent=second_window)
                reset_game()
            elif button7.cget("text") == 'O':
                player_o += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player O won", parent=second_window)
                reset_game()

        # vertical lines
        elif button1.cget("text") == button4.cget("text") == button7.cget("text"):
            if button1.cget("text") == 'X':
                player_x += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player X won", parent=second_window)
                reset_game()
            elif button1.cget("text") == 'O':
                player_o += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player O won", parent=second_window)
                reset_game()

        elif button2.cget("text") == button5.cget("text") == button8.cget("text"):
            if button2.cget("text") == 'X':
                player_x += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player X won", parent=second_window)
                reset_game()
            elif button2.cget("text") == 'O':
                player_o += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player O won", parent=second_window)
                reset_game()

        elif button3.cget("text") == button6.cget("text") == button9.cget("text"):
            if button3.cget("text") == 'X':
                player_x += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player X won", parent=second_window)
                reset_game()
            elif button3.cget("text") == 'O':
                player_o += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player O won", parent=second_window)
                reset_game()

        # Diagonals
        elif button1.cget("text") == button5.cget("text") == button9.cget("text"):
            if button1.cget("text") == 'X':
                player_x += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player X won", parent=second_window)
                reset_game()
            elif button1.cget("text") == 'O':
                player_o += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player O won", parent=second_window)
                reset_game()

        elif button3.cget("text") == button5.cget("text") == button7.cget("text"):
            if button3.cget("text") == 'X':
                player_x += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player X won", parent=second_window)
                reset_game()
            elif button3.cget("text") == 'O':
                player_o += 1
                update_score()
                messagebox.showinfo(title="Winner", message="Player O won", parent=second_window)
                reset_game()
        elif all([button1.cget("text"), button2.cget("text"), button3.cget("text"),
                  button4.cget("text"), button5.cget("text"), button6.cget("text"),
                  button7.cget("text"), button8.cget("text"), button9.cget("text")]):
            messagebox.showinfo(title="Draw", message="It's a draw!", parent=second_window)
            reset_game()

    def button_name(button):
        return button_names[button]

    game_state = {"is_player_x_turn": True, "starting_player": "X"}

    # Function to handle button click FOR 2 PLAYERS
    def on_button_click(button):
        if button.cget('text') != '':
            return
        if two_players:
            if game_state["is_player_x_turn"]:
                button.config(text="X")
                moves_logger.append(button_name(button))
            else:
                button.config(text="O")
                moves_logger.append(button_name(button))
            game_state["is_player_x_turn"] = not game_state["is_player_x_turn"]
            is_winner()
        else:
            button.config(text="O")
            moves_logger.append(button_name(button))
            if start_center2nd:
                bot.bot_start_center()
            elif bot_corner1:
                bot.bot_start_corner()
            elif bot_strt_center_edg:
                bot.bot_start_center_edge()
            elif bot_strt_center_crn:
                bot.bot_start_center_corner()
            elif bot_strt_center_edge_fnl:
                bot.bot_start_center_edge_final()
            elif bot_strt_mid_final:
                bot.bot_start_center_final()
            elif bot_strt_mid_2ndcorner:
                bot.bot_start_center_corner_twice()
            elif bot_strt_mid_corner_final:
                bot.bot_start_center_corner_final2()
            elif bot_corner_human_not_cntr:
                bot.bot_corner_human_ntcenter_1()
            elif bot_corner_human_mid:
                bot.bot_corner_human_center()
            elif bot_corner_human_notmid_final:
                bot.bot_corner_human_ntcenter_final()
            elif bot_corner_human_mid1:
                bot.bot_corner_human_center1()
            elif bot_corner_human_mid2:
                bot.bot_corner_human_center2()
            elif human_1st:
                print('Human first is executed')
                bot.human_first()
            elif human_go_center:
                bot.human_1st_center1()
            elif human_1st_is_center:
                bot.human_1st_center2()
            elif human_1st_cntr3:
                bot.human_1st_center3()
            elif human_1st_cntr4:
                bot.human_1st_center4()
            elif human_go_corner:
                bot.human_1st_corner()
            elif human_1st_diagonal:
                bot.human_1st_corner_diagonal()
            elif human_1st_diagonal2:
                bot.human_1st_corner_diagonal2()
            elif human_1st_no_diag:
                bot.human_1st_corner_ntdiagonal()
            elif human_1st_no_diag2:
                bot.human_1st_corner_ntdiagonal2()
            elif human_first_edge:
                bot.human_1st_edge()
            elif human_first_edge2:
                bot.human_1st_edge_2()
            elif human_first_edge3:
                bot.human_1st_edge_3()
            elif human_first_edge_end:
                bot.human_1st_edge_end()

    edges= ['button4', 'button2', 'button6', 'button8']

    corners= ['button1', 'button3', 'button7', 'button9']

    winning_combinations = {
        'combination1': ['button1', 'button5', 'button9'],
        'combination2': ['button3', 'button5', 'button7'],
        'combination3': ['button1', 'button4', 'button7'],
        'combination4': ['button2', 'button5', 'button8'],
        'combination5': ['button3', 'button6', 'button9'],
        'combination6': ['button1', 'button2', 'button3'],
        'combination7': ['button4', 'button5', 'button6'],
        'combination8': ['button7', 'button8', 'button9'],
    }

    def button_to_win(moves_log, winning_moves):
        print("Moves log: ", moves_log)  # Print moves_log
        print("Winning moves: ", winning_moves)  # Print winning_moves
        for combination in winning_moves.values():
            matched_buttons = [button for button in moves_log if button in combination]
            if len(matched_buttons) == 2:
                remaining_button = list(set(combination) - set(matched_buttons))[0]
                # Check if both matched buttons have text 'X'
                if all(buttons[button].cget('text') == 'X' for button in matched_buttons):
                    print(f"Winning move found: {remaining_button}")
                    return remaining_button
        print("No winning move found")
        return None

    def button_to_counter(moves_log, winning_moves):
        print("Moves log: ", moves_log)  # Print moves_log
        print("Buttons for counter: ", winning_moves)
        for combination in winning_moves.values():
            matched_buttons = [button for button in moves_log if button in combination]
            if len(matched_buttons) == 2:
                remaining_button = list(set(combination) - set(matched_buttons))[0]
                if all(buttons[button].cget('text') == 'O' for button in matched_buttons):
                    print(f"Counter move found: {remaining_button}")
                    return remaining_button
        print("No counter found")
        return None

    def find_unpressed_buttons(target_buttons, moves_log):
        unpressed_buttons = []
        for button in target_buttons:
            if button not in moves_log:
                unpressed_buttons.append(button)
        return unpressed_buttons

    def find_button(target_buttons, moves_log):
        for button in target_buttons:
            if button in moves_log:
                return button
        return None

    def corner_inrow():
        if button1.cget('text') == 'X':
            if button3.cget('text') == '' and button2.cget('text') == '':
                update_button_text('button3', 'X')
            elif button7.cget('text') == '' and button4.cget('text') == '':
                update_button_text('button7', 'X')
        elif button3.cget('text') == 'X':
            if button1.cget('text') == '' and button2.cget('text') == '':
                update_button_text('button1', 'X')
            elif button9.cget('text') == '' and button6.cget('text') == '':
                update_button_text('button9', 'X')
        elif button7.cget('text') == 'X':
            if button1.cget('text') == '' and button4.cget('text') == '':
                update_button_text('button1', 'X')
            elif button9.cget('text') == '' and button8.cget('text') == '':
                update_button_text('button9', 'X')
        elif button9.cget('text') == 'X':
            if button7.cget('text') == '' and button8.cget('text') == '':
                update_button_text('button7', 'X')
            elif button3.cget('text') == '' and button6.cget('text') == '':
                update_button_text('button3', 'X')

    def update_button_text(bttn_name, new_text):
        if buttons[bttn_name].cget('text') == '':
            buttons[bttn_name].config(text=new_text)
            moves_logger.append(bttn_name)

    class Bot:
        def __init__(self, bot_frst):
            self.bot_first = bot_frst
            if self.bot_first:
                self.state = self.bot_first_move
            else:
                self.state = self.human_first0

        def start(self):
            self.state()

        def bot_first_move(self):
            start_center = random.choice([True, False])
            if start_center:
                update_button_text('button5', 'X')
                self.state = self.bot_start_center
                global start_center2nd
                start_center2nd = True
            else:
                update_button_text(random.choice(corners), 'X')
                self.state = self.bot_start_corner
                global bot_corner1
                bot_corner1 = True

        def bot_start_center(self):
            global start_center2nd
            start_center2nd = False
            # Bot goes to the furthest edge
            if 'button4' in moves_logger:
                update_button_text(random.choice(['button3', 'button9']), 'X')
                global bot_strt_center_edg
                bot_strt_center_edg = True
            elif 'button8' in moves_logger:
                update_button_text(random.choice(['button1', 'button3']), 'X')
                bot_strt_center_edg = True
            elif 'button6' in moves_logger:
                update_button_text(random.choice(['button1', 'button7']), 'X')
                bot_strt_center_edg = True
            elif 'button2' in moves_logger:
                update_button_text(random.choice(['button7', 'button9']), 'X')
                bot_strt_center_edg = True

            # Player goes to a corner, mark opposite.
            if button1.cget('text') == 'O' and button5.cget('text') == 'X' and button9.cget('text') == '':
                update_button_text('button9', 'X')
                global bot_strt_center_crn
                bot_strt_center_crn = True
            elif button3.cget('text') == 'O' and button5.cget('text') == 'X' and button7.cget('text') == '':
                update_button_text('button7', 'X')
                bot_strt_center_crn = True
            elif button7.cget('text') == 'O' and button5.cget('text') == 'X' and button3.cget('text') == '':
                update_button_text('button3', 'X')
                bot_strt_center_crn = True
            elif button9.cget('text') == 'O' and button5.cget('text') == 'X' and button1.cget('text') == '':
                update_button_text('button1', 'X')
                bot_strt_center_crn = True

        # if player blocks bot, block it back: or in case it doesn't block, still makes a winning move
        def bot_start_center_edge(self):
            global bot_strt_center_edg
            bot_strt_center_edg = False
            winning_button = button_to_win(moves_logger, winning_combinations)
            counter_button = button_to_counter(moves_logger, winning_combinations)
            if winning_button:
                update_button_text(winning_button, 'X')
                is_winner()
            elif counter_button:
                update_button_text(counter_button, 'X')
                print('first good counter')
                self.state = self.bot_start_center_edge_final
                global bot_strt_center_edge_fnl
                bot_strt_center_edge_fnl = True

        def bot_start_center_edge_final(self):
            global bot_strt_center_edge_fnl
            bot_strt_center_edge_fnl = False
            winning_button = button_to_win(moves_logger, winning_combinations)
            unpressed_buttons = find_unpressed_buttons(buttons_str, moves_logger)
            if winning_button:
                print('moving to win')
                update_button_text(winning_button, 'X')
                is_winner()
            elif unpressed_buttons:
                print('this is called ')
                update_button_text(random.choice(unpressed_buttons), 'X')
                is_winner()

        def bot_start_center_corner(self):
            global bot_strt_center_crn
            bot_strt_center_crn = False
            # PLAYER MAKES MISTAKE AND CHOOSE AN EDGE
            # NEED TO BLOCK + TRAP
            if button2.cget('text') == 'O' or button4.cget('text') == 'O' or button6.cget('text') == 'O' or button8.cget('text') == 'O':
                winning_button = button_to_win(moves_logger, winning_combinations)
                counter_button = button_to_counter(moves_logger, winning_combinations)
                if winning_button:
                    update_button_text(winning_button, 'X')
                    is_winner()
                elif counter_button:
                    update_button_text(counter_button, 'X')
                    self.state = self.bot_start_center_final
                    global bot_strt_mid_final
                    bot_strt_mid_final = True
                else:
                    unpressed_buttons = find_unpressed_buttons(corners, moves_logger)
                    if unpressed_buttons:
                        update_button_text(random.choice(unpressed_buttons), 'X')
                        self.state = self.bot_start_center_final
                        bot_strt_mid_final = True

            else:
                # PLAYER CHOSES ANOTHER CORNER AS FOURTH MOVE
                # GO FOR TIE, KEEP COUNTER-ATTACKING
                counter_button = button_to_counter(moves_logger, winning_combinations)
                if counter_button:
                    update_button_text(counter_button, 'X')
                    self.state = self.bot_start_center_corner_twice
                    global bot_strt_mid_2ndcorner
                    bot_strt_mid_2ndcorner = True

        def bot_start_center_final(self):
            global bot_strt_mid_final
            bot_strt_mid_final = False
            winning_button = button_to_win(moves_logger, winning_combinations)
            if winning_button:
                update_button_text(winning_button, 'X')
                is_winner()

        def bot_start_center_corner_twice(self):
            global bot_strt_mid_2ndcorner
            bot_strt_mid_2ndcorner = False
            winning_button = button_to_win(moves_logger, winning_combinations)
            if winning_button:
                update_button_text(winning_button, 'X')
                is_winner()
            else:
                unpressed_buttons = find_unpressed_buttons(buttons_str, moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
                self.state = self.bot_start_center_corner_final2
                global bot_strt_mid_corner_final
                bot_strt_mid_corner_final = True

        def bot_start_center_corner_final2(self):
            global bot_strt_mid_corner_final
            bot_strt_mid_corner_final = False
            unpressed_buttons = find_unpressed_buttons(buttons_str, moves_logger)
            if unpressed_buttons:
                update_button_text(random.choice(unpressed_buttons), 'X')
            is_winner()  # TIE

        def bot_start_corner(self):
            global bot_corner1
            bot_corner1 = False
            # HUMAN 1 st MOVE is NOT center
            if button5.cget('text') == '':
                corner_inrow()  # tick the free corner in the same row
                self.state = self.bot_corner_human_ntcenter_1
                global bot_corner_human_not_cntr
                bot_corner_human_not_cntr = True
            else:
                # HUMAN FIRST MOVE IS CENTER
                if button1.cget('text') == 'X':
                    update_button_text('button9', 'X')
                elif button3.cget('text') == 'X':
                    update_button_text('button7', 'X')
                elif button7.cget('text') == 'X':
                    update_button_text('button3', 'X')
                elif button9.cget('text') == 'X':
                    update_button_text('button1', 'X')
                self.state = self.bot_corner_human_center
                global bot_corner_human_mid
                bot_corner_human_mid = True

        def bot_corner_human_ntcenter_1(self):
            global bot_corner_human_not_cntr
            bot_corner_human_not_cntr = False
            # If did not block
            winning_button = button_to_win(moves_logger, winning_combinations)
            if winning_button:
                update_button_text(winning_button, 'X')
                is_winner()
            else:  # Blocked
                if button1.cget('text') == '' and button7.cget('text') == 'X' and button4.cget('text') == '':
                    update_button_text('button1', 'X')
                elif button1.cget('text') == '' and button7.cget('text') == 'X' and button4.cget('text') == 'O':
                    update_button_text('button3', 'X')

                elif button1.cget('text') == '' and button3.cget('text') == 'X' and button2.cget('text') == '':
                    update_button_text('button1', 'X')
                elif button1.cget('text') == '' and button3.cget('text') == 'X' and button2.cget('text') == 'O':
                    update_button_text('button7', 'X')


                elif button3.cget('text') == '' and button9.cget('text') == 'X' and button6.cget('text') == '':
                    update_button_text('button3', 'X')
                elif button3.cget('text') == '' and button9.cget('text') == 'X' and button6.cget('text') == 'O':
                    update_button_text('button1', 'X')

                elif button3.cget('text') == '' and button1.cget('text') == 'X' and button2.cget('text') == '':
                    update_button_text('button3', 'X')
                elif button3.cget('text') == '' and button1.cget('text') == 'X' and button2.cget('text') == 'O':
                    update_button_text('button9', 'X')


                elif button7.cget('text') == '' and button1.cget('text') == 'X' and button4.cget('text') == '':
                    update_button_text('button7', 'X')
                elif button7.cget('text') == '' and button1.cget('text') == 'X' and button4.cget('text') == 'O':
                    update_button_text('button9', 'X')

                elif button7.cget('text') == '' and button9.cget('text') == 'X' and button8.cget('text') == '':
                    update_button_text('button7', 'X')
                elif button7.cget('text') == '' and button9.cget('text') == 'X' and button8.cget('text') == 'O':
                    update_button_text('button1', 'X')


                elif button9.cget('text') == '' and button7.cget('text') == 'X' and button8.cget('text') == '':
                    update_button_text('button9', 'X')
                elif button9.cget('text') == '' and button7.cget('text') == 'X' and button8.cget('text') == 'O':
                    update_button_text('button3', 'X')

                elif button9.cget('text') == '' and button3.cget('text') == 'X' and button4.cget('text') == '':
                    update_button_text('button9', 'X')
                elif button9.cget('text') == '' and button3.cget('text') == 'X' and button4.cget('text') == 'O':
                    update_button_text('button7', 'X')

                self.state = self.bot_corner_human_ntcenter_final
                global bot_corner_human_notmid_final
                bot_corner_human_notmid_final = True

        def bot_corner_human_ntcenter_final(self):
            global bot_corner_human_notmid_final
            bot_corner_human_notmid_final = False
            winning_button = button_to_win(moves_logger, winning_combinations)
            if winning_button:
                update_button_text(winning_button, 'X')
                is_winner()

        def bot_corner_human_center(self):
            global bot_corner_human_mid
            bot_corner_human_mid = False
            # if player goes to a corner, it is blocked, then beat
            counter_button = button_to_counter(moves_logger, winning_combinations)
            if counter_button:
                update_button_text(counter_button, 'X')
                self.state = self.bot_corner_human_center1
                global bot_corner_human_mid1
                bot_corner_human_mid1 = True

        def bot_corner_human_center1(self):
            global bot_corner_human_mid1
            bot_corner_human_mid1 = False
            winning_button = button_to_win(moves_logger, winning_combinations)
            counter_button = button_to_counter(moves_logger, winning_combinations)
            if winning_button:
                update_button_text(winning_button, 'X')
                is_winner()
            elif counter_button:
                update_button_text(counter_button, 'X')
                self.state = self.bot_corner_human_center2
                global bot_corner_human_mid2
                bot_corner_human_mid2 = True

        # IF HUMAN GOES TO AN EDGE IN 4TH MOVE
        def bot_corner_human_center2(self):
            global bot_corner_human_mid2
            bot_corner_human_mid2 = False
            unpressed_buttons = find_unpressed_buttons(buttons_str, moves_logger)
            if unpressed_buttons:
                update_button_text(random.choice(unpressed_buttons), 'X')
            is_winner()  # draw

        def human_first0(self):
            global human_1st
            human_1st = True
            print('human first is set to True')

        def human_first(self):
            global human_1st
            human_1st = False
            print('Human 1st move is center')
            if button5.cget('text') == 'O':
                update_button_text(random.choice(corners), 'X')
                self.state = self.human_1st_center1
                global human_go_center
                human_go_center = True

            elif button1.cget('text') == 'O' or button3.cget('text') == 'O' or button7.cget('text') == 'O' or button9.cget('text') == 'O':
                update_button_text('button5', 'X')
                # human first move is to a corner
                global human_go_corner
                human_go_corner = True

            # Human 1st move is to an edge
            elif button2.cget('text') == 'O' or button4.cget('text') == 'O' or button6.cget('text') == 'O' or button8.cget('text') == 'O':
                update_button_text('button5', 'X')
                global human_first_edge
                human_first_edge = True

        def human_1st_center1(self):
            global human_go_center #GOOD
            human_go_center = False
            print(moves_logger)
            counter_button = button_to_counter(moves_logger, winning_combinations)
            if counter_button:
                update_button_text(counter_button, 'X')
            else:
                update_button_text(random.choice(corners), 'X')
            self.state = self.human_1st_center2
            global human_1st_is_center
            human_1st_is_center = True

        def human_1st_center2(self):
            global human_1st_is_center
            human_1st_is_center = False
            winning_button = button_to_win(moves_logger, winning_combinations)
            counter_button = button_to_counter(moves_logger, winning_combinations)
            if winning_button:
                update_button_text(winning_button, 'X')
                is_winner()
            elif counter_button:
                update_button_text(counter_button, 'X')
            else:
                unpressed_buttons = find_unpressed_buttons(corners, moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
            self.state = self.human_1st_center3
            global human_1st_cntr3
            human_1st_cntr3 = True

        def human_1st_center3(self):
            global human_1st_cntr3
            human_1st_cntr3 = False
            winning_button = button_to_win(moves_logger, winning_combinations)
            counter_button = button_to_counter(moves_logger, winning_combinations)
            if winning_button:
                update_button_text(winning_button, 'X')
                is_winner()
            elif counter_button:
                update_button_text(counter_button, 'X')
                self.state = self.human_1st_center4
                global human_1st_cntr4
                human_1st_cntr4 = True

        def human_1st_center4(self):
            global human_1st_cntr4
            human_1st_cntr4 = False
            is_winner()
            counter_button = button_to_counter(moves_logger, winning_combinations)
            if counter_button:
                update_button_text(counter_button, 'X')
                is_winner()
            else:
                unpressed_buttons = find_unpressed_buttons(buttons_str, moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
                    is_winner()

        def human_1st_corner(self):
            global human_go_corner
            human_go_corner = False
            # forms a diagonal
            if button1.cget('text') == 'O' and button9.cget('text') == 'O' or button3.cget('text') == 'O' and button7.cget('text') == 'O':
                update_button_text(random.choice(edges), 'X') #NOT WORKING
                self.state = self.human_1st_corner_diagonal
                global human_1st_diagonal
                human_1st_diagonal = True
            else:
                # player did not form a diagonal in the THIRD MOVE
                counter_button = button_to_counter(moves_logger, winning_combinations)
                if counter_button:
                    update_button_text(counter_button, 'X')
                else:
                    unpressed_buttons = find_unpressed_buttons(buttons_str, moves_logger)
                    if unpressed_buttons:
                        update_button_text(random.choice(unpressed_buttons), 'X')
                self.state = self.human_1st_corner_ntdiagonal
                global human_1st_no_diag
                human_1st_no_diag = True

        def human_1st_corner_diagonal(self):
            global human_1st_diagonal
            human_1st_diagonal = False
            # doesn't block
            winning_button = button_to_win(moves_logger, winning_combinations)
            counter_button = button_to_counter(moves_logger, winning_combinations)
            if winning_button:
                update_button_text(winning_button, 'X')
                is_winner()
            # blocked
            elif counter_button:
                update_button_text(counter_button, 'X')
                is_winner()
            else:
                unpressed_buttons = find_unpressed_buttons(buttons_str, moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
                self.state = self.human_1st_corner_diagonal2
                global human_1st_diagonal2
                human_1st_diagonal2 = True

        def human_1st_corner_diagonal2(self):
            global human_1st_diagonal2
            human_1st_diagonal2 = False
            winning_button = button_to_win(moves_logger, winning_combinations)
            if winning_button:
                update_button_text(winning_button, 'X')
                is_winner()
            else:
                unpressed_buttons = find_unpressed_buttons(buttons_str, moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
                    is_winner()

        def human_1st_corner_ntdiagonal(self):
            global human_1st_no_diag
            human_1st_no_diag = False
            winning_button = button_to_win(moves_logger, winning_combinations)
            counter_button = button_to_counter(moves_logger, winning_combinations)
            if winning_button:
                update_button_text(winning_button, 'X')
                is_winner()
            elif counter_button:
                update_button_text(counter_button, 'X')
            else:
                unpressed_buttons = find_unpressed_buttons(buttons_str, moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
            self.state = self.human_1st_corner_ntdiagonal2
            global human_1st_no_diag2
            human_1st_no_diag2 = True

        def human_1st_corner_ntdiagonal2(self):
            global human_1st_no_diag2
            human_1st_no_diag2 = False
            winning_button = button_to_win(moves_logger, winning_combinations)
            counter_button = button_to_counter(moves_logger, winning_combinations)
            if winning_button:
                update_button_text(winning_button, 'X')
            elif counter_button:
                update_button_text(counter_button, 'X')
            else:
                unpressed_buttons = find_unpressed_buttons(buttons_str, moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
            is_winner()

        def human_1st_edge(self):
            global human_first_edge
            human_first_edge = False

            counter_button = button_to_counter(moves_logger, winning_combinations)
            if counter_button:
                update_button_text(counter_button, 'X')

            # to prevent to get trapped
            elif button7.cget('text') == 'O' and button2.cget('text') == 'O':
                update_button_text('button1', 'X')
            elif button9.cget('text') == 'O' and button2.cget('text') == 'O':
                update_button_text('button3', 'X')

            elif button9.cget('text') == 'O' and button4.cget('text') == 'O':
                update_button_text('button7', 'X')
            elif button3.cget('text') == 'O' and button4.cget('text') == 'O':
                update_button_text('button1', 'X')

            elif button1.cget('text') == 'O' and button8.cget('text') == 'O':
                update_button_text('button7', 'X')
            elif button3.cget('text') == 'O' and button8.cget('text') == 'O':
                update_button_text('button9', 'X')

            elif button1.cget('text') == 'O' and button6.cget('text') == 'O':
                update_button_text('button3', 'X')
            elif button7.cget('text') == 'O' and button6.cget('text') == 'O':
                update_button_text('button9', 'X')

            elif button2.cget('text') == 'O':
                unpressed_buttons = find_unpressed_buttons(('button7', 'button9'), moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
            elif button4.cget('text') == 'O':
                unpressed_buttons = find_unpressed_buttons(('button3', 'button9'), moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
            elif button6.cget('text') == 'O':
                unpressed_buttons = find_unpressed_buttons(('button1', 'button7'), moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
            elif button8.cget('text') == 'O':
                unpressed_buttons = find_unpressed_buttons(('button1', 'button3'), moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')

            self.state = self.human_1st_edge_2
            global human_first_edge2
            human_first_edge2 = True

        def human_1st_edge_2(self):
            global human_first_edge2
            human_first_edge2 = False

            counter_button = button_to_counter(moves_logger, winning_combinations)
            winning_button = button_to_win(moves_logger, winning_combinations)
            if winning_button:
                update_button_text(winning_button, 'X')
                is_winner()

            elif counter_button:
                update_button_text(counter_button, 'X')

            elif 'button4' in moves_logger:
                unpressed_buttons = find_unpressed_buttons(('button9', 'button3'), moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
            elif 'button8' in moves_logger:
                unpressed_buttons = find_unpressed_buttons(('button1', 'button3'), moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
            elif 'button6' in moves_logger:
                unpressed_buttons = find_unpressed_buttons(('button1', 'button7'), moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
            elif 'button2' in moves_logger:
                unpressed_buttons = find_unpressed_buttons(('button7', 'button9'), moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
            self.state = self.human_1st_edge_3
            global human_first_edge3
            human_first_edge3 = True

        def human_1st_edge_3(self):
            global human_first_edge3
            human_first_edge3 = False

            counter_button = button_to_counter(moves_logger, winning_combinations)
            winning_button = button_to_win(moves_logger, winning_combinations)
            if counter_button:
                update_button_text(counter_button, 'X')
                global human_first_edge_end
                human_first_edge_end = True
            elif winning_button:
                update_button_text(winning_button, 'X')
                is_winner()
            else:
                unpressed_buttons = find_unpressed_buttons(buttons_str, moves_logger)
                if unpressed_buttons:
                    update_button_text(random.choice(unpressed_buttons), 'X')
                    human_first_edge_end = True

        def human_1st_edge_end(self):
            global human_first_edge_end
            human_first_edge_end = False
            is_winner()


    if not two_players:
        # Initialize the bot.
        global bot_first
        bot = Bot(bot_first)
        bot.start()

    buttons_str = ('button1', 'button2', 'button3', 'button4', 'button5', 'button6', 'button7', 'button8', 'button9')


    # Function to reset the game
    def reset_game():
        button1.config(text="")
        button2.config(text="")
        button3.config(text="")
        button4.config(text="")
        button5.config(text="")
        button6.config(text="")
        button7.config(text="")
        button8.config(text="")
        button9.config(text="")

        global moves_logger
        moves_logger = []

        if not two_players:
            global bot_first
            bot_first = not bot_first
            bot2 = Bot(bot_first)
            bot2.start()

        if game_state["starting_player"] == "X":
            game_state["starting_player"] = "O"
        else:
            game_state["starting_player"] = "X"

        game_state["is_player_x_turn"] = game_state["starting_player"] == "X" #if starting_player equals any other character than X, is_player_x_turn will be False

    def update_score():
        score.config(text=f"X: {player_x} pts | O: {player_o} pts")

root.mainloop()
