import tkinter as tk
from tkinter import messagebox
import time

class MCQQuiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MCQ Quiz")
        self.geometry("400x300")

        self.name_label = tk.Label(self, text="Enter user name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.start_button = tk.Button(self, text="Start Quiz", command=self.start_quiz)
        self.start_button.pack()

    def start_quiz(self):
        name = self.name_entry.get()

        if name == "":
            messagebox.showerror("Error", "Please enter user name.")
            return

        self.destroy()  # Close the login window
        QuizWindow(name)

class QuizWindow(tk.Toplevel):
    def __init__(self, name):
        super().__init__()
        self.title("MCQ Quiz")
        self.geometry("600x400")

        self.name = name
        self.question_number = 0
        self.score = 0

        self.questions = [
            ("What is the capital of India?", ["Hyderabad", "Mumbai", "New Delhi", "Bangalore"], 3),
            ("Which planet is known as the Red Planet?", ["Venus", "Jupiter", "Mars", "Saturn"], 2),
            ("Who is the author of the famous play Romeo and Juliet?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy"], 1),
            ("What is the largest mammal on Earth?", ["African Elephant", "Blue Whale", "Giraffe", "Polar Bear"], 1),
            ("What is the currency of Japan?", ["Yen", "Dollar", "Euro", "Rupee"], 0)
        ]

        self.welcome_label = tk.Label(self, text=f"Welcome {name} to the MCQ Quiz!")
        self.welcome_label.pack()

        self.question_label = tk.Label(self, text="")
        self.question_label.pack()

        self.options_frame = tk.Frame(self)
        self.options_frame.pack()

        self.radio_var = tk.IntVar()

        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.timer_label = tk.Label(self, text="Time left: 30 seconds")
        self.timer_label.pack()

        self.remaining_time = 30
        self.timer()

        self.load_question()

    def load_question(self):
        if self.question_number < len(self.questions):
            self.question_label.config(text=f"Question {self.question_number + 1}: {self.questions[self.question_number][0]}")
            self.radio_var.set(-1)

            for widget in self.options_frame.winfo_children():
                widget.destroy()

            options = self.questions[self.question_number][1]
            for idx, option in enumerate(options, start=1):
                radio_button = tk.Radiobutton(self.options_frame, text=option, variable=self.radio_var, value=idx)
                radio_button.pack(anchor="w")
        else:
            messagebox.showinfo("Quiz Finished", f"Congratulations {self.name}! Quiz finished. Your score is {self.score * 10}.")
            self.destroy()

    def timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.timer_label.config(text=f"Time left: {self.remaining_time} seconds")
            self.after(1000, self.timer)
        else:
            self.check_answer()

    def check_answer(self):
        answer = self.radio_var.get()
        correct_answer = self.questions[self.question_number][2]
        if answer == correct_answer + 1:
            self.score += 1
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", "Your answer is incorrect.")

        self.question_number += 1
        self.load_question()

if __name__ == "__main__":
    app = MCQQuiz()
    app.mainloop()
