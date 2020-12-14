import os
import subprocess
try: #displays an error if tkinter is not installed or is executed with Python 2
    import tkinter
    from tkinter import ttk
except:
    print("ERROR! You need to run this program with Python 3. Make sure tkinter is installed.")
    exit()

#empty list for drives
drives = list()


root = tkinter.Tk()
root.title("FreeBSD USB Quick Formatter")
root.geometry("400x320")
style = ttk.Style()
style.theme_use("clam")



def addDrives():
    for i in os.listdir("/dev"):
        if i[:2] == "da" and not "p" in i and not "s" in i:
            drives.append(i)

def run():
    if drivesCombo.get() != "": #checks if a drive is selected
        drive = "/dev/" + drivesCombo.get()
        if tableCombo.get() == "GPT":
            table = "gpt"
        else:
            table="mbr"
        if formatCombo.get() == "FAT32":
            format = "fat32"
        elif formatCombo.get() == "UFS":
            format = "freebsd-ufs"
        elif formatCombo.get() == "NTFS":
            format = "ntfs"
        else:
            format ="ext4" # might not work
        cmd = "xterm -e '" + "sudo gpart destroy -F " + drive + "; " + "sudo gpart create -s " + table + " " + drive + "; " + "sudo gpart add -t " + format + " " + drive + "; " + "sudo newfs " + drive + "p1" + "'"
        #subprocess.call(cmd, shell=True)

def refresh():
    drives.clear()
    addDrives()
    drivesCombo.configure(values=drives)


addDrives()

drivesLabel = tkinter.Label(root, text="Drives:", font=('', 10))
drivesCombo = ttk.Combobox(root, values=drives, state="readonly", font=('', 10))
tableLabel = tkinter.Label(root, text="Partition Table:", font=('', 10))
tableCombo = ttk.Combobox(root, values=("GPT", "MBR"), state="readonly", font=('', 10))
tableCombo.current(0)
formatLabel = tkinter.Label(root, text="Format:", font=('', 10))
formatCombo = ttk.Combobox(root, values=("FAT32", "UFS", "NTFS", "Ext4"), state="readonly", font=('', 10))
formatCombo.current(0)
refreshButton = ttk.Button(root, command=refresh, text="Refresh")
runButton = ttk.Button(root, command=run, text="Run")


tkinter.Label(root, font=('', 8)).pack() #empty line workaround
drivesLabel.pack()
drivesCombo.pack()
tkinter.Label(root, font=('', 8)).pack()
tableLabel.pack()
tableCombo.pack()
tkinter.Label(root, font=('', 8)).pack()
formatLabel.pack()
formatCombo.pack()
tkinter.Label(root, font=('', 8)).pack()
tkinter.Label(root, font=('', 8)).pack()
refreshButton.pack()
tkinter.Label(root, font=('', 8)).pack()
runButton.pack()


root.mainloop()
