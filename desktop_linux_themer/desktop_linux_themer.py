#!/usr/bin/env python3
from lib_desktop_linux_themer import themer
import PySimpleGUI as sg
themerobj = themer()
Layout = [
	[sg.Text("Desktop detected: {}".format(themerobj.memCurrentSession))],
	[sg.Text("GTK+ Theme"), sg.Combo(list(themerobj.gtkThemes.keys()), key='gtk', default_value=themerobj.getCurrentGtkTheme()), sg.Button("Set GTK+ Theme")],
	[sg.Text("Window Manager Theme"), sg.Combo(list(themerobj.WMthemes.keys()), key='WM', default_value=themerobj.getCurrentWMtheme()), sg.Button("Set WM Theme")],
	[sg.Text("Desktop Theme"), sg.Combo(list(themerobj.desktopThemes.keys()), key='desktop', default_value=themerobj.getCurrentDesktopTheme()), sg.Button("Set Desktop Theme")],
	[sg.Text("Icons"), sg.Combo(list(themerobj.icons.keys()), key='icons', default_value=themerobj.getCurrentIconTheme()), sg.Button("Set Icons")],
	[sg.Text("Cursors"), sg.Combo(list(themerobj.cursors.keys()), key='cursors', default_value=themerobj.getCurrentCursorTheme()), sg.Button("Set Cursors")], 
	[sg.Exit()]
	]
if themerobj.memCurrentSession in themerobj.XFCEsessions: # Beacuse we dont have desktop themes in xfce, xfce interface is guided by gtk.
	Layout.pop(3)
if themerobj.memCurrentSession in themerobj.GNOMEsessions or themerobj.memCurrentSession in themerobj.BudgieSessions: # Budgie and GNOME don't respect window manager theme and rely on GTK for window manager
	Layout.pop(2)
if themerobj.memCurrentSession in themerobj.swaySessions: # Beacuse we dont have desktop themes in Sway
	Layout.pop(3)
if themerobj.memCurrentSession in themerobj.swaySessions : # No WM themes in sway
	Layout.pop(2)
Window = sg.Window("Linux Themer", Layout)
while True:
	event, values = Window.read()
	if event in [sg.WIN_CLOSED, "Exit"]:
		break
	elif event == "Set GTK+ Theme":
                themerobj.changeGtkTheme(values["gtk"])
                if themerobj.memCurrentSession in themerobj.GNOMEsessions or themerobj.memCurrentSession in themerobj.BudgieSessions:
                        themerobj.changeWMtheme(values["gtk"]) # because budgie and gnome dont care about window manager theme
	elif event == "Set WM Theme":
		themerobj.changeWMtheme(values["WM"])
	elif event == "Set Desktop Theme":
		themerobj.changeDesktopTheme(values["desktop"])
	elif event == "Set Icons":
		themerobj.changeIconTheme(values["icons"])
	elif event == "Set Cursors":
		themerobj.changeCursorTheme(values["cursors"])
Window.close()

