# Autor: Ghita Mihai & Marin Marius
from helpers import *
from builder import *
from client_page import *
import helpers as hp
from leader_page import *

# dictionary for users
users = {}


# save the registration in the dictionary of users
def save_registration(username, password, window):
    if username in users:
        # show error message
        messagebox.showerror(title="Error", message="Username already exists.")
    else:
        # hash the password
        hashed_password = hash_password(password)
        # save the username and password in the dictionary
        messagebox.showinfo(title="Registration", message="New account registered.")
        users[username] = hashed_password
        # add them to the leaderboard
        leaderboard[username] = 0

    window.destroy()


# check the credentials
def check_credential(username_entry, password_entry, window):
    hashed_password = hash_password(password_entry)
    if username_entry in users and users[username_entry] == hashed_password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        window.destroy()
        client_page(username_entry)
    else:
        messagebox.showerror(title="Error", message="Invalid login.")



def register_page():
    # create register window
    register_window = Toplevel()
    register_window.title("Register")
    register_window.geometry('800x800+400+100')
    register_window.configure(bg='#89C18F')

    # Creating widgets for the registration window
    new_username_label = return_new_username_label(register_window)
    new_username_entry = return_new_username_entry(register_window)
    new_password_label = return_new_password_label(register_window)
    new_password_entry = return_new_password_entry(register_window)
    save_button = Button(register_window, text="Save", bg="#3A6351", fg="#FFFFFF", font=("Arial", 12),
                         command=lambda: save_registration(new_username_entry.get(), new_password_entry.get(),
                                                           register_window))

    # Placing widgets in the registration window
    new_username_label.place(x=200, y=200, width=150, height=50, anchor="nw")
    new_username_entry.place(x=350, y=200, width=250, height=50, anchor="nw")
    new_password_label.place(x=200, y=300, width=150, height=50, anchor="nw")
    new_password_entry.place(x=350, y=300, width=250, height=50, anchor="nw")
    save_button.place(x=290, y=400, width=250, height=50, anchor="nw")

    register_window.mainloop()


def login_page():
    # instantiate the window
    login_window = Tk()

    # set the window title
    login_window.title("Bank application")

    # set icon for the window
    icon = PhotoImage(file=r'photo/logo.png')
    login_window.iconphoto(True, icon)

    # set photo for the window
    photo = PhotoImage(file=r'photo/login_image.png')
    # photo = photo.subsample(2, 2)

    label_welcome = Label(login_window,
                          text="Welcome to the bank application!",
                          bg='#89C18F',
                          fg="#3A6351",
                          font=("Arial", 20),
                          image=photo,
                          compound="bottom")

    # set username label
    username_label = Label(login_window,
                           text="Username",
                           bg='#3A6351',
                           fg="#FFFFFF",
                           font=("Arial", 16))

    # set password label
    password_label = Label(login_window,
                           text="Password",
                           bg='#3A6351',
                           fg="#FFFFFF",
                           font=("Arial", 16))

    # entry for username
    username_entry = Entry(login_window, font=("Arial", 16))
    # entry for password
    password_entry = Entry(login_window, show="*", font=("Arial", 16))

    # set login button
    login_button = Button(login_window,
                          text="Sign in",
                          bg='#333333',
                          fg="#FFFFFF",
                          font=("Arial", 16),
                          padx=20,
                          pady=20,
                          command=lambda: check_credential(username_entry.get(), password_entry.get(), login_window))

    # set register button
    register_button = Button(login_window,
                             text="Register",
                             bg='#333333',
                             fg="#FFFFFF",
                             font=("Arial", 16),
                             padx=20,
                             pady=20,
                             command=lambda: register_page())

    # Placing widgets on the screen
    label_welcome.place(x=50, y=0, width=700, height=400)
    username_label.place(x=200, y=400, width=150, height=50, anchor="nw")
    password_label.place(x=200, y=500, width=150, height=50, anchor="nw")
    username_entry.place(x=350, y=400, width=250, height=50, anchor="nw")
    password_entry.place(x=350, y=500, width=250, height=50, anchor="nw")
    login_button.place(x=290, y=600, width=250, height=50, anchor="nw")
    register_button.place(x=290, y=670, width=250, height=50, anchor="nw")

    login_window.geometry('800x800+400+100')  # set the window size
    login_window.configure(bg='#89C18F')
    login_window.mainloop()  # run the application, listen for events


def main():
    login_page()

if __name__ == "__main__":
    main()
