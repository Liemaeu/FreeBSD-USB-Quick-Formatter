# FreeBSD-USB-Quick-Formatter

This is a small tool for quickly formating USB drives (/dev/da* only) on FreeBSD.

**Supported formats: FAT32, UFS, NTFS and Ext4**

![Screenshot1](https://raw.githubusercontent.com/Liemaeu/FreeBSD-USB-Quick-Formatter/main/Screenshots/Screenshot1.png)

## Dependencies

- Python 3
- Tkinter
- sudo
- xterm
- fusefs-ext2 *and* fusefs-ntfs


## Run

`python3 FreeBSD-USB-Quick-Formatter.py`

</br>

**Select your drive, the format and click on "Run".**

---

## What it does

It wipes everything on the USB drive and formats it. Only one partition is created, with the selected format. It uses GPT for UFS & Ext4 and MBR for FAT32 & NTFS.


## More screenshots

![Screenshot2](https://raw.githubusercontent.com/Liemaeu/FreeBSD-USB-Quick-Formatter/main/Screenshots/Screenshot2.png)

![Screenshot3](https://raw.githubusercontent.com/Liemaeu/FreeBSD-USB-Quick-Formatter/main/Screenshots/Screenshot3.png)

![Screenshot4](https://raw.githubusercontent.com/Liemaeu/FreeBSD-USB-Quick-Formatter/main/Screenshots/Screenshot4.png)
