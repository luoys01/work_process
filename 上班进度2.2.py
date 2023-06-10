import datetime
import time
import tkinter as tk
from tkinter import ttk


def update_progress():
    start_time_str = start_time_entry.get()
    end_time_str = end_time_entry.get()
    current_time_str = current_time_entry.get()

    start_time = datetime.datetime.strptime(start_time_str, '%H:%M')
    end_time = datetime.datetime.strptime(end_time_str, '%H:%M')
    current_time = datetime.datetime.strptime(current_time_str, '%H:%M')

    total_seconds = (end_time - start_time).total_seconds()
    elapsed_seconds = (current_time - start_time).total_seconds()
    remaining_seconds = total_seconds - elapsed_seconds

    progress_bar['maximum'] = total_seconds
    progress_bar['value'] = elapsed_seconds

    start_time_label.pack_forget()
    start_time_entry.pack_forget()
    end_time_label.pack_forget()
    end_time_entry.pack_forget()
    current_time_label.pack_forget()
    current_time_entry.pack_forget()
    auto_button.pack_forget()
    update_button.pack_forget()

    progress_bar.pack()
    progress_label.pack()

    while remaining_seconds > 0:
        current_time += datetime.timedelta(seconds=1)
        current_time_str = current_time.strftime('%H:%M')

        elapsed_seconds += 1
        remaining_seconds -= 1

        progress_bar['value'] = elapsed_seconds

        remaining_time_str = str(datetime.timedelta(seconds=int(remaining_seconds)))
        percentage = format((elapsed_seconds / total_seconds) * 100, '.2f')
        progress_text = f'{percentage}% (剩余时间: {remaining_time_str})'
        progress_label['text'] = progress_text

        root.update()  # 更新Tkinter窗口

        time.sleep(1)

    progress_bar.pack_forget()
    progress_label.pack_forget()

    start_time_label.pack()
    start_time_entry.pack()
    end_time_label.pack()
    end_time_entry.pack()
    current_time_label.pack(side=tk.LEFT)
    current_time_entry.pack(side=tk.LEFT)
    auto_button.pack(side=tk.LEFT)
    update_button.pack()


def fill_current_time():
    current_time = datetime.datetime.now().strftime('%H:%M')
    current_time_entry.delete(0, tk.END)
    current_time_entry.insert(tk.END, current_time)


def auto_fill_minutes(event):
    hour_str = start_time_entry.get()
    if hour_str.isdigit():
        hour = int(hour_str)
        if 0 <= hour <= 23 and len(hour_str) == 2:
            start_time_entry.insert(tk.END, ':00')
            start_time_entry.configure(state='normal')

    hour_str = end_time_entry.get()
    if hour_str.isdigit():
        hour = int(hour_str)
        if 0 <= hour <= 23 and len(hour_str) == 2:
            end_time_entry.insert(tk.END, ':00')
            end_time_entry.configure(state='normal')


root = tk.Tk()
root.title("上班进度")
root.geometry("400x150")

style = ttk.Style()
style.configure('TEntry', padding=5)

progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate')
progress_label = tk.Label(root, text="")

start_time_label = tk.Label(root, text="上班时间（格式为HH:MM）：")
start_time_entry = ttk.Entry(root, style='TEntry')
start_time_entry.bind('<KeyRelease>', auto_fill_minutes)

end_time_label = tk.Label(root, text="下班时间（格式为HH:MM）：")
end_time_entry = ttk.Entry(root, style='TEntry')
end_time_entry.bind('<KeyRelease>', auto_fill_minutes)

current_time_label = tk.Label(root, text="当前时间（格式为HH:MM）：")
current_time_entry = ttk.Entry(root, style='TEntry')

update_button = tk.Button(root, text="开始", command=update_progress)
auto_button = tk.Button(root, text="自动", command=fill_current_time)

start_time_label.pack()
start_time_entry.pack()
end_time_label.pack()
end_time_entry.pack()
current_time_label.pack(side=tk.LEFT)
current_time_entry.pack(side=tk.LEFT)
auto_button.pack(side=tk.LEFT)
update_button.pack()

root.mainloop()
