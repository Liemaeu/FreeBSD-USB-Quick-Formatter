import os
import subprocess
import tkinter
from tkinter import ttk
from tkinter import messagebox


#empty list for drives
drives = list()


root = tkinter.Tk()
root.title("USB Quick Formatter")
root.geometry("400x400")
style = ttk.Style()
style.theme_use("clam")



def addDrives():
    for i in os.listdir("/dev"):
        if i[:2] == "da" and not "p" in i and not "s" in i:
            drives.append(i)

def run():
    if drivesCombo.get() != "": #checks if a drive is selected
        drive = "/dev/" + drivesCombo.get()
        if formatCombo.get() == "Ext4":
            formatcmd = "sudo gpart destroy -F " + drive + " ; " + "sudo gpart create -s gpt " + drive + " && " + "sudo gpart add -t linux-data " + drive + " && sleep 5 && " + "sudo mke2fs -t ext4 " + drive + "p1"
        elif formatCombo.get() == "FAT32":
            formatcmd = "sudo gpart destroy -F " + drive + " ; " + "sudo gpart create -s mbr " + drive + " && " + "sudo gpart add -t fat32 " + drive + " && sleep 5 && " + "sudo newfs_msdos -F 32 " + drive + "s1"
        elif formatCombo.get() == "NTFS":
            formatcmd = "sudo gpart destroy -F " + drive + " ; " + "sudo gpart create -s mbr " + drive + " && " + "sudo gpart add -t ntfs " + drive + " && sleep 5 && " + "sudo mkntfs --quick " + drive + "s1"
        elif formatCombo.get() == "UFS":
            formatcmd = "sudo gpart destroy -F " + drive + " ; " + "sudo gpart create -s gpt " + drive + " && " + "sudo gpart add -t freebsd-ufs " + drive + " && sleep 5 && " + "sudo newfs " + drive + "p1"
        cmd = "xterm -hold -e '" + formatcmd + " && echo Done. You can close the window." + "'"
        confirmation = tkinter.messagebox.askquestion("Confirmation", "Command: " + formatcmd)
        if confirmation == "yes":
            subprocess.call(cmd, shell=True)

def refresh():
    drives.clear()
    addDrives()
    drivesCombo.configure(values=drives)

def driveInfo():
    subprocess.call("xterm -sb -hold -e 'geom disk list'", shell=True)


addDrives()


drivesLabel = tkinter.Label(root, text="Drives:", font=("", 10))
drivesCombo = ttk.Combobox(root, values=drives, state="readonly", font=("", 10))
drivesButton = ttk.Button(root, command=driveInfo, text="Show Drives Info")
formatLabel = tkinter.Label(root, text="Format:", font=("", 10))
formatCombo = ttk.Combobox(root, values=("Ext4", "FAT32", "NTFS", "UFS"), state="readonly", font=("", 10))
formatCombo.current(0)
refreshButton = ttk.Button(root, command=refresh, text="Refresh")
runButton = ttk.Button(root, command=run, text="Run")


tkinter.Label(root, font=("", 6)).pack() #empty line workaround
tkinter.Label(root, text="If the drive's filesystem is mounted: unmount it before proceeding.", font=("", 9)).pack()
tkinter.Label(root, font=("", 8)).pack()
drivesLabel.pack()
drivesCombo.pack()
tkinter.Label(root, font=("", 8)).pack()
formatLabel.pack()
formatCombo.pack()
tkinter.Label(root, font=("", 28)).pack()
refreshButton.pack()
tkinter.Label(root, font=("", 8)).pack()
drivesButton.pack()
tkinter.Label(root, font=("", 8)).pack()
runButton.pack()


root.mainloop()
