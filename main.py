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


def open_speedometer():
    app = SpeedometerApp("speed_data.txt")
    app.mainloop()

def function1():
    print("Function 1 executed")

#More functions can be added here


if __name__ == "__main__":
    root = tk.Tk()

    # Create a 3x3 grid
    for i in range(3):
        root.columnconfigure(i, weight=1, minsize=100)
        root.rowconfigure(i, weight=1, minsize=100)

        for j in range(3):
            button = ttk.Button(
                root,
                text=f"Button {i*3+j+1}",
                command=lambda i=i, j=j: button_click(i, j),
            )
            button.grid(row=i, column=j, padx=10, pady=10)

    def button_click(i, j):
        # Define the actions for each button
        if i == 0 and j == 0:
            open_speedometer()
        elif i == 0 and j == 1:
            function1()
        elif i == 0 and j == 2:
            function2()
        elif i == 1 and j == 0:
            function3()
        elif i == 1 and j == 1:
            # Add actions for other buttons here
            pass
        elif i == 1 and j == 2:
            pass
        elif i == 2 and j == 0:
            pass
        elif i == 2 and j == 1:
            pass
        elif i == 2 and j == 2:
            pass

    root.mainloop()
