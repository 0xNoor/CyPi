import tkinter as tk

class SpeedometerApp(tk.Tk):
    def __init__(self, file_path):
        super().__init__()

        self.title("Speedometer")
        self.geometry("400x400")

        self.speed_label = tk.Label(self, text="0", font=("Arial", 36))
        self.speed_label.pack(pady=50)

        self.file_path = file_path
        self.read_speed()

    def read_speed(self):
        try:
            with open(self.file_path, "r") as file:
                speed = int(file.read())
                if speed > 210:
                    speed = 210  # Limit the maximum speed to 210

                self.speed_label.config(text=str(speed))

        except FileNotFoundError:
            print("File not found.")

        self.after(1000, self.read_speed)  # Read the speed every 1 second

if __name__ == "__main__":
    app = SpeedometerApp("speed_data.txt")
    app.mainloop()
