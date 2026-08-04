import os
import sys
import rumps
from playsound3 import playsound

# Dynamic directory path lookup for portability
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALARM_PATH = os.path.join(BASE_DIR, "alarm.mp3")

class MacMenuTimer(rumps.App):
    def __init__(self, total_seconds):
        super(MacMenuTimer, self).__init__("🍅 Loading...")
        self.total_seconds = total_seconds
        self.remaining = total_seconds
        
        # FIX: Explicit track running state using our own reliable flag
        self.is_running = True
        
        # Interactive drop-down window menu elements
        self.menu = [
            rumps.MenuItem("Pause/Resume", callback=self.toggle_timer),
            rumps.MenuItem("Reset", callback=self.reset_timer),
            None, 
            rumps.MenuItem("Quit Timer", callback=rumps.quit_application)
        ]
        
        # Ticks down every 1 second
        self.clock_ticker = rumps.Timer(self.update_timer, 1)
        self.clock_ticker.start()

    def update_timer(self, sender):
        """Runs every second to update the clock countdown display text."""
        if self.remaining >= 0:
            mins, secs = divmod(self.remaining, 60)
            self.title = f"🍅 {mins:02d}:{secs:02d}"
            self.remaining -= 1
        else:
            self.trigger_alarm()

    def trigger_alarm(self):
        """Triggers the completion updates when the focus cycle runs out."""
        self.clock_ticker.stop()
        self.is_running = False # Update our state tracking flag
        
        self.title = "💥 SPLAT! Time's Up"
        
        rumps.notification(
            title="Pomodoro Completed!",
            subtitle="Time for a break!",
            message="Your tomato focus block has exploded.",
            sound=False 
        )
        try:
            playsound(ALARM_PATH)
        except Exception:
            print("\a") 

    def toggle_timer(self, sender):
        """Pauses or resumes the timer clock loop cleanly using our state flag."""
        if self.is_running:
            self.clock_ticker.stop()
            self.is_running = False
            sender.title = "▶️ Resume"
        else:
            self.clock_ticker.start()
            self.is_running = True
            sender.title = "⏸️ Pause"

    def reset_timer(self, sender):
        """Resets the timer back to its starting time without throwing attributes errors."""
        self.remaining = self.total_seconds
        
        # If it was stopped or completed, start it back up cleanly
        if not self.is_running:
            self.clock_ticker.start()
            self.is_running = True
            
        # Reset the Pause text label state in the drop down menu layout
        self.menu["Pause/Resume"].title = "⏸️ Pause"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        seconds = 1500 
    else:
        try:
            # FIX: Added [1] to pull the actual string out of the argument list
            seconds = int(sys.argv[1])
        except ValueError:
            print("Invalid input string parsed. Defaulting to 1500.")
            seconds = 1500

    app = MacMenuTimer(seconds)
    app.run()

