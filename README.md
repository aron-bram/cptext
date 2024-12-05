# cptext
A rapid screenshotting tool for copying text to clipboard extracted from a selected region of a screenshot.

## Installation (fedora):
`sudo dnf install cairo cairo-devel`

`sudo dnf install gobject-introspection gobject-introspection-devel`

`sudo dnf install cairo-gobject cairo-gobject-devel`

`sudo dnf install gi`

`sudo dnf install tesseract`

`pip install evdev pyscreenshot pytesseract pyperclip`
`pip install PyGObject`

`python3 -c "import gi; print(gi.__version__)"`

## Usage:
Run `python cptext.py`

 1.  This opens up a full screen transparent window with a red border for better visual representation of the area you can select
 2.  Select an area within this window by clicking twice, where the first click defines the top left corner of the selection, and the second click defines the bottom right corner
 3.  The text is automatically extracted, and copied to the clipboard
 4.  Paste your text anywhere
