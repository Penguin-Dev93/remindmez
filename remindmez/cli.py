# remindmez/cli.py

import time
import argparse
import os
import platform
import subprocess
import threading

try:
    from plyer import notification
except ImportError:
    notification = None

from pyfiglet import figlet_format


PENGUIN_ASCII = r"""
      __
   -=(o '.
      '.-.\
     /|   \\
     '|   ||
     _\_):,_
"""

VERSION = "1.0.0"

def play_sound():
    try:
        if platform.system() == "Darwin":
            os.system("afplay /System/Library/Sounds/Glass.aiff")
        elif platform.system() == "Linux":
            os.system("paplay /usr/share/sounds/freedesktop/stereo/complete.oga")
        elif platform.system() == "Windows":
            import winsound
            winsound.MessageBeep()
    except Exception as e:
        print(f"(Sound failed: {e})")

def send_notification(title, message):
    system = platform.system()
    try:
        if system == "Darwin":
            subprocess.run([
                "osascript", "-e",
                f'display notification "{message}" with title "{title}"'
            ])
        else:
            notification.notify(
                title=title,
                message=message,
                timeout=10
            )
    except Exception as e:
        print(f"🐧 Notification error: {e}")
def show_reminder(reminder_text):
    print(PENGUIN_ASCII)
    print(f"🐧 Reminder: {reminder_text}")
    threading.Thread(target=play_sound).start()
    send_notification("remindmez 🐧", reminder_text)


def main():
    parser = argparse.ArgumentParser(
        description="A cute CLI reminder tool with a penguin and ASCII flair 🐧"
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {VERSION}"
    )
    args = parser.parse_args()

    print(figlet_format("remindmez", font="slant"))
    print("🐧 Welcome to remindmez!")
    reminder = input("🔔 What do you want to be reminded about? ")
    try:
        minutes = float(input("⏱️  In how many minutes? "))
    except ValueError:
        print("❌ Invalid time input. Please enter a number.")
        return

    print(f"\n⏳ Okay! I'll remind you in {minutes} minute(s)...\n")
    time.sleep(int(minutes * 60))
    show_reminder(reminder)
