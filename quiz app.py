
import random
import tkinter as tk
from tkinter import messagebox

# Define a list of questions and their corresponding answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "correct_answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Venus", "Saturn", "Jupiter", "Mars"],
        "correct_answer": "Jupiter"
    },
    {
        "question": "Which mammal can fly?",
        "options": ["Bat", "Rat", "Cat", "Dog"],
        "correct_answer": "Bat"
    },
    # Add more questions here
]

def shuffle_options(options):
    # Randomly shuffle the options to make the quiz more challenging
    random.shuffle(options)
    return options

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz App")
        self.geometry("400x300")
        
        self.score = 0
        self.question_index = 0
        
        self.question_label = tk.Label(self, text="", font=("Helvetica", 14), wraplength=380)
        self.question_label.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self, text="", command=lambda idx=i: self.check_answer(idx))
            self.option_buttons.append(button)
            button.pack(fill="x", padx=10, pady=5)
        
        self.update_question()
        self.start_timer()

    def update_question(self):
        if self.question_index < len(questions):
            question_data = questions[self.question_index]
            self.question_label.config(text=question_data["question"])
            options = shuffle_options(question_data["options"])
            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option)
        else:
            self.show_result()

    def check_answer(self, selected_index):
        selected_option = self.option_buttons[selected_index]["text"]
        correct_answer = questions[self.question_index]["correct_answer"]
        
        if selected_option == correct_answer:
            self.score += 1
        
        self.question_index += 1
        self.update_question()

    def start_timer(self):
        self.remaining_time = 120  # Set the timer for 120 seconds (2 minutes)
        self.update_timer()

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.after(1000, self.update_timer)rr
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"Your final score is: {self.score}/{len(questions)}")
        self.quit()

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
