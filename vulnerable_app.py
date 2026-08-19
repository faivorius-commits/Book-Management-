import tkinter as tk
from tkinter import messagebox


# =========================
# COLORS
# =========================

BG = "#F7F3EE"
SIDEBAR = "#3E3A36"
CARD = "#FFFFFF"
TEXT = "#302D2A"
MUTED = "#8A837D"
ACCENT = "#8B6F5A"
AVAILABLE = "#6B8E6B"
BORROWED = "#B56B6B"


# =========================
# BOOK DATA
# =========================

books = [
    {
        "title": "The Tale of Genji",
        "status": "Available"
    },
    {
        "title": "The Book of Five Rings",
        "status": "Available"
    },
    {
        "title": "Introduction to Classical Chinese Philosophy",
        "status": "Available"
    }
]


# =========================
# APPLICATION
# =========================

class LibraryApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Library Management System")
        self.root.geometry("1000x650")
        self.root.minsize(850, 550)

        self.current_user = None
        self.role = None

        self.show_login()


    # =========================
    # CLEAR SCREEN
    # =========================

    def clear_screen(self):

        for widget in self.root.winfo_children():
            widget.destroy()


    # =========================
    # LOGIN PAGE
    # =========================

    def show_login(self):

        self.clear_screen()

        self.root.configure(bg=BG)

        container = tk.Frame(
            self.root,
            bg=BG
        )

        container.pack(
            expand=True
        )


        tk.Label(
            container,
            text="📚",
            font=("Arial", 50),
            bg=BG
        ).pack(pady=(0, 10))


        tk.Label(
            container,
            text="Library Management",
            font=("Arial", 26, "bold"),
            fg=TEXT,
            bg=BG
        ).pack()


        tk.Label(
            container,
            text="Welcome back",
            font=("Arial", 12),
            fg=MUTED,
            bg=BG
        ).pack(
            pady=(5, 30)
        )


        tk.Label(
            container,
            text="Username",
            font=("Arial", 10, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            anchor="w"
        )


        self.username_entry = tk.Entry(
            container,
            width=35,
            font=("Arial", 12),
            relief="solid",
            bd=1
        )

        self.username_entry.pack(
            ipady=8,
            pady=(5, 15)
        )


        tk.Label(
            container,
            text="Password",
            font=("Arial", 10, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            anchor="w"
        )


        self.password_entry = tk.Entry(
            container,
            width=35,
            font=("Arial", 12),
            show="*",
            relief="solid",
            bd=1
        )

        self.password_entry.pack(
            ipady=8,
            pady=(5, 20)
        )


        tk.Button(
            container,
            text="Login",
            width=30,
            bg=ACCENT,
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.login
        ).pack(
            ipady=8
        )


    # =========================
    # LOGIN
    # =========================

    def login(self):

        username = self.username_entry.get()
        password = self.password_entry.get()

        # Intentionally hardcoded for security review
        if username == "admin" and password == "admin123":

            self.current_user = username
            self.role = "admin"

            self.show_dashboard()

        elif username == "user" and password == "user123":

            self.current_user = username
            self.role = "user"

            self.show_dashboard()

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid username or password."
            )


    # =========================
    # SIDEBAR
    # =========================

    def create_sidebar(self):

        sidebar = tk.Frame(
            self.root,
            bg=SIDEBAR,
            width=220
        )

        sidebar.pack(
            side="left",
            fill="y"
        )

        sidebar.pack_propagate(False)


        tk.Label(
            sidebar,
            text="📚 Library",
            font=("Arial", 20, "bold"),
            fg="white",
            bg=SIDEBAR
        ).pack(
            pady=(35, 40)
        )


        self.sidebar_button(
            sidebar,
            "🏠  Dashboard",
            self.show_dashboard
        )


        self.sidebar_button(
            sidebar,
            "📖  Books",
            self.show_books
        )


        if self.role == "admin":

            self.sidebar_button(
                sidebar,
                "➕  Add Book",
                self.add_book
            )

            self.sidebar_button(
                sidebar,
                "🗑  Remove Book",
                self.remove_book
            )


        self.sidebar_button(
            sidebar,
            "🚪  Logout",
            self.show_login
        )


    # =========================
    # SIDEBAR BUTTON
    # =========================

    def sidebar_button(
        self,
        parent,
        text,
        command
    ):

        tk.Button(
            parent,
            text=text,
            anchor="w",
            padx=25,
            bg=SIDEBAR,
            fg="white",
            activebackground=ACCENT,
            activeforeground="white",
            relief="flat",
            font=("Arial", 11),
            cursor="hand2",
            command=command
        ).pack(
            fill="x",
            ipady=12
        )


    # =========================
    # DASHBOARD
    # =========================

    def show_dashboard(self):

        self.clear_screen()

        self.root.configure(bg=BG)

        self.create_sidebar()


        main = tk.Frame(
            self.root,
            bg=BG
        )

        main.pack(
            side="left",
            fill="both",
            expand=True
        )


        tk.Label(
            main,
            text=f"Welcome, {self.current_user} 👋",
            font=("Arial", 26, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            anchor="w",
            padx=40,
            pady=(35, 5)
        )


        tk.Label(
            main,
            text="Here's your library overview.",
            font=("Arial", 11),
            fg=MUTED,
            bg=BG
        ).pack(
            anchor="w",
            padx=40
        )


        # Statistics

        stats = tk.Frame(
            main,
            bg=BG
        )

        stats.pack(
            fill="x",
            padx=40,
            pady=30
        )


        total = len(books)

        available = sum(
            1
            for book in books
            if book["status"] == "Available"
        )

        borrowed = sum(
            1
            for book in books
            if book["status"] == "Borrowed"
        )


        self.stat_card(
            stats,
            "Total Books",
            total
        )


        self.stat_card(
            stats,
            "Available",
            available
        )


        self.stat_card(
            stats,
            "Borrowed",
            borrowed
        )


        tk.Label(
            main,
            text="Books",
            font=("Arial", 18, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            anchor="w",
            padx=40
        )


        self.show_book_cards(
            main,
            books
        )


    # =========================
    # STAT CARD
    # =========================

    def stat_card(
        self,
        parent,
        title,
        value
    ):

        card = tk.Frame(
            parent,
            bg=CARD,
            width=180,
            height=100
        )

        card.pack(
            side="left",
            padx=(0, 15)
        )

        card.pack_propagate(False)


        tk.Label(
            card,
            text=title,
            font=("Arial", 10),
            fg=MUTED,
            bg=CARD
        ).pack(
            anchor="w",
            padx=15,
            pady=(15, 0)
        )


        tk.Label(
            card,
            text=str(value),
            font=("Arial", 24, "bold"),
            fg=TEXT,
            bg=CARD
        ).pack(
            anchor="w",
            padx=15
        )


    # =========================
    # BOOK CARDS
    # =========================

    def show_book_cards(
        self,
        parent,
        book_list
    ):

        container = tk.Frame(
            parent,
            bg=BG
        )

        container.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=20
        )


        for book in book_list:

            card = tk.Frame(
                container,
                bg=CARD,
                width=250,
                height=150
            )

            card.pack(
                side="left",
                padx=(0, 15),
                pady=5
            )

            card.pack_propagate(False)


            tk.Label(
                card,
                text="📖",
                font=("Arial", 25),
                bg=CARD
            ).pack(
                pady=(10, 0)
            )


            tk.Label(
                card,
                text=book["title"],
                font=("Arial", 11, "bold"),
                fg=TEXT,
                bg=CARD,
                wraplength=220
            ).pack(
                pady=5
            )


            status_color = (
                AVAILABLE
                if book["status"] == "Available"
                else BORROWED
            )


            tk.Label(
                card,
                text=book["status"],
                font=("Arial", 10, "bold"),
                fg=status_color,
                bg=CARD
            ).pack()


            if self.role == "user":

                if book["status"] == "Available":

                    tk.Button(
                        card,
                        text="Borrow",
                        bg=ACCENT,
                        fg="white",
                        relief="flat",
                        cursor="hand2",
                        command=lambda b=book:
                        self.borrow_book(b)
                    ).pack(
                        pady=5
                    )

                else:

                    tk.Button(
                        card,
                        text="Return",
                        bg=BORROWED,
                        fg="white",
                        relief="flat",
                        cursor="hand2",
                        command=lambda b=book:
                        self.return_book(b)
                    ).pack(
                        pady=5
                    )


    # =========================
    # BOOKS PAGE
    # =========================

    def show_books(self):

        self.clear_screen()

        self.root.configure(bg=BG)

        self.create_sidebar()


        main = tk.Frame(
            self.root,
            bg=BG
        )

        main.pack(
            side="left",
            fill="both",
            expand=True
        )


        tk.Label(
            main,
            text="Books",
            font=("Arial", 26, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            anchor="w",
            padx=40,
            pady=(35, 5)
        )


        # Search bar

        search_frame = tk.Frame(
            main,
            bg=BG
        )

        search_frame.pack(
            fill="x",
            padx=40,
            pady=20
        )


        search_entry = tk.Entry(
            search_frame,
            font=("Arial", 12),
            relief="solid",
            bd=1
        )

        search_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=8
        )


        def search():

            keyword = search_entry.get().lower()

            results = [
                book
                for book in books
                if keyword in book["title"].lower()
            ]

            for widget in cards.winfo_children():
                widget.destroy()

            self.show_book_cards(
                cards,
                results
            )


        tk.Button(
            search_frame,
            text="Search 🔎",
            bg=ACCENT,
            fg="white",
            relief="flat",
            cursor="hand2",
            command=search
        ).pack(
            side="left",
            padx=10,
            ipady=6
        )


        cards = tk.Frame(
            main,
            bg=BG
        )

        cards.pack(
            fill="both",
            expand=True
        )


        self.show_book_cards(
            cards,
            books
        )


    # =========================
    # BORROW
    # =========================

    def borrow_book(self, book):

        if book["status"] == "Available":

            book["status"] = "Borrowed"

            messagebox.showinfo(
                "Success",
                f"You borrowed:\n{book['title']}"
            )

            self.show_books()


    # =========================
    # RETURN
    # =========================

    def return_book(self, book):

        if book["status"] == "Borrowed":

            book["status"] = "Available"

            messagebox.showinfo(
                "Success",
                f"You returned:\n{book['title']}"
            )

            self.show_books()


    # =========================
    # ADD BOOK
    # =========================

    def add_book(self):

        window = tk.Toplevel(
            self.root
        )

        window.title("Add Book")
        window.geometry("450x220")
        window.configure(bg=BG)


        tk.Label(
            window,
            text="Add New Book",
            font=("Arial", 18, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            pady=20
        )


        entry = tk.Entry(
            window,
            width=40,
            font=("Arial", 11)
        )

        entry.pack(
            ipady=8
        )


        def save():

            title = entry.get().strip()

            if title == "":

                messagebox.showerror(
                    "Error",
                    "Book title cannot be empty."
                )

                return


            books.append({
                "title": title,
                "status": "Available"
            })


            messagebox.showinfo(
                "Success",
                "Book added successfully."
            )


            window.destroy()

            self.show_dashboard()


        tk.Button(
            window,
            text="Add Book",
            bg=ACCENT,
            fg="white",
            relief="flat",
            command=save
        ).pack(
            pady=20,
            ipadx=20,
            ipady=5
        )


    # =========================
    # REMOVE BOOK
    # =========================

    def remove_book(self):

        window = tk.Toplevel(
            self.root
        )

        window.title("Remove Book")
        window.geometry("500x300")
        window.configure(bg=BG)


        tk.Label(
            window,
            text="Remove Book",
            font=("Arial", 18, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            pady=20
        )


        titles = [
            book["title"]
            for book in books
        ]


        selected = tk.StringVar()


        dropdown = tk.OptionMenu(
            window,
            selected,
            *titles
        )

        dropdown.pack(
            pady=10
        )


        def delete():

            title = selected.get()

            if title == "":

                messagebox.showerror(
                    "Error",
                    "Select a book."
                )

                return


            for book in books:

                if book["title"] == title:

                    books.remove(book)

                    break


            messagebox.showinfo(
                "Success",
                "Book removed."
            )


            window.destroy()

            self.show_dashboard()


        tk.Button(
            window,
            text="Remove",
            bg=BORROWED,
            fg="white",
            relief="flat",
            command=delete
        ).pack(
            pady=20,
            ipadx=20,
            ipady=5
        )


# =========================
# START PROGRAM
# =========================

root = tk.Tk()

app = LibraryApp(root)

root.mainloop()
