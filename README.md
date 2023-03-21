<h1 style="text-align: center; display: box">Desktop Linux Themer</h1>

Desktop Linux Themer is a software helping beginners on Linux to theme their GNOME, XFCE, Cinnamon and Budgie Desktops (generally, GTK-based desktops).

## Requirements

- <details>
      <summary> Supported Desktop Environnements </summary>
      <ul>
          <li>GNOME</li>  
          <li>XFCE</li>  
          <li>Cinnamon</li>  
          <li>Budgie</li>
      </ul>
  </details>

- <details>
      <summary> Supported Distros </summary>
      <ul>
          <li>Ubuntu (Budgie, Xubuntu/XFCE)</li>
          <li>Linux Mint (Cinnamon, XFCE)</li>
          <li>Zorin OS (+ Lite)</li>
          <li>Fedora (GNOME, XFCE, Cinnamon)</li>
          <li>RedHat Enterprise Linux (vanilla)</li>
          <li>Manjaro (GNOME, XFCE, Cinnamon, Budgie)</li>
      </ul>
  </details>
- Python 3 (type `python3` in terminal, use your package manager to install Python 3 if not)

## Installation

The following steps should be followed for downloading:

- Make sure that you are using a [supported desktop environment](#requirements).

- Make sure that you have [Python 3 installed on your system](#check-python-installation). (Most GNU/Linux distros have python3 preinstalled.)

- In a terminal, install the `pysimplegui` library by typing `sudo pip install pysimplegui` (if this errors, [check the official documentation.](https://pip.pypa.io/en/stable/installation/))

- Download the latest archive (either tar.gz or .zip) in the [releases](../../releases/latest).
- Unzip it using your favorite unarchiver.
- Open a terminal, and navigate to the unarchived folder.
- Build the installer script using `chmod +x ./build_installer.sh && sh ./build_installer.sh`.
- Verify that the installer is executable : `chmod +x ./installer.sh`
- Lauch the installer : `sudo ./installer.sh`.

Finally, you have installed it!

##### Additional step for GNOME and Budgie users:

Make sure that the `user-theme` extension is installed and enabled through <https://extensions.gnome.org/extension/19/user-themes/>.

## Check Python installation

1. Type `python3` in your terminal. It should output this (more or less) :

```bash
Python 3.8.10 (default, Mar 13 2023, 10:26:41)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

2. If any errors occur, [check the official documentation](https://wiki.python.org/moin/BeginnersGuide/Download) to correctly install the latest Python 3 on your system.

## Usage

Use applications menu/whisker menu/start menu/gnome app drawer or anything like start menu on your desktop and search for "Desktop Linux Themer" and launch the application.
Then use it to switch GTK, Window Manager, Desktop, Icons, Cursors theme through drop down menus and buttons provided.

## To do

- Add lxde desktop support
- Provide mechanism for downloading and installing popular themes within the application
- Make installation simpler
