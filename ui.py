import time

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20,padx=20)
        self.scoretext = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.scoretext.grid(row=0, column=1)
        self.window.config(bg=THEME_COLOR)
        self.canvas = Canvas(self.window, height=250, width=300, highlightthickness=0)
        self.qtxt = self.canvas.create_text(150,125,text=self.quiz.next_question(), font=FONT, width=250)
        self.canvas.grid(row=1,column=0,columnspan=2, pady=20, padx=20)
        self.pos_button = Button(command=self.true_press)
        self.neg_button = Button(command=self.false_press)
        pos_img = PhotoImage(file="./images/true.png")
        neg_img = PhotoImage(file="./images/false.png")
        self.pos_button.config(image=pos_img, pady=20,padx=20,highlightthickness=0)
        self.neg_button.config(image=neg_img, pady=20,padx=20,highlightthickness=0)
        self.pos_button.grid(row=2,column=0, pady=20)
        self.neg_button.grid(row=2, column=1, pady=20)
        self.window.mainloop()

    def true_press(self):
        answer = self.quiz.check_answer("True")
        self.answer_right(answer)
    def false_press(self):
        answer = self.quiz.check_answer("False")
        self.answer_right(answer)

    def get_next_question(self):
        self.scoretext.config(text=f"Score: {self.quiz.score}")
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.qtxt, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.qtxt, text=f"You have reached the end of the quiz. You got {self.quiz.score} / 10 correct.")
            self.pos_button.config(state="disabled")
            self.neg_button.config(state="disabled")

    def answer_right(self, answer: bool):
        if answer:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000,self.get_next_question)
