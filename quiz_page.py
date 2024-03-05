from tkinter import *

from tkinter import messagebox

import helpers as hp


def take_the_quiz(window, update_label, username):
    window.destroy()

    window_question = Toplevel()
    window_question.title("Wiki Lesson")
    window_question.geometry('800x800+400+100')
    window_question.configure(bg='#89C18F')

    questions = ["What are microplastics, and how are they formed?",
                 "How does plastic pollution impact marine life?",
                 "What actions can individuals take to reduce plastic pollution?",
                 ]

    options = [["Microscopic organisms in the ocean.",
                "Tiny particles resulting from the breakdown of larger plastic items.",
                "A type of natural minera."],
               ["It has no impact on marine life.",
                "It can lead to increased biodiversity.",
                "Plastics can harm marine life through ingestion and entanglement."],
               ["Increase single-use plastic consumption.",
                "Avoid recycling.",
                "Use fewer single-use plastics, recycle responsibly, and participate in cleanup efforts."]
               ]

    answers = [IntVar() for i in range(3)]

    for i in range(3):
        question_label = Label(window_question,
                               text=questions[i],
                               font=("Arial", 20),
                               bg='#89C18F',
                               fg="#3A6351")
        question_label.pack(pady=25)

        for j, option in enumerate(options[i]):
            # Use j as the integer value for the Radiobutton
            radio_button = Radiobutton(window_question,
                                       text=option,
                                       variable=answers[i],
                                       value=j,
                                       font=("Arial", 13, "bold"),
                                       bg='#89C18F',
                                       fg="#3A6351"
                                       )
            radio_button.pack(anchor=CENTER, pady=5)

    def calculate_score():
        correct_answer = [1, 2, 2]
        score = sum(1 for i, answer in enumerate(answers) if answer.get() == correct_answer[i])

        hp.my_virtual_coins += score
        hp.leaderboard[username] += score

        # modify the leaderboard

        update_label.config(text="Your balance is " + str(hp.my_virtual_coins) + " VIRTUAL COIN")
        messagebox.showinfo("Score", f"Your score is {score} out of {len(questions)}")
        window_question.destroy()

    submit_button = Button(window_question,
                           text="Submit",
                           command=calculate_score,
                           bg='#3A6351',
                           fg="#FFFFFF",
                           font=("Arial", 15))

    submit_button.place(x=300, y=670, width=200, height=60)

    window_question.mainloop()


lesson_text = (
    "Plastic pollution is a global environmental issue that results from the accumulation of plastic waste "
    "in various ecosystems. Plastics are synthetic polymers made from petrochemicals, and their widespread use "
    "has led to significant environmental challenges. Plastic pollution affects terrestrial and marine "
    "environments,"
    "posing threats to wildlife, ecosystems, and human health."
    "\n\n"
    "The main sources of plastic pollution include single-use plastics, such as bottles, bags, and packaging, "
    "as well as microplastics. Microplastics are tiny particles that result from the breakdown of larger plastic "
    "items or are intentionally manufactured for certain products. These particles can be found in water bodies, "
    "soil, and even in the air."
    "\n\n"
    "The environmental impact of plastic pollution is vast. Marine life, in particular, is significantly affected. "
    "Sea animals may mistake plastic debris for food, leading to ingestion and potential harm. Additionally, "
    "plastics can entangle marine life, causing injuries and hindering their ability to move and feed."
    "\n\n"
    "Plastic pollution also has consequences for human health. Plastics contain harmful chemicals that can leach "
    "into"
    "the environment and find their way into the food chain. As a result, humans may be exposed to these chemicals "
    "through the consumption of contaminated food and water."
    "\n\n"
    "Addressing plastic pollution requires a multifaceted approach. Individuals can contribute by reducing their "
    "use of single-use plastics, recycling responsibly, and participating in cleanup efforts. Governments and "
    "industries"
    "play a crucial role in implementing policies to regulate plastic production, promote recycling, "
    "and encourage the"
    "development of sustainable alternatives."
)


def quiz_page(update_label, username):
    window_quiz = Toplevel()
    window_quiz.title("Quiz")
    window_quiz.geometry('800x800+400+100')
    icon = PhotoImage(file=r'photo/quiz.png')
    window_quiz.iconphoto(True, icon)
    window_quiz.configure(bg='#89C18F')

    # create frame for header information
    header_frame = Frame(window_quiz, bg='#3A6351')
    header_frame.place(x=0, y=0, width=800, height=200, anchor="nw")
    welcome_quiz_photo = PhotoImage(file=r'photo/lessons.png')
    welcome_quiz_photo = welcome_quiz_photo.subsample(5, 5)
    welcome_quiz = Label(header_frame,
                         text="Weekly Lesson",
                         bg='#3A6351',
                         fg="#FFFFFF",
                         font=("Arial", 40),
                         image=welcome_quiz_photo,
                         compound="left")
    welcome_quiz.place(x=0, y=0, width=800, height=200, anchor="nw")

    # info quiz
    info_frame = Frame(window_quiz, bg='#89C18F')
    info_frame.place(x=0, y=200, width=800, height=700, anchor="nw")
    info_quiz = Label(info_frame,
                      text=lesson_text,
                      bg='#89C18F',
                      fg="#3A6351",
                      font=("Arial", 12),
                      justify=LEFT,
                      wraplength=700)
    info_quiz.place(x=0, y=0, width=800, height=500, anchor="nw")

    # take the questions
    take_quiz = Button(window_quiz,
                       text="Take the quiz",
                       bg='#3A6351',
                       fg="#FFFFFF",
                       font=("Arial", 12),
                       padx=20,
                       pady=20,
                       command=lambda: take_the_quiz(window_quiz, update_label, username))
    take_quiz.place(x=275, y=700, width=250, height=50, anchor="nw")

    # run the application, listen for events
    window_quiz.mainloop()
