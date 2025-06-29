# main.py

from ui import build_main_screen
from views import build_view_screen
from charts import build_chart_screen
from accrual import build_accrual_screen

import tkinter as tk

root = tk.Tk()
root.title("Expense Tracker")
root.geometry("450x800")
root.configure(bg="#f0f2f5")

# Screens
screens = {
    'main': tk.Frame(root, bg="#f0f2f5"),
    'view': tk.Frame(root, bg="#f0f2f5"),
    'charts': tk.Frame(root, bg="#f0f2f5"),
    'accrual': tk.Frame(root, bg="#f0f2f5")
}

for screen in screens.values():
    screen.place(relwidth=1, relheight=1)

file_path = "../expense_tracking.xlsx"

# Build all screens
build_main_screen(screens['main'], root, screens, file_path)
build_view_screen(screens['view'], root, screens, file_path)
build_chart_screen(screens['charts'], root, screens, file_path)
build_accrual_screen(screens['accrual'], root, screens, file_path)

# Launch app
screens['main'].tkraise()
root.mainloop()