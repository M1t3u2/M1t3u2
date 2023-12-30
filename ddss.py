import tkinter as tk
from tkinter import ttk
import time

class LoadingWindow:
    def __init__(self, root, callback):
        self.root = root
        self.root.title("Loading")

        self.canvas = tk.Canvas(root, width=1800, height=1080, bg="black")
        self.canvas.pack()

        self.progress_label = ttk.Label(root, text="Chargement en cours...", font=("Helvetica", 16), foreground="white", background="black")
        self.progress_label.place(relx=0.5, rely=0.4, anchor="center")

        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
        self.progress_bar.place(relx=0.5, rely=0.6, anchor="center")

        self.callback = callback

    def start(self):
        self.progress_bar.start()
        self.root.after(5000, self.callback)  # Simuler une tâche de chargement de 5 secondes
        self.root.mainloop()

    def stop(self):
        self.progress_bar.stop()
        self.root.destroy()

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Netflix")

        self.canvas = tk.Canvas(root, width=1800, height=1080, bg="black")
        self.canvas.pack()

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Netflix")

        self.canvas = tk.Canvas(root, width=1800, height=1080, bg="black")
        self.canvas.pack()

        # Charger le logo Netflix
        image_path = "/home/onlymitsu/M1t3u/logo_netflix.png" # Remplacez par le chemin de votre image
        netflix_logo = tk.PhotoImage(file=image_path)

        # Afficher le logo dans un label
        self.logo_label = ttk.Label(root, image=netflix_logo)
        self.logo_label.place(relx=0.5, rely=0.5, anchor="center")


if __name__ == "__main__":
    root_loading = tk.Tk()
    root_loading.geometry("1800x1080")
    
    def on_loading_complete():
        root_loading.destroy()

        root_home = tk.Tk()
        root_home.geometry("1800x1080")
        app_home = HomePage(root_home)
        root_home.mainloop()

    app_loading = LoadingWindow(root_loading, on_loading_complete)
    app_loading.start()
