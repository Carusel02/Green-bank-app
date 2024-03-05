import random

import quiz_page
from quiz_page import *
from shop_page import *
import helpers as hp
from leader_page import *

tips = ["Utilizează serviciile noastre online pentru a renunța la hârtie.",
        "Explorează cardurile noastre cu recompense pentru călătorii eco-friendly.",
        "Fericirea și sănătatea noastră sunt strâns legate de sănătatea planetei. Îngrijirea mediului înseamnă "
        "îngrijirea de sine.",
        "Sustenabilitatea nu este doar despre a face mai puțin rău, ci și despre a face mai mult bine."
        ]


# client page
def client_page(name):
    # create client window
    client_window = Tk()
    client_window.title("Client Page")
    client_window.geometry('800x800+400+100')
    client_window.configure(bg='#89C18F')
    icon = PhotoImage(file=r'photo/logo.png')
    client_window.iconphoto(True, icon)

    # create frame for the tips
    tips_frame = Frame(client_window, bg='#3A6351')
    tips_frame.place(x=0, y=0, width=800, height=200, anchor="nw")

    # create area for tips
    tip_photo = PhotoImage(file=r'photo/light.png')
    tip_photo = tip_photo.subsample(10, 10)
    random_index = random.randint(0, len(tips) - 1)
    tips_label = Label(tips_frame,
                       text=tips[random_index],
                       bg='#3A6351',
                       fg="#FFFFFF",
                       font=("Arial", 10),
                       image=tip_photo,
                       compound="left",
                       pady=10)
    tips_label.place(x=0, y=70, width=800, height=200, anchor="nw")

    # create area for welcome
    profile_photo = PhotoImage(file=r'photo/client.png')
    profile_photo = profile_photo.subsample(5, 5)
    welcome_label = Label(tips_frame,
                          text="Welcome back, " + name,
                          bg='#3A6351',
                          fg="#FFFFFF",
                          font=("Arial", 20),
                          padx=20,
                          pady=20,
                          image=profile_photo,
                          compound="left")
    welcome_label.pack(side=TOP)

    # create frame for balance
    money = 100

    balance_frame = Frame(client_window, bg='#3C9970')
    balance_frame.place(x=0, y=200, width=800, height=200, anchor="nw")
    money_photo = PhotoImage(file=r'photo/cash.png')
    money_photo = money_photo.subsample(5, 5)
    money_label = Label(balance_frame,
                        text="Your balance is " + str(money) + " RON",
                        bg='#3C9970',
                        fg="#FFFFFF",
                        font=("Arial", 20),
                        padx=20,
                        image=money_photo,
                        compound="left", )
    money_label.pack(side=TOP)

    virtual_money_photo = PhotoImage(file=r'photo/currency.png')
    virtual_money_photo = virtual_money_photo.subsample(5, 5)
    virtual_money_photo = virtual_money_photo.subsample(5, 5)
    virtual_coin_label = Label(balance_frame,
                               text="Your balance is " + str(hp.my_virtual_coins) + " VIRTUAL COIN",
                               bg='#3C9970',
                               fg="#FFFFFF",
                               font=("Arial", 20),
                               image=virtual_money_photo,
                               padx=20,
                               compound="left")
    virtual_coin_label.pack(side=BOTTOM)

    # create frame for my rewards
    my_rewards_frame = Frame(client_window, bg='#366651')
    my_rewards_frame.place(x=0, y=400, width=800, height=200, anchor="nw")
    my_rewards_photo = PhotoImage(file=r'photo/reward.png')
    my_rewards_photo = my_rewards_photo.subsample(5, 5)
    my_rewards_label = Label(my_rewards_frame,
                             text="My rewards",
                             bg='#366651',
                             fg="#FFFFFF",
                             font=("Arial", 20),
                             padx=20,
                             pady=40,
                             image=my_rewards_photo,
                             compound="left", )
    my_rewards_label.pack(side=TOP)

    my_rewards_button_image = PhotoImage(file=r'photo/see_rewards.png')
    my_rewards_button_image = my_rewards_button_image.subsample(5, 5)
    my_rewards_button = Button(my_rewards_frame,
                               text="See shop rewards",
                               bg='#333333',
                               fg="#FFFFFF",
                               font=("Arial", 16),
                               padx=20,
                               pady=20,
                               command=lambda: shop_page(virtual_coin_label, name),
                               image=my_rewards_button_image,
                               compound="top")
    my_rewards_button.place(x=600, y=0, width=200, height=200, anchor="nw")

    quiz_button_image = PhotoImage(file=r'photo/question.png')
    quiz_button_image = quiz_button_image.subsample(5, 5)
    take_quiz_button = Button(my_rewards_frame,
                              text="Take a quiz",
                              bg='#333333',
                              fg="#FFFFFF",
                              font=("Arial", 16),
                              padx=20,
                              pady=20,
                              command=lambda: quiz_page(virtual_coin_label, name),
                              image=quiz_button_image,
                              compound="top")
    take_quiz_button.place(x=0, y=0, width=200, height=200, anchor="nw")

    # create frame for leaderboards
    leaderboards_frame = Frame(client_window, bg='#3C9970')
    leaderboards_frame.place(x=0, y=600, width=800, height=200, anchor="nw")
    leaderboards_photo = PhotoImage(file=r'photo/leaderboards.png')
    leaderboards_photo = leaderboards_photo.subsample(30, 30)
    leaderboards_button = Button(leaderboards_frame,
                                 text="Leaderboard",
                                 bg='#3C9970',
                                 fg="#FFFFFF",
                                 font=("Arial", 20),
                                 padx=20,
                                 pady=40,
                                 image=leaderboards_photo,
                                 compound="left",
                                 command=lambda: leader_page())
    leaderboards_button.place(x=0, y=0, width=800, height=200, anchor="nw")
    client_window.mainloop()
