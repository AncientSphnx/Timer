# ⏱️ Timer, Stopwatch & Alarm in Python  

A simple **Python utility** that includes:  
- ⏲️ **Countdown Timer**  
- ⏱️ **Stopwatch**  
- ⏰ **Alarm Clock**  

This project is built using Python’s built-in libraries and a few external ones for sound and keyboard input.

---

## 🚀 Features

- **Timer** – enter seconds and get countdown with sound alerts  
- **Stopwatch** – start/stop with key press (`g` to start, `s` to stop)  
- **Alarm** – set an alarm for a specific time (HH:MM:SS AM/PM)  
- **Sound Notifications** using `playsound`  

---

## 📂 Project Structure
```
Timer-Project/
├── Timer.py # Main script with timer, stopwatch, alarm functions
└── README.md # Documentation
```

---

## 🛠️ Requirements  

Make sure you have **Python 3.8+** installed.  

Install required libraries:  
```bash
pip install playsound keyboard
```
⚙️ Usage

Run the script:
```
python Timer.py

```
Choose an option:
```
enter one of the options
1) Timer
2) Stop watch
3) Alarm
```
1. For Timer:
- Enter seconds (e.g., 10)
- Wait for countdown → sound plays when time is up
2. For Stopwatch:
- Type g and press Enter to start
- Press s to stop
3. For Alarm:
- Enter time in HH:MM:SS AM/PM format (e.g., 07:30:00 AM)
- Script checks continuously until time matches → sound plays

🔊 Adding Your Own Sound

Replace this placeholder in the code with the path to your .mp3 or .wav file:
```
playsound(r'Path of the sound You want to play')
```

⚠️ Notes

* On Linux/macOS, playsound may behave differently. Consider using pygame or winsound (Windows only) as alternatives.
* The stopwatch relies on the keyboard module → it requires admin/root permissions on some systems.
* Make sure your terminal/IDE allows key detection.

📜 License

This project is licensed under the MIT License.
