import tkinter as tk
import random

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 650

#Keeping track of Match, User winnings and Computer winnings
match_count = 0
user_wins = 0
computer_wins = 0

def main():
    global match_count, user_wins, computer_wins, root, canvas, rock_img, paper_img, scissors_img
    match_count = 0
    user_wins = 0
    computer_wins = 0

    root = tk.Tk()
    root.title("Rock, Paper, Scissors")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="#27464f")
    canvas.pack()

    #Images for Rock,Paper and Scissors
    rock_img = tk.PhotoImage(file="rock.png")
    paper_img = tk.PhotoImage(file="paper.png")
    scissors_img = tk.PhotoImage(file="scissors.png")

    setup_game()

    root.mainloop()

#Once the game ends, start again.
def setup_game():
    global match_count, user_wins, computer_wins, canvas, rock_img, paper_img, scissors_img
    match_count = 0
    user_wins = 0
    computer_wins = 0

    canvas.delete("all")

    #Chose Rock, Paper or Scissors text
    canvas.create_text(
        300, 50,
        text="Choose Rock, Paper, or Scissors",
        fill="white",
        font=("Helvetica", 25)
    )

    # Rock image
    canvas.create_image(
        100, 225,
        image=rock_img,
        tags="rock"
    )

    # Paper image
    canvas.create_image(
        300, 225,
        image=paper_img,
        tags="paper"
    )

    # Scissors image
    canvas.create_image(
        500, 225,
        image=scissors_img,
        tags="scissors"
    )

    #Computer has chosen text
    computer_choice_text = canvas.create_text(
        300, 450,
        text="Computer has chosen: ",
        fill="white",
        font=("Helvetica", 15)
    )

    #Result text
    result_text = canvas.create_text(
        300, 500,
        text="",
        fill="red",
        font=("Helvetica", 15)
    )

    #Score text
    score_text = canvas.create_text(
        300, 550,
        text="Score - You: 0, Computer: 0",
        fill="green",
        font=("Helvetica", 20)
    )

    #Clicking on a circle image binds event
    canvas.tag_bind("rock", "<Button-1>", lambda event: handle_click(event, canvas, "Rock", computer_choice_text, result_text, score_text))
    canvas.tag_bind("paper", "<Button-1>", lambda event: handle_click(event, canvas, "Paper", computer_choice_text, result_text, score_text))
    canvas.tag_bind("scissors", "<Button-1>", lambda event: handle_click(event, canvas, "Scissors", computer_choice_text, result_text, score_text))

def handle_click(event, canvas, user_choice, computer_choice_text, result_text, score_text):
    global match_count, user_wins, computer_wins

    #Random choice for computer
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    #Update computer choice text
    canvas.itemconfig(computer_choice_text, text=f"Computer has chosen: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        user_wins += 1
    else:
        result = "You lose!"
        computer_wins += 1

    #Mach count update
    match_count += 1

    #Result text update
    canvas.itemconfig(result_text, text=result)

    #Score text update
    canvas.itemconfig(score_text, text=f"Score - You: {user_wins}, Computer: {computer_wins}")

    #Check if three matches have been played
    if match_count == 3:
        if user_wins > computer_wins:
            final_result = "You Win!"
        elif computer_wins > user_wins:
            final_result = "Computer Wins!"
        else:
            final_result = "It's a Tie!"
        
        # Display final result in a new text object
        final_result_text = canvas.create_text(
            300, 600,
            text=final_result,
            fill="white",
            font=("Helvetica", 25)
        )

        # Reset game after showing the result for a few seconds
        canvas.after(3000, setup_game)

if __name__ == '__main__':
    main()
