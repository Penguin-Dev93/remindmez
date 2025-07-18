# 🐧 remindmez

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![AUR](https://img.shields.io/aur/version/remindmez)](https://aur.archlinux.org/packages/remindmez)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Install with pipx](https://img.shields.io/badge/Install%20with-pipx-blue?logo=pip)](https://github.com/Penguin-Dev93/remindmez)
[![GitHub Stars](https://img.shields.io/github/stars/Penguin-Dev93/remindmez?style=social)](https://github.com/Penguin-Dev93/remindmez/stargazers)

**remindmez** is a fun and simple Python CLI tool that reminds you of anything — with ASCII penguins, system notifications, and a little bit of flair.

When it's time, your reminder will pop up in the terminal as a penguin along with your message, plus optional system notification and sound.

---

## 🚀 Installation

Install from the AUR (recommended):

```bash
yay -S remindmez
---------------------------------------------

Install via `pipx` (recommended for non Arch systems):

```bash
pipx install git+https://github.com/Penguin-Dev93/remindmez

# ⚠️ If you see the warning:
# UserWarning: The Python dbus package is not installed
# You may need to manually install it depending on your system:

# For Arch-based systems:
sudo pacman -S python-dbus

# For Debian/Ubuntu-based systems:
sudo apt install python-dbus

# Then, inject dbus-python into the remindmez venv:
pipx inject remindmez dbus-python
