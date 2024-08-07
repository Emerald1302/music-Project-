import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
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





class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('2560x1600')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        # Background image
        self.bg_frame = Image.open('images\\bbbb.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # Login Frame
        self.lgn_frame = Frame(self.window, bg='#040405', width=950, height=600)
        self.lgn_frame.place(x=400, y=200)

        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405", fg='white', bd=5, relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)
       
        self.side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(self.side_image)
        self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.side_image_label.image = photo
        self.side_image_label.place(x=5, y=100)

        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=620, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=650, y=240)


        # Username
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=550, y=300)
        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69", font=("yu gothic ui", 12, "bold"), insertbackground='#6b6a69')
        self.username_entry.place(x=580, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=550, y=359)

        self.username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(self.username_icon)
        self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=550, y=332)




        # Password
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=550, y=380)
        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69", font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.password_entry.place(x=580, y=416, width=244)
        # ======== Password icon ================
        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=550, y=440)

        self.password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(self.password_icon)
        self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=550, y=414)
   
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)


        # Login button
        self.lgn_button_image = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button_image)

        # Create label for the image and place it
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo  # Keep a reference to avoid garbage collection
        self.lgn_button_label.place(x=550, y=450)  # Use place on the label

        # Create the login button and place it
        self.login_button = Button(self.lgn_frame, text='LOGIN', font=("yu gothic ui", 13, "bold"),
                                width=25, bd=0, bg='#3047ff', cursor='hand2',
                                activebackground='#3047ff', fg='white', command=self.check_login)
        self.login_button.place(x=575, y=465) 

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "admin":
            messagebox.showinfo("Welcome", "Welcome Back")
            self.window.destroy()  # Close the login window
            main_page()  # Open the main music player interface
        else:
            messagebox.showerror("Login", "Invalid Username or Password")


    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')




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

def display_all_songs(prev_screen):
    display_all(prev_screen, "All Songs", all_songs)

def display_fav_songs(prev_screen):
    display_all(prev_screen, "Favourite Songs", fav_songs)

# def display_all(prev_screen, label, song_list):
#     prev_screen.destroy()
#     display_page = tk.Toplevel(root)
#     display_page.title(label)

#     # Create frames for listboxes to center content
#     number_frame = tk.Frame(display_page)
#     title_frame = tk.Frame(display_page)
#     singer_frame = tk.Frame(display_page)
#     genre_frame = tk.Frame(display_page)
#     duration_frame = tk.Frame(display_page)

#     # Listboxes are placed inside the respective frames
#     listbox_numbers = tk.Listbox(number_frame, height=10)
#     listbox_titles = tk.Listbox(title_frame, height=10)
#     listbox_singer = tk.Listbox(singer_frame, height=10)
#     listbox_genre = tk.Listbox(genre_frame, height=10)
#     listbox_durations = tk.Listbox(duration_frame, height=10)

#     for index, song in enumerate(song_list, start=1):
#         listbox_numbers.insert(tk.END, index)
#         listbox_titles.insert(tk.END, song.title)
#         listbox_singer.insert(tk.END, song.singer)
#         listbox_genre.insert(tk.END, song.genre)
#         listbox_durations.insert(tk.END, song.duration)

#     # Disable direct scrolling of the listboxes
#     def no_scroll(event):
#         return "break"

#     listbox_numbers.bind("<MouseWheel>", no_scroll)
#     listbox_titles.bind("<MouseWheel>", no_scroll)
#     listbox_singer.bind("<MouseWheel>", no_scroll)
#     listbox_genre.bind("<MouseWheel>", no_scroll)
#     listbox_durations.bind("<MouseWheel>", no_scroll)

#     # Create and configure the scrollbar
#     scrollbar = tk.Scrollbar(display_page, orient=tk.VERTICAL)
#     scrollbar.config(command=lambda *args: [listbox_numbers.yview(*args), listbox_titles.yview(*args),
#                                             listbox_singer.yview(*args), listbox_genre.yview(*args),
#                                             listbox_durations.yview(*args)])
#     listbox_numbers.config(yscrollcommand=scrollbar.set)
#     listbox_titles.config(yscrollcommand=scrollbar.set)
#     listbox_singer.config(yscrollcommand=scrollbar.set)
#     listbox_genre.config(yscrollcommand=scrollbar.set)
#     listbox_durations.config(yscrollcommand=scrollbar.set)

#     # Place listboxes within frames and center frames
#     number_frame.grid(row=2, column=0)
#     listbox_numbers.pack(expand=True)
#     title_frame.grid(row=2, column=1)
#     listbox_titles.pack(expand=True)
#     singer_frame.grid(row=2, column=2)
#     listbox_singer.pack(expand=True)
#     genre_frame.grid(row=2, column=3)
#     listbox_genre.pack(expand=True)
#     duration_frame.grid(row=2, column=4)
#     listbox_durations.pack(expand=True)

#     # Place the scrollbar
#     scrollbar.grid(row=2, column=5, sticky='ns')

#     button_back = tk.Button(display_page, text="Back", command=lambda: [display_page.destroy(), root.deiconify()])
#     button_back.grid(row=5, column=1, columnspan=2, pady=10)



def display_all(prev_screen, label, song_list):
    # Destroy the previous window
    prev_screen.destroy()

    # Create a new window for displaying all songs
    display_page = tk.Toplevel(root)
    display_page.title(label)
    
    # Calculate the number of results
    display_all_count = len(song_list)

    # Frame for result headers
    header_frame = tk.Frame(display_page)
    header_frame.grid(row=0, column=0, columnspan=6, pady=10, padx=10)

    # Label showing the number of results
    display_all_count_label = tk.Label(header_frame, text=f"Number of Results: {display_all_count}", font=("Helvetica", 12, "bold"))
    display_all_count_label.grid(row=0, column=0, columnspan=6, pady=5)

    headers = ["No.", "Song Title", "Singer", "Genre", "Duration"]
    widths = [10, 35, 25, 20, 15]  # Fixed widths for each column

    for idx, (header, width) in enumerate(zip(headers, widths)):
        tk.Label(header_frame, text=header, font=("Helvetica", 12, "bold"), width=width, anchor='w').grid(row=1, column=idx, padx=5)

    # Frames for each column
    number_frame = tk.Frame(display_page)
    title_frame = tk.Frame(display_page)
    singer_frame = tk.Frame(display_page)
    genre_frame = tk.Frame(display_page)
    duration_frame = tk.Frame(display_page)

    number_frame.grid(row=2, column=0, sticky='nsew')
    title_frame.grid(row=2, column=1, sticky='nsew')
    singer_frame.grid(row=2, column=2, sticky='nsew')
    genre_frame.grid(row=2, column=3, sticky='nsew')
    duration_frame.grid(row=2, column=4, sticky='nsew')

    listbox_numbers = tk.Listbox(number_frame, height=15, width=5)
    listbox_titles = tk.Listbox(title_frame, height=15, width=35)
    listbox_singer = tk.Listbox(singer_frame, height=15, width=25)
    listbox_genre = tk.Listbox(genre_frame, height=15, width=20)
    listbox_durations = tk.Listbox(duration_frame, height=15, width=15)

    for index, song in enumerate(song_list, start=1):
        listbox_numbers.insert(tk.END, f"{index:02d}")  # Format song number with leading zero
        listbox_titles.insert(tk.END, song.title)
        listbox_singer.insert(tk.END, song.singer)
        listbox_genre.insert(tk.END, song.genre)
        listbox_durations.insert(tk.END, song.duration)

    # Place the listboxes within their frames
    listbox_numbers.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    listbox_titles.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    listbox_singer.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    listbox_genre.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    listbox_durations.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create and configure the scrollbar
    scrollbar = tk.Scrollbar(display_page, orient=tk.VERTICAL)
    scrollbar.config(command=lambda *args: [listbox_numbers.yview(*args), listbox_titles.yview(*args),
                                            listbox_singer.yview(*args), listbox_genre.yview(*args), listbox_durations.yview(*args)])
    listbox_numbers.config(yscrollcommand=scrollbar.set)
    listbox_titles.config(yscrollcommand=scrollbar.set)
    listbox_singer.config(yscrollcommand=scrollbar.set)
    listbox_genre.config(yscrollcommand=scrollbar.set)
    listbox_durations.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=2, column=5, sticky='ns')

    # Back button to return to the main page
    button_back = tk.Button(display_page, text="Back", command=lambda: [display_page.destroy(), root.deiconify()])
    button_back.grid(row=3, column=0, columnspan=6, pady=10)

    # Configure the grid to expand properly
    display_page.grid_columnconfigure(0, weight=1)
    display_page.grid_columnconfigure(1, weight=1)
    display_page.grid_columnconfigure(2, weight=1)
    display_page.grid_columnconfigure(3, weight=1)
    display_page.grid_columnconfigure(4, weight=1)
    display_page.grid_columnconfigure(5, weight=0)  

def add_to_favorites():
    root.withdraw()
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
                    f.write(','.join([selected_song.title, selected_song.singer, selected_song.genre, selected_song.duration]) + '\n')
                messagebox.showinfo("Add to Favorite", f"Added {selected_song.title} to favorites")
                add_page.destroy()
                root.deiconify()

    button_add = tk.Button(add_page, text="Add", command=add_selected_song)
    button_add.grid(row=1, column=0, padx=10, pady=10)

    button_back = tk.Button(add_page, text="Back", command=lambda: [add_page.destroy(), root.deiconify()])
    button_back.grid(row=2, column=0, padx=10, pady=10)

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
    
    def search_singers():
        singer_name = askstring("Search", "Enter singer name:")
        if singer_name:
            results = [song for song in all_songs if song.singer.lower() == singer_name.lower()]
            if results:
                display_search_results(search_page, "All Songs", results)
            else:
                messagebox.showinfo("Search Results", "No singer found.")

    def search_genres():
        genre_name = askstring("Search", "Enter genre name:")
        if genre_name:
            results = [song for song in all_songs if song.genre.lower() == genre_name.lower()]
            if results:
                display_search_results(search_page, "All Songs", results)
            else:
                messagebox.showinfo("Search Results", "No genre found.")
    




    search_all_song_button = ttk.Button(search_page, text='Search from All Songs', command=search_all_songs, width=20)
    search_all_song_button.grid(row=0, column=0, padx=10, pady=10)
    
    search_fav_song_button = ttk.Button(search_page, text='Search from Favourite Songs', command=search_fav_songs, width=20)
    search_fav_song_button.grid(row=0, column=1, padx=10, pady=10)
    
    search_all_singer_button = ttk.Button(search_page, text='Search By Singers', command=search_singers, width=20)
    search_all_singer_button.grid(row=1, column=0, columnspan=2, pady=10)
    
    search_all_genre_button = ttk.Button(search_page, text='Search By Genres', command=search_genres, width=20)
    search_all_genre_button.grid(row=2, column=0, columnspan=2, pady=10)
        
    back_button = ttk.Button(search_page, text='Back', command=lambda: back_to_main(search_page), width=20)
    back_button.grid(row=3, column=0, columnspan=2, pady=10)


def display_search_results(prev_window, title, results):
    prev_window.destroy()  # Destroy the previous window
    results_page = tk.Toplevel(root)
    results_page.title(title)

    # Calculate the number of results
    results_count = len(results)

    # Create a frame for labels at the top
    header_frame = tk.Frame(results_page)
    header_frame.grid(row=0, column=0, columnspan=5, pady=10)

    # Add a label showing the number of results
    results_count_label = tk.Label(header_frame, text=f"Number of Results: {results_count}", font=("Helvetica", 12, "bold"))
    results_count_label.grid(row=0, column=0, columnspan=5, pady=5)

    # Create labels for the headers
    tk.Label(header_frame, text="No", font=("Helvetica", 12, "bold")).grid(row=1, column=0, padx=5)
    tk.Label(header_frame, text="Song Title", font=("Helvetica", 12, "bold")).grid(row=1, column=1, padx=5)
    tk.Label(header_frame, text="Singer", font=("Helvetica", 12, "bold")).grid(row=1, column=2, padx=5)
    tk.Label(header_frame, text="Genre", font=("Helvetica", 12, "bold")).grid(row=1, column=3, padx=5)
    tk.Label(header_frame, text="Duration", font=("Helvetica", 12, "bold")).grid(row=1, column=4, padx=5)

    # # Frame for result headers
    # header_frame = tk.Frame(results_page)
    # header_frame.grid(row=0, column=0, columnspan=6, pady=10, padx=10)

    # # Label showing the number of results
    # display_all_count_label = tk.Label(header_frame, text=f"Number of Results: {results_count}", font=("Helvetica", 12, "bold"))
    # display_all_count_label.grid(row=0, column=0, columnspan=6, pady=5)

    # headers = ["No.", "Song Title", "Singer", "Genre", "Duration"]
    # widths = [10, 35, 25, 20, 15]  # Fixed widths for each column

    # for idx, (header, width) in enumerate(zip(headers, widths)):
    #     tk.Label(header_frame, text=header, font=("Helvetica", 12, "bold"), width=width, anchor='w').grid(row=1, column=idx, padx=5)



    # Create frames for the listboxes to center content
    number_frame = tk.Frame(results_page)
    title_frame = tk.Frame(results_page)
    singer_frame = tk.Frame(results_page)
    genre_frame = tk.Frame(results_page)
    duration_frame = tk.Frame(results_page)

    listbox_numbers = tk.Listbox(number_frame, height=15, width=5)
    listbox_titles = tk.Listbox(title_frame, height=15, width=35)
    listbox_singer = tk.Listbox(singer_frame, height=15, width=25)
    listbox_genre = tk.Listbox(genre_frame, height=15, width=20)
    listbox_durations = tk.Listbox(duration_frame, height=15, width=15)

    for index, song in enumerate(results, start=1):
        listbox_numbers.insert(tk.END, f"{index:02d}")  # Format song number with leading zero
        listbox_titles.insert(tk.END, song.title)
        listbox_singer.insert(tk.END, song.singer)
        listbox_genre.insert(tk.END, song.genre)
        listbox_durations.insert(tk.END, song.duration)

    # Place listboxes within frames using grid
    number_frame.grid(row=2, column=0)
    listbox_numbers.pack(expand=True, fill=tk.BOTH)
    title_frame.grid(row=2, column=1)
    listbox_titles.pack(expand=True, fill=tk.BOTH)
    singer_frame.grid(row=2, column=2)
    listbox_singer.pack(expand=True, fill=tk.BOTH)
    genre_frame.grid(row=2, column=3)
    listbox_genre.pack(expand=True, fill=tk.BOTH)
    duration_frame.grid(row=2, column=4)
    listbox_durations.pack(expand=True, fill=tk.BOTH)

    # Create and configure the scrollbar
    scrollbar = tk.Scrollbar(results_page, orient=tk.VERTICAL)
    scrollbar.config(command=lambda *args: [listbox_numbers.yview(*args), listbox_titles.yview(*args),
                                            listbox_singer.yview(*args), listbox_genre.yview(*args),
                                            listbox_durations.yview(*args)])
    listbox_numbers.config(yscrollcommand=scrollbar.set)
    listbox_titles.config(yscrollcommand=scrollbar.set)
    listbox_singer.config(yscrollcommand=scrollbar.set)
    listbox_genre.config(yscrollcommand=scrollbar.set)
    listbox_durations.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=2, column=5, sticky='ns')

    # Center the back button
    button_back = tk.Button(results_page, text="Back", command=lambda: [results_page.destroy(), root.deiconify()])
    button_back.grid(row=3, column=1, columnspan=3, pady=10)



# def display_search_results(prev_window, title, results):
#     prev_window.destroy()  # Destroy the previous window
#     results_page = tk.Toplevel(root)
#     results_page.title(title)

#     listbox_titles = tk.Listbox(results_page, height=10)
#     listbox_singer = tk.Listbox(results_page, height=10)
#     listbox_genre = tk.Listbox(results_page, height=10)
#     listbox_durations = tk.Listbox(results_page, height=10)

#     for song in results:
#         listbox_titles.insert(tk.END, song.title)
#         listbox_singer.insert(tk.END, song.singer)
#         listbox_genre.insert(tk.END, song.genre)
#         listbox_durations.insert(tk.END, song.duration)

#     listbox_titles.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#     listbox_singer.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#     listbox_genre.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#     listbox_durations.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#     scrollbar = tk.Scrollbar(results_page, orient=tk.VERTICAL)
#     scrollbar.config(command=lambda *args: [listbox_titles.yview(*args), listbox_singer.yview(*args), listbox_genre.yview(*args), listbox_durations.yview(*args)])
#     listbox_titles.config(yscrollcommand=scrollbar.set)
#     listbox_singer.config(yscrollcommand=scrollbar.set)
#     listbox_genre.config(yscrollcommand=scrollbar.set)
#     listbox_durations.config(yscrollcommand=scrollbar.set)
#     scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#     button_back = tk.Button(results_page, text="Back", command=lambda: back_to_main(results_page))
#     button_back.pack(pady=10)

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


# def edit():
#     root.withdraw()
#     edit_page = tk.Toplevel(root)
#     edit_page.geometry('300x200')
#     edit_page.title("Edit Songs")




#     edit_new_button = ttk.Button(edit_page, text='Edit from songs', command=edit_songs, width=20)
#     edit_new_button.grid(row=1, column=0, columnspan=2, pady=10)

#     update_button = ttk.Button(edit_page, text='ADD new Song', command=add_song, width=20)
#     update_button.grid(row=2, column=0, columnspan=2, pady=10)

#     back_button = ttk.Button(edit_page, text='Back', command=lambda: back_to_main(edit_page), width=20)
#     back_button.grid(row=3, column=0, columnspan=2, pady=10)

    

# def edit_songs():
#     root.withdraw()
#     edit_page = tk.Toplevel(root)
#     edit_page.title("Edit Songs")

#     listbox_titles = tk.Listbox(edit_page, selectmode=tk.SINGLE, height=10)
#     for song in all_songs:
#         listbox_titles.insert(tk.END, song.title)
#     listbox_titles.grid(row=0, column=0, padx=10, pady=10)

#     def load_song_details():
#         selected_index = listbox_titles.curselection()
#         if selected_index:
#             selected_song = all_songs[selected_index[0]]
#             title_entry.delete(0, tk.END)
#             title_entry.insert(0, selected_song.title)
#             singer_entry.delete(0, tk.END)
#             singer_entry.insert(0, selected_song.singer)
#             genre_entry.delete(0, tk.END)
#             genre_entry.insert(0, selected_song.genre)
#             duration_entry.delete(0, tk.END)
#             duration_entry.insert(0, selected_song.duration)

#     def save_changes():
#         selected_index = listbox_titles.curselection()
#         if selected_index:
#             selected_song = all_songs[selected_index[0]]
#             new_title = title_entry.get()
#             new_singer = singer_entry.get()
#             new_genre = genre_entry.get()
#             new_duration = duration_entry.get()

#             # Update the song in the list
#             selected_song.title = new_title
#             selected_song.singer = new_singer
#             selected_song.genre = new_genre
#             selected_song.duration = new_duration

#             # Save the updated song list to the file
#             with open('all_songs.txt', 'w') as f:
#                 for song in all_songs:
#                     f.write(','.join([song.title, song.singer, song.genre, song.duration]) + '\n')

#             messagebox.showinfo("Edit Song", f"Updated {new_title}")
#             edit_page.destroy()
#             root.deiconify()

#     title_label = tk.Label(edit_page, text="Title:")
#     title_label.grid(row=1, column=0, padx=10, pady=5)
#     title_entry = tk.Entry(edit_page)
#     title_entry.grid(row=1, column=1, padx=10, pady=5)

#     singer_label = tk.Label(edit_page, text="Singer:")
#     singer_label.grid(row=2, column=0, padx=10, pady=5)
#     singer_entry = tk.Entry(edit_page)
#     singer_entry.grid(row=2, column=1, padx=10, pady=5)

#     genre_label = tk.Label(edit_page, text="Genre:")
#     genre_label.grid(row=3, column=0, padx=10, pady=5)
#     genre_entry = tk.Entry(edit_page)
#     genre_entry.grid(row=3, column=1, padx=10, pady=5)

#     duration_label = tk.Label(edit_page, text="Duration:")
#     duration_label.grid(row=4, column=0, padx=10, pady=5)
#     duration_entry = tk.Entry(edit_page)
#     duration_entry.grid(row=4, column=1, padx=10, pady=5)

#     load_button = tk.Button(edit_page, text="Load Details", command=load_song_details)
#     load_button.grid(row=5, column=0, padx=10, pady=10)

#     save_button = tk.Button(edit_page, text="Save Changes", command=save_changes)
#     save_button.grid(row=5, column=1, padx=10, pady=10)

#     back_button = tk.Button(edit_page, text="Back", command=lambda: [edit_page.destroy(), root.deiconify()])
#     back_button.grid(row=6, column=0, columnspan=2, pady=10)






# def edit_songs():
#     root.withdraw()
#     edit_page = tk.Toplevel(root)
#     edit_page.title("Edit Songs")

#     listbox_titles = tk.Listbox(edit_page, selectmode=tk.EXTENDED, height=10)
#     for song in all_songs:
#         listbox_titles.insert(tk.END, song.title)
#     listbox_titles.grid(row=0, column=0, padx=10, pady=10)

#     def load_song_details():
#         selected_indices = listbox_titles.curselection()
#         if selected_indices:
#             selected_song = all_songs[selected_indices[0]]
#             title_entry.delete(0, tk.END)
#             title_entry.insert(0, selected_song.title)
#             singer_entry.delete(0, tk.END)
#             singer_entry.insert(0, selected_song.singer)
#             genre_entry.delete(0, tk.END)
#             genre_entry.insert(0, selected_song.genre)
#             duration_entry.delete(0, tk.END)
#             duration_entry.insert(0, selected_song.duration)

#     def save_changes():
#         selected_indices = listbox_titles.curselection()
#         if selected_indices:
#             for index in selected_indices:
#                 selected_song = all_songs[index]
#                 new_title = title_entry.get()
#                 new_singer = singer_entry.get()
#                 new_genre = genre_entry.get()
#                 new_duration = duration_entry.get()

#                 # Update the song in the list
#                 selected_song.title = new_title
#                 selected_song.singer = new_singer
#                 selected_song.genre = new_genre
#                 selected_song.duration = new_duration

#             # Save the updated song list to the file
#             with open('all_songs.txt', 'w') as f:
#                 for song in all_songs:
#                     f.write(','.join([song.title, song.singer, song.genre, song.duration]) + '\n')

#             messagebox.showinfo("Edit Song", f"Updated {len(selected_indices)} song(s)")
#             edit_page.destroy()
#             root.deiconify()

    # title_label = tk.Label(edit_page, text="Title:")
    # title_label.grid(row=1, column=0, padx=10, pady=5)
    # title_entry = tk.Entry(edit_page)
    # title_entry.grid(row=1, column=1, padx=10, pady=5)

    # singer_label = tk.Label(edit_page, text="Singer:")
    # singer_label.grid(row=2, column=0, padx=10, pady=5)
    # singer_entry = tk.Entry(edit_page)
    # singer_entry.grid(row=2, column=1, padx=10, pady=5)

    # genre_label = tk.Label(edit_page, text="Genre:")
    # genre_label.grid(row=3, column=0, padx=10, pady=5)
    # genre_entry = tk.Entry(edit_page)
    # genre_entry.grid(row=3, column=1, padx=10, pady=5)

    # duration_label = tk.Label(edit_page, text="Duration:")
    # duration_label.grid(row=4, column=0, padx=10, pady=5)
    # duration_entry = tk.Entry(edit_page)
    # duration_entry.grid(row=4, column=1, padx=10, pady=5)

    # load_button = tk.Button(edit_page, text="Load Details", command=load_song_details)
    # load_button.grid(row=5, column=0, padx=10, pady=10)

    # save_button = tk.Button(edit_page, text="Save Changes", command=save_changes)
    # save_button.grid(row=5, column=1, padx=10, pady=10)

    # back_button = tk.Button(edit_page, text="Back", command=lambda: [edit_page.destroy(), root.deiconify()])
    # back_button.grid(row=6, column=0, columnspan=2, pady=10)






def edit_songs():
    root.withdraw()
    edit_page = tk.Toplevel(root)
    edit_page.title("Edit Songs")

    listbox_titles = tk.Listbox(edit_page, selectmode=tk.EXTENDED, height=10)
    for song in all_songs:
        listbox_titles.insert(tk.END, song.title)
    listbox_titles.grid(row=0, column=0, padx=10, pady=10)

    def load_song_details():
        selected_indices = listbox_titles.curselection()
        if selected_indices:
            selected_song = all_songs[selected_indices[0]]
            title_entry.delete(0, tk.END)
            title_entry.insert(0, selected_song.title)
            singer_entry.delete(0, tk.END)
            singer_entry.insert(0, selected_song.singer)
            genre_entry.delete(0, tk.END)
            genre_entry.insert(0, selected_song.genre)
            duration_entry.delete(0, tk.END)
            duration_entry.insert(0, selected_song.duration)

    def save_changes():
        selected_indices = listbox_titles.curselection()
        if selected_indices:
            new_title = title_entry.get()
            new_singer = singer_entry.get()
            new_genre = genre_entry.get()
            new_duration = duration_entry.get()

            for index in selected_indices:
                selected_song = all_songs[index]
                selected_song.title = new_title
                selected_song.singer = new_singer
                selected_song.genre = new_genre
                selected_song.duration = new_duration

            # Save the updated song list to the file
            with open('all_songs.txt', 'w') as f:
                for song in all_songs:
                    f.write(','.join([song.title, song.singer, song.genre, song.duration]) + '\n')

            messagebox.showinfo("Edit Song", f"Updated {len(selected_indices)} song(s)")
            edit_page.destroy()
            root.deiconify()

    title_label = tk.Label(edit_page, text="Title:")
    title_label.grid(row=1, column=0, padx=10, pady=5)
    title_entry = tk.Entry(edit_page)
    title_entry.grid(row=1, column=1, padx=10, pady=5)

    singer_label = tk.Label(edit_page, text="Singer:")
    singer_label.grid(row=2, column=0, padx=10, pady=5)
    singer_entry = tk.Entry(edit_page)
    singer_entry.grid(row=2, column=1, padx=10, pady=5)

    genre_label = tk.Label(edit_page, text="Genre:")
    genre_label.grid(row=3, column=0, padx=10, pady=5)
    genre_entry = tk.Entry(edit_page)
    genre_entry.grid(row=3, column=1, padx=10, pady=5)

    duration_label = tk.Label(edit_page, text="Duration:")
    duration_label.grid(row=4, column=0, padx=10, pady=5)
    duration_entry = tk.Entry(edit_page)
    duration_entry.grid(row=4, column=1, padx=10, pady=5)

    load_button = tk.Button(edit_page, text="Load Details", command=load_song_details)
    load_button.grid(row=5, column=0, padx=10, pady=10)

    save_button = tk.Button(edit_page, text="Save Changes", command=save_changes)
    save_button.grid(row=5, column=1, padx=10, pady=10)

    back_button = tk.Button(edit_page, text="Back", command=lambda: [edit_page.destroy(), root.deiconify()])
    back_button.grid(row=6, column=0, columnspan=2, pady=10)








def add_song():
    # Create a new window for adding a song
    root.withdraw()
    add_song_page = tk.Toplevel(root)
    add_song_page.title("Add Song")

    # Define labels and entry fields for song details
    tk.Label(add_song_page, text="Song Title:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    title_entry = tk.Entry(add_song_page)
    title_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(add_song_page, text="Singer:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    singer_entry = tk.Entry(add_song_page)
    singer_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(add_song_page, text="Genre:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    genre_entry = tk.Entry(add_song_page)
    genre_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(add_song_page, text="Duration:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    duration_entry = tk.Entry(add_song_page)
    duration_entry.grid(row=3, column=1, padx=10, pady=5)

    def save_song():
        title = title_entry.get().strip()
        singer = singer_entry.get().strip()
        genre = genre_entry.get().strip()
        duration = duration_entry.get().strip()

        # Validate inputs
        if not title or not singer or not genre or not duration:
            messagebox.showwarning("Input Error", "All fields must be filled out.")
            return

        # Create a new Song object
        new_song = Song(title, singer, genre, duration)

        # Check if the song already exists
        if any(song.title == new_song.title and
               song.singer == new_song.singer and
               song.genre == new_song.genre and
               song.duration == new_song.duration
               for song in all_songs):
            messagebox.showinfo("Add Song", f"{new_song.title} already exists in the song list.")
        else:
            # Add the song to the list and update the file
            all_songs.append(new_song)
            with open('all_songs.txt', 'a') as f:
                f.write(','.join([new_song.title, new_song.singer, new_song.genre, new_song.duration]) + '\n')
            messagebox.showinfo("Add Song", f"Added {new_song.title} to the song list.")
            add_song_page.destroy()
            root.deiconify()  # Show the main window again

    # Save button
    save_button = tk.Button(add_song_page, text="Save", command=save_song)
    save_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Back button
    back_button = tk.Button(add_song_page, text="Back", command=lambda: [add_song_page.destroy(), root.deiconify()])
    back_button.grid(row=5, column=0, columnspan=2, pady=10)






def back_to_main(window):
    window.destroy()
    root.deiconify()

def main_page():
    global root
    root = tk.Tk()
    root.geometry('300x200')
    root.title('Music Player')

    display_button = ttk.Button(root, text='Display', command=display_songs, width=20)
    display_button.grid(row=0, column=0, padx=10, pady=10)

    add_button = ttk.Button(root, text='Add to Favourite', command=add_to_favorites, width=20)
    add_button.grid(row=0, column=1, padx=10, pady=10)

    search_button = ttk.Button(root, text='Search Song', command=search_songs, width=20)
    search_button.grid(row=1, column=0, padx=10, pady=10)

    delete_button = ttk.Button(root, text='Delete Song', command=delete_songs, width=20)
    delete_button.grid(row=1, column=1, padx=10, pady=10)

    edit_button = ttk.Button(root, text='Edit', command=edit_songs, width=20)
    edit_button.grid(row=2, column=0, padx=10, pady=10)

    update_button = ttk.Button(root, text='Add New Song', command=add_song, width=20)
    update_button.grid(row=2, column=1,  padx=10, pady=10)


    exit_button = ttk.Button(root, text='Exit', command=confirm, width=20)
    exit_button.grid(row=3, column=0, columnspan=2, pady=10)


# main_page()

    root.mainloop()

if __name__ == "__main__":
    window = tk.Tk()
    login_page = LoginPage(window)
    window.mainloop()