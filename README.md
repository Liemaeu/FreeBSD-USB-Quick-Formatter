# FreeBSD-USB-Quick-Formatter

This is a small tool for quickly formating USB drives (/dev/da* only) on FreeBSD.

**Supported formats: FAT32, UFS, NTFS and Ext4**

![Screenshot1](https://raw.githubusercontent.com/Liemaeu/FreeBSD-USB-Quick-Formatter/main/Screenshots/Screenshot1.png)

## Dependencies

- Python 3 – <https://www.freshports.org/lang/python3/>
- Tkinter – one flavor e.g. `py311-tkinter` – <https://www.freshports.org/x11-toolkits/py-tkinter/>
- sudo – <https://www.freshports.org/security/sudo/>
- xterm – <https://www.freshports.org/x11/xterm/>
- fusefs-ext2 – <https://www.freshports.org/filesystems/ext2/>
- fusefs-ntfs – <https://www.freshports.org/filesystems/ntfs/>.

Please note: [mkntfs(8)](https://man.freebsd.org/cgi/man.cgi?query=mkntfs&sektion=8&manpath=freebsd-ports) can **not** create an NTFS filesystem quickly with the FreeBSD Project-provided package of fusefs-ntfs. You can work around [FreeBSD bug 206978](https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=206978) by building your own package with UBLIO disabled.

## Run

`python3 FreeBSD-USB-Quick-Formatter.py`

</br>
</br>

**Select your drive, the format and click on "Run".**

---

## What it does

1. If any partition exists, delete all partitions
2. add a single partition
3. create a filesystem in the partition.

Partition schemes: 

- MBR for FAT32 and NTFS
- GPT for Ext4 and UFS.

## More screenshots

![Screenshot2](https://raw.githubusercontent.com/Liemaeu/FreeBSD-USB-Quick-Formatter/main/Screenshots/Screenshot2.png)

![Screenshot3](https://raw.githubusercontent.com/Liemaeu/FreeBSD-USB-Quick-Formatter/main/Screenshots/Screenshot3.png)

![Screenshot4](https://raw.githubusercontent.com/Liemaeu/FreeBSD-USB-Quick-Formatter/main/Screenshots/Screenshot4.png)
