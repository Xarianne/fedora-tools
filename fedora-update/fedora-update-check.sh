#!/usr/bin/env bash
set -euo pipefail

# Check for updates (quiet)
# dnf check-update exit codes: 0 = no updates, 100 = updates available, else = error
set +e
dnf check-update --quiet --refresh >/dev/null 2>&1
rc=$?
set -e

case "$rc" in
    0)
        # 0 = no updates
        exit 0
        ;;
    100)
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