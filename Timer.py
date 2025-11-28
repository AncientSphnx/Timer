import tkinter as tk
from tkinter import ttk, messagebox
import time
from datetime import datetime
from threading import Thread
import os
from playsound import playsound
import math

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("⏱️ Timer Suite")
        self.root.geometry("800x600")
        self.root.configure(bg='#1e1e2e')
        
        # Colors
        self.bg_color = '#1e1e2e'
        self.fg_color = '#cdd6f4'
        self.accent_color = '#89b4fa'
        self.success_color = '#a6e3a1'
        self.warning_color = '#fab387'
        self.danger_color = '#f38ba8'
        
        # Sound paths
        self.sound_dir = os.path.join(os.path.dirname(__file__), 'Sounds')
        self.tick_sound = os.path.join(self.sound_dir, 'click-button-140881.mp3')
        self.alarm_sound = os.path.join(self.sound_dir, 'smartphone_vibrating_alarm_silent-7040.mp3')
        self.complete_sound = os.path.join(self.sound_dir, 'winfantasia-6912.mp3')
        
        # Timer variables
        self.timer_running = False
        self.timer_seconds = 0
        self.timer_thread = None
        
        # Stopwatch variables
        self.stopwatch_running = False
        self.stopwatch_start_time = 0
        self.stopwatch_elapsed = 0
        self.stopwatch_thread = None
        self.lap_times = []
        
        # Alarm variables
        self.alarm_running = False
        self.alarm_thread = None
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(main_frame, text="⏱️ TIMER SUITE", 
                              font=('Arial', 24, 'bold'),
                              bg=self.bg_color, fg=self.accent_color)
        title_label.pack(pady=(0, 20))
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Style for notebook
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background=self.bg_color)
        style.configure('TNotebook.Tab', padding=[20, 10], 
                       background='#313244', foreground=self.fg_color,
                       font=('Arial', 12, 'bold'))
        style.map('TNotebook.Tab', background=[('selected', self.accent_color)],
                 foreground=[('selected', self.bg_color)])
        
        # Create tabs
        self.create_timer_tab()
        self.create_stopwatch_tab()
        self.create_alarm_tab()
        
    def create_timer_tab(self):
        timer_frame = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(timer_frame, text="⏲️ Timer")
        
        # Timer display
        self.timer_display = tk.Label(timer_frame, text="00:00:00",
                                    font=('Digital-7', 72, 'bold'),
                                    bg=self.bg_color, fg=self.accent_color)
        self.timer_display.pack(pady=50)
        
        # Input frame
        input_frame = tk.Frame(timer_frame, bg=self.bg_color)
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Set Timer (HH:MM:SS):",
                font=('Arial', 14), bg=self.bg_color, fg=self.fg_color).grid(row=0, column=0, columnspan=3, pady=10)
        
        self.timer_hours = tk.Spinbox(input_frame, from_=0, to=23, width=5, 
                                     font=('Arial', 16), justify='center')
        self.timer_hours.grid(row=1, column=0, padx=5)
        
        tk.Label(input_frame, text=":", font=('Arial', 16), 
                bg=self.bg_color, fg=self.fg_color).grid(row=1, column=1)
        
        self.timer_minutes = tk.Spinbox(input_frame, from_=0, to=59, width=5,
                                       font=('Arial', 16), justify='center')
        self.timer_minutes.grid(row=1, column=2, padx=5)
        
        tk.Label(input_frame, text=":", font=('Arial', 16),
                bg=self.bg_color, fg=self.fg_color).grid(row=1, column=3)
        
        self.timer_seconds_input = tk.Spinbox(input_frame, from_=0, to=59, width=5,
                                             font=('Arial', 16), justify='center')
        self.timer_seconds_input.grid(row=1, column=4, padx=5)
        
        # Control buttons
        button_frame = tk.Frame(timer_frame, bg=self.bg_color)
        button_frame.pack(pady=30)
        
        self.timer_start_btn = tk.Button(button_frame, text="▶️ START",
                                        font=('Arial', 14, 'bold'),
                                        bg=self.success_color, fg=self.bg_color,
                                        width=12, height=2,
                                        command=self.start_timer)
        self.timer_start_btn.grid(row=0, column=0, padx=10)
        
        self.timer_pause_btn = tk.Button(button_frame, text="⏸️ PAUSE",
                                        font=('Arial', 14, 'bold'),
                                        bg=self.warning_color, fg=self.bg_color,
                                        width=12, height=2,
                                        command=self.pause_timer, state=tk.DISABLED)
        self.timer_pause_btn.grid(row=0, column=1, padx=10)
        
        self.timer_reset_btn = tk.Button(button_frame, text="🔄 RESET",
                                        font=('Arial', 14, 'bold'),
                                        bg=self.danger_color, fg=self.bg_color,
                                        width=12, height=2,
                                        command=self.reset_timer)
        self.timer_reset_btn.grid(row=0, column=2, padx=10)
        
    def create_stopwatch_tab(self):
        stopwatch_frame = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(stopwatch_frame, text="⏱️ Stopwatch")
        
        # Stopwatch display
        self.stopwatch_display = tk.Label(stopwatch_frame, text="00:00:00.00",
                                        font=('Digital-7', 64, 'bold'),
                                        bg=self.bg_color, fg=self.success_color)
        self.stopwatch_display.pack(pady=50)
        
        # Control buttons
        button_frame = tk.Frame(stopwatch_frame, bg=self.bg_color)
        button_frame.pack(pady=20)
        
        self.stopwatch_start_btn = tk.Button(button_frame, text="▶️ START",
                                            font=('Arial', 14, 'bold'),
                                            bg=self.success_color, fg=self.bg_color,
                                            width=12, height=2,
                                            command=self.start_stopwatch)
        self.stopwatch_start_btn.grid(row=0, column=0, padx=10)
        
        self.stopwatch_pause_btn = tk.Button(button_frame, text="⏸️ PAUSE",
                                            font=('Arial', 14, 'bold'),
                                            bg=self.warning_color, fg=self.bg_color,
                                            width=12, height=2,
                                            command=self.pause_stopwatch, state=tk.DISABLED)
        self.stopwatch_pause_btn.grid(row=0, column=1, padx=10)
        
        self.stopwatch_lap_btn = tk.Button(button_frame, text="🏁 LAP",
                                          font=('Arial', 14, 'bold'),
                                          bg=self.accent_color, fg=self.bg_color,
                                          width=12, height=2,
                                          command=self.add_lap, state=tk.DISABLED)
        self.stopwatch_lap_btn.grid(row=0, column=2, padx=10)
        
        self.stopwatch_reset_btn = tk.Button(button_frame, text="🔄 RESET",
                                            font=('Arial', 14, 'bold'),
                                            bg=self.danger_color, fg=self.bg_color,
                                            width=12, height=2,
                                            command=self.reset_stopwatch)
        self.stopwatch_reset_btn.grid(row=0, column=3, padx=10)
        
        # Lap times frame
        lap_frame = tk.Frame(stopwatch_frame, bg=self.bg_color)
        lap_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        tk.Label(lap_frame, text="Lap Times",
                font=('Arial', 14, 'bold'), bg=self.bg_color, fg=self.fg_color).pack()
        
        # Lap times listbox with scrollbar
        listbox_frame = tk.Frame(lap_frame, bg=self.bg_color)
        listbox_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.lap_listbox = tk.Listbox(listbox_frame, font=('Courier', 12),
                                     bg='#313244', fg=self.fg_color,
                                     yscrollcommand=scrollbar.set)
        self.lap_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.lap_listbox.yview)
        
    def create_alarm_tab(self):
        alarm_frame = tk.Frame(self.notebook, bg=self.bg_color)
        self.notebook.add(alarm_frame, text="⏰ Alarm")
        
        # Current time display
        self.current_time_label = tk.Label(alarm_frame, text="",
                                         font=('Digital-7', 36, 'bold'),
                                         bg=self.bg_color, fg=self.fg_color)
        self.current_time_label.pack(pady=20)
        
        # Alarm time display
        self.alarm_display = tk.Label(alarm_frame, text="00:00:00",
                                     font=('Digital-7', 64, 'bold'),
                                     bg=self.bg_color, fg=self.warning_color)
        self.alarm_display.pack(pady=30)
        
        # Input frame
        input_frame = tk.Frame(alarm_frame, bg=self.bg_color)
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Set Alarm (HH:MM:SS):",
                font=('Arial', 14), bg=self.bg_color, fg=self.fg_color).grid(row=0, column=0, columnspan=3, pady=10)
        
        self.alarm_hours = tk.Spinbox(input_frame, from_=0, to=23, width=5,
                                     font=('Arial', 16), justify='center')
        self.alarm_hours.grid(row=1, column=0, padx=5)
        
        tk.Label(input_frame, text=":", font=('Arial', 16),
                bg=self.bg_color, fg=self.fg_color).grid(row=1, column=1)
        
        self.alarm_minutes = tk.Spinbox(input_frame, from_=0, to=59, width=5,
                                       font=('Arial', 16), justify='center')
        self.alarm_minutes.grid(row=1, column=2, padx=5)
        
        tk.Label(input_frame, text=":", font=('Arial', 16),
                bg=self.bg_color, fg=self.fg_color).grid(row=1, column=3)
        
        self.alarm_seconds = tk.Spinbox(input_frame, from_=0, to=59, width=5,
                                       font=('Arial', 16), justify='center')
        self.alarm_seconds.grid(row=1, column=4, padx=5)
        
        # Control buttons
        button_frame = tk.Frame(alarm_frame, bg=self.bg_color)
        button_frame.pack(pady=30)
        
        self.alarm_set_btn = tk.Button(button_frame, text="⏰ SET ALARM",
                                      font=('Arial', 14, 'bold'),
                                      bg=self.warning_color, fg=self.bg_color,
                                      width=15, height=2,
                                      command=self.set_alarm)
        self.alarm_set_btn.grid(row=0, column=0, padx=10)
        
        self.alarm_cancel_btn = tk.Button(button_frame, text="❌ CANCEL",
                                         font=('Arial', 14, 'bold'),
                                         bg=self.danger_color, fg=self.bg_color,
                                         width=15, height=2,
                                         command=self.cancel_alarm, state=tk.DISABLED)
        self.alarm_cancel_btn.grid(row=0, column=1, padx=10)
        
        # Status label
        self.alarm_status = tk.Label(alarm_frame, text="Alarm not set",
                                    font=('Arial', 12), bg=self.bg_color, fg=self.fg_color)
        self.alarm_status.pack(pady=10)
        
        # Update current time
        self.update_current_time()
        
    def update_current_time(self):
        current_time = datetime.now().strftime("%I:%M:%S %p")
        self.current_time_label.config(text=current_time)
        self.root.after(1000, self.update_current_time)
        
    def format_time(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
        
    def format_stopwatch_time(self, elapsed):
        hours = int(elapsed // 3600)
        minutes = int((elapsed % 3600) // 60)
        seconds = int(elapsed % 60)
        milliseconds = int((elapsed % 1) * 100)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"
        
    def start_timer(self):
        if not self.timer_running:
            try:
                hours = int(self.timer_hours.get())
                minutes = int(self.timer_minutes.get())
                seconds = int(self.timer_seconds_input.get())
                self.timer_seconds = hours * 3600 + minutes * 60 + seconds
                
                if self.timer_seconds <= 0:
                    messagebox.showerror("Error", "Please set a valid time")
                    return
                    
                self.timer_running = True
                self.timer_start_btn.config(state=tk.DISABLED)
                self.timer_pause_btn.config(state=tk.NORMAL)
                
                self.timer_thread = Thread(target=self.run_timer, daemon=True)
                self.timer_thread.start()
                
            except ValueError:
                messagebox.showerror("Error", "Invalid time format")
                
    def run_timer(self):
        while self.timer_running and self.timer_seconds > 0:
            self.timer_display.config(text=self.format_time(self.timer_seconds))
            time.sleep(1)
            
            if self.timer_seconds > 0:
                self.timer_seconds -= 1
                # Play tick sound
                try:
                    playsound(self.tick_sound, block=False)
                except:
                    pass
                    
        if self.timer_seconds == 0:
            self.timer_display.config(text="00:00:00")
            try:
                playsound(self.complete_sound)
            except:
                pass
            messagebox.showinfo("Timer Complete", "Timer finished! ⏰")
            self.reset_timer()
            
    def pause_timer(self):
        self.timer_running = False
        self.timer_start_btn.config(state=tk.NORMAL, text="▶️ RESUME")
        self.timer_pause_btn.config(state=tk.DISABLED)
        
    def reset_timer(self):
        self.timer_running = False
        self.timer_seconds = 0
        self.timer_display.config(text="00:00:00")
        self.timer_start_btn.config(state=tk.NORMAL, text="▶️ START")
        self.timer_pause_btn.config(state=tk.DISABLED)
        
    def start_stopwatch(self):
        if not self.stopwatch_running:
            self.stopwatch_running = True
            self.stopwatch_start_time = time.time() - self.stopwatch_elapsed
            self.stopwatch_start_btn.config(state=tk.DISABLED)
            self.stopwatch_pause_btn.config(state=tk.NORMAL)
            self.stopwatch_lap_btn.config(state=tk.NORMAL)
            
            self.stopwatch_thread = Thread(target=self.run_stopwatch, daemon=True)
            self.stopwatch_thread.start()
            
    def run_stopwatch(self):
        while self.stopwatch_running:
            self.stopwatch_elapsed = time.time() - self.stopwatch_start_time
            self.stopwatch_display.config(text=self.format_stopwatch_time(self.stopwatch_elapsed))
            time.sleep(0.01)
            
    def pause_stopwatch(self):
        self.stopwatch_running = False
        self.stopwatch_start_btn.config(state=tk.NORMAL, text="▶️ RESUME")
        self.stopwatch_pause_btn.config(state=tk.DISABLED)
        self.stopwatch_lap_btn.config(state=tk.DISABLED)
        
    def reset_stopwatch(self):
        self.stopwatch_running = False
        self.stopwatch_elapsed = 0
        self.stopwatch_display.config(text="00:00:00.00")
        self.stopwatch_start_btn.config(state=tk.NORMAL, text="▶️ START")
        self.stopwatch_pause_btn.config(state=tk.DISABLED)
        self.stopwatch_lap_btn.config(state=tk.DISABLED)
        self.lap_times.clear()
        self.lap_listbox.delete(0, tk.END)
        
    def add_lap(self):
        if self.stopwatch_running:
            lap_time = self.format_stopwatch_time(self.stopwatch_elapsed)
            self.lap_times.append(lap_time)
            self.lap_listbox.insert(tk.END, f"Lap {len(self.lap_times)}: {lap_time}")
            
    def set_alarm(self):
        try:
            hours = int(self.alarm_hours.get())
            minutes = int(self.alarm_minutes.get())
            seconds = int(self.alarm_seconds.get())
            
            alarm_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.alarm_display.config(text=alarm_time)
            
            self.alarm_running = True
            self.alarm_set_btn.config(state=tk.DISABLED)
            self.alarm_cancel_btn.config(state=tk.NORMAL)
            self.alarm_status.config(text=f"Alarm set for {alarm_time}", fg=self.success_color)
            
            self.alarm_thread = Thread(target=self.run_alarm, daemon=True)
            self.alarm_thread.start()
            
        except ValueError:
            messagebox.showerror("Error", "Invalid time format")
            
    def run_alarm(self):
        while self.alarm_running:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            
            alarm_hours = int(self.alarm_hours.get())
            alarm_minutes = int(self.alarm_minutes.get())
            alarm_seconds = int(self.alarm_seconds.get())
            alarm_time_str = f"{alarm_hours:02d}:{alarm_minutes:02d}:{alarm_seconds:02d}"
            
            if current_time == alarm_time_str:
                try:
                    playsound(self.alarm_sound)
                except:
                    pass
                messagebox.showinfo("Alarm", "Wake Up! ⏰")
                self.cancel_alarm()
                break
                
            time.sleep(0.5)
            
    def cancel_alarm(self):
        self.alarm_running = False
        self.alarm_set_btn.config(state=tk.NORMAL)
        self.alarm_cancel_btn.config(state=tk.DISABLED)
        self.alarm_status.config(text="Alarm not set", fg=self.fg_color)

def main():
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
