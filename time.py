import time
import tkinter as tk
from tkinter import messagebox
from pydub import AudioSegment
from pygame import mixer

# 创建一个窗口
window = tk.Tk()
window.title("专注时钟")
window.geometry("300x250")

# 设置默认时间（以分钟为单位）
default_minutes = 25
total_seconds = default_minutes * 60

# 设置默认番茄工作法周期
default_cycles = 4
completed_cycles = 0

# 创建显示时间的标签
timer_label = tk.Label(window, text="25:00", font=("Helvetica", 48))
timer_label.pack(pady=20)

# 创建目标输入框
target_entry = tk.Entry(window, width=30)
target_entry.pack(pady=10)
target_entry.insert(tk.END, "设定你的目标...")

# 创建背景音乐
mixer.init()
background_music = AudioSegment.from_file("background_music.mp3", format="mp3")

# 播放背景音乐
def play_background_music():
    mixer.music.load("background_music.mp3")
    mixer.music.play(-1)

# 停止背景音乐
def stop_background_music():
    mixer.music.stop()

# 计时函数
def countdown():
    global total_seconds, completed_cycles

    # 更新时间显示
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

    # 番茄时间结束
    if total_seconds == 0:
        window.bell()  # 播放提示音
        window.focus_set()  # 获取焦点，确保提示框置顶
        completed_cycles += 1

        # 检查是否所有番茄周期已完成
        if completed_cycles == default_cycles:
            tk.messagebox.showinfo("专注时间结束", "恭喜，所有番茄周期已完成！")
            window.destroy()
            return

        # 休息时间
        tk.messagebox.showinfo("专注时间结束", "休息一下吧！")
        total_seconds = 5 * 60  # 默认5分钟的休息时间
        play_background_music()
    else:
        # 倒计时减一秒
        total_seconds -= 1

    window.after(1000, countdown)  # 一秒后继续倒计时

# 启动倒计时
def start_timer():
    global total_seconds, completed_cycles
    total_seconds = default_minutes * 60
    completed_cycles = 0
    stop_background_music()
    countdown()

# 创建开始按钮
start_button = tk.Button(window, text="开始", command=start_timer)
start_button.pack(pady=10)

# 创建设置按钮
def open_settings():
    settings_window = tk.Toplevel(window)
    settings_window.title("设置")
    settings_window.geometry("300x200")

    # 番茄工作法周期设置
    cycles_label = tk.Label(settings_window, text="番茄工作法周期:")
    cycles_label.pack(pady=10)
    cycles_entry = tk.Entry(settings_window)
    cycles_entry.insert(tk.END, str(default_cycles))
    cycles_entry.pack()

    # 保存设置
    def save_settings():
        nonlocal default_cycles
        default_cycles = int(cycles_entry.get())
        settings_window.destroy()

    save_button = tk.Button(settings_window, text="保存", command=save_settings)
    save_button.pack(pady=10)

settings_button = tk.Button(window, text="设置", command=open_settings)
settings_button.pack(pady=10)

# 创建专注统计
def show_statistics():
    statistics_window = tk.Toplevel(window)
    statistics_window.title("专注统计")
    statistics_window.geometry("200x150")

    # 统计信息
    completed_minutes = (default_minutes * completed_cycles) + ((default_cycles - completed_cycles) * 5)
    completed_tasks = completed_cycles

    # 显示统计信息
    stats_label = tk.Label(statistics_window, text=f"总专注时间：{completed_minutes} 分钟\n已完成任务数：{completed_tasks}")
    stats_label.pack(pady=20)

statistics_button = tk.Button(window, text="专注统计", command=show_statistics)
statistics_button.pack(pady=10)

# 运行窗口主循环
window.mainloop()
