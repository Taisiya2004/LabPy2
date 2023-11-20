import os
import tkinter as tk
from tkinter import filedialog, messagebox

def search_file(directory, filename):
    results = []
    for root, dirs, files in os.walk(directory):
        if filename in files:
            file_path = os.path.join(root, filename)
            results.append(file_path)
    return results

def browse_button():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

def search_button():
    directory = directory_entry.get()
    filename = filename_entry.get()
    if not directory or not filename:
        messagebox.showerror("Ошибка", "Введите путь к каталогу и имя файла")
        return
    results = search_file(directory, filename)
    if results:
        messagebox.showinfo("Результаты поиска", "\n".join(results))
    else:
        messagebox.showinfo("Результаты поиска", "Файл не найден")

# Создание графического интерфейса
window = tk.Tk()
window.title("Поиск файла")
window.geometry("400x200")

# Поле для ввода пути к каталогу
directory_label = tk.Label(window, text="Каталог:")
directory_label.pack()
directory_entry = tk.Entry(window)
directory_entry.pack()

# Кнопка выбора каталога
browse_button = tk.Button(window, text="Выбрать каталог", command=browse_button)
browse_button.pack()

# Поле для ввода имени файла
filename_label = tk.Label(window, text="Имя файла:")
filename_label.pack()
filename_entry = tk.Entry(window)
filename_entry.pack()

# Кнопка поиска файла
search_button = tk.Button(window, text="Поиск", command=search_button)
search_button.pack()

window.mainloop()
