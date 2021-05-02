#!/usr/bin/env python3
# To do: check if modules are iinstalled or not
import sys
import os
import subprocess
import shutil
if str(sys.platform) in ["linux", "linux32", "linux2", "linux3", "linux4", "linux5"]:
    if os.geteuid() in ["0", 0]:
        try:
            import requests
        except:
            print("Requests module not found")
            print("Trying to install requests")
            os.popen("/usr/bin/env python3 -m pip install requests")
        try:
            import PySimpleGUI
        except:
            print("PySimpleGUI module not found.")
            print("Trying to install")
            os.popen("/usr/bin/env python3 -m pip install PySimpleGUI")
        try:
            shutil.copyfile("desktop_linux_themer.py", "/usr/bin/desktop_linux_themer.py")
            shutil.copyfile("lib_desktop_linux_themer.py", "/usr/bin/lib_desktop_linux_themer.py")
            shutil.copyfile("desktop_linux_themer.desktop", "/usr/share/applications/desktop_linux_themer.desktop")
            os.popen("chmod 755 /usr/bin/desktop_linux_themer.py")
            os.popen("chmod 755 /usr/bin/lib_desktop_linux_themer.py")
            os.popen("chmod 755 /usr/share/applications/desktop_linux_themer.desktop")
        except:
            print("Installation failed due to some error. Please try to reinstall.")
            exit()
    else:
        print("Installation requires root/sudo permissions. Installation failed. Please reinstall with root permissions.")
        exit()
else:
    print("This script is only meant to be run on Desktop GNU/Linux Platforms")
    exit()
