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

    start_time_label.grid_forget()
    start_time_entry.grid_forget()
    end_time_label.grid_forget()
    end_time_entry.grid_forget()
    current_time_label.grid_forget()
    current_time_entry.grid_forget()
    auto_button.grid_forget()
    update_button.grid_forget()

    progress_bar.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    progress_label.grid(row=1, column=0, padx=10, sticky='w')

    root.update_idletasks()
    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{int(root.winfo_screenwidth()/2 - root.winfo_width()/2)}+{int(root.winfo_screenheight()/2 - root.winfo_height()/2)}")

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

    progress_bar.grid_forget()
    progress_label.grid_forget()

    start_time_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
    start_time_entry.grid(row=1, column=0, padx=10, pady=5, sticky='w')
    end_time_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
    end_time_entry.grid(row=3, column=0, padx=10, pady=5, sticky='w')
    current_time_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
    current_time_entry.grid(row=5, column=0, padx=10, pady=5, sticky='w')
    auto_button.grid(row=6, column=0, padx=10, pady=10, sticky='w')
    update_button.grid(row=7, column=0, padx=10, sticky='w')

    root.update_idletasks()
    root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{int(root.winfo_screenwidth()/2 - root.winfo_width()/2)}+{int(root.winfo_screenheight()/2 - root.winfo_height()/2)}")


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

style = ttk.Style()
style.configure('TEntry', padding=5)

main_frame = tk.Frame(root)
main_frame.pack(expand=True, padx=10, pady=10)  # 使用pack布局，并设置expand为True

progress_bar = ttk.Progressbar(main_frame, orient='horizontal', mode='determinate')
progress_label = tk.Label(main_frame, text="")

start_time_label = tk.Label(main_frame, text="上班时间（格式为HH:MM）：")
start_time_entry = ttk.Entry(main_frame, style='TEntry')
start_time_entry.bind('<KeyRelease>', auto_fill_minutes)

end_time_label = tk.Label(main_frame, text="下班时间（格式为HH:MM）：")
end_time_entry = ttk.Entry(main_frame, style='TEntry')
end_time_entry.bind('<KeyRelease>', auto_fill_minutes)

current_time_label = tk.Label(main_frame, text="当前时间（格式为HH:MM）：")
current_time_entry = ttk.Entry(main_frame, style='TEntry')

update_button = tk.Button(main_frame, text="开始", command=update_progress)
auto_button = tk.Button(main_frame, text="自动", command=fill_current_time)

start_time_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')
start_time_entry.grid(row=1, column=0, padx=10, pady=5, sticky='w')
end_time_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')
end_time_entry.grid(row=3, column=0, padx=10, pady=5, sticky='w')
current_time_label.grid(row=4, column=0, padx=10, pady=5, sticky='w')
current_time_entry.grid(row=5, column=0, padx=10, pady=5, sticky='w')
auto_button.grid(row=6, column=0, padx=10, pady=10, sticky='w')
update_button.grid(row=7, column=0, padx=10, sticky='w')

root.update_idletasks()

# 获取屏幕尺寸
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 计算窗口在屏幕中央的坐标
window_width = root.winfo_width()
window_height = root.winfo_height()
position_x = int(screen_width / 2 - window_width / 2)
position_y = int(screen_height / 2 - window_height / 2)

# 设置窗口位置
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

root.mainloop()
