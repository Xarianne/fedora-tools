#!/usr/bin/env python3

import os
import subprocess
import sys
import threading
import time

import pystray
from pystray import MenuItem as Item
from PIL import Image, ImageDraw

# Use absolute path to ensure systemd user services can find the binary
TERMINAL_CMD = ["/usr/bin/xdg-terminal-exec"]
ICON_NAME = "fedora-logo-icon"
ICON_FALLBACK = "/usr/share/icons/hicolor/32x32/apps/fedora-logo-icon.png"

# Where fedora-update-check.sh publishes its state: "<state> <unix-timestamp>"
XDG_RUNTIME_DIR = os.environ.get("XDG_RUNTIME_DIR") or f"/run/user/{os.getuid()}"
STATE_FILE = os.path.join(XDG_RUNTIME_DIR, "fedora-update.status")

# How often the tray re-reads the state file
POLL_SECONDS = 60

# Badge colors: updates available / check failed / no check yet
BADGE_COLORS = {
    "updates": (230, 126, 34),   # orange
    "error": (204, 51, 51),      # red
    "unknown": (140, 140, 140),  # gray
}


def run_fedora_update():
    cmd = TERMINAL_CMD + ["/usr/bin/fedora-update"]
    try:
        subprocess.Popen(cmd)
    except FileNotFoundError:
        subprocess.Popen(["xdg-terminal-exec", "/usr/bin/fedora-update"])


def load_fedora_icon():
    """Load the Fedora icon by theme name, with a hard-coded fallback."""
    try:
        import gi

        gi.require_version("Gtk", "3.0")
        from gi.repository import Gtk

        info = Gtk.IconTheme.get_default().lookup_icon(ICON_NAME, 32, 0)
        if info is not None:
            path = info.get_filename()
            if path:
                return Image.open(path)
    except Exception:
        pass
    return Image.open(ICON_FALLBACK)


def badge(base, color):
    """Draw a small corner badge onto a copy of the base icon."""
    img = base.copy().convert("RGBA")
    d = ImageDraw.Draw(img)
    d.ellipse((20, 20, 30, 30), fill=color + (255,))
    d.ellipse((21, 21, 29, 29), fill=(255, 255, 255, 255))
    return img


def read_state():
    """Return the last published check state, or 'unknown'."""
    try:
        state, ts = open(STATE_FILE).read().split()
        if time.time() - float(ts) > 2 * 86400:
            return "unknown"  # too old; checks have stopped
        return state
    except (OSError, ValueError):
        return "unknown"


class UpdateTray:
    def __init__(self):
        base = load_fedora_icon()
        self.icons = {"ok": base}
        self.icons.update(
            {s: badge(base, c) for s, c in BADGE_COLORS.items()}
        )
        self.state = "unknown"

        self.icon = pystray.Icon(
            "fedora-update",
            icon=self.icons["unknown"],
            title="Fedora Update",
            menu=pystray.Menu(
                Item("Run updates", lambda _: run_fedora_update()),
                Item(
                    lambda _: "Up to date"
                    if self.state == "ok"
                    else f"Check state: {self.state}",
                    None,
                    enabled=False,
                ),
                Item("Quit", self.quit),
            ),
        )

    def poll(self):
        """Re-read state; swap icon and refresh the menu on change."""
        state = read_state()
        if state != self.state:
            self.state = state
            self.icon.icon = self.icons.get(state, self.icons["unknown"])
            self.icon.update_menu()

    def quit(self, _):
        self.icon.stop()

    def poll_loop(self):
        while True:
            self.poll()
            time.sleep(POLL_SECONDS)

    def run(self):
        # Poll from a background thread; icon updates are safe because
        # pystray schedules them on the GLib main loop (GObject.idle_add).
        threading.Thread(target=self.poll_loop, daemon=True).start()
        # icon.run() blocks on the GLib main loop until stop() is called.
        self.icon.run(setup=lambda icon: setattr(icon, "visible", True))


def main():
    try:
        UpdateTray().run()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main