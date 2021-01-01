@echo off

:: How to obtain relative path: https://stackoverflow.com/questions/1645843/resolve-absolute-path-from-relative-path-and-or-file-name

reg add HKEY_LOCAL_MACHINE\SOFTWARE\Mozilla\NativeMessagingHosts\rune_inator /d "C:\Users\dumre\Rune-inator\firefox\app\rune-inator.json"