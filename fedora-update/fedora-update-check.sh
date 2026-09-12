#!/usr/bin/env bash
set -euo pipefail

# Check for updates (quiet)
# dnf check-update exit codes: 0 = no updates, 100 = updates available, else = error

XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR:-/run/user/$(id -u)}"
STATE_FILE="$XDG_RUNTIME_DIR/fedora-update.status"

set +e
dnf check-update --quiet --refresh >/dev/null 2>&1
rc=$?
set -e

state=error
case "$rc" in
    0)   state=ok ;;
    100) state=updates ;;
esac

# Publish state for the tray icon: "<state> <unix-timestamp>"
printf '%s %s\n' "$state" "$(date +%s)" > "$STATE_FILE"

case "$state" in
    ok)
        # 0 = no updates; no notification, the tray icon reflects it
        ;;
    updates)
        # 100 = updates available
        notify-send -u normal -i fedora-logo-icon \
            "Fedora updates available" \
            "Click the tray icon to run Fedora Update."
        ;;
    *)
        notify-send -u low -i dialog-warning \
            "Fedora update check failed" \
            "dnf check-update exited with $rc (repo or network error)."
        ;;
esac