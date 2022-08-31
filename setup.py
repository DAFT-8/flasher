#!/usr/bin/env python3
from setuptools import setup, find_packages
from shutil import copyfile
import os, subprocess


changelog = 'debian/changelog'
if os.path.exists(changelog):
    head = open(changelog).readline()
    try:
        version = head.split("(")[1].split(")")[0]
    except:
        print("debian/changelog format is wrong for get version")
        version = ""
    f = open('src/__version__', 'w')
    f.write(version)
    f.close()

copyfile("icon.svg", "flasher.svg")

def create_mo_files():
    podir = "po"
    mo = []
    for po in os.listdir(podir):
        if po.endswith(".po"):
            os.makedirs("{}/{}/LC_MESSAGES".format(podir, po.split(".po")[0]), exist_ok=True)
            mo_file = "{}/{}/LC_MESSAGES/{}".format(podir, po.split(".po")[0], "flasher.mo")
            msgfmt_cmd = 'msgfmt {} -o {}'.format(podir + "/" + po, mo_file)
            subprocess.call(msgfmt_cmd, shell=True)
            mo.append(("/usr/share/locale/" + po.split(".po")[0] + "/LC_MESSAGES",
                       ["po/" + po.split(".po")[0] + "/LC_MESSAGES/flasher.mo"]))
    return mo

data_files = [
    ("/usr/share/applications/", ["tr.org.daft-8.flasher.desktop"]),
    ("/usr/share/daft-8/flasher/", ["icon.svg", "main.svg", "iso.svg", "disk.svg", "settings.svg", "uefi-ntfs.img"]),
    ("/usr/share/daft-8/flasher/src",
     ["src/main.py", "src/MainWindow.py", "src/ISOCopier.py", "src/ImageWriter.py", "src/USBDeviceManager.py",
      "src/WinUSB.py", "src/__version__"]),
    ("/usr/share/daft-8/flasher/ui", ["ui/MainWindow.glade"]),
    ("/usr/share/polkit-1/actions", ["tr.org.daft-8.pkexec.flasher.policy"]),
    ("/usr/bin/", ["flasher"]),
    ("/usr/share/icons/hicolor/scalable/apps/", ["flasher.svg"]),
] + create_mo_files()

setup(
    name="flasher",
    version=version,
    packages=find_packages(),
    scripts=["flasher"],
    install_requires=["PyGObject"],
    data_files=data_files,
    author="Yurin Doctrine",
    author_email="dummy@email.org",
    description="Image Writer.",
    license="GPLv3",
    keywords="iso usb image burn write flash",
    url="https://www.github.com/daft-8",
)
