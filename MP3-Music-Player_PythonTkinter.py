MP3-Music-Player_PythonTkinter.py"



from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ttkthemes import ThemedTk
from pygame import mixer
from mutagen.mp3 import MP3
import os
import time
import threading

main_application = ThemedTk(theme = "breeze")
main_application.title('SC Music Player')
main_application.geometry('600x600')
main_application.wm_iconbitmap('SC Media Player.ico')

status_bar_label = ttk.Label(main_application, text = '\"Welcome To SC Music Player\"', relief = GROOVE, borderwidth = 2, font = ('Times New Roman', 15, 'italic','bold'))
status_bar_label.pack(side = TOP, fill = Y)

button_frame = Frame(main_application)
button_frame.pack(side  = BOTTOM, fill = X)

length_frame = Frame(main_application)
length_frame.pack(side = BOTTOM, fill = X)




