import tkinter as tk
from tkinter import ttk
import random
import threading
import time

chaos_active = True


def random_text_line(length=100):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;':,./<>?"
    return ''.join(random.choice(chars) for _ in range(length))


def matrix_effect(canvas, width, height):
    font_size = random.randint(10, 20)
    columns = width // font_size
    column_positions = [random.randint(0, height) for _ in range(columns)]

    while chaos_active:
        canvas.delete("all")
        for col in range(columns):
            char = random.choice("01")
            color = random.choice(["#0F0", "#0A0", "#FFF", "#FF0"])
            x = col * font_size
            y = column_positions[col] * font_size
            canvas.create_text(x, y, text=char, fill=color, font=("Courier", font_size), anchor="nw")
            column_positions[col] = (column_positions[col] + 1) % (height // font_size)
        canvas.update()
        time.sleep(random.uniform(0.01, 0.03))


def fake_hacking_output(text_widget):
    commands = [
        "ls -la",
        "ping -c 100 8.8.8.8",
        "cat /etc/passwd",
        "nc -vz target.com 80",
        "echo 'Zugriff auf Zielsystem...'",
        "scp file.txt user@192.168.1.100:/tmp",
        "ssh root@192.168.1.1",
        "rm -rf / --no-preserve-root",
        "wget http://malware.download/hack.zip",
        "dd if=/dev/zero of=/dev/null"
    ]

    while chaos_active:
        cmd = random.choice(commands)
        output = f"$ {cmd}\n" + random_text_line(random.randint(50, 100))
        text_widget.insert(tk.END, output + "\n\n")
        text_widget.see(tk.END)
        if random.random() > 0.8:
            text_widget.config(fg=random.choice(["green", "red", "yellow", "blue", "cyan"]))
        time.sleep(random.uniform(0.01, 0.03))


def infinite_error_windows():
    while chaos_active:
        threading.Thread(target=show_error_window, daemon=True).start()
        time.sleep(random.uniform(0.05, 0.1))  


def show_error_window():
    root = tk.Tk()
    root.title("Critical Error")
    x = random.randint(0, 1200)
    y = random.randint(0, 700)
    width = random.randint(200, 500)
    height = random.randint(100, 300)
    root.geometry(f"{width}x{height}+{x}+{y}")

    label = tk.Label(root, text="System Integrity Compromised!", fg="red", font=("Arial", random.randint(14, 20)))
    label.pack(pady=20)

    def move_window():
        while chaos_active:
            try:
                root.geometry(f"{width}x{height}+{random.randint(0, 1200)}+{random.randint(0, 700)}")
                root.update()
                time.sleep(random.uniform(0.1, 0.2))
            except tk.TclError:
                break

    def blink_window():
        colors = ["red", "green", "blue", "yellow", "white", "purple"]
        while chaos_active:
            label.config(fg=random.choice(colors))
            root.update()
            time.sleep(0.1)

    threading.Thread(target=move_window, daemon=True).start()
    threading.Thread(target=blink_window, daemon=True).start()

    tk.Button(root, text="Dismiss", command=lambda: spawn_more_windows(root)).pack()
    root.protocol("WM_DELETE_WINDOW", lambda: spawn_more_windows(root))
    root.mainloop()


def spawn_more_windows(root):
    root.destroy()
    for _ in range(random.randint(4, 7)):  
        threading.Thread(target=show_error_window, daemon=True).start()


def fullscreen_hacking_window():
    root = tk.Tk()
    root.title("Hacking in Progress...")
    root.attributes("-fullscreen", True)
    root.configure(bg="black")

    canvas = tk.Canvas(root, bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    text_widget = tk.Text(root, bg="black", fg="green", font=("Courier", 12), insertbackground="green")
    text_widget.place(relx=0.5, rely=0.5, anchor="center", width=800, height=400)

    threading.Thread(target=matrix_effect, args=(canvas, width, height), daemon=True).start()
    threading.Thread(target=fake_hacking_output, args=(text_widget,), daemon=True).start()

    root.bind("<Escape>", lambda e: print("Escape deaktiviert!"))
    root.mainloop()


def fake_terminal_interaction():
    commands = [
        "ls -la", "ping -c 3 8.8.8.8", "cat /etc/passwd",
        "whoami", "ps aux", "ifconfig", "nmap -sP 192.168.0.0/24"
    ]
    while chaos_active:
        cmd = random.choice(commands)
        print(f"\033[1;32m$ {cmd}\033[0m")
        print(f"\033[1;36m{random_text_line(80)}\033[0m\n")
        time.sleep(0.02)


def main():
    global chaos_active

    threads = [
        threading.Thread(target=fullscreen_hacking_window, daemon=True),
        threading.Thread(target=infinite_error_windows, daemon=True),
        threading.Thread(target=fake_terminal_interaction, daemon=True),
        threading.Thread(target=infinite_error_windows, daemon=True),
        threading.Thread(target=infinite_error_windows, daemon=True)  
    ]

    for thread in threads:
        thread.start()

    try:
        while chaos_active:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation beendet.")
        chaos_active = False


if __name__ == "__main__":
    main()
