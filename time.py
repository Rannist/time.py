import time
import tkinter as tk

# 创建一个窗口
window = tk.Tk()
window.title("专注时钟")
window.geometry("300x200")

# 设置默认时间（以分钟为单位）
default_minutes = 25
total_seconds = default_minutes * 60

# 创建显示时间的标签
timer_label = tk.Label(window, text="25:00", font=("Helvetica", 48))
timer_label.pack(pady=20)

# 计时函数
def countdown():
    global total_seconds

    # 更新时间显示
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

    # 倒计时结束，弹出提示框
    if total_seconds == 0:
        window.bell()  # 播放提示音
        window.focus_set()  # 获取焦点，确保提示框置顶
        tk.messagebox.showinfo("专注时间结束", "休息一下吧！")
        return

    # 倒计时减一秒
    total_seconds -= 1
    window.after(1000, countdown)  # 一秒后继续倒计时

# 启动倒计时
def start_timer():
    global total_seconds
    total_seconds = default_minutes * 60
    countdown()

# 创建开始按钮
start_button = tk.Button(window, text="开始", command=start_timer)
start_button.pack(pady=10)

# 运行窗口主循环
window.mainloop()
