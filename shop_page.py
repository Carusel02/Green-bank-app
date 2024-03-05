from tkinter import *
import helpers as hp


def click_button(button, price, label_balance, frame, username):
    if price - hp.my_virtual_coins <= 0:
        button.configure(bg='#3C9970')
        button.configure(text="Bought")
        button.configure(state=DISABLED)
        hp.my_virtual_coins -= price
        hp.leaderboard[username] -= price
        label_balance.configure(text="Your balance is " + str(hp.my_virtual_coins) + " VIRTUAL COIN")
        frame.config(text="You have " + str(hp.my_virtual_coins) + " VIRTUAL COIN left")


    else:
        button.configure(bg='#FF0000')
        button.configure(text="Not enough coins")


def shop_page(frame, username):
    window_shop = Toplevel()
    window_shop.title("Shop")
    window_shop.geometry('800x800+400+100')
    window_shop.configure(bg='#184728')

    label_balance = Label(window_shop,
                          text="Your balance is " + str(hp.my_virtual_coins) + " VIRTUAL COIN",
                          bg='#184728',
                          fg="#FFFFFF",
                          font=("Arial", 20),
                          padx=20,
                          pady=20)
    label_balance.place(x=0, y=600, width=800, height=100, anchor="nw")

    # create frame for the tips
    header_items = Frame(window_shop, bg='#184728')
    header_items.place(x=0, y=20, width=800, height=100, anchor="nw")
    header_image = PhotoImage(file=r'photo/voucher.png')
    header_image = header_image.subsample(5, 5)
    header_label = Label(header_items,
                         text="Items",
                         bg='#184728',
                         fg="#FFFFFF",
                         font=("Arial", 40),
                         image=header_image,
                         padx=20,
                         pady=20,
                         compound="left")
    header_label.place(x=0, y=0, width=750, height=100, anchor="nw")

    # create frame for first set of items
    items_frame = Frame(window_shop, bg='#184728')
    items_frame.place(x=0, y=200, width=800, height=400, anchor="nw")

    item1 = PhotoImage(file=r'photo/station.png')
    item1 = item1.subsample(5, 5)
    item1_button = Button(items_frame,
                          text="Bus subscription (3)",
                          bg='#184728',
                          fg="#FFFFFF",
                          font=("Arial", 20),
                          image=item1,
                          padx=20,
                          pady=20,
                          compound="left",
                          command=lambda: click_button(item1_button, 3, label_balance, frame, username))
    item1_button.place(x=0, y=0, width=400, height=200, anchor="nw")

    item2 = PhotoImage(file=r'photo/shop_voucher.png')
    item2 = item2.subsample(5, 5)
    item2_button = Button(items_frame,
                          text="Shop voucher (3)",
                          bg='#184728',
                          fg="#FFFFFF",
                          font=("Arial", 20),
                          image=item2,
                          padx=20,
                          pady=20,
                          compound="left",
                          command=lambda: click_button(item2_button, 3, label_balance, frame, username))
    item2_button.place(x=400, y=0, width=400, height=200, anchor="nw")

    item3 = PhotoImage(file=r'photo/fuel.png')
    item3 = item3.subsample(5, 5)
    item3_button = Button(items_frame,
                          text="Eco cashback (2)",
                          bg='#184728',
                          fg="#FFFFFF",
                          font=("Arial", 20),
                          image=item3,
                          padx=20,
                          pady=20,
                          compound="left",
                          command=lambda: click_button(item3_button, 2, label_balance, frame, username))
    item3_button.place(x=0, y=200, width=400, height=200, anchor="nw")

    item4 = PhotoImage(file=r'photo/donation.png')
    item4 = item4.subsample(5, 5)
    item4_button = Button(items_frame,
                          text="Donation (1)",
                          bg='#184728',
                          fg="#FFFFFF",
                          font=("Arial", 20),
                          image=item4,
                          padx=20,
                          pady=20,
                          compound="left",
                          command=lambda: click_button(item4_button, 1, label_balance, frame, username))
    item4_button.place(x=400, y=200, width=400, height=200, anchor="nw")

    # run the application, listen for events
    window_shop.mainloop()
