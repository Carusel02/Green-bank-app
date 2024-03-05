from tkinter import *
import helpers as hp


def leader_page():
    leader_window = Toplevel()
    leader_window.title("Leaderboard")
    leader_window.geometry('800x800+400+100')
    leader_window.configure(bg='#89C18F')

    # sort the leaderboard
    sorted_items = sorted(hp.leaderboard.items(), key=lambda x: x[1], reverse=True)
    # create a new dictionary
    sorted_leaderboard = dict(sorted_items)

    img = PhotoImage(file=r'photo/rankings.png')
    img = img.subsample(5, 5)

    # create label for leaderboard
    leaderboard_label = Label(leader_window,
                              text="Leaderboard",
                              bg='#89C18F',
                              fg="#3A6351",
                              font=("Arial", 40),
                              image=img,
                              compound="left",
                              padx=20,
                              pady=20)
    leaderboard_label.place(x=0, y=50, width=800, height=75, anchor="nw")

    # display the leaderboard with the first 10 users
    for i, (username, score) in enumerate(sorted_leaderboard.items()):
        if i == 10:
            break
        if i == 0:
            nr1 = PhotoImage(file=r'photo/first.png')
            nr1 = nr1.subsample(15, 15)
            label = Label(leader_window,
                          text=f" {username} - {score} points",
                          bg='#89C18F',
                          fg="#3A6351",
                          font=("Arial", 20),
                          image=nr1,
                          compound="left")
            label.place(x=200, y=180 + i * 50, width=400, height=50, anchor="nw")
            continue
        if i == 1:
            nr2 = PhotoImage(file=r'photo/second.png')
            nr2 = nr2.subsample(15, 15)
            label = Label(leader_window,
                          text=f" {username} - {score} points",
                          bg='#89C18F',
                          fg="#3A6351",
                          font=("Arial", 20),
                          image=nr2,
                          compound="left")
            label.place(x=200, y=180 + i * 50, width=400, height=50, anchor="nw")
            continue
        if i == 2:
            nr3 = PhotoImage(file=r'photo/third.png')
            nr3 = nr3.subsample(15, 15)
            label = Label(leader_window,
                          text=f" {username} - {score} points",
                          bg='#89C18F',
                          fg="#3A6351",
                          font=("Arial", 20),
                          image=nr3,
                          compound="left")
            label.place(x=200, y=180 + i * 50, width=400, height=50, anchor="nw")
            continue

        label = Label(leader_window,
                      text=f"{i + 1}. {username} - {score} points",
                      bg='#89C18F',
                      fg="#3A6351",
                      font=("Arial", 20))
        label.place(x=200, y=180 + i * 50, width=400, height=50, anchor="nw")

    leader_window.mainloop()
