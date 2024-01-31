import tkinter as tk
import os

class ScriptLauncherApp:
    def __init__(self, master):
        self.master = master
        master.title("Script Launcher")

        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        self.create_buttons()

    def create_buttons(self):
        # Add buttons for each script
        scripts = ["modules.py", "object-detect.py", "pose-tracking.py"]  # Put your script filenames here
        for script in scripts:
            button = tk.Button(self.button_frame, text=script, command=lambda s=script: self.launch_script(s))
            button.pack()

    def launch_script(self, script):
        # Launch the selected script
        os.system("python " + script)

def main():
    root = tk.Tk()
    app = ScriptLauncherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


