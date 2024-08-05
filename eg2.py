import tkinter as tk
from tkinter import messagebox
from song import Song

# Songs for display
f = open('all_songs.txt')
all_songs=[]
lines = f.readlines()
for line in lines:
    data = line.split(',')
    all_songs.append(Song(title=data[0],singer=data[1],genre=data[2],duration=data[3])) 
    
    

fav_songs = []

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
                                   display_all(display_page), display_page.withdraw()], width=15)
    button_display_all.grid(row=0, column=0, padx=10, pady=10)

    button_display_favorite_songs = tk.Button(display_page, text="Display Favorite Songs", command=lambda: [
                                              display_fav(display_page), display_page.withdraw()], width=15)
    button_display_favorite_songs.grid(row=0, column=1, padx=10, pady=10)

    button_back = tk.Button(display_page, text="Back", command=lambda: [
        display_page.destroy(),
        next_page.deiconify()])
    button_back.grid(row=1, column=0, columnspan=2, pady=10)


# Function to display a message
def display_all(prevScreen):
    display_page = tk.Toplevel(root)
    display_page.title("Display All")

    # Create frames for listboxes to center content
    title_frame = tk.Frame(display_page)
    artist_frame = tk.Frame(display_page)
    album_frame = tk.Frame(display_page)
    duration_frame = tk.Frame(display_page)

    # Create listboxes
    listbox_titles = tk.Listbox(title_frame, height=10)
    listbox_artists = tk.Listbox(artist_frame, height=10)
    listbox_albums = tk.Listbox(album_frame, height=10)
    listbox_durations = tk.Listbox(duration_frame, height=10)

    for song in all_songs:
        listbox_titles.insert(tk.END, song.title)
        listbox_artists.insert(tk.END, song.singer)
        listbox_albums.insert(tk.END, song.genre)
        listbox_durations.insert(tk.END, song.duration)

    # Disable direct scrolling of the listboxes
    def no_scroll(event):
        return "break"

    listbox_titles.bind("<MouseWheel>", no_scroll)
    listbox_artists.bind("<MouseWheel>", no_scroll)
    listbox_albums.bind("<MouseWheel>", no_scroll)
    listbox_durations.bind("<MouseWheel>", no_scroll)

    # Create and configure the scrollbar
    scrollbar = tk.Scrollbar(display_page, orient=tk.VERTICAL)
    scrollbar.config(command=lambda *args: [listbox_titles.yview(*args), listbox_artists.yview(*args), listbox_albums.yview(*args), listbox_durations.yview(*args)])
    listbox_titles.config(yscrollcommand=scrollbar.set)
    listbox_artists.config(yscrollcommand=scrollbar.set)
    listbox_albums.config(yscrollcommand=scrollbar.set)
    listbox_durations.config(yscrollcommand=scrollbar.set)

    # Place listboxes within frames and center frames
    title_frame.grid(row=2, column=0)
    listbox_titles.pack(expand=True)
    artist_frame.grid(row=2, column=1)
    listbox_artists.pack(expand=True)
    album_frame.grid(row=2, column=2)
    listbox_albums.pack(expand=True)
    duration_frame.grid(row=2, column=3)
    listbox_durations.pack(expand=True)

    # Place the scrollbar
    scrollbar.grid(row=2, column=4, sticky='ns')

    button_back = tk.Button(display_page, text="Back", command=lambda: [
        display_page.destroy(),
        prevScreen.deiconify()])
    button_back.grid(row=5, column=1, columnspan=2, pady=10)


def display_fav(prevScreen):
    display_page = tk.Toplevel(root)
    display_page.title("Display Favourite songs")

    button_back = tk.Button(display_page, text="Back", command=lambda: [
        display_page.destroy(),
        prevScreen.deiconify()])
    button_back.grid(row=1, column=0, columnspan=2, pady=10)


def add_to_favorite(message):
    messagebox.showinfo("Add to Favorite", {message})


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

