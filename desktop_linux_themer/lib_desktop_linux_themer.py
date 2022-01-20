#!/usr/bin/env python3
import os
from os.path import expanduser as _
from os.path import join as joinp

def createDirIfNotExists(path):
	if os.path.exists(str(path)) == False:
		os.mkdir(str(path))
	else:
		pass

def createFileIfNotExists(path):
	if os.path.exists(str(path)) == False:
		with open(str(path), "x") as y:
			pass
	else:
		pass

def mergeDict(dict1, dict2):
	res = {**dict1, **dict2}
	return res

def listFolders(path):
	templist = os.listdir(path)
	anothertemplist = []
	for item in templist:
		if os.path.isdir(os.path.join(path, item)):
			anothertemplist.append(item)
	return anothertemplist

def sanitiseString(suppliedArg):
	temp = suppliedArg
	while " " in temp:
		temp = temp.replace(" ", "")
	while "'" in temp:
		temp = temp.replace("'", "")
	return temp

def changeConfigIni(file, group, key, value):
	from configparser import ConfigParser
	parser = ConfigParser()
	parser.read(file)
	print(parser[group][key])
	parser.set(group, key, value)
	try:
		with open(file, "wt") as f:
			parser.write(f)
	except:
		print("Exception")

def changeGtkThemeIni(theme):
	createDirIfNotExists(joinp(_("~"), ".config"))
	createDirIfNotExists(joinp(_("~"), ".config", "gtk-3.0"))
	filen = joinp(_("~"), ".config", "gtk-3.0", "settings.ini")
	changeConfigIni(filen, "Settings", "gtk-theme-name", theme)

def changeCursorThemeIni(theme):
	createDirIfNotExists(joinp(_("~"), ".config"))
	createDirIfNotExists(joinp(_("~"), ".config", "gtk-3.0"))
	filen = joinp(_("~"), ".config", "gtk-3.0", "settings.ini")
	changeConfigIni(filen, "Settings", "gtk-cursor-theme-name", theme)

def changeIconThemeIni(theme):
	createDirIfNotExists(joinp(_("~"), ".config"))
	createDirIfNotExists(joinp(_("~"), ".config", "gtk-3.0"))
	filen = joinp(_("~"), ".config", "gtk-3.0", "settings.ini")
	changeConfigIni(filen, "Settings", "gtk-icon-theme-name", theme)

# To do:
# check gnome user themes extension and enable it
# if the user is root, then instead of /root use /usr/share/themes and usr/share/icons
# Add support for lxde

class themer(object):

	homeDir = str(os.path.expanduser("~"))
	confPathRoot = str(os.path.join(homeDir, ".linuxThemer/"))
	XFCEsessions = ["Xubuntu", "XFCE", "xfce", "Xfce"]
	GNOMEsessions = ["Ubuntu", "Ubuntu on Wayland", "Ubuntu on Xorg", "GNOME", "GNOME on Wayland", "GNOME on Xorg", "gnome", "Gnome", "ubuntu:GNOME"]
	CinnamonSessions = ["Cinnamon", "Cinnnamon (Software Rendering)", "cinnamon", "CINNAMON", "X-Cinnamon"]
	BudgieSessions = ["Budgie", "Budgie:GNOME"]
	swaySessions = ["sway", "Sway"]

	# def confPath(self, arg):
	# 	return str(os.path.join(self.confPathRoot, (arg+".conf")))
	@staticmethod
	def createDirIfNotExists(path):
		if os.path.exists(str(path)) == False:
			os.mkdir(str(path))
		else:
			pass

	@staticmethod
	def createFileIfNotExists(path):
		if os.path.exists(str(path)) == False:
			with open(str(path), "x") as y:
				pass
		else:
			pass

	def __init__(self):
		# self.createDirIfNotExists(self.confPathRoot)
		self.createDirIfNotExists(os.path.join(self.homeDir, ".themes"))
		self.createDirIfNotExists(os.path.join(self.homeDir, ".icons"))
		self.update()
	
	def checkThemeCompatibility(self, themePath):
		folderstemp = os.listdir(themePath)
		compat = {}
		for item in folderstemp:
			if "gtk" in item:
				compat["gtk"] = True
		if not "gtk" in compat:
			compat["gtk"] = False
		for item in folderstemp:
			if "metacity" in item:
				compat["metacity"] = True
		if not "metacity" in compat:
			compat["metacity"] = False
		if "cinnamon" in folderstemp:
			compat["cinnamon"] = True
		else:
			compat["cinnamon"] = False
		if "xfwm4" in folderstemp:
			compat["xfce"] = True
		else:
			compat["xfce"] = False
		if "gnome-shell" in folderstemp:
			compat["gnome"] = True
		else:
			compat["gnome"] = False
		return compat
	
	def checkCursorCompatibility(self, path):
		if "cursors" in os.listdir(path):
			return True
		else:
			return False
	
	def checkIconsCompatibility(self, path):
		if "index.theme" in os.listdir(path):
			return True
		else:
			return False
	def checkCinnamonCompatibility(self, path): # Cinnamon compatibility means cinnamon-desktop themes
		return self.checkThemeCompatibility(path)["cinnamon"]
	
	def checkGnomeCompatibility(self, path): # Gnome compatility means gnome-shell themes
		return self.checkThemeCompatibility(path)["gnome"]
	
	def checkXfceCompatibility(self, path): # Xfce compatibility means xfwm themes
		return self.checkThemeCompatibility(path)["xfce"]
	
	def checkGtkCompatibility(self, path):
		return self.checkThemeCompatibility(path)["gtk"]
	
	def checkMetacityCompatibility(self, path): # metacity is primarily for cinnamon
		return self.checkThemeCompatibility(path)["metacity"]
	
	def update(self):
		self.memSystemThemes = {}
		for item in listFolders("/usr/share/themes"):
			self.memSystemThemes[item] = str(os.path.join("/usr/share/themes", item))
		self.memUserThemes = {}
		for item in listFolders(os.path.join(self.homeDir, ".themes")):
			self.memUserThemes[item] = str(os.path.join(self.homeDir, ".themes", item))
		self.memSystemIcons = {}
		for item in listFolders("/usr/share/icons"):
			self.memSystemIcons[item] = str(os.path.join("/usr/share/icons", item))
		self.memUserIcons = {}
		for item in listFolders(os.path.join(self.homeDir, ".icons")):
			self.memUserIcons[item] = str(os.path.join(self.homeDir, ".icons", item))
		self.memThemes = mergeDict(self.memSystemThemes, self.memUserThemes)
		self.memIcons = mergeDict(self.memSystemIcons, self.memUserIcons)

		# Determining current desktop environment
		try:
			self.memCurrentSession = (str(os.environ["XDG_CURRENT_DESKTOP"]))
		except:
			try:
				self.memCurrentSession = (str(os.environ["XDG_SESSION_DESKTOP"]))
			except:
				pass

		# Final output
		self.gtkThemes = {}
		self.icons = {}
		self.cursors = {}
		self.WMthemes = {}
		self.desktopThemes = {}

		# ----- gtk themes ------
		templist = list(self.memThemes.values())
		anothertemplist = list(filter(self.checkGtkCompatibility, templist))
		for key, value in self.memThemes.items():
			if value in anothertemplist:
				self.gtkThemes[key] = str(value)
		# ----------------

		# ---- Window manager themes ------
		if self.memCurrentSession in self.XFCEsessions:
			templist = list(self.memThemes.values())
			anothertemplist = list(filter(self.checkXfceCompatibility, templist))
			for key, value in self.memThemes.items():
				if value in anothertemplist:
					self.WMthemes[key] = str(value)
		
		if self.memCurrentSession in self.CinnamonSessions:
			templist = list(self.memThemes.values())
			anothertemplist = list(filter(self.checkMetacityCompatibility, templist))
			for key, value in self.memThemes.items():
				if value in anothertemplist:
					self.WMthemes[key] = str(value)
		# ----------------------

		# ----- Desktop Themes -----
		if self.memCurrentSession in self.GNOMEsessions:
			templist = list(self.memThemes.values())
			anothertemplist = list(filter(self.checkGnomeCompatibility, templist))
			for key, value in self.memThemes.items():
				if value in anothertemplist:
					self.desktopThemes[key] = str(value)
		if self.memCurrentSession in self.CinnamonSessions:
			templist = list(self.memThemes.values())
			anothertemplist = list(filter(self.checkCinnamonCompatibility, templist))
			for key, value in self.memThemes.items():
				if value in anothertemplist:
					self.desktopThemes[key] = str(value)
		if self.memCurrentSession in self.BudgieSessions: # Budgie's themeing works the same as GNOME
			templist = list(self.memThemes.values())
			anothertemplist = list(filter(self.checkGnomeCompatibility, templist))
			for key, value in self.memThemes.items():
				if value in anothertemplist:
					self.desktopThemes[key] = str(value)
		# ---------------------------

		# ----- Icons --------
		templist = list(self.memIcons.values())
		anothertemplist = list(filter(self.checkIconsCompatibility, templist))
		for key, value in self.memIcons.items():
			if value in anothertemplist:
				self.icons[key] = str(value)
		# ----------------------

		# ---- Cursors ----------
		templist = list(self.memIcons.values())
		anothertemplist = list(filter(self.checkCursorCompatibility, templist))
		for key, value in self.memIcons.items():
			if value in anothertemplist:
				self.cursors[key] = str(value)
		# ---------------------

		# self.memAllSessions = list(map(lambda x: x.split(".desktop")[0], list(os.listdir("/usr/share/xsessions"))))
		
	def getCurrentIconTheme(self):
		self.update()
		if (self.memCurrentSession in self.GNOMEsessions) == True:
			tempTheme = os.popen("gsettings get org.gnome.desktop.interface icon-theme").readline().rstrip()
		elif (self.memCurrentSession in self.BudgieSessions) == True: # same as gnome
			tempTheme = os.popen("gsettings get org.gnome.desktop.interface icon-theme").readline().rstrip()
		elif (self.memCurrentSession in self.XFCEsessions) == True:
			tempTheme = str(os.popen("xfconf-query -lvc xsettings -p /Net/IconThemeName").readline().rstrip()).split("Name ")[1]
		elif (self.memCurrentSession in self.CinnamonSessions) == True:
			tempTheme = os.popen("gsettings get org.cinnamon.desktop.interface icon-theme").readline().rstrip()
		elif (self.memCurrentSession in self.swaySessions) == True:
			tempTheme = os.popen("gsettings get org.gnome.desktop.interface icon-theme").readline().rstrip()
			# Sway can have gtk2 theme, gtk3 theme or gnome conf as reference, here using gnome conf
		else:
			tempTheme = str("not Found")
		return sanitiseString(tempTheme)
	
	def getCurrentGtkTheme(self):
		self.update()
		if (self.memCurrentSession in self.GNOMEsessions) == True:
			tempTheme = os.popen("gsettings get org.gnome.desktop.interface gtk-theme").readline().rstrip()
		elif (self.memCurrentSession in self.BudgieSessions) == True:
			tempTheme = os.popen("gsettings get org.gnome.desktop.interface gtk-theme").readline().rstrip() #same as gnome
		elif (self.memCurrentSession in self.XFCEsessions) == True:
			tempTheme = str(os.popen("xfconf-query -lvc xsettings -p /Net/ThemeName").readline().rstrip()).split("Name ")[1]
		elif (self.memCurrentSession in self.CinnamonSessions) == True:
			tempTheme = os.popen("gsettings get org.cinnamon.desktop.interface gtk-theme").readline().rstrip()
		elif (self.memCurrentSession in self.swaySessions) == True:
			tempTheme = os.popen("gsettings get org.gnome.desktop.interface gtk-theme").readline().rstrip()
			# Sway can have gtk2 theme, gtk3 theme or gnome conf as reference, here using gnome conf
		else:
			tempTheme = str("not Found")
		return sanitiseString(tempTheme)

	def getCurrentWMtheme(self):
		self.update()
		if (self.memCurrentSession in self.GNOMEsessions) == True:
			tempTheme = os.popen("gsettings get org.gnome.desktop.wm.preferences theme").readline().rstrip()
		elif (self.memCurrentSession in self.BudgieSessions) == True: # same as gnome
			tempTheme = os.popen("gsettings get org.gnome.desktop.wm.preferences theme").readline().rstrip()
		elif (self.memCurrentSession in self.XFCEsessions) == True:
			tempTheme = str(os.popen("xfconf-query -lvc xfwm4 -p /general/theme").readline().rstrip()).split("/theme ")[1]
		elif (self.memCurrentSession in self.CinnamonSessions) == True:
			tempTheme = os.popen("gsettings get org.cinnamon.desktop.wm.preferences theme").readline().rstrip()
		else:
			tempTheme = str("not Found")
		return sanitiseString(tempTheme)

	def getCurrentCursorTheme(self):
		self.update()
		if (self.memCurrentSession in self.GNOMEsessions) == True:
			tempTheme = os.popen("gsettings get org.gnome.desktop.interface cursor-theme").readline().rstrip()
		elif (self.memCurrentSession in self.BudgieSessions) == True: #same as gnome
			tempTheme = os.popen("gsettings get org.gnome.desktop.interface cursor-theme").readline().rstrip()
		elif (self.memCurrentSession in self.XFCEsessions) == True:
                        try:
                                tempTheme = str(os.popen("xfconf-query -lvc xsettings -p /Gtk/CursorThemeName").readline().rstrip()).split("Name ")[1]
                        except:
                                stream = os.popen('xfconf-query -v -n -c xsettings -p /Gtk/CursorThemeName -t string -s "Adwaita"')
                                tempTheme = tempTheme = str(os.popen("xfconf-query -lvc xsettings -p /Gtk/CursorThemeName").readline().rstrip()).split("Name ")[1]
                                stream.close()
		elif (self.memCurrentSession in self.CinnamonSessions) == True:
			tempTheme = os.popen("gsettings get org.cinnamon.desktop.interface cursor-theme").readline().rstrip()
		else:
			tempTheme = str("not Found")
		return sanitiseString(tempTheme)

	def getCurrentDesktopTheme(self):
		self.update()
		if (self.memCurrentSession in self.GNOMEsessions) == True:
			tempTheme = os.popen("gsettings get org.gnome.shell.extensions.user-theme name").readline().rstrip()
		elif (self.memCurrentSession in self.BudgieSessions) == True: # same as gnome
			tempTheme = os.popen("gsettings get org.gnome.shell.extensions.user-theme name").readline().rstrip()
		elif (self.memCurrentSession in self.XFCEsessions) == True:
			return self.getCurrentGtkTheme() # XFCE does not have any desktop theme of its own and everything including panel depend on gtk theme
		elif (self.memCurrentSession in self.CinnamonSessions) == True:
			tempTheme = os.popen("gsettings get org.cinnamon.theme name").readline().rstrip()
		else:
			tempTheme = str("not Found")
		return sanitiseString(tempTheme)

	def changeGtkTheme(self, suppliedArg):
		if self.memCurrentSession in self.GNOMEsessions:
			stream = os.popen("gsettings set org.gnome.desktop.interface gtk-theme '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.BudgieSessions: # same as gnome
			stream = os.popen("gsettings set org.gnome.desktop.interface gtk-theme '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.XFCEsessions:
			stream = os.popen("xfconf-query -c xsettings -p /Net/ThemeName -s '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.CinnamonSessions:
			stream = os.popen("gsettings set org.cinnamon.desktop.interface gtk-theme '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.swaySessions:
			stream = os.popen("echo dummy")
			changeGtkThemeIni(suppliedArg)
		else:
			stream = os.popen("echo notFound")
		stream.close()
		n = os.popen("gsettings set org.gnome.desktop.interface gtk-theme '{}'".format(suppliedArg))
		n.close() # some applications pickup gnome conf instead of gtk conf
	
	def changeIconTheme(self, suppliedArg):
		if self.memCurrentSession in self.GNOMEsessions:
			stream = os.popen("gsettings set org.gnome.desktop.interface icon-theme '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.BudgieSessions: # same as gnome
			stream = os.popen("gsettings set org.gnome.desktop.interface icon-theme '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.XFCEsessions:
			stream = os.popen("xfconf-query -c xsettings -p /Net/IconThemeName -s '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.CinnamonSessions:
			stream = os.popen("gsettings set org.cinnamon.desktop.interface icon-theme '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.swaySessions:
			stream = os.popen("echo dummy")
			changeIconThemeIni(suppliedArg)
		else:
			stream =  os.popen("echo notFound")
		stream.close()
		n = os.popen("gsettings set org.gnome.desktop.interface icon-theme '{}'".format(suppliedArg))
		n.close() # some applications pickup gnome conf instead of gtk conf

	def changeWMtheme(self, suppliedArg):
		if self.memCurrentSession in self.GNOMEsessions:
			stream = os.popen("gsettings set org.gnome.desktop.wm.preferences theme '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.BudgieSessions: #same as gnome
			stream = os.popen("gsettings set org.gnome.desktop.wm.preferences theme '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.XFCEsessions:
			stream = os.popen("xfconf-query -c xfwm4 -p /general/theme -s '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.CinnamonSessions:
			stream = os.popen("gsettings set org.cinnamon.desktop.wm.preferences theme '{}'".format(suppliedArg))
		else:
			stream = os.popen("echo notFound")
		stream.close()

	def changeCursorTheme(self, suppliedArg):
		if self.memCurrentSession in self.GNOMEsessions:
			stream = os.popen("gsettings set org.gnome.desktop.interface cursor-theme '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.BudgieSessions: # same as gnome
			stream = os.popen("gsettings set org.gnome.desktop.interface cursor-theme '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.XFCEsessions:
			stream = os.popen("xfconf-query -c xsettings -p /Gtk/CursorThemeName -s '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.CinnamonSessions:
			stream = os.popen("gsettings set org.cinnamon.desktop.interface cursor-theme '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.swaySessions:
			stream = os.popen("echo dummy")
			changeCursorThemeIni(suppliedArg)
		else:
			stream = os.popen("echo notFound")
		stream.close()
		n = os.popen("gsettings set org.gnome.desktop.interface cursor-theme '{}'".format(suppliedArg))
		n.close() # some applications pickup gnome conf instead of gtk conf

	def changeDesktopTheme(self, suppliedArg):
		if self.memCurrentSession in self.GNOMEsessions:
			stream = os.popen("gsettings set org.gnome.shell.extensions.user-theme name '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.BudgieSessions: #same as gnome
			stream = os.popen("gsettings set org.gnome.shell.extensions.user-theme name '{}'".format(suppliedArg))
		elif self.memCurrentSession in self.XFCEsessions:
			self.changeGtkTheme(suppliedArg) # XFCE relies on GTK for desktop appearance
			stream = os.popen("echo dummycommand")
		elif self.memCurrentSession in self.CinnamonSessions:
			stream = os.popen("gsettings set org.cinnamon.theme name '{}'".format(suppliedArg))
		else:
			stream = os.popen("echo notFound")
		stream.close()
	
# themerobj = themer()
# print(themerobj.getCurrentIconTheme())
# print(themerobj.getCurrentGtkTheme())
# print(themerobj.getCurrentWMtheme())
# print(themerobj.getCurrentCursorTheme())
# print(themerobj.getCurrentDesktopTheme())
# themerobj.changeGtkTheme("WhiteSur-dark")
# themerobj.changeIconTheme("ePapirus")
# themerobj.changeWMtheme("WhiteSur-dark")
# themerobj.changeCursorTheme("WhiteSur-cursors")
# themerobj.changeDesktopTheme("WhiteSur-dark")
