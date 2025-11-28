# ⏱️ Timer, Stopwatch & Alarm in Python  

A **modern GUI application** built with tkinter that includes:  
- ⏲️ **Countdown Timer** with visual display  
- ⏱️ **Stopwatch** with lap times functionality  
- ⏰ **Alarm Clock** with time setting and display  

This project features a beautiful dark theme interface with sound notifications and smooth animations.

---

## 🚀 Features

- **Modern GUI** with dark theme and tabbed interface
- **Timer** – set countdown with hours, minutes, seconds and visual progress
- **Stopwatch** – start/stop/lap functionality with millisecond precision
- **Alarm** – set daily alarms with visual time display
- **Sound Notifications** using built-in sound files
- **Responsive Design** – clean, modern interface with intuitive controls
- **Threading Support** – non-blocking operations for smooth performance

---

## 📂 Project Structure
```
Timer-Project/
├── Timer.py # Modern GUI application
├── Sounds/ # Sound effects directory
│   ├── click-button-140881.mp3 # Timer tick sound
│   ├── smartphone_vibrating_alarm_silent-7040.mp3 # Alarm sound
│   └── winfantasia-6912.mp3 # Timer completion sound
├── requirements.txt # Python dependencies
└── README.md # Documentation
```

---

## 🛠️ Requirements  

Make sure you have **Python 3.8+** installed.  

Install required libraries:  
```bash
pip install -r requirements.txt
```

## ⚙️ Usage

Run the modern GUI application:
```bash
python Timer.py
```

Features:
- **Timer Tab**: Set countdown with hours, minutes, seconds
- **Stopwatch Tab**: Start/stop with lap times recording
- **Alarm Tab**: Set alarms with visual time display

### How to Use:

1. **Timer**:
   - Set hours, minutes, and seconds using the spinboxes
   - Click START to begin countdown
   - Use PAUSE to temporarily stop
   - Click RESET to clear and set new time

2. **Stopwatch**:
   - Click START to begin timing
   - Click LAP to record current time
   - Use PAUSE to stop temporarily
   - Click RESET to clear all lap times

3. **Alarm**:
   - Set desired alarm time using spinboxes
   - Click SET ALARM to activate
   - Click CANCEL to deactivate
   - Current time is displayed above

## 🎨 GUI Features

- **Dark Theme**: Modern dark interface with accent colors
- **Tabbed Interface**: Easy navigation between Timer, Stopwatch, and Alarm
- **Visual Feedback**: Large digital displays for time
- **Sound Integration**: Built-in tick, alarm, and completion sounds
- **Responsive Controls**: Intuitive start/pause/reset buttons
- **Lap Times**: Stopwatch includes lap recording functionality
- **Real-time Clock**: Alarm tab shows current time

## 🔊 Sound Files

The application includes three sound effects:
- `click-button-140881.mp3` - Timer tick sound
- `smartphone_vibrating_alarm_silent-7040.mp3` - Alarm notification
- `winfantasia-6912.mp3` - Timer completion sound

All sounds are automatically loaded from the `Sounds/` directory.

⚠️ Notes

* On Linux/macOS, playsound may behave differently. Consider using pygame or winsound (Windows only) as alternatives.
* The GUI application uses tkinter which comes pre-installed with Python.
* Sound files are automatically loaded from the Sounds directory.
* Make sure the Sounds directory exists with the provided MP3 files for full functionality.

📜 License

This project is licensed under the MIT License.
