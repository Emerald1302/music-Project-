import tkinter as tk
from tkinter import messagebox
from song import Song

# read all songs file
f = open('all_songs.txt')
all_songs = []
lines = f.readlines()
for line in lines:
    data = line.split(',')
    all_songs.append(
        Song(title=data[0], singer=data[1], genre=data[2], duration=data[3]))
    f.close()

# read fav songs file
f2 = open('fav_song.txt')
fav_songs = []
lines2 = f2.readlines()
for line in lines2:
    data = line.split(',')
    fav_songs.append(Song(title=data[0], singer=data[1], genre=data[2], duration=data[3]))
    
print(fav_songs)
# Function for Login Button click

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Use a fixed username and password
    if username == "emerald" and password == "1311":
        messagebox.showinfo("Login", "Login Successful!")
        root.withdraw()
        main_page()
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

# Function to show the main page


def main_page():
    global next_page
    next_page = tk.Toplevel(root)
    next_page.title("Main Page")
    button_display = tk.Button(next_page, text="Display Songs", command=lambda: [
        display_songs(), next_page.withdraw()], width=20)
    button_display.grid(row=0, column=0, padx=10, pady=10)

    button_add_favorite = tk.Button(next_page, text="Add to Favorite", command=lambda: [
                                    add_to_favorite(), next_page.withdraw()], width=20)
    button_add_favorite.grid(row=0, column=1, padx=10, pady=10)

    button_search_song = tk.Button(next_page, text="Search Song", command=lambda: [
                                   search_song(), next_page.withdraw()], width=20)
    button_search_song.grid(row=1, column=0, padx=10, pady=10)

    button_delete_song = tk.Button(next_page, text="Delete Song", command=lambda: [
                                   delete_song(), next_page.withdraw()], width=20)
    button_delete_song.grid(row=1, column=1, padx=10, pady=10)

    button_exit = tk.Button(next_page, text="Exit", command=next_page.destroy)
    button_exit.grid(row=2, column=0, columnspan=2, pady=10)

# Update the function for displaying all songs


def display_songs():
    display_page = tk.Toplevel(root)
    display_page.title("Display Songs")
    button_display_all = tk.Button(display_page, text='Display all songs', command=lambda: [
                                   display_all(display_page, 'Display All Songs', all_songs), display_page.withdraw()], width=15)
    button_display_all.grid(row=0, column=0, padx=10, pady=10)

    button_display_favorite_songs = tk.Button(display_page, text="Display Favorite Songs", command=lambda: [
                                              display_all(display_page, 'Display Favourite Songs', fav_songs), display_page.withdraw()], width=15)
    button_display_favorite_songs.grid(row=0, column=1, padx=10, pady=10)

    button_back = tk.Button(display_page, text="Back", command=lambda: [
        display_page.destroy(),
        next_page.deiconify()])
    button_back.grid(row=1, column=0, columnspan=2, pady=10)


# Function to display a message
def display_all(prevScreen, label, songList):
    display_page = tk.Toplevel(root)
    display_page.title(label)

    # Create frames for listboxes to center content
    title_frame = tk.Frame(display_page)
    singer_frame = tk.Frame(display_page)
    genre_frame = tk.Frame(display_page)
    duration_frame = tk.Frame(display_page)

    # Listboxes are placed inside the respective frames
    listbox_titles = tk.Listbox(title_frame, height=10)
    listbox_singer = tk.Listbox(singer_frame, height=10)
    listbox_genre = tk.Listbox(genre_frame, height=10)
    listbox_durations = tk.Listbox(duration_frame, height=10)

    for song in songList:
        listbox_titles.insert(tk.END, song.title)
        listbox_singer.insert(tk.END, song.singer)
        listbox_genre.insert(tk.END, song.genre)
        listbox_durations.insert(tk.END, song.duration)

    # Disable direct scrolling of the listboxes
    def no_scroll(event):
        return "break"

    listbox_titles.bind("<MouseWheel>", no_scroll)
    listbox_singer.bind("<MouseWheel>", no_scroll)
    listbox_genre.bind("<MouseWheel>", no_scroll)
    listbox_durations.bind("<MouseWheel>", no_scroll)

    # Create and configure the scrollbar
    scrollbar = tk.Scrollbar(display_page, orient=tk.VERTICAL)
    scrollbar.config(command=lambda *args: [listbox_titles.yview(*args), listbox_singer.yview(
        *args), listbox_genre.yview(*args), listbox_durations.yview(*args)])
    listbox_titles.config(yscrollcommand=scrollbar.set)
    listbox_singer.config(yscrollcommand=scrollbar.set)
    listbox_genre.config(yscrollcommand=scrollbar.set)
    listbox_durations.config(yscrollcommand=scrollbar.set)

    # Place listboxes within frames and center frames
    title_frame.grid(row=2, column=0)
    listbox_titles.pack(expand=True)
    singer_frame.grid(row=2, column=1)
    listbox_singer.pack(expand=True)
    genre_frame.grid(row=2, column=2)
    listbox_genre.pack(expand=True)
    duration_frame.grid(row=2, column=3)
    listbox_durations.pack(expand=True)

    # Place the scrollbar
    scrollbar.grid(row=2, column=4, sticky='ns')

    button_back = tk.Button(display_page, text="Back", command=lambda: [
    display_page.destroy(),
    prevScreen.deiconify()])
    button_back.grid(row=5, column=1, columnspan=2, pady=10)


def add_to_favorite():
    add_page = tk.Toplevel(root)
    add_page.title("Add to Favorite")

    listbox_titles = tk.Listbox(add_page, selectmode=tk.SINGLE, height=10)
    for song in all_songs:
        listbox_titles.insert(tk.END, song.title)
    listbox_titles.grid(row=0, column=0, padx=10, pady=10)

    def add_selected_song():
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
                    f.write(str(selected_song) + '\n')  # Ensure each song is on a new line
                messagebox.showinfo("Add to Favorite", f"Added {selected_song.title} to favorites")
                add_page.destroy()
                next_page.deiconify()

    button_add = tk.Button(add_page, text="Add", command=add_selected_song)
    button_add.grid(row=1, column=0, padx=10, pady=10)

    button_back = tk.Button(add_page, text="Back", command=lambda: [
        add_page.destroy(), next_page.deiconify()])
    button_back.grid(row=2, column=0, padx=10, pady=10)

def search_song():
    messagebox.showinfo("Search Song", "Searching for a song")


def delete_song():
    messagebox.showinfo("Delete Song", "Deleting a song")


# Create the main window
root = tk.Tk()
root.title("Music Library")
root.geometry('300x200')

# Create and place the username label and entry
label_username = tk.Label(root, text="Username")
label_username.grid(row=1, column=0, padx=(20, 0), pady=(20, 10))
entry_username = tk.Entry(root, width=15)
entry_username.grid(row=1, column=1, padx=(30, 0), pady=(20, 10))

# Create and place the password label and entry
label_password = tk.Label(root, text="Password")
label_password.grid(row=2, column=0, padx=(20, 0), pady=10)
entry_password = tk.Entry(root, show="*", width=15)
entry_password.grid(row=2, column=1, padx=(30, 0), pady=10)

# Create and place the login button
button_login = tk.Button(root, text="Login", command=login)
button_login.grid(row=3, column=0, columnspan=2, pady=10)

# run mainloop
root.mainloop()
