import random 
from tkinter import *
from itertools import count
# this answers are in the real book
answer = [
           "YES", "DEFINITELY", "ABSOLUTELY", "IT IS CERTAIN", 
           "YOU ARE SURE TO HAVE SUPPORT", "GOOD THINGS ARE SEEKING YOU out",
            "IT WILL BE A PLEASURE", "TAKE A CHANCE", "YOUR ACTIONS WILL IMPROVE THINGS", 
            "THERE IS GOOD REASON TO BE OPTIMISTIC", "GENTLE PERSISTENCE WILL PAY OFF", 
            "A STRONG COMMITMENT WILL ACHIEVE GOOD RESULTS", "NO", "ABSOLUTELY NOT",
            "DON'T BET ON IT", "IT IS UNCERTAIN", "DON'T BE PRESSURED INTO ACTING TOO QUICKLY", 
            "MISHAPS ARE HIGHLY PROBABLE", "YOU COULD BE DISAPPOINTED", "IT WOULD BE BETTER TO FOCUS ON YOUR WORK",
            "MOVE ON", "DON'T GET CAUGHT UP IN YOUR EMOTIONS", "ADOPT AN ADVENTUROUS ATTITUDE", "FOLLOW THE ADVICE OF EXPERTS",
            "YOU’LL NEED TO TAKE THE INITIATIVE", "BE DELIBERATE", "EXPLORE IT WITH PLAYFUL CURIOSITY", "REPRIORITIZE WHAT IS IMPORTANT", 
            "RECONSIDER YOUR APPROACH", "REMAIN FLEXIBLE", "RESPECT THE RULES", "TAKE THE LEAD", "CHOOSE YOUR WORDS THOUGHTFULLY", 
            "BE YOUR OWN BEST ADVOCATE", "PAY ATTENTION TO THE DETAILS", "SPEAK UP ABOUT IT", "THIS IS A GOOD TIME TO MAKE A NEW PLAN", 
            "SEEK OUT THE PATH OF LEAST RESISTANCE", "BETTER TO WAIT","PERHAPS, WHEN YOU’RE OLDER", "WATCH AND SEE WHAT HAPPENS",
            "TAKE MORE TIME TO DECIDE", "DON’T WAIT",
            "COUNT TO TEN; ASK AGAIN", "WAIT UNTIL LATER", 
            "LET IT GO", "YOU KNOW BETTER NOW THAN EVER BEFORE", "IT WILL AFFECT HOW OTHERS SEE YOU", "THE BEST SOLUTION MAY NOT BE THE OBVIOUS ONE", 
            "THERE IS A SUBSTANTIAL LINK TO ANOTHER SITUATION", "YOU MAY HAVE OPPOSITION", "IT WILL REMAIN UNPREDICTABLE",
            "CONSIDER IT AN OPPORTUNITY", "YOU MAY BE HANGING ON TO AN OUTDATED IDEAL", "YOU’LL HAVE THE ENTHUSIASM YOU’LL NEED",
            "LAUGH ABOUT IT", "A YEAR FROM NOW IT WON'T MATTER", "KNOW WHEN IT'S TIME TO GO", "ACCEPT A CHANGE TO YOUR ROUTINE",
            "TRUST YOUR ORIGINAL THOUGHT", "MAKE A LIST OF WHY", "MAKE A LIST OF WHY NOT", "DON’T LEAVE ROOM FOR REGRET", 
            "PRESS FOR CLOSURE", "YOU DON'T REALLY CARE", "ACT AS THOUGH IT IS ALREADY REAL", "BE PATIENT", 
            "YOU WILL FIND OUT EVERYTHING YOU'LL NEED TO KNOW", "REVEAL YOUR THOUGHTS TO A TRUSTED CONFIDANTE",
            "FOLLOW SOMEONE ELSE'S LEAD", "YOU COULD FIND YOURSELF UNABLE TO COMPROMISE", "ASK FOR HELP", "YOU'LL HAVE TO COMPROMISE",
            "YOU NEED MORE INFORMATION", "IT WILL CREATE A STIR", "YOU'LL OVERCOME ANY OBSTACLES", "BE MORE GENEROUS", "BET ON IT", 
            "MAKE A CONTRIBUTION", "REALIZE THAT TOO MANY CHOICES CAN BE AS DIFFICULT AS TOO FEW", "LISTEN CAREFULLY; THEN YOU WILL KNOW", 
            "THE ANSWER IS IN YOUR BACKYARD", "LET YOUR EMOTIONS GUIDE YOU", "OTHERS WILL DEPEND ON YOUR CHOICES", "IT'S TIME FOR YOU TO GO",
            "DON'T BE DISTRACTED", "GIVE IT ALL YOU'VE GOT", "YOU'LL NEED TO CONSIDER OTHER WAYS", "IT COULD BE EXTRAORDINARY", "BE PRACTICAL",
            "ARE YOU READY?", "SAVE YOUR ENERGY", "YOU MAY HAVE TO DROP OTHER THINGS", "DON'T BE CONCERNED", "PREPARE FOR THE UNEXPECTED",
            "TELL SOMEONE WHAT IT MEANS TO YOU", "WHATEVER YOU do, THE RESULTS WILL BE LASTING", "KEEP AN OPEN MIND",
            "IT'S A GOOD TIME TO MAKE PLANS", "IT MAY BE AMBITIOUS, BUT YOU WILL FIND VALUE IN IT", "IT IS WORTH THE TROUBLE", 
            "RELATED ISSUES MAY SURFACE", "ASSISTANCE WOULD MAKE YOUR PROGRESS A SUCCESS", "COLLABORATION WILL BE THE KEY",
            "TAKE CHARGE", "IT CANNOT FAIL", "YOU MUST ACT NOW", "IT MAY ALREADY BE A DONE DEAL",
            "FOLLOW THROUGH WITH YOUR GOOD INTENTIONS", "DON'T IGNORE THE OBVIOUS"
        ]


def answers():
    result = random.choice(answer)
    answer.config(text=result)

# ------------------ STYLE PRESETS ------------------
PRIM_BG = "#FDFCF0"    
ACCENT_MIST = "#6B8E23" 
TEXT_QUIET = "#4A4E69" 
FONT_SERIF = "Georgia" 

app = Tk()
app.geometry("800x600")
app.title("The Book of your Answer")
app.configure(bg=PRIM_BG)
app.resizable(False, False)

canvas = Canvas(app, width=800, height=600, bg=PRIM_BG, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ------------------ DIM DUST-MOTE STARS ------------------
class SoftStarBackground:
    def __init__(self, canvas, gif_path):
        self.canvas = canvas
        self.frames = []
        for i in count(0):
            try:
                # Subsample(6,6) makes them tiny and very subtle
                img = PhotoImage(file=gif_path, format=f"gif -index {i}").subsample(2, 2)
                self.frames.append(img)
            except:
                break
        self.index = 0
        # Scattered randomly like motes of light in a room
        self.star_instances = [
           self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(40, 550), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0]),
            self.canvas.create_image(random.randint(50, 750), random.randint(50, 550), image=self.frames[0])
            ]
        self.animate()

    def animate(self):
        self.index = (self.index + 1) % len(self.frames)
        for star in self.star_instances:
            self.canvas.itemconfig(star, image=self.frames[self.index])
        app.after(200, self.animate) # Slower animation speed

try:
    
    bg_stars = SoftStarBackground(canvas, "C:\\Users\\sarod\\coding material\\all language\\team\\download.gif")
    bg_stars.zoom(50)
except:
    pass




# ------------------ STORYBOOK GUI ELEMENTS ------------------
# Subtle decorative line (Morning sky horizon feel)
canvas.create_line(250, 145, 550, 145, fill="#DCDCB4", width=1)

# ------------------ MINIMALIST UI ------------------
title = Label(app, text="THE BOOK OF ANSWER", font=(FONT_SERIF, 22), fg=TEXT_QUIET, bg=PRIM_BG)
canvas.create_window(400, 100, window=title)

subtitle = Label(app, text="Close your eyes. Ask your question.\nTake a breath.", 
                 font=(FONT_SERIF, 12, "italic"), fg="#9A8C98", bg=PRIM_BG, justify="center")
canvas.create_window(400, 180, window=subtitle)

# Calm Answer Display
answer_text = Label(
    app, 
    text=". . .", 
    wraplength=500, 
    font=(FONT_SERIF, 20), 
    fg=TEXT_QUIET, 
    bg=PRIM_BG,
    justify="center"
)
canvas.create_window(400, 340, window=answer_text)

# ------------------ LOGIC ------------------
def reveal_answer():
    text = random.choice(answer)
    button.config(state=DISABLED)
    animate_text(text, 0)

def animate_text(text, i):
    if i <= len(text):
        answer_text.config(text=text[:i])
        app.after(80, animate_text, text, i + 1) # Slower typing speed
    else:
        button.config(state=NORMAL)

# ------------------ QUIET BUTTON ------------------
def on_enter(e):
    button.config(bg="#E9E7D0", fg=ACCENT_MIST)

def on_leave(e):
    button.config(bg=PRIM_BG, fg=ACCENT_MIST)

button = Button(
    app, 
    text="REVEAL ANSWER", 
    font=(FONT_SERIF, 11), 
    bg=PRIM_BG, 
    fg=ACCENT_MIST, 
    activebackground=PRIM_BG, 
    activeforeground=ACCENT_MIST,
    bd=1, 
    highlightthickness=1,
    highlightbackground=ACCENT_MIST,
    padx=35, 
    pady=8, 
    command=reveal_answer, 
    cursor="hand2",
    relief="flat"
)
canvas.create_window(400, 500, window=button)

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

footer = Label(app, text="softly, carefully", font=(FONT_SERIF, 9), fg="#C9ADA7", bg=PRIM_BG)
canvas.create_window(400, 560, window=footer)

app.mainloop()