from tkinter import *
from tkinter.ttk import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
work_session_num = 0
timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- #
#
def start_timer():
    global reps
    global work_session_num
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title.config(text=f'Long Break #{reps // 8}', foreground=RED)
        countdown(3 * 10)
        reset_timer()
    elif reps % 2 == 0:
        title.config(text=f'Short Break #{reps // 2}', foreground=PINK)
        countdown(1 * 10)
    else:
        work_session_num = math.ceil(reps / 2)
        title.config(text=f'Work Session #{work_session_num}', foreground=GREEN)
        countdown(2 * 10)
        if work_session_num != 1:
            current_check_amount = checkmark_counter.cget("text")
            new_check_amount = f"{current_check_amount}✔"
            checkmark_counter.config(text=new_check_amount)
    start_button.config(state="disabled")
    window.attributes('-topmost', 0)
    window.deiconify()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time_amount):
    global timer
    time_in_mins = math.floor(time_amount / 60)
    time_in_secs = time_amount % 60
    if time_in_mins < 10:
        time_in_mins = f"0{time_in_mins}"
    if time_in_secs < 10:
        time_in_secs = f"0{time_in_secs}"
    canvas.itemconfig(timer_id, text=f"{time_in_mins}:{time_in_secs}")
    if time_amount > 0:
        timer = window.after(1000, countdown, time_amount - 1)
    else:
        window.attributes('-topmost', 1)
        start_timer()



# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    title.config(text="Timer", foreground=GREEN)
    window.after_cancel(timer)
    canvas.itemconfig(timer_id, text="00:00")
    checkmark_counter.config(text="")
    reps = 0
    start_button.config(state="normal")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODOROO")
window.config(padx=100, pady=50, bg=YELLOW, )

title = Label(text="Timer", font=(FONT_NAME, 35, "bold"), background=YELLOW, foreground=GREEN)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_id = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_timer)
checkmark_counter = Label(foreground=GREEN, background=YELLOW)

canvas.grid(column=1, row=1)
title.grid(column=1, row=0)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
checkmark_counter.grid(column=1, row=3)

window.mainloop()
