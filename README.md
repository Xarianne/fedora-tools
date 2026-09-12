# Fedora Tools

A personal collection of Fedora rpms. COPR available: https://copr.fedorainfracloud.org/coprs/xariann/tools/

This has my own tools (described in the README) and also serves as a staging repo for other useful tools I packaged, which didn't have a rpm home.

## Fedora Update [![Copr build status](https://copr.fedorainfracloud.org/coprs/xariann/tools/package/boot-windows/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xariann/tools/package/boot-windows/)
Emulates arch-update by updating your system, then cleans up old dependencies and cache. Once installed enable the systemd service for the system tray icon:

```bash
systemctl --user enable --now fedora-update-tray.service
```

To make sure the updates are checked every hour also enable the timer:

```bash
systemctl --user enable --now fedora-update-check.timer
```

## Boot Windows [![Copr build status](https://copr.fedorainfracloud.org/coprs/xariann/tools/package/boot-windows/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xariann/tools/package/boot-windows/)
A script that finds your Windows boot entry and then asks you if you want to reboot to Windows.
