import os
import sys
import rumps
from playsound3 import playsound

# DYNAMIC PATH: This finds the exact folder this script is sitting in, on any computer.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALARM_PATH = os.path.join(BASE_DIR, "alarm.mp3")

class MacMenuTimer(rumps.App):
    def __init__(self, total_seconds):
        super(MacMenuTimer, self).__init__("⏳ Loading...")
        self.total_seconds = total_seconds
        self.remaining = total_seconds
        
        self.menu = [
            rumps.MenuItem("Pause/Resume", callback=self.toggle_timer),
            rumps.MenuItem("Reset", callback=self.reset_timer),
            None, 
            rumps.MenuItem("Quit Timer", callback=rumps.quit_application)
        ]
        
        self.clock_ticker = rumps.Timer(self.update_timer, 1)
        self.clock_ticker.start()

    def update_timer(self, sender):
        if self.remaining >= 0:
            mins, secs = divmod(self.remaining, 60)
            if self.remaining > (self.total_seconds * 0.5):
                emoji = "🍏" 
            elif self.remaining > (self.total_seconds * 0.2):
                emoji = "🍊" 
            else:
                emoji = "🚨" 
                
            self.title = f"{emoji} {mins:02d}:{secs:02d}"
            self.remaining -= 1
        else:
            self.trigger_alarm()

    def trigger_alarm(self):
        self.clock_ticker.stop()
        self.title = "💥 TIME'S UP! 💥"
        rumps.notification(
            title="Workflow Completed",
            subtitle="Time to stretch!",
            message="Your countdown timer has expired.",
            sound=False 
        )
        try:
            # Uses the dynamic path instead of a hardcoded one
            playsound(ALARM_PATH)
        except Exception:
            print("\a") 

    def toggle_timer(self, sender):
        if self.clock_ticker.is_running:
            self.clock_ticker.stop()
            sender.title = "▶️ Resume"
        else:
            self.clock_ticker.start()
            sender.title = "⏸️ Pause"

    def reset_timer(self, sender):
        self.remaining = self.total_seconds
        if not self.clock_ticker.is_running:
            self.clock_ticker.start()
            self.menu["Pause/Resume"].title = "⏸️ Pause"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        seconds = 1500 
    else:
        try:
            seconds = int(sys.argv[1])
        except ValueError:
            print("Invalid input. Defaulting to 1500 seconds.")
            seconds = 1500

    app = MacMenuTimer(seconds)
    app.run()
