import os
import random
import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import webbrowser


html_file = 'index.html'


flag_file = 'flag.txt'
if not os.path.exists(flag_file):
    webbrowser.open(html_file)


    with open(flag_file, 'w') as file:
        file.write('Flag')

pygame.mixer.init() 

def play_music(track_name, folder_path, volume):
    pygame.mixer.music.stop()
    pygame.mixer.music.set_volume(volume / 100)
    pygame.mixer.music.load(os.path.join(folder_path, track_name))
    pygame.mixer.music.play()

def choose_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)
        update_track_list()

def update_track_list():
    folder = folder_path.get()
    tracks = sorted(os.listdir(folder))
    track_list.delete(0, tk.END)
    for track in tracks:
        track_list.insert(tk.END, track)

def play_selected_track():
    selected_track = track_list.get(tk.ACTIVE)
    folder = folder_path.get()
    volume = volume_scale.get()
    play_music(selected_track, folder, volume)

def stop_music():
    pygame.mixer.music.stop()

def play_random_track():
    folder = folder_path.get()
    volume = volume_scale.get()
    tracks = track_list.get(0, tk.END)
    random_track = random.choice(tracks)
    play_music(random_track, folder, volume)

def change_volume(value):
    volume = volume_scale.get()
    pygame.mixer.music.set_volume(volume / 100)

root = tk.Tk()
root.title("player")
root.geometry("400x400")


folder_path = tk.StringVar()
folder_label = ttk.Label(root, text="Выберите папку с музыкой:")
folder_label.pack(pady=10)
folder_frame = ttk.Frame(root)
folder_frame.pack()
folder_entry = ttk.Entry(folder_frame, textvariable=folder_path)
folder_entry.pack(side=tk.LEFT, padx=5)
folder_button = ttk.Button(folder_frame, text="Обзор", command=choose_folder)
folder_button.pack(side=tk.LEFT, padx=5)


track_frame = ttk.Frame(root)
track_frame.pack(pady=10)
track_label = ttk.Label(track_frame, text="Список треков:")
track_label.pack()
scrollbar = ttk.Scrollbar(track_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
track_list = tk.Listbox(track_frame, yscrollcommand=scrollbar.set, width=60) 
track_list.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=track_list.yview)



control_frame = ttk.Frame(root)
control_frame.pack(pady=10)
play_button = ttk.Button(control_frame, text="Воспроизвести", command=play_selected_track)
play_button.pack(side=tk.LEFT, padx=5)
stop_button = ttk.Button(control_frame, text="Остановить", command=stop_music)
stop_button.pack(side=tk.LEFT, padx=5)
random_button = ttk.Button(control_frame, text="Случайный трек", command=play_random_track)
random_button.pack(side=tk.LEFT, padx=5)


volume_frame = ttk.Frame(root)
volume_frame.pack(pady=10)
volume_label = ttk.Label(volume_frame, text="Громкость:")
volume_label.pack(side=tk.LEFT, padx=5)
volume_scale = ttk.Scale(volume_frame, from_=0, to=100, orient=tk.HORIZONTAL, command=change_volume)
volume_scale.pack(side=tk.LEFT, padx=5)

root.mainloop()
