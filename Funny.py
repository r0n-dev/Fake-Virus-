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
    while chaos_active:
        x = random.randint(0, width)
        y = random.randint(0, height)
        char = random.choice("01")
        color = random.choice(["#0F0", "#0A0", "#050"])
        canvas.create_text(x, y, text=char, fill=color, font=("Courier", 12))
        canvas.update()
        time.sleep(0.01)

def fake_hacking_output(text_widget):
    while chaos_active:
        line = random_text_line(random.randint(50, 100))
        text_widget.insert(tk.END, line + "\n")
        text_widget.see(tk.END)  
        time.sleep(0.05)

def moving_error_window():
    while chaos_active:
        root = tk.Tk()
        root.title("Critical Error")
        root.geometry("300x150+" + str(random.randint(0, 800)) + "+" + str(random.randint(0, 600)))
        tk.Label(root, text="System Integrity Compromised!", fg="red", font=("Arial", 14)).pack(pady=20)
        tk.Button(root, text="Dismiss", command=root.destroy).pack()
        root.after(5000, root.destroy) 
        root.mainloop()

def dramatic_progress_bar(canvas, progress_var, label_var):
    for i in range(101):
        progress_var.set(i)
        label_var.set(f"Übernahme zu {i}% abgeschlossen...")
        canvas.update_idletasks()
        time.sleep(0.05)

def dramatic_loading_screen():
    root = tk.Tk()
    root.title("System Breach")
    root.geometry("400x200")
    progress_var = tk.IntVar()
    label_var = tk.StringVar(value="Initialisiere Angriff...")
    tk.Label(root, textvariable=label_var, font=("Arial", 16)).pack(pady=20)
    progress_bar = ttk.Progressbar(root, maximum=100, length=300, variable=progress_var)
    progress_bar.pack(pady=20)
    threading.Thread(target=dramatic_progress_bar, args=(root, progress_var, label_var), daemon=True).start()
    root.mainloop()

def fullscreen_hacking_window():
    root = tk.Tk()
    root.title("Hacking in Progress...")
    root.attributes("-fullscreen", True)  
    root.configure(bg="black")

    canvas = tk.Canvas(root, bg="black", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    text_widget = tk.Text(root, bg="black", fg="green", font=("Courier", 10), insertbackground="green")
    text_widget.place(relx=0.5, rely=0.5, anchor="center", width=800, height=400)

    threading.Thread(target=matrix_effect, args=(canvas, width, height), daemon=True).start()
    threading.Thread(target=fake_hacking_output, args=(text_widget,), daemon=True).start()

    root.bind("<Escape>", lambda e: root.destroy())
    root.mainloop()

def fake_terminal_interaction():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    while chaos_active:
        line = ''.join(random.choice(chars) for _ in range(80))
        print(f"\033[1;32m{line}\033[0m")  # Grüner Text
        time.sleep(0.1)

def main():
    """Startet die erweiterte Hacking-Simulation."""
    global chaos_active

    
    dramatic_loading_screen()

    threading.Thread(target=fullscreen_hacking_window, daemon=True).start()

    threading.Thread(target=moving_error_window, daemon=True).start()

    threading.Thread(target=fake_terminal_interaction, daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        chaos_active = False
        print("\nSimulation beendet.")

if __name__ == "__main__":
    main()
