from tkinter import *
import random
system = random.randrange(1, 50)
attempt = 1
lives = 10
score = 0

def check():
    global attempt, lives, score, system

    try:
        mychoice = int(echoice.get())

        if lives <= 0:
            result_label.config(text="💀 Game Over! Press Restart", fg="red")
            return

        if mychoice == system:
            if attempt<=5:
                score +=15
                result_label.config(
                text=f"🎉 Best! Score: {score}",
                fg="#00FFAA"
            )
            elif attempt<=7:
                score +=10
                result_label.config(
                    text=f"🎉 Better! Score: {score}",
                    fg="#E5FF00"
                )
            else:                
                score +=5
                result_label.config(
                    text=f"🎉 Correct! Score: {score}",
                    fg="#E5FF4FFF"
                )
            new_round()

        elif mychoice > system:
            lives -= 1
            result_label.config(
                text=f"📉 Too High guess low! Lives: {lives}",
                fg="#FF6B6B"
            )
        else:
            lives -= 1
            result_label.config(
                text=f"📈 Too Low guess high! Lives: {lives}",
                fg="#FF6B6B"
            )

        attempt += 1
        update_status()

        if lives == 0:
            result_label.config(
                text=f"💀 Game Over! Number was {system}",
                fg="red"
            )

    except ValueError:
        result_label.config(text="⚠ Enter valid number", fg="yellow")


def new_round():
    global system, lives, attempt
    system = random.randrange(1, 50)
    lives = 10
    attempt = 1
    echoice.delete(0, END)
    update_status()


def restart():
    global score
    score = 0
    new_round()
    result_label.config(text="🔄 Game Restarted!", fg="cyan")


def update_status():
    status_label.config(
        text=f"❤️ Lives: {lives}    🎯 Score: {score}"
    )



win = Tk()
win.title("🎮 Number Guessing Game")
win.geometry("420x400")
win.config(bg="#1E1E2E")

Label(
    win,
    text="Guess The Number",
    font=("Arial", 20, "bold"),
    bg="#1E1E2E",
    fg="white"
).pack(pady=10)


status_label = Label(
    win,
    text="",
    font=("Arial", 12),
    bg="#1E1E2E",
    fg="#AAAAAA"
)
status_label.pack()


echoice = Entry(
    win,
    font=("Arial", 16),
    justify="center",
    bg="#2A2A3C",
    fg="white",
    insertbackground="white",
    bd=0
)
echoice.pack(pady=20, ipadx=10, ipady=5)


frame = Frame(win, bg="#1E1E2E")
frame.pack()

Button(
    frame,
    text="Check",
    font=("Arial", 12, "bold"),
    bg="#6C63FF",
    fg="white",
    bd=0,
    padx=15,
    command=check
).grid(row=0, column=0, padx=10)

Button(
    frame,
    text="Restart",
    font=("Arial", 12, "bold"),
    bg="#FF9F43",
    fg="white",
    bd=0,
    padx=15,
    command=restart
).grid(row=0, column=1, padx=10)


result_label = Label(
    win,
    text="Start Guessing (1-50)",
    font=("Arial", 12),
    bg="#1E1E2E",
    fg="#CCCCCC"
)
result_label.pack(pady=20)

update_status()

win.mainloop()