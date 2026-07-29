import tkinter as tk
import keyboard
import time
import threading

class DotaSpammerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automaton Attack abuse")
        self.root.geometry("350x150")
        self.root.attributes('-topmost', True)

        self.letters = "abcdefghijklmnopqrstuvwxyz"
        self.is_running = False
        self.current_index = 0

        self.status_label = tk.Label(root, text="Статус/Status: Выключен/Off", fg="red", font=("Arial", 16, "bold"))
        self.status_label.pack(pady=15)

        self.info_label = tk.Label(root, text="Горячие клавиши/Hot Key:\n[ 1 ] - Старт/Start\n[ 2 ] - Стоп/Stop", font=("Arial", 12))
        self.info_label.pack(pady=5)

        keyboard.on_release_key('1', self.start_script)
        keyboard.on_release_key('2', self.stop_script)

        self.spam_thread = threading.Thread(target=self.spam_loop, daemon=True)
        self.spam_thread.start()

    def start_script(self, event=None):
        if not self.is_running:
            for mod in ['ctrl', 'shift', 'alt', 'windows']:
                keyboard.release(mod)
            
            self.is_running = True
            self.root.after(0, lambda: self.status_label.config(text="Статус/Status: Работает/On", fg="green"))

    def stop_script(self, event=None):
        if self.is_running:
            self.is_running = False
            self.root.after(0, lambda: self.status_label.config(text="Статус/Status: Выключен/Off", fg="red"))

    def spam_loop(self):
        while True:
            if self.is_running:
                keyboard.write(self.letters[self.current_index])
                self.current_index = (self.current_index + 1) % len(self.letters)
                
                time.sleep(0.0001)
            else:
                time.sleep(0.1)

if __name__ == "__main__":
    root = tk.Tk()
    app = DotaSpammerApp(root)
    root.mainloop()