# desktop_linux_themer
Desktop Linux Themer is intended to be used by beginners on Linux to theme their GNOME, XFCE and Cinnamon Desktops

# Installation
The following steps should be followed for downloading:  
- Make sure that you are using a desktop environment listed here:
GNOME, XFCE, Cinnamon, Budgie
If you are on vanilla Ubuntu, Ubuntu-Budgie, Xubuntu, Linux Mint Cinnamon, Linux Mint XFCE, Zorin OS, Zorin OS Lite, vanilla Fedora, Fedora XFCE spin, Fedora Cinnamon spin, vanilla RHEL, Manjaro XFCE, Manjaro GNOME, Manjaro Cinnamon, Manjaro Budgie or any other distro using this desktop environment, you are good to go.  
- Make sure that you have Python 3 installed on your system. (Most GNU/Linux distros have python3 preinstalled.)   
To check if it is installed or not, simply open Terminal and type "python3" (without quotes) and press Enter. If you see a message that the command was not found or something wrong happened, it means that if you don't have Python3 installed. If you see something like this:   
```bash
Type "help", "copyright", "credits" or "license" for more information.
>>>
```  
this means that you have python3 installed.   
To install Python3 (if not installed), first make sure that Interent Connection is available and then follow the steps given below:  
If on Ubuntu or Debian or distros based on these two: open terminal and type "sudo apt install python3 -y" (without quotes) and press enter and put in your account password and wait for the installation to complete.  
If on Fedora or Red Hat Enterprise Linux or distros based on these: open terminal and type "sudo dnf install python3 -y" (without quotes) and press enter and put in your account password and wait for the installation to complete.  
If on Arch Linux or Manjaro or distros based on Arch: open terminal and type "sudo pacman -S python3 -y" (without quotes) and press enter and put in your account password and wait for the installation to complete.  
- Then follow the steps for respective distros:  
If on Ubuntu or Debian or distros based on these two: open terminal and type "sudo apt install tk tcl python3-tk python3-pip -y" and press enter and put in your account password and wait for the installation to complete.  
If on Fedora or Red Hat Enterprise Linux or distros based on these: open terminal and type "sudo dnf install tk tcl python3-tk python3-pip -y" (without quotes) and press enter and put in your account password and wait for the installation to complete.  
If on Arch Linux or Manjaro or Garuda or distros based on Arch: open terminal and type "sudo pacman -S tk tcl python3-tk python3-pip -y" (without quotes) and press enter and put in your account password and wait for the installation to complete. 
- Then in terminal, (for all distros) type "sudo pip install pysimplegui" (without quotes) and type in your account password and wait for the installation to complete.
- Download the latest installer script by clicking this link: https://github.com/hemish04082005/desktop_linux_themer/releases/latest/download/installer.sh and open terminal and navigate to folder containing the downloaded script using "cd" command and then type "sudo ./installer.sh" (without quotes). If you get an error claiming "Command not found", type this in terminal "chmod +x installer.sh" (without quotest). Then, put in your account password and wait for the installation to succeeed. Finally, you have installed it!
- Additional step for GNOME and Budgie users: Make sure that user-theme extension is installed through https://extensions.gnome.org/extension/19/user-themes/ and enabled too.  

# Usage:  
Use applications menu/whisker menu/start menu/gnome app drawer or anything like start menu on your desktop and search for "Desktop Linux Themer" and launch the application.
Then use it to switch GTK, Window Manager, Desktop, Icons, Cursors theme through drop down menus and buttons provided. 

# To do:  
- add lxde desktop support
- provide mechanism for downloading and installing popular themes within the application
- make installation simple