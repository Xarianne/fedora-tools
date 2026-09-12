#!/usr/bin/env python3

import subprocess
import sys

import pystray
from pystray import MenuItem as Item
from PIL import Image

FEDORA_ICON_OK = "/usr/share/icons/hicolor/32x32/apps/fedora-logo-icon.png"

# Use absolute path to ensure systemd user services can find the binary
TERMINAL_CMD = ["/usr/bin/xdg-terminal-exec"]


def run_fedora_update():
    # Use absolute path to ensure the script is found
    cmd = TERMINAL_CMD + ["/usr/bin/fedora-update"]
    try:
        subprocess.Popen(cmd)
    except FileNotFoundError:
        # Fallback if xdg-terminal-exec is not at the absolute path
        subprocess.Popen(["xdg-terminal-exec", "/usr/bin/fedora-update"])


def load_icon(path):
    return Image.open(path)


class UpdateTray:
    def __init__(self):
        self.icon_ok = load_icon(FEDORA_ICON_OK)

        self.icon = pystray.Icon(
            "fedora-update",
            icon=self.icon_ok,
            title="Fedora Update",
            menu=pystray.Menu(
                Item("Run updates", lambda _: run_fedora_update()),
                Item("Quit", self.quit),
            ),
        )

    def quit(self, _):
        self.icon.stop()

    def run(self):
        self.icon.run()


def main():
    try:
        UpdateTray().run()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
