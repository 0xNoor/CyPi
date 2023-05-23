import tkinter as tk
from tkinter import ttk

class SpeedometerApp(tk.Tk):
    def __init__(self, file_path):
        super().__init__()

        self.title("Speedometer")
        self.geometry("400x150")

        self.progress_bar = ttk.Progressbar(
            self, orient="horizontal", length=300, mode="determinate"
        )
        self.progress_bar.pack(pady=20)

        self.file_path = file_path
        self.update_progress()

    def update_progress(self):
        try:
            with open(self.file_path, "r") as file:
                speed = int(file.read())
                if speed > 220:
                    speed = 220  # Limit the maximum speed to 220

                self.progress_bar["value"] = speed

        except FileNotFoundError:
            print("File not found.")

        self.after(1000, self.update_progress)  # Update the progress every 1 second

if __name__ == "__main__":
    app = SpeedometerApp("speed_data.txt")
    app.mainloop()
