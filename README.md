# Image Writer

_flasher_ is a simple Disk Image USB burner tool..

_It is currently a work in progress. Maintenance is done by <a href="https://www.github.com/DAFT-8/">DAFT-8</a> team._

## Dependencies

* This application is developed based on Python3 and GTK+3. Dependencies:
  * ```gir1.2-glib-2.0 gir1.2-gtk-3.0 dh-python python3-all python3-setuptools gettext```

## Run Application from Source

* Install dependencies :
  * ```sudo apt install gir1.2-glib-2.0 gir1.2-gtk-3.0 dh-python python3-all python3-setuptools gettext```
* Clone the repository :
  * ```git clone https://github.com/DAFT-8/flasher.git ~/flasher```
* Run application :
  * ```python3 ~/flasher/src/main.py```

## Build the package

* `sudo apt install devscripts git-buildpackage`
* `cd ~/flasher/`
* `sudo mk-build-deps -ir`
* `gbp buildpackage --git-ignore-new -us -uc`

## Screenshot(s)

![flasher](screenshot.png)
