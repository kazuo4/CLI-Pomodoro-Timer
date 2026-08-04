# 🍅 CLI macOS Menu Bar Pomodoro Timer

A lightweight, high-performance workflow countdown timer that sits directly inside your macOS menu bar. 

It keeps you focused with a fresh tomato emoji, flashes a squashed tomato splat when time expires, triggers a native Mac notification, and plays an audio alarm.

---

## 🚀 One-Command Installation

You can install this tool instantly from **any folder or directory location** on your Mac. Open your terminal app, copy the command block below, paste it, and press Enter:

```bash
curl -sSL https://github.com/kazuo4/CLI-Pomodoro-Timer.git | bash
```

*Note: After the installation success message appears, open a new terminal window or tab to start using the command.*

---

## ⚡ How to Use

The `worktimer` command is registered globally on your system. You can close your terminal, change folders, or reboot your machine—it will always run instantly from anywhere:

* **Start a Standard 25-Minute Focus Block:**
  ```bash
  worktimer
  ```

* **Start a Custom Countdown (in seconds):**
  ```bash
  worktimer 300  # 5-minute timer
  ```
  ```bash
  worktimer 10   # Quick 10-second test
  ```

---

## 🛠️ Features & Controls

* **Zero Workspace Clutter:** The application files automatically install inside a hidden directory (`~/.cli-pomodoro-timer`) to keep your user folders completely clean.
* **Interactive Dropdown Interface:** Click the `🍅` display in your Mac menu bar with your mouse to pause, resume, reset, or cleanly quit the countdown loop.
* **Smart Reset Loop:** Resetting the timer after an expiration automatically cleans the interface states and boots up a fresh session without throwing terminal crashes.
* **Audio Interleaving:** Automatically attempts to read and execute an `alarm.mp3` file stored inside the application directory on completion.
