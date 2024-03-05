import tkinter
from tkinter import *

my_font = ("Arial", 12)
background_color = '#3A6351'
foreground_color = "#FFFFFF"


def return_new_username_label(window):
    return Label(window, text="New Username", bg=background_color, fg=foreground_color, font=my_font)


def return_new_username_entry(window):
    return Entry(window, font=my_font)


def return_new_password_label(window):
    return Label(window, text="New Password", bg=background_color, fg=foreground_color, font=my_font)


def return_new_password_entry(window):
    return Entry(window, show="*", font=my_font)
