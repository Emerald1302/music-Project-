

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import askyesno
from tkinter.simpledialog import askstring
from song import Song

# Read all songs and favorite songs
def load_songs():
    global all_songs, fav_songs
    with open('all_songs.txt') as f:
        all_songs = [Song(*line.strip().split(',')) for line in f.readlines()]
    with open('fav_song.txt') as f:
        fav_songs = [Song(*line.strip().split(',')) for line in f.readlines()]

load_songs()

def confirm():
    if askyesno(title='Confirm', message='Do you want to Exit?'):
        root.destroy()


####### Emerald#######



def display_songs():
    root.withdraw()
    display_page = tk.Toplevel(root)
    display_page.geometry('300x200')
    display_page.title("Display Songs")
    
    all_song_button = ttk.Button(display_page, text='Display All Songs', command=lambda: display_all_songs(display_page), width=20)
    all_song_button.grid(row=0, column=0, padx=10, pady=10)
    
    fav_song_button = ttk.Button(display_page, text='Display Favourite Songs', command=lambda: display_fav_songs(display_page), width=20)
    fav_song_button.grid(row=0, column=1, padx=10, pady=10)
    
    back_button = ttk.Button(display_page, text='Back', command=lambda: back_to_main(display_page), width=20)
    back_button.grid(row=2, column=0, columnspan=2, pady=10)

def display_all_songs(prev_window):
    root.withdraw()
    display_page = tk.Toplevel(root)
    display_page.title("All Songs")

    listbox_titles = tk.Listbox(display_page, height=10)
    listbox_singer = tk.Listbox(display_page, height=10)
    listbox_genre = tk.Listbox(display_page, height=10)
    listbox_durations = tk.Listbox(display_page, height=10)

    for song in all_songs:
        listbox_titles.insert(tk.END, song.title)
        listbox_singer.insert(tk.END, song.singer)
        listbox_genre.insert(tk.END, song.genre)
        listbox_durations.insert(tk.END, song.duration)

    listbox_titles.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    listbox_singer.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    listbox_genre.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    listbox_durations.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(display_page, orient=tk.VERTICAL)
    scrollbar.config(command=lambda *args: [listbox_titles.yview(*args), listbox_singer.yview(*args), listbox_genre.yview(*args), listbox_durations.yview(*args)])
    listbox_titles.config(yscrollcommand=scrollbar.set)
    listbox_singer.config(yscrollcommand=scrollbar.set)
    listbox_genre.config(yscrollcommand=scrollbar.set)
    listbox_durations.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    button_back = tk.Button(display_page, text="Back", command=lambda: back_to_main(display_page))
    button_back.pack(pady=10)

def display_fav_songs(prev_window):
    root.withdraw()
    display_page = tk.Toplevel(root)
    display_page.title("Favorite Songs")

    listbox_titles = tk.Listbox(display_page, height=10)
    listbox_singer = tk.Listbox(display_page, height=10)
    listbox_genre = tk.Listbox(display_page, height=10)
    listbox_durations = tk.Listbox(display_page, height=10)

    for song in fav_songs:
        listbox_titles.insert(tk.END, song.title)
        listbox_singer.insert(tk.END, song.singer)
        listbox_genre.insert(tk.END, song.genre)
        listbox_durations.insert(tk.END, song.duration)

    listbox_titles.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    listbox_singer.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    listbox_genre.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    listbox_durations.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(display_page, orient=tk.VERTICAL)
    scrollbar.config(command=lambda *args: [listbox_titles.yview(*args), listbox_singer.yview(*args), listbox_genre.yview(*args), listbox_durations.yview(*args)])
    listbox_titles.config(yscrollcommand=scrollbar.set)
    listbox_singer.config(yscrollcommand=scrollbar.set)
    listbox_genre.config(yscrollcommand=scrollbar.set)
    listbox_durations.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    button_back = tk.Button(display_page, text="Back", command=lambda: back_to_main(display_page))
    button_back.pack(pady=10)

def add_to_favorites():
    root.withdraw()
    add_page = tk.Toplevel(root)
    add_page.title("Add to Favorite")

    listbox_titles = tk.Listbox(add_page, selectmode=tk.SINGLE, height=10)
    for song in all_songs:
        listbox_titles.insert(tk.END, song.title)
    listbox_titles.grid(row=0, column=0, padx=10, pady=10)

    def add_selected_song():
        root.withdraw()
        selected_index = listbox_titles.curselection()
        if selected_index:
            selected_song = all_songs[selected_index[0]]
            if any(song.title == selected_song.title and
                   song.singer == selected_song.singer and
                   song.genre == selected_song.genre and
                   song.duration == selected_song.duration
                   for song in fav_songs):
                messagebox.showinfo("Add to Favorite", f"{selected_song.title} is already in the favorites.")
            else:
                fav_songs.append(selected_song)
                with open('fav_song.txt', 'a') as f:
                    f.write(','.join([selected_song.title, selected_song.singer, selected_song.genre, selected_song.duration]) + '\n')
                messagebox.showinfo("Add to Favorite", f"Added {selected_song.title} to favorites")
                add_page.destroy()
                root.deiconify()

    button_add = tk.Button(add_page, text="Add", command=add_selected_song)
    button_add.grid(row=1, column=0, padx=10, pady=10)

    button_back = tk.Button(add_page, text="Back", command=lambda: [add_page.destroy(), root.deiconify()])
    button_back.grid(row=2, column=0, padx=10, pady=10)


########Dante############


def search_songs():
    root.withdraw()
    search_page = tk.Toplevel(root)
    search_page.geometry('300x200')
    search_page.title("Search Songs")

    def search_all_songs():
        song_name = askstring("Search", "Enter song name:")
        if song_name:
            results = [song for song in all_songs if song.title.lower() == song_name.lower()]
            if results:
                display_search_results(search_page, "All Songs", results)
            else:
                messagebox.showinfo("Search Results", "No songs found.")

    def search_fav_songs():
        song_name = askstring("Search", "Enter song name:")
        if song_name:
            results = [song for song in fav_songs if song.title.lower() == song_name.lower()]
            if results:
                display_search_results(search_page, "Favorite Songs", results)
            else:
                messagebox.showinfo("Search Results", "No songs found.")

    search_all_song_button = ttk.Button(search_page, text='Search from All Songs', command=search_all_songs, width=20)
    search_all_song_button.grid(row=0, column=0, padx=10, pady=10)
    
    search_fav_song_button = ttk.Button(search_page, text='Search from Favourite Songs', command=search_fav_songs, width=20)
    search_fav_song_button.grid(row=0, column=1, padx=10, pady=10)
    
    back_button = ttk.Button(search_page, text='Back', command=lambda: back_to_main(search_page), width=20)
    back_button.grid(row=2, column=0, columnspan=2, pady=10)

def display_search_results(prev_window, title, results):
    root.withdraw()
    results_page = tk.Toplevel(root)
    results_page.title(title)

    listbox_titles = tk.Listbox(results_page, height=10)
    listbox_singer = tk.Listbox(results_page, height=10)
    listbox_genre = tk.Listbox(results_page, height=10)
    listbox_durations = tk.Listbox(results_page, height=10)

    for song in results:
        listbox_titles.insert(tk.END, song.title)
        listbox_singer.insert(tk.END, song.singer)
        listbox_genre.insert(tk.END, song.genre)
        listbox_durations.insert(tk.END, song.duration)

    listbox_titles.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    listbox_singer.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    listbox_genre.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    listbox_durations.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(results_page, orient=tk.VERTICAL)
    scrollbar.config(command=lambda *args: [listbox_titles.yview(*args), listbox_singer.yview(*args), listbox_genre.yview(*args), listbox_durations.yview(*args)])
    listbox_titles.config(yscrollcommand=scrollbar.set)
    listbox_singer.config(yscrollcommand=scrollbar.set)
    listbox_genre.config(yscrollcommand=scrollbar.set)
    listbox_durations.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    button_back = tk.Button(results_page, text="Back", command=lambda: back_to_main(results_page))
    button_back.pack(pady=10)

def delete_songs():
    root.withdraw()
    delete_page = tk.Toplevel(root)
    delete_page.geometry('200x300')
    delete_page.title("Delete Songs")

    listbox_titles = tk.Listbox(delete_page, selectmode=tk.SINGLE, height=10)
    for song in fav_songs:
        listbox_titles.insert(tk.END, song.title)
    listbox_titles.grid(row=0, column=0, padx=10, pady=10)

    def delete_selected_song():
        selected_index = listbox_titles.curselection()
        if selected_index:
            selected_song_title = listbox_titles.get(selected_index)
            global fav_songs
            fav_songs = [song for song in fav_songs if song.title != selected_song_title]
            with open('fav_song.txt', 'w') as f:
                for song in fav_songs:
                    f.write(','.join([song.title, song.singer, song.genre, song.duration]) + '\n')
            messagebox.showinfo("Delete Song", f"Deleted {selected_song_title} from favorites")
            delete_page.destroy()
            root.deiconify()

    button_delete = tk.Button(delete_page, text="Delete", command=delete_selected_song)
    button_delete.grid(row=1, column=0, padx=10, pady=10)

    button_back = tk.Button(delete_page, text="Back", command=lambda: [delete_page.destroy(), root.deiconify()])
    button_back.grid(row=2, column=0, padx=10, pady=10)

def back_to_main(window):
    window.destroy()
    root.deiconify()

def main_page():
    display_button = ttk.Button(root, text='Display', command=display_songs, width=20)
    display_button.grid(row=0, column=0, padx=10, pady=10)

    add_button = ttk.Button(root, text='Add to Favourite', command=add_to_favorites, width=20)
    add_button.grid(row=0, column=1, padx=10, pady=10)

    search_button = ttk.Button(root, text='Search Song', command=search_songs, width=20)
    search_button.grid(row=1, column=0, padx=10, pady=10)

    delete_button = ttk.Button(root, text='Delete Song', command=delete_songs, width=20)
    delete_button.grid(row=1, column=1, padx=10, pady=10)

    exit_button = ttk.Button(root, text='Exit', command=confirm, width=20)
    exit_button.grid(row=2, column=0, columnspan=2, pady=10)


root = tk.Tk()
root.geometry('300x200')
root.title('Music Player')

main_page()

root.mainloop()
