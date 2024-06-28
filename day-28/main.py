from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#1A4D2E"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    mark = ""
    global reps
    reps = 0
    timer_label.config(text="⏳Timer⌛", fg=GREEN)
    canvas.itemconfig(time_text, text="00:00")
    window.after_cancel(timer)


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="Rest😴", fg=PINK)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer_label.config(text="Break😊", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer_label.config(text="Work💪", fg=RED)
        count_down(WORK_MIN * 60)


def count_down(count):
    global timer
    if count > 0:
        count_min = count // 60
        count_sec = count % 60

        timer = window.after(1000, count_down, count-1)
        # timer is the identifier that keeps track of the after function
        if count_sec in range(0, 10):
            canvas.itemconfig(time_text, text=f"0{count_min}:0{count_sec}")
        else:
            canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    else:
        start_timer()
        mark = ""
        if reps % 2 == 0:
            mark += "✅"
        check_mark.config(text=mark)


window = Tk()
window.config(width=500, height=500, bg=YELLOW, padx=50, pady=50)
window.title("Studying with Pomodoro")

canvas = Canvas(width=200, height=226, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 113, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 34, "bold"), fill="white")
canvas.grid(column=1, row=1)

timer_label = Label(text="⏳Timer⌛", bg=YELLOW, font=(FONT_NAME, 30, "bold"), fg=GREEN, width=15)
timer_label.grid(row=0, column=1)

start = Button(text="Start", command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="Reset", command=reset_timer)
reset.grid(row=2, column=2)

check_mark = Label(text="", bg=YELLOW)
check_mark.grid(row=4, column=1)


window.mainloop()
