# Fedora Tools

A personal collection of Fedora rpms. COPR available: https://copr.fedorainfracloud.org/coprs/xariann/tools/

This has my own tools (described in the README) and also serves as a staging repo for other useful tools I packaged, which didn't have a rpm home.

## Fedora Update [![Copr build status](https://copr.fedorainfracloud.org/coprs/xariann/tools/package/fedora-update/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xariann/tools/package/fedora-update/)
Emulates arch-update by updating your system, then cleans up old dependencies and cache. Once installed enable the systemd service for the system tray icon:

```bash
systemctl --user enable --now fedora-update-tray.service
```

To make sure the updates are checked every hour also enable the timer:

```bash
systemctl --user enable --now fedora-update-check.timer
```

The tray icon reflects the last check: the plain Fedora logo means up to date, an orange badge means updates are available, a red badge means the last check failed, and a gray badge means no check has run yet (or the timer is not enabled).

## Boot Windows [![Copr build status](https://copr.fedorainfracloud.org/coprs/xariann/tools/package/boot-windows/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/xariann/tools/package/boot-windows/)
A script that finds your Windows boot entry and then asks you if you want to reboot to Windows.
