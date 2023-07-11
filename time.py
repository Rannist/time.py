import time
import tkinter as tk
from tkinter import messagebox

# 创建一个窗口
window = tk.Tk()
window.title("专注时钟")
window.geometry("300x250")

# 设置默认时间和循环次数
default_work_minutes = 25
default_break_minutes = 5
default_cycles = 4
total_seconds = default_work_minutes * 60
cycles_completed = 0

# 创建显示时间的标签
timer_label = tk.Label(window, text="25:00", font=("Helvetica", 48))
timer_label.pack(pady=20)

# 计时函数
def countdown():
    global total_seconds, cycles_completed

    # 更新时间显示
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

    # 专注时间结束
    if total_seconds == 0:
        window.bell()  # 播放提示音
        window.focus_set()  # 获取焦点，确保提示框置顶
        cycles_completed += 1

        # 检查是否所有循环已完成
        if cycles_completed == default_cycles:
            tk.messagebox.showinfo("专注时间结束", "恭喜，所有循环已完成！")
            window.destroy()
            return

        # 休息时间
        tk.messagebox.showinfo("专注时间结束", "休息一下吧！")
        total_seconds = default_break_minutes * 60
    else:
        # 倒计时减一秒
        total_seconds -= 1

    window.after(1000, countdown)  # 一秒后继续倒计时

# 启动倒计时
def start_timer():
    global total_seconds, cycles_completed
    total_seconds = default_work_minutes * 60
    cycles_completed = 0
    countdown()

# 创建设置选项
def open_settings():
    settings_window = tk.Toplevel(window)
    settings_window.title("设置")
    settings_window.geometry("300x200")

    # 专注时间输入框
    work_label = tk.Label(settings_window, text="专注时间（分钟）:")
    work_label.pack(pady=10)
    work_entry = tk.Entry(settings_window)
    work_entry.insert(tk.END, str(default_work_minutes))
    work_entry.pack()

    # 休息时间输入框
    break_label = tk.Label(settings_window, text="休息时间（分钟）:")
    break_label.pack(pady=10)
    break_entry = tk.Entry(settings_window)
    break_entry.insert(tk.END, str(default_break_minutes))
    break_entry.pack()

    # 循环次数输入框
    cycles_label = tk.Label(settings_window, text="循环次数:")
    cycles_label.pack(pady=10)
    cycles_entry = tk.Entry(settings_window)
    cycles_entry.insert(tk.END, str(default_cycles))
    cycles_entry.pack()

    # 保存设置
    def save_settings():
        nonlocal default_work_minutes, default_break_minutes, default_cycles
        default_work_minutes = int(work_entry.get())
        default_break_minutes = int(break_entry.get())
        default_cycles = int(cycles_entry.get())
        settings_window.destroy()

    save_button = tk.Button(settings_window, text="保存", command=save_settings)
    save_button.pack(pady=10)

# 创建开始按钮和设置按钮
start_button = tk.Button(window, text="开始", command=start_timer)
start_button.pack(pady=10)

settings_button = tk.Button(window, text="设置", command=open_settings)
settings_button.pack(pady=10)

# 运行窗口主循环
window.mainloop()
